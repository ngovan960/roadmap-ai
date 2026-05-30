"""Seed script to populate industries table."""

import sqlite3
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

DB_PATH = "data/roadmaps.db"

INDUSTRIES = [
    # IT & Technology
    {"id": "backend-developer", "name": "Backend Developer", "slug": "backend-developer", "category": "IT", "description": "Phát triển server-side, API, database", "avg_salary_junior": "8-15 triệu", "avg_salary_mid": "15-30 triệu", "avg_salary_senior": "30-60 triệu", "demand_level": "Cao"},
    {"id": "frontend-developer", "name": "Frontend Developer", "slug": "frontend-developer", "category": "IT", "description": "Phát triển giao diện người dùng", "avg_salary_junior": "7-12 triệu", "avg_salary_mid": "12-25 triệu", "avg_salary_senior": "25-50 triệu", "demand_level": "Cao"},
    {"id": "fullstack-developer", "name": "Fullstack Developer", "slug": "fullstack-developer", "category": "IT", "description": "Phát triển cả frontend và backend", "avg_salary_junior": "10-18 triệu", "avg_salary_mid": "18-35 triệu", "avg_salary_senior": "35-70 triệu", "demand_level": "Cao"},
    {"id": "data-analyst", "name": "Data Analyst", "slug": "data-analyst", "category": "IT", "description": "Phân tích dữ liệu, báo cáo, insights", "avg_salary_junior": "8-15 triệu", "avg_salary_mid": "15-30 triệu", "avg_salary_senior": "30-55 triệu", "demand_level": "Cao"},
    {"id": "ai-engineer", "name": "AI/ML Engineer", "slug": "ai-engineer", "category": "IT", "description": "Phát triển mô hình AI và Machine Learning", "avg_salary_junior": "12-20 triệu", "avg_salary_mid": "20-40 triệu", "avg_salary_senior": "40-80 triệu", "demand_level": "Rất cao"},
    {"id": "devops-engineer", "name": "DevOps Engineer", "slug": "devops-engineer", "category": "IT", "description": "Quản lý hạ tầng, CI/CD, deployment", "avg_salary_junior": "10-18 triệu", "avg_salary_mid": "18-35 triệu", "avg_salary_senior": "35-65 triệu", "demand_level": "Cao"},
    {"id": "mobile-developer", "name": "Mobile Developer", "slug": "mobile-developer", "category": "IT", "description": "Phát triển ứng dụng di động iOS/Android", "avg_salary_junior": "8-15 triệu", "avg_salary_mid": "15-30 triệu", "avg_salary_senior": "30-55 triệu", "demand_level": "Cao"},
    {"id": "cybersecurity", "name": "Cybersecurity", "slug": "cybersecurity", "category": "IT", "description": "Bảo mật hệ thống, phân tích lỗ hổng", "avg_salary_junior": "10-18 triệu", "avg_salary_mid": "18-35 triệu", "avg_salary_senior": "35-70 triệu", "demand_level": "Rất cao"},
    {"id": "ui-ux-designer", "name": "UI/UX Designer", "slug": "ui-ux-designer", "category": "IT", "description": "Thiết kế giao diện và trải nghiệm người dùng", "avg_salary_junior": "8-14 triệu", "avg_salary_mid": "14-28 triệu", "avg_salary_senior": "28-50 triệu", "demand_level": "Cao"},
    
    # Marketing
    {"id": "digital-marketing", "name": "Digital Marketing", "slug": "digital-marketing", "category": "Marketing", "description": "Marketing trên nền tảng số", "avg_salary_junior": "7-12 triệu", "avg_salary_mid": "12-25 triệu", "avg_salary_senior": "25-45 triệu", "demand_level": "Cao"},
    {"id": "seo-specialist", "name": "SEO Specialist", "slug": "seo-specialist", "category": "Marketing", "description": "Tối ưu hóa công cụ tìm kiếm", "avg_salary_junior": "7-12 triệu", "avg_salary_mid": "12-22 triệu", "avg_salary_senior": "22-40 triệu", "demand_level": "Trung bình"},
    {"id": "content-marketing", "name": "Content Marketing", "slug": "content-marketing", "category": "Marketing", "description": "Sáng tạo nội dung marketing", "avg_salary_junior": "6-10 triệu", "avg_salary_mid": "10-20 triệu", "avg_salary_senior": "20-35 triệu", "demand_level": "Trung bình"},
    
    # Design
    {"id": "graphic-designer", "name": "Graphic Designer", "slug": "graphic-designer", "category": "Design", "description": "Thiết kế đồ họa, branding", "avg_salary_junior": "6-10 triệu", "avg_salary_mid": "10-20 triệu", "avg_salary_senior": "20-35 triệu", "demand_level": "Trung bình"},
    {"id": "video-editor", "name": "Video Editor", "slug": "video-editor", "category": "Design", "description": "Dựng video, motion graphics", "avg_salary_junior": "7-12 triệu", "avg_salary_mid": "12-22 triệu", "avg_salary_senior": "22-40 triệu", "demand_level": "Trung bình"},
    
    # Business
    {"id": "business-analyst", "name": "Business Analyst", "slug": "business-analyst", "category": "Business", "description": "Phân tích nghiệp vụ, yêu cầu hệ thống", "avg_salary_junior": "10-18 triệu", "avg_salary_mid": "18-30 triệu", "avg_salary_senior": "30-55 triệu", "demand_level": "Cao"},
    {"id": "product-manager", "name": "Product Manager", "slug": "product-manager", "category": "Business", "description": "Quản lý sản phẩm, chiến lược", "avg_salary_junior": "12-20 triệu", "avg_salary_mid": "20-40 triệu", "avg_salary_senior": "40-70 triệu", "demand_level": "Cao"},
    {"id": "project-manager", "name": "Project Manager", "slug": "project-manager", "category": "Business", "description": "Quản lý dự án, điều phối nhóm", "avg_salary_junior": "10-18 triệu", "avg_salary_mid": "18-35 triệu", "avg_salary_senior": "35-60 triệu", "demand_level": "Trung bình"},
    
    # Finance
    {"id": "accountant", "name": "Kế toán", "slug": "accountant", "category": "Finance", "description": "Kế toán tài chính, thuế", "avg_salary_junior": "6-10 triệu", "avg_salary_mid": "10-18 triệu", "avg_salary_senior": "18-30 triệu", "demand_level": "Trung bình"},
    
    # Education
    {"id": "teacher", "name": "Giáo viên", "slug": "teacher", "category": "Education", "description": "Giảng dạy, đào tạo", "avg_salary_junior": "6-10 triệu", "avg_salary_mid": "10-15 triệu", "avg_salary_senior": "15-25 triệu", "demand_level": "Trung bình"},
    
    # Engineering
    {"id": "civil-engineer", "name": "Kỹ sư xây dựng", "slug": "civil-engineer", "category": "Engineering", "description": "Thiết kế, thi công công trình", "avg_salary_junior": "8-14 triệu", "avg_salary_mid": "14-25 triệu", "avg_salary_senior": "25-45 triệu", "demand_level": "Trung bình"},
]


def seed_industries():
    """Insert industries into database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS industries (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            slug TEXT UNIQUE NOT NULL,
            category TEXT,
            description TEXT,
            avg_salary_junior TEXT,
            avg_salary_mid TEXT,
            avg_salary_senior TEXT,
            demand_level TEXT,
            view_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert industries
    for ind in INDUSTRIES:
        try:
            cursor.execute("""
                INSERT OR REPLACE INTO industries 
                (id, name, slug, category, description, avg_salary_junior, avg_salary_mid, avg_salary_senior, demand_level)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                ind["id"], ind["name"], ind["slug"], ind["category"],
                ind["description"], ind["avg_salary_junior"],
                ind["avg_salary_mid"], ind["avg_salary_senior"],
                ind["demand_level"]
            ))
            print(f"  ✓ {ind['name']}")
        except Exception as e:
            print(f"  ✗ {ind['name']}: {e}")
    
    conn.commit()
    conn.close()
    print(f"\nSeeded {len(INDUSTRIES)} industries")


if __name__ == "__main__":
    seed_industries()
