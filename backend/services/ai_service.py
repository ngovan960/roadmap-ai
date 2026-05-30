"""AI service - Xiaomi MiMo integration for roadmap generation."""

import json
from typing import Optional, List
import httpx

from backend.config import settings


async def call_xiaomi_mimo(messages: list, model: str = "mimo-v2.5") -> dict:
    """Call Xiaomi MiMo API using httpx."""
    
    api_key = settings.XIAOMI_API_KEY
    base_url = settings.XIAOMI_BASE_URL
    
    print(f"[DEBUG] API Key length: {len(api_key)}")
    print(f"[DEBUG] Model: {model}")
    
    if not api_key:
        print("[ERROR] XIAOMI_API_KEY not set!")
        raise ValueError("XIAOMI_API_KEY not set")
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 32000
    }
    
    print(f"[DEBUG] Calling API: {base_url}/chat/completions")
    
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{base_url}/chat/completions",
            headers=headers,
            json=data,
            timeout=300.0
        )
        
        print(f"[DEBUG] Response status: {response.status_code}")
        
        if response.status_code != 200:
            print(f"[ERROR] API error: {response.text[:500]}")
        
        response.raise_for_status()
        result = response.json()
        
        # Handle reasoning models
        message = result["choices"][0]["message"]
        content = message.get("content", "")
        reasoning = message.get("reasoning_content", "")
        
        if not content and reasoning:
            print(f"[DEBUG] Using reasoning_content (length: {len(reasoning)})")
            content = reasoning
        
        print(f"[DEBUG] Final content length: {len(content)}")
        
        return {"choices": [{"message": {"content": content}}]}


def _fix_truncated_json(json_str: str) -> str:
    """Fix truncated JSON by closing open brackets and strings."""
    # Count open brackets
    open_brackets = 0
    open_braces = 0
    in_string = False
    escape_next = False
    
    for i, char in enumerate(json_str):
        if escape_next:
            escape_next = False
            continue
        if char == '\\':
            escape_next = True
            continue
        if char == '"' and not escape_next:
            in_string = not in_string
            continue
        if in_string:
            continue
        if char == '[':
            open_brackets += 1
        elif char == ']':
            open_brackets -= 1
        elif char == '{':
            open_braces += 1
        elif char == '}':
            open_braces -= 1
    
    # If we're in a string, close it
    if in_string:
        json_str += '"'
    
    # Close any open brackets/braces
    json_str += ']' * max(0, open_brackets)
    json_str += '}' * max(0, open_braces)
    
    # Remove trailing comma if exists
    json_str = json_str.rstrip()
    if json_str.endswith(','):
        json_str = json_str[:-1]
    
    return json_str


SYSTEM_PROMPT = """Bạn là chuyên gia tư vấn nghề nghiệp tại Việt Nam với 15 năm kinh nghiệm.
Nhiệm vụ: Tạo roadmap học tập CHI TIẾT theo 4 cấp: Phase → Module → Task → Resource.

CẤU TRÚC OUTPUT:
- 4 Phases (mỗi phase 1-2 tháng)
- 3 Modules per phase (tổng 12 modules)
- 3 Tasks per module (tổng 36 tasks)
- 3 Resources per task (tổng 180 resources)

QUY TẮC:
1. Tất cả output bằng tiếng Việt
2. Mức lương tính bằng VNĐ, sát thị trường VN
3. Tasks phải CỤ THỂ và THỰC HÀNH được ngay
4. Mỗi task phải có: Resource (video/bài viết) + Exercise/Bài tập + Checklist
5. Resources phải là link thật, có thật (YouTube, freeCodeCamp, MDN, etc.)
6. Skills theo thứ tự học hợp lý (cơ bản → nâng cao)
7. Timeline phải thực tế
8. JSON MUST be valid

Output JSON format:
{
  "overview": "Tổng quan 2-3 câu",
  "total_weeks": 24,
  "total_tasks": 60,
  "total_hours": 360,
  "salary_range": {"junior": "X triệu", "mid": "X triệu", "senior": "X triệu"},
  "competitive_advantage": "Lý do cạnh tranh",
  "market_demand": "Nhu cầu thị trường",
  "phases": [
    {
      "id": "phase-1",
      "name": "Phase 1: Tên phase",
      "duration": "Tháng 1-2",
      "description": "Mô tả phase",
      "skills": ["skill1", "skill2"],
      "total_hours": 90,
      "milestone": "Milestone của phase",
      "modules": [
        {
          "id": "module-1-1",
          "name": "Module 1.1: Tên module",
          "description": "Mô tả module",
          "tasks": [
            {
              "id": "task-1-1-1",
              "name": "Tên task cụ thể",
              "days": "Day 1-2",
              "hours": 4,
              "resource": {
                "name": "Tên resource",
                "url": "https://...",
                "type": "free",
                "language": "vi"
              },
              "exercise": {
                "title": "Tên bài tập",
                "description": "Mô tả bài tập chi tiết",
                "deliverable": "File/Output cụ thể"
              },
              "checklist": [
                "Điều 1 đã hoàn thành",
                "Điều 2 đã hoàn thành",
                "Điều 3 đã hoàn thành"
              ]
            }
          ]
        }
      ]
    }
  ]
}"""


async def generate_roadmap(
    age: int,
    industry: str,
    level: str,
    goal: str,
    duration: int,
    current_job: Optional[str] = None,
    hours_per_day: str = "3-4",
    learning_style: List[str] = None
) -> dict:
    """Generate roadmap using Xiaomi MiMo API."""
    
    # Industry name mapping
    industry_names = {
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
    
    industry_name = industry_names.get(industry, industry.replace("-", " ").title())
    
    # Level names
    level_names = {
        "beginner": "Beginner (chưa biết gì)",
        "junior": "Junior (biết cơ bản)",
        "mid": "Mid (1-3 năm kinh nghiệm)",
        "senior": "Senior (3+ năm kinh nghiệm)"
    }
    level_name = level_names.get(level, level)
    
    # Learning style
    if learning_style is None:
        learning_style = ["video", "reading", "practice"]
    style_str = ", ".join(learning_style)
    
    # Build user prompt
    user_prompt = f"""Tạo roadmap học tập CHI TIẾT cho:

Thông tin người dùng:
- Tuổi: {age}
- Ngành muốn học: {industry_name}
- Trình độ hiện tại: {level_name}
- Mục tiêu: {goal}
- Thời gian dự kiến: {duration} tháng
- Công việc hiện tại: {current_job or 'Không chọn'}
- Số giờ học/ngày: {hours_per_day}
- Phong cách học: {style_str}

YÊU CẦU:
- 4 Phases (mỗi phase 1-{duration//4} tháng)
- 3 Modules per phase (tổng 12 modules)
- 3 Tasks per module (tổng 36 tasks)
- Mỗi task có: Resource + Exercise + Checklist (3 items)
- Resources phải là link THẬT (YouTube, freeCodeCamp, MDN, etc.)
- Tasks phải CỤ THỂ, THỰC HÀNH được ngay

Output JSON theo schema đã định."""
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]
    
    try:
        print("[DEBUG] Calling Xiaomi MiMo API...")
        response = await call_xiaomi_mimo(messages, settings.XIAOMI_MODEL)
        content = response["choices"][0]["message"]["content"]
        print(f"[DEBUG] API response received, length: {len(content)}")
        
        # Parse response - handle markdown code blocks and truncated JSON
        raw_content = content.strip()
        if raw_content.startswith("```json"):
            raw_content = raw_content[7:]
        if raw_content.startswith("```"):
            raw_content = raw_content[3:]
        if raw_content.endswith("```"):
            raw_content = raw_content[:-3]
        raw_content = raw_content.strip()
        
        # Try to parse JSON
        try:
            roadmap_data = json.loads(raw_content)
        except json.JSONDecodeError as e:
            print(f"[DEBUG] JSON parse error at char {e.pos}: {e.msg}")
            # Try to fix truncated JSON
            fixed = _fix_truncated_json(raw_content)
            try:
                roadmap_data = json.loads(fixed)
                print("[DEBUG] Fixed truncated JSON successfully")
            except:
                print("[ERROR] Cannot fix JSON, using fallback")
                return get_fallback_roadmap(industry, age, level, duration)
        
        print("[DEBUG] JSON parsed successfully")
        return roadmap_data
        
    except Exception as e:
        import traceback
        print(f"[ERROR] {type(e).__name__}: {e}")
        traceback.print_exc()
        return get_fallback_roadmap(industry, age, level, duration)


def get_fallback_roadmap(industry: str, age: int, level: str, duration: int) -> dict:
    """Get fallback roadmap when AI fails."""
    industry_title = industry.replace("-", " ").title()
    
    return {
        "overview": f"Lộ trình học tập cá nhân hóa cho ngành {industry_title}. Được thiết kế để giúp bạn từ người mới bắt đầu đến có thể apply việc.",
        "total_weeks": duration * 4,
        "total_tasks": 60,
        "total_hours": duration * 60,
        "salary_range": {
            "junior": "8-15 triệu",
            "mid": "15-30 triệu",
            "senior": "30-60 triệu"
        },
        "competitive_advantage": "Thị trường lao động Việt Nam đang thiếu nhân lực chất lượng cao. Đầu tư vào học tập là đầu tư vào tương lai.",
        "market_demand": "Nhu cầu tuyển dụng tăng 20-30%/năm cho các vị trí chuyên môn.",
        "phases": [
            {
                "id": "phase-1",
                "name": "Phase 1: Nền tảng",
                "duration": f"Tháng 1-{max(2, duration // 4)}",
                "description": "Xây dựng kiến thức nền tảng cơ bản",
                "skills": ["Kiến thức cơ bản", "Công cụ cần thiết", "Tư duy ngành"],
                "total_hours": duration * 15,
                "milestone": "Hiểu rõ bản chất ngành và có nền tảng vững chắc",
                "modules": [
                    {
                        "id": "module-1-1",
                        "name": "Module 1.1: Giới thiệu ngành",
                        "description": "Tổng quan về ngành và các vị trí việc làm",
                        "tasks": [
                            {
                                "id": "task-1-1-1",
                                "name": "Nghiên cứu ngành",
                                "days": "Day 1-2",
                                "hours": 4,
                                "resource": {"name": "YouTube - Tìm hiểu ngành", "url": "https://youtube.com", "type": "free"},
                                "exercise": {"title": "Viết bài phân tích ngành", "description": f"Viết 500 từ về ngành {industry_title}", "deliverable": "File PDF"},
                                "checklist": ["Xem 3 video về ngành", "Ghi chú các vị trí việc làm", "Viết bài phân tích"]
                            }
                        ]
                    }
                ]
            },
            {
                "id": "phase-2",
                "name": "Phase 2: Kỹ năng chuyên môn",
                "duration": f"Tháng {max(3, duration // 4 + 1)}-{max(4, duration // 2)}",
                "description": "Học các kỹ năng chuyên môn cốt lõi",
                "skills": ["Kỹ năng chính", "Thực hành dự án", "Portfolio"],
                "total_hours": duration * 15,
                "milestone": "Hoàn thành dự án đầu tiên trong portfolio",
                "modules": []
            },
            {
                "id": "phase-3",
                "name": "Phase 3: Nâng cao",
                "duration": f"Tháng {max(5, duration // 2 + 1)}-{max(6, duration * 3 // 4)}",
                "description": "Nâng cao kỹ năng và thực chiến",
                "skills": ["Kỹ năng nâng cao", "Dự án thực tế", "Optimization"],
                "total_hours": duration * 15,
                "milestone": "Hoàn thành 2-3 dự án thực tế",
                "modules": []
            },
            {
                "id": "phase-4",
                "name": "Phase 4: Portfolio & Apply việc",
                "duration": f"Tháng {max(7, duration * 3 // 4 + 1)}-{duration}",
                "description": "Xây portfolio và chuẩn bị apply việc",
                "skills": ["Portfolio", "Phỏng vấn", "Networking"],
                "total_hours": duration * 15,
                "milestone": "Sẵn sàng apply việc với portfolio hoàn chỉnh",
                "modules": []
            }
        ],
        "_fallback": True
    }
