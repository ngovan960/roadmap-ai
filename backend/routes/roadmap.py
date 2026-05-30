"""Roadmap API routes."""

import time
import uuid
import hashlib
import secrets
import json
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from typing import Optional, List

from backend.services.ai_service import generate_roadmap

router = APIRouter()
templates = Jinja2Templates(directory="backend/templates")


class RoadmapRequest(BaseModel):
    """Roadmap creation request."""
    age: int = Field(..., ge=15, le=60, description="Tuổi (15-60)")
    industry: str = Field(..., description="Ngành (slug)")
    level: str = Field(..., description="Trình độ (beginner/junior/mid/senior)")
    goal: str = Field(..., min_length=10, description="Mục tiêu")
    duration: int = Field(..., description="Thời gian (tháng)")
    current_job: Optional[str] = Field(None, description="Công việc hiện tại")
    hours_per_day: Optional[str] = Field("3-4", description="Số giờ học/ngày")
    learning_style: Optional[List[str]] = Field(["video", "reading", "practice"], description="Phong cách học")


class RoadmapResponse(BaseModel):
    """Roadmap creation response."""
    success: bool
    slug: Optional[str] = None
    url: Optional[str] = None
    error: Optional[str] = None


def generate_slug(industry: str, age: int) -> str:
    """Generate unique slug for roadmap."""
    base = f"{industry}-{age}tuoi"
    hash_input = f"{industry}-{age}-{secrets.token_hex(4)}"
    short_hash = hashlib.sha256(hash_input.encode()).hexdigest()[:4]
    return f"{base}-{short_hash}"


# Industry name mapping
INDUSTRY_NAMES = {
    "backend-developer": "Backend Developer",
    "frontend-developer": "Frontend Developer",
    "fullstack-developer": "Fullstack Developer",
    "data-analyst": "Data Analyst",
    "ai-engineer": "AI/ML Engineer",
    "devops-engineer": "DevOps Engineer",
    "mobile-developer": "Mobile Developer",
    "cybersecurity": "Cybersecurity",
    "ui-ux-designer": "UI/UX Designer",
    "digital-marketing": "Digital Marketing",
    "seo-specialist": "SEO Specialist",
    "content-marketing": "Content Marketing",
    "graphic-designer": "Graphic Designer",
    "video-editor": "Video Editor",
    "accountant": "Kế toán",
    "business-analyst": "Business Analyst",
    "product-manager": "Product Manager",
    "project-manager": "Project Manager",
    "teacher": "Giáo viên",
    "civil-engineer": "Kỹ sư xây dựng",
}


@router.post("/api/generate", response_model=RoadmapResponse)
async def create_roadmap(request: RoadmapRequest):
    """Generate a new roadmap using AI."""
    start_time = time.time()
    
    try:
        # Generate slug
        slug = generate_slug(request.industry, request.age)
        
        # Generate roadmap using AI
        roadmap_data = await generate_roadmap(
            age=request.age,
            industry=request.industry,
            level=request.level,
            goal=request.goal,
            duration=request.duration,
            current_job=request.current_job,
            hours_per_day=request.hours_per_day,
            learning_style=request.learning_style
        )
        
        # Calculate generation time
        generation_time = int((time.time() - start_time) * 1000)
        
        # Get industry name
        industry_name = INDUSTRY_NAMES.get(request.industry, request.industry)
        
        # Save to database
        roadmap_id = str(uuid.uuid4())
        
        import aiosqlite
        from backend.config import settings
        
        async with aiosqlite.connect(settings.db_path) as db:
            await db.execute("""
                INSERT INTO roadmaps (
                    id, slug, age, industry, industry_name, level, goal,
                    duration_months, current_job, hours_per_day, learning_style,
                    overview, total_weeks, total_tasks, total_hours,
                    salary_junior, salary_mid, salary_senior,
                    competitive_advantage, market_demand, roadmap_json,
                    ai_model, generation_time_ms
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                roadmap_id, slug, request.age, request.industry, industry_name,
                request.level, request.goal, request.duration,
                request.current_job, request.hours_per_day,
                json.dumps(request.learning_style),
                roadmap_data.get("overview", ""),
                roadmap_data.get("total_weeks", 0),
                roadmap_data.get("total_tasks", 0),
                roadmap_data.get("total_hours", 0),
                roadmap_data.get("salary_range", {}).get("junior", ""),
                roadmap_data.get("salary_range", {}).get("mid", ""),
                roadmap_data.get("salary_range", {}).get("senior", ""),
                roadmap_data.get("competitive_advantage", ""),
                roadmap_data.get("market_demand", ""),
                json.dumps(roadmap_data, ensure_ascii=False),
                "mimo-v2.5",
                generation_time
            ))
            await db.commit()
        
        return RoadmapResponse(
            success=True,
            slug=slug,
            url=f"/roadmap/{slug}"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/roadmap/{slug}", response_class=HTMLResponse)
async def view_roadmap(request: Request, slug: str):
    """View a roadmap by slug."""
    import aiosqlite
    from backend.config import settings
    
    # Load from database
    async with aiosqlite.connect(settings.db_path) as db:
        db.row_factory = aiosqlite.Row
        async with db.execute(
            "SELECT * FROM roadmaps WHERE slug = ?", (slug,)
        ) as cursor:
            row = await cursor.fetchone()
    
    if not row:
        return templates.TemplateResponse("404.html", {
            "request": request,
            "page_title": "Không tìm thấy - AI Career Roadmap",
            "slug": slug
        }, status_code=404)
    
    # Parse roadmap JSON
    roadmap_data = json.loads(row["roadmap_json"]) if row["roadmap_json"] else {}
    
    # Prepare template data
    template_data = {
        "request": request,
        "page_title": f"Roadmap {row['industry_name']} - AI Career Roadmap",
        "page_description": f"Lộ trình học {row['industry_name']} cá nhân hóa",
        "roadmap": {
            "age": row["age"],
            "industry": row["industry"],
            "industry_name": row["industry_name"],
            "level": row["level"],
            "goal": row["goal"],
            "duration_months": row["duration_months"],
            "overview": roadmap_data.get("overview", ""),
            "total_weeks": roadmap_data.get("total_weeks", 0),
            "total_tasks": roadmap_data.get("total_tasks", 0),
            "total_hours": roadmap_data.get("total_hours", 0),
            "salary_range": roadmap_data.get("salary_range", {}),
            "competitive_advantage": roadmap_data.get("competitive_advantage", ""),
            "market_demand": roadmap_data.get("market_demand", ""),
            "phases": roadmap_data.get("phases", [])
        },
        "slug": slug
    }
    
    return templates.TemplateResponse("roadmap.html", template_data)
