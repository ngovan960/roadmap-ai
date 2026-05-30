# Decision Log

> Track architectural and technical decisions.

## Decisions

### 2026-05-30: Model Strategy

**Decision**: Phân loại task theo model
- **mimo-v2.5**: Task đơn giản (boilerplate, HTML/CSS, tests, docs)
- **mimo-v2.5-pro**: Task phức tạp (architecture, debug, AI logic, security)

**Rationale**:
- Tiết kiệm token: 80% task dùng model rẻ
- Chất lượng: Task quan trọng dùng model mạnh
- Escalation: mimo-v2.5 gặp khó → chuyển lên pro

**Cost Estimate**:
- mimo-v2.5: ~$0.001/task
- mimo-v2.5-pro: ~$0.01/task
- Average: ~$0.003/task (80% cheap, 20% expensive)

**Status**: Approved

### 2026-05-30: Tech Stack Selection

**Decision**: Python FastAPI + SQLite + OpenAI API + Vanilla HTML/CSS/JS
**Rationale**: 
- FastAPI: Async, fast, good for API
- SQLite: Simple, no setup, good for MVP
- OpenAI: Best AI API, GPT-4o-mini is cheap
- Vanilla JS: No framework complexity for MVP
**Status**: Approved

### 2026-05-30: Business Model

**Decision**: Ad-supported free + Premium 49k/tháng
**Rationale**:
- Ads: Low friction, monetize from day 1
- Premium: Recurring revenue for power users
- Affiliate: Passive income from course links
**Status**: Approved

### 2026-05-30: Slug Format

**Decision**: {industry}-{age}tuoi-{4hex}
**Rationale**: 
- Readable: Shows industry and age
- Unique: 4 hex chars = 65,536 combinations
- SEO-friendly: Contains keywords
**Status**: Approved

### 2026-05-30: AI Model Selection

**Decision**: GPT-4o-mini for MVP
**Rationale**:
- Cost: $0.006/roadmap (vs $0.06 for GPT-4o)
- Quality: Good enough for structured output
- Speed: Faster than GPT-4o
**Status**: Approved

### 2026-05-30: Deployment Platform

**Decision**: Railway.app
**Rationale**:
- Free tier: 500h/month
- Easy deploy: Git push
- Auto SSL: Built-in
**Status**: Approved

---

*Last updated: 30/05/2026*
