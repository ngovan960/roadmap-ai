"""Page routes - Serve HTML templates."""

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="backend/templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Homepage."""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "page_title": "AI Career Roadmap - Tạo lộ trình học tập cá nhân hóa",
        "page_description": "Nhập thông tin, AI tạo roadmap riêng cho bạn theo 3 cấp: Tổng quan → Giai đoạn → Tasks hàng ngày"
    })


@router.get("/tao-roadmap", response_class=HTMLResponse)
async def create_roadmap_form(request: Request):
    """Roadmap creation form."""
    # TODO: Load industries from database
    industries = [
        {"slug": "backend-developer", "name": "Backend Developer", "category": "IT"},
        {"slug": "frontend-developer", "name": "Frontend Developer", "category": "IT"},
        {"slug": "fullstack-developer", "name": "Fullstack Developer", "category": "IT"},
        {"slug": "data-analyst", "name": "Data Analyst", "category": "IT"},
        {"slug": "ai-engineer", "name": "AI/ML Engineer", "category": "IT"},
        {"slug": "devops-engineer", "name": "DevOps Engineer", "category": "IT"},
        {"slug": "mobile-developer", "name": "Mobile Developer", "category": "IT"},
        {"slug": "cybersecurity", "name": "Cybersecurity", "category": "IT"},
        {"slug": "ui-ux-designer", "name": "UI/UX Designer", "category": "IT"},
        {"slug": "digital-marketing", "name": "Digital Marketing", "category": "Marketing"},
        {"slug": "seo-specialist", "name": "SEO Specialist", "category": "Marketing"},
        {"slug": "content-marketing", "name": "Content Marketing", "category": "Marketing"},
        {"slug": "graphic-designer", "name": "Graphic Designer", "category": "Design"},
        {"slug": "video-editor", "name": "Video Editor", "category": "Design"},
        {"slug": "accountant", "name": "Kế toán", "category": "Finance"},
        {"slug": "business-analyst", "name": "Business Analyst", "category": "Business"},
        {"slug": "product-manager", "name": "Product Manager", "category": "Business"},
        {"slug": "project-manager", "name": "Project Manager", "category": "Business"},
        {"slug": "teacher", "name": "Giáo viên", "category": "Education"},
        {"slug": "civil-engineer", "name": "Kỹ sư xây dựng", "category": "Engineering"},
    ]
    
    # Group by category
    categories = {}
    for ind in industries:
        cat = ind["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(ind)
    
    return templates.TemplateResponse("form.html", {
        "request": request,
        "page_title": "Tạo Roadmap - AI Career Roadmap",
        "page_description": "Nhập thông tin để AI tạo lộ trình học tập cá nhân hóa cho bạn",
        "industries": industries,
        "categories": categories
    })


@router.get("/nganh/{slug}", response_class=HTMLResponse)
async def industry_page(request: Request, slug: str):
    """Industry landing page."""
    # TODO: Load from database
    return templates.TemplateResponse("industry.html", {
        "request": request,
        "page_title": f"Lộ trình {slug} - AI Career Roadmap",
        "page_description": f"Tạo lộ trình học {slug} cá nhân hóa bằng AI",
        "slug": slug
    })
