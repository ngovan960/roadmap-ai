# Project Context

> This file contains permanent project understanding. Update when project fundamentals change.

## Project Identity

**Name**: AI Career Roadmap
**Purpose**: Website tạo lộ trình học NGHỀ NGHIỆP cá nhân hóa bằng AI (MỌI NGÀNH)
**Repository**: ~/projects/ai-career-roadmap/
**Language**: Vietnamese

## Tech Stack

| Layer | Technology | Version |
|-------|------------|---------|
| Language | Python | 3.11+ |
| Framework | FastAPI | 0.100+ |
| Database | SQLite | 3 |
| AI | OpenAI API | GPT-4o-mini |
| Frontend | HTML/CSS/JS | Vanilla |
| Template | Jinja2 | 3.1+ |
| Deploy | Railway.app | - |

## Architecture Overview

```
User → Browser → FastAPI Server → OpenAI API
                  ↓
               SQLite DB
                  ↓
              Jinja2 Templates → HTML Response
```

## Key Directories

| Directory | Purpose |
|-----------|---------|
| `backend/` | FastAPI server, routes, services |
| `frontend/` | HTML templates, CSS, JavaScript |
| `data/` | SQLite database, fallbacks |
| `scripts/` | Utility scripts |
| `tests/` | Test files |

## Core Feature

3-Level Roadmap System:
- Level 1: Roadmap lớn (tổng quan hành trình)
- Level 2: Phases (giai đoạn 1-2 tháng)
- Level 3: Tasks (việc hàng ngày)

## Target Users

- Primary: Sinh viên, người đi làm (18-35 tuổi)
- Secondary: Người muốn chuyển ngành (25-35 tuổi)

## Business Model

- Free + Ads (Google AdSense)
- Premium: 49,000đ/tháng (không quảng cáo)
- Affiliate: Links khóa học, sách

---

*Last updated: 30/05/2026*
