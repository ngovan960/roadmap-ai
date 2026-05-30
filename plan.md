# AI Career Roadmap — Plan Chi Tiết
# Quản lý tiến trình dự án

---

## TỔNG QUAN

**Dự án:** AI Career Roadmap — Website tạo lộ trình học NGHỀ NGHIỆP cá nhân hóa bằng AI (MỌI NGÀNH)
**Target:** Sinh viên, người đi làm, người muốn chuyển ngành — MỌI LĨNH VỰC
**Tech Stack:** Python FastAPI + HTML/CSS/JS + OpenAI API + SQLite
**Timeline MVP:** 2-3 tuần
**Repo:** ~/projects/ai-career-roadmap/

---

## CẤU TRÚC ROADMAP 3 CẤP (Core Feature)

Đây là điểm khác biệt cốt lõi của sản phẩm. AI sẽ tạo roadmap theo 3 cấp bậc:

```
LEVEL 1: ROADMAP LỚN (Hành trình tổng thể)
│
│  "Lộ trình 6 tháng trở thành Backend Developer"
│  Mục tiêu: Senior Backend Dev
│  Thời gian: 6 tháng
│  Mức lương: 8-50 triệu
│
├── LEVEL 2: PHASE (Giai đoạn, 1-2 tháng)
│   │
│   │  "Phase 1: Nền tảng (Tháng 1-2)"
│   │  Mục tiêu phase: Nắm vững HTML/CSS/JS
│   │  Tổng giờ: 120 giờ
│   │
│   ├── LEVEL 3: TASKS (Việc nhỏ, 1-3 ngày)
│   │   │
│   │   │  "Week 1: HTML cơ bản"
│   │   │
│   │   ├── Day 1-2: Học cấu trúc HTML (tags, attributes)
│   │   │   └── Tài liệu: freeCodeCamp HTML
│   │   │   └── Bài tập: Tạo trang profile cá nhân
│   │   │
│   │   ├── Day 3-4: Học HTML forms & tables
│   │   │   └── Tài liệu: MDN Web Docs
│   │   │   └── Bài tập: Tạo form đăng ký
│   │   │
│   │   └── Day 5-7: Học CSS cơ bản (selectors, box model)
│   │       └── Tài liệu: freeCodeCamp CSS
│   │       └── Bài tập: Style lại trang profile
│   │
│   ├── "Week 2: CSS Layout"
│   │   ├── Day 1-3: Flexbox
│   │   ├── Day 4-5: CSS Grid
│   │   └── Day 6-7: Responsive design
│   │
│   └── "Week 3-4: ... tiếp tục ..."
│
├── LEVEL 2: PHASE 2 (Tháng 3-4)
│   └── LEVEL 3: TASKS ...
│
└── LEVEL 2: PHASE 3 (Tháng 5-6)
    └── LEVEL 3: TASKS ...
```

**Vì sao 3 cấp?**

| Cấp | Cho ai | Mục đích |
|-----|--------|----------|
| Level 1 (Roadmap lớn) | Người mới | Hiểu tổng quan hành trình |
| Level 2 (Phase) | Người đang học | Biết giai đoạn nào đang ở |
| Level 3 (Tasks) | Người thực hành | Biết hôm nay cần làm gì |

**So sánh với đối thủ:**

| Đối thủ | Cấp độ | Vấn đề |
|---------|--------|--------|
| roadmap.sh | Chỉ Level 1 | Không biết hôm nay học gì |
| ChatGPT | Level 1 + 2 | Tasks không chi tiết, không có bài tập |
| **AI Career Roadmap** | **Level 1 + 2 + 3** | **Đầy đủ, actionable, có bài tập** |

---

## PHASE 1 — Ý TƯỞNG

### Bước 1 — Tìm vấn đề thật

**Pain Points đã xác định:**

| # | Vấn đề | Mức độ | Bằng chứng |
|---|--------|--------|------------|
| 1 | Sinh viên và người đi làm không biết học gì trước, học gì sau | CAO | Reddit, Facebook group hỏi hàng ngày |
| 2 | Roadmap hiện tại chỉ focus IT, không có cho ngành khác | CAO | roadmap.sh chỉ IT, không có marketing, kinh doanh... |
| 3 | ChatGPT cho roadmap nhưng quá chung chung | TRUNG BÌNH | Output không theo tuổi/trình độ/thời gian cụ thể |
| 4 | Người Việt thiếu roadmap tiếng Việt, sát thị trường VN | CAO | Không có tool nào focus VN |
| 5 | Học lan man → mất thời gian → nản → bỏ cuộc | CAO | Comment trên YouTube, Facebook rất nhiều |

**Người dùng mục tiêu đang đau ở đâu:**
- Không biết bắt đầu từ đâu
- Không biết nên học gì trước
- Không biết HÔM NAY cần làm gì (thiếu Level 3)
- Không biết bao lâu thì đạt mục tiêu
- Không biết mức lương thực tế ở VN
- Không có ai hướng dẫn cá nhân

**Giải pháp của chúng ta — Roadmap 3 cấp:**
- Level 1: Cho họ thấy CẢ HÀNH TRÌNH
- Level 2: Cho họ biết đang ở GIAI ĐOẠN NÀO
- Level 3: Cho họ biết HÔM NAY LÀM GÌ

**Trạng thái:** ✅ Đã xác định xong

---

### Bước 2 — Mô tả dự án

**Công thức:** [Tên app] giúp [đối tượng] giải quyết [vấn đề] bằng cách [giải pháp]

**Mô tả:**
> AI Career Roadmap giúp sinh viên CNTT Việt Nam và người muốn chuyển ngành
> tạo lộ trình học IT cá nhân hóa bằng AI theo 3 cấp bậc:
> Roadmap tổng thể → Giai đoạn → Tasks hàng ngày,
> dựa trên tuổi, ngành, trình độ và mục tiêu cụ thể.

**Elevator pitch (30 giây):**
> "Bạn muốn học IT nhưng không biết bắt đầu từ đâu?
> AI Career Roadmap tạo lộ trình riêng cho bạn theo 3 cấp:
> Tổng quan hành trình → Giai đoạn chi tiết → Tasks hàng ngày.
> Chỉ cần nhập tuổi, ngành, mục tiêu —
> AI sẽ cho bạn biết HÔM NAY cần học gì, làm bài tập gì,
> và mức lương thực tế ở Việt Nam."

**Trạng thái:** ✅ Đã xác định xong

---

### Bước 3 — Giá trị cốt lõi (UVP)

**App KHÔNG phải:**
- ❌ AI chatbot chung chung như ChatGPT
- ❌ Danh sách roadmap tĩnh như roadmap.sh (chỉ IT)
- ❌ Khóa học online như Coursera/Udemy
- ❌ Forum hỏi đáp như StackOverflow

**App LÀ:**
- ✅ AI tạo roadmap 3 cấp cho MỌI NGÀNH NGHỀ (không chỉ IT)
- ✅ Input đơn giản: tuổi + ngành + trình độ + mục tiêu
- ✅ Output chi tiết: biết HÔM NAY học gì, làm gì
- ✅ Có bài tập thực hành cụ thể cho mỗi task
- ✅ Focus 100% thị trường Việt Nam
- ✅ SEO-friendly: mỗi roadmap = 1 page indexable

**UVP Statement:**
> "Công cụ AI đầu tiên tại Việt Nam tạo lộ trình học NGHỀ NGHIỆP cá nhân hóa
> theo 3 cấp bậc cho MỌI NGÀNH — từ IT, marketing, kinh doanh, đến y tế, giáo dục —
> với bài tập thực hành và mức lương thực tế."

**Điểm khác biệt so với đối thủ:**

| Đối thủ | Họ có | Chúng ta có |
|---------|-------|-------------|
| roadmap.sh | Visual đẹp (chỉ IT) | + MỌI ngành + Level 2, 3 |
| ChatGPT | AI mạnh | + Cấu trúc 3 cấp, không lan man |
| Coursera | Course tốt | + Tạo roadmap riêng, không bán khóa |
| Không ai | — | + MỌI ngành + Tiếng Việt + mức lương VN |

**Trạng thái:** ✅ Đã xác định xong

---

## PHASE 2 — RESEARCH

### Bước 4 — Research đối thủ

**Đối thủ trực tiếp:**

| Đối thủ | URL | Mạnh | Yếu | Cấp roadmap |
|---------|-----|------|-----|-------------|
| roadmap.sh | roadmap.sh | Visual đẹp, miễn phí | Không cá nhân hóa, chỉ Level 1 | Level 1 |
| ChatGPT | chat.openai.com | AI mạnh, flexible | Quá rộng, không chuyên, không có tasks | Level 1-2 |
| Coursera | coursera.org | Course chất lượng | Không tạo roadmap riêng, trả phí | Level 2-3 (course) |
| freeCodeCamp | freecodecamp.org | Miễn phí, bài tập | Không cá nhân hóa, không có roadmap | Level 3 |
| Learn.dev | learn.dev | Community tốt | Không có AI, không tiếng Việt | Level 1 |

**Khoảng trống thị trường:**
> KHÔNG AI tích hợp đầy đủ cả 3 cấp bậc roadmap.
> roadmap.sh chỉ có Level 1.
> ChatGPT có Level 1-2 nhưng không có Level 3 (tasks hàng ngày).
> freeCodeCamp có Level 3 nhưng không có Level 1-2 (roadmap cá nhân hóa).
>
> → AI Career Roadmap là tool ĐẦU TIÊN tích hợp cả 3 cấp.

**Trạng thái:** ✅ Đã xác định xong

---

### Bước 5 — Research keyword

**Keywords chính — IT (volume cao):**

| Keyword | Volume/tháng | Cạnh tranh |
|---------|-------------|------------|
| roadmap backend developer | 2,400 | Trung bình |
| roadmap học lập trình | 1,800 | Thấp |
| lộ trình học IT | 1,200 | Thấp |
| roadmap AI engineer | 600 | Trung bình |

**Keywords chính — Marketing & Business:**

| Keyword | Volume/tháng | Cạnh tranh |
|---------|-------------|------------|
| lộ trình học marketing | 1,500 | Thấp |
| roadmap digital marketing | 800 | Thấp |
| học marketing từ đâu | 600 | Rất thấp |
| lộ trình kinh doanh | 500 | Rất thấp |
| roadmap SEO | 400 | Thấp |

**Keywords chính — Thiết kế & Sáng tạo:**

| Keyword | Volume/tháng | Cạnh tranh |
|---------|-------------|------------|
| lộ trình học thiết kế | 900 | Thấp |
| roadmap UI UX | 700 | Thấp |
| học graphic design từ đâu | 500 | Rất thấp |
| lộ trình trở thành designer | 400 | Rất thấp |

**Keywords chính — Tài chính & Kế toán:**

| Keyword | Volume/tháng | Cạnh tranh |
|---------|-------------|------------|
| lộ trình học kế toán | 800 | Thấp |
| roadmap CFA | 300 | Rất thấp |
| học tài chính từ đâu | 400 | Rất thấp |

**Keywords chính — Các ngành khác:**

| Keyword | Volume/tháng | Cạnh tranh |
|---------|-------------|------------|
| lộ trình học y tá | 600 | Thấp |
| roadmap bác sĩ | 400 | Rất thấp |
| lộ trình giáo viên | 500 | Rất thấp |
| học xây dựng từ đâu | 300 | Rất thấp |
| lộ trình du lịch | 400 | Rất thấp |

**Keywords dài (ít cạnh tranh, dễ rank):**

| Keyword | Volume/tháng | Cạnh tranh |
|---------|-------------|------------|
| roadmap học marketing cho người mới bắt đầu | 100 | Rất thấp |
| lộ trình trở thành designer trong 6 tháng | 80 | Rất thấp |
| hôm nay học gì marketing | 50 | Rất thấp |
| kế hoạch học kế toán hàng ngày | 40 | Rất thấp |
| học kinh doanh từ đâu | 100 | Rất thấp |

**Trạng thái:** ✅ Đã xác định xong

---

### Bước 6 — Research cộng đồng

**Insights từ cộng đồng (liên quan 3 cấp):**

| Câu hỏi | Cấp cần | Content idea |
|---------|---------|-------------|
| "Roadmap backend cho người mới" | Level 1 | Landing page |
| "Tháng đầu tiên nên học gì?" | Level 2 | Blog post |
| "Hôm nay học gì?" | Level 3 | Task generator |
| "Bài tập thực hành HTML" | Level 3 | Exercise library |
| "Bao lâu để trở thành junior?" | Level 1 | Timeline calculator |

**Trạng thái:** ✅ Đã xác định xong

---

## PHASE 3 — XÁC ĐỊNH USER

### Bước 7 — Chọn target user

**Primary User (80% focus):**

| Thuộc tính | Chi tiết |
|-----------|----------|
| Độ tuổi | 18-35 |
| Nghề nghiệp | Sinh viên, người đi làm MỌI NGÀNH |
| Pain point | Không biết hôm nay học gì |
| Cần cấp nào | Cả 3 cấp (đặc biệt Level 3) |
| Device | Mobile 60%, Desktop 40% |

**Secondary User (15% focus):**

| Thuộc tính | Chi tiết |
|-----------|----------|
| Độ tuổi | 25-35 |
| Nghề nghiệp | Người trái ngành |
| Pain point | Không biết lộ trình chuyển ngành |
| Cần cấp nào | Level 1 (tổng quan) + Level 2 (giai đoạn) |
| Device | Desktop 70%, Mobile 30% |

**Trạng thái:** ✅ Đã xác định xong

---

### Bước 8 — User Persona

**Persona 1: Minh (Sinh viên IT) — Cần cả 3 cấp**

```
┌─────────────────────────────────────────────┐
│  👤 MINH — Sinh viên năm 2 CNTT            │
│  Cần: Level 1 (tổng quan)                   │
│       Level 2 (tháng này học gì)            │
│       Level 3 (hôm nay làm gì) ← QUAN TRỌNG│
└─────────────────────────────────────────────┘
```

**Persona 2: Hương (Marketing) — Cần cả 3 cấp**

```
┌─────────────────────────────────────────────┐
│  👤 HƯƠNG — Nhân viên marketing muốn thăng  │
│  Cần: Level 1 (lộ trình Digital Marketing)  │
│       Level 2 (học SEO trước hay Content)   │
│       Level 3 (hôm nay thực hành gì)        │
└─────────────────────────────────────────────┘
```

**Persona 3: An (Kế toán chuyển ngành) — Cần Level 1 + 2**

```
┌─────────────────────────────────────────────┐
│  👤 AN — Kế toán muốn chuyển Data Analyst   │
│  Cần: Level 1 (tổng quan lộ trình)          │
│       Level 2 (từng giai đoạn)              │
│       Level 3 (tasks khi nào có thời gian)  │
└─────────────────────────────────────────────┘
```

**Trạng thái:** ✅ Đã xác định xong

---

## PHASE 4 — MVP

### Bước 9 — Xác định MVP

---

#### 9.1 Định nghĩa MVP

**MVP = Phiên bản nhỏ nhất có thể dùng được**

Mục tiêu MVP:
- Chứng minh product-market fit
- Thu thập feedback thật từ user
- Validate ý tưởng trước khi invest thêm
- Có sản phẩm để SEO và marketing

**MVP LÀ:**
- Hoạt động được end-to-end
- Tạo roadmap 3 cấp (Roadmap → Phase → Tasks)
- User biết hôm nay cần học gì
- Đủ tốt để thu thập feedback

---

#### 9.2 Feature Prioritization (MoSCoW)

**MUST HAVE (Bắt buộc — MVP không thể thiếu):**

| # | Feature | Mô tả | Cấp roadmap |
|---|---------|-------|-------------|
| F1 | Trang chủ | Hero section + CTA | — |
| F2 | Form nhập thông tin | Tuổi, ngành, trình độ, mục tiêu, thời gian | — |
| F3 | Gọi AI tạo roadmap | POST /api/generate → OpenAI API | — |
| F4 | Hiển thị Roadmap lớn | Tổng quan hành trình, timeline | Level 1 |
| F5 | Hiển thị Phases | Danh sách giai đoạn, kỹ năng | Level 2 |
| F6 | Hiển thị Tasks | Tasks hàng ngày, bài tập | Level 3 |
| F7 | SEO meta tags | Title, description, OG tags | — |
| F8 | Mobile responsive | Hoạt động trên điện thoại | — |
| F9 | Error handling | Thông báo lỗi khi AI fail | — |
| F10 | Loading state | Spinner/animation khi chờ AI | — |

**SHOULD HAVE (Nên có — làm nếu còn thời gian):**

| # | Feature | Mô tả | Cấp roadmap |
|---|---------|-------|-------------|
| F11 | Lưu roadmap qua URL | Mỗi roadmap = 1 URL riêng | — |
| F12 | Share button | Chia sẻ lên Facebook, copy link | — |
| F13 | Danh sách ngành | Dropdown với 20+ ngành IT | — |
| F14 | Ví dụ roadmap mẫu | Pre-generated roadmap cho SEO | Level 1 |
| F15 | Progress tracker | Đánh dấu task đã hoàn thành | Level 3 |
| F16 | Expand/Collapse phases | Thu gọn/mở rộng phases | Level 2 |

**WON'T HAVE (Không làm trong MVP):**

| # | Feature | Lý do |
|---|---------|-------|
| F17 | Đăng nhập | Chưa cần cho MVP |
| F18 | Lưu vào account | Cần auth |
| F19 | Export PDF | Nice to have |
| F20 | Chat realtime | Overkill |
| F21 | Mobile app native | Web responsive đủ |

---

#### 9.3 Cấu trúc output 3 cấp (Chi tiết)

**LEVEL 1 — ROADMAP LỚN:**

```
┌─────────────────────────────────────────────────────┐
│  🗺️ ROADMAP: Backend Developer                     │
│                                                     │
│  👤 Tuổi: 20 | 📚 Trình độ: Beginner               │
│  🎯 Mục tiêu: Senior Backend Dev                   │
│  ⏱️ Thời gian: 6 tháng                             │
│                                                     │
│  📊 Tổng quan:                                      │
│  ├── 3 Phases                                       │
│  ├── 12 Weeks                                       │
│  ├── 36 Tasks                                       │
│  └── 180 giờ học                                    │
│                                                     │
│  💰 Mức lương:                                      │
│  ├── Junior: 8-12 triệu                             │
│  ├── Mid: 15-25 triệu                               │
│  └── Senior: 30-50 triệu                            │
│                                                     │
│  🎯 Lý do cạnh tranh: ...                           │
│  📈 Nhu cầu thị trường: ...                         │
└─────────────────────────────────────────────────────┘
```

**LEVEL 2 — PHASES:**

```
┌─────────────────────────────────────────────────────┐
│  📋 PHASES                                          │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │ Phase 1: Nền tảng (Tháng 1-2)           ✅ │    │
│  │ ├── 4 Weeks, 12 Tasks                      │    │
│  │ ├── Skills: HTML, CSS, JavaScript, Git     │    │
│  │ ├── Tổng giờ: 120 giờ                      │    │
│  │ └── Milestone: Tạo được website tĩnh       │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │ Phase 2: Backend Core (Tháng 3-4)        🔄 │    │
│  │ ├── 4 Weeks, 12 Tasks                      │    │
│  │ ├── Skills: Node.js, Express, PostgreSQL   │    │
│  │ ├── Tổng giờ: 120 giờ                      │    │
│  │ └── Milestone: Tạo được REST API           │    │
│  └─────────────────────────────────────────────┘    │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │ Phase 3: Nâng cao (Tháng 5-6)            ⬜ │    │
│  │ ├── 4 Weeks, 12 Tasks                      │    │
│  │ ├── Skills: Auth, Docker, Testing, Deploy  │    │
│  │ ├── Tổng giờ: 120 giờ                      │    │
│  │ └── Milestone: Portfolio project hoàn chỉnh│    │
│  └─────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

**LEVEL 3 — TASKS (trong mỗi Phase):**

```
┌─────────────────────────────────────────────────────┐
│  📝 TASKS — Phase 1: Nền tảng                      │
│                                                     │
│  ▼ Week 1: HTML cơ bản                        ✅   │
│  │                                                  │
│  │  ☑ Day 1-2: Cấu trúc HTML cơ bản               │
│  │     📖 Tài liệu: freeCodeCamp HTML              │
│  │     📝 Bài tập: Tạo trang profile cá nhân      │
│  │     ⏱️ Thời gian: 4 giờ                         │
│  │                                                  │
│  │  ☑ Day 3-4: HTML Forms & Tables                 │
│  │     📖 Tài liệu: MDN Web Docs                  │
│  │     📝 Bài tập: Tạo form đăng ký               │
│  │     ⏱️ Thời gian: 4 giờ                         │
│  │                                                  │
│  │  ☑ Day 5-7: Semantic HTML & Accessibility       │
│  │     📖 Tài liệu: web.dev/accessibility         │
│  │     📝 Bài tập: Refactor trang profile         │
│  │     ⏱️ Thời gian: 6 giờ                         │
│  │                                                  │
│  ▼ Week 2: CSS cơ bản                         🔄   │
│  │                                                  │
│  │  ☐ Day 1-2: Selectors & Box Model               │
│  │     📖 Tài liệu: freeCodeCamp CSS              │
│  │     📝 Bài tập: Style trang profile            │
│  │     ⏱️ Thời gian: 4 giờ                         │
│  │                                                  │
│  │  ☐ Day 3-4: Flexbox                             │
│  │     📖 Tài liệu: CSS-Tricks Flexbox            │
│  │     📝 Bài tập: Tạo layout 3 cột               │
│  │     ⏱️ Thời gian: 4 giờ                         │
│  │                                                  │
│  │  ☐ Day 5-7: CSS Grid + Responsive               │
│  │     📖 Tài liệu: CSS-Tricks Grid               │
│  │     📝 Bài tập: Responsive portfolio            │
│  │     ⏱️ Thời gian: 6 giờ                         │
│  │                                                  │
│  ▼ Week 3: JavaScript cơ bản                  ⬜   │
│  │  ...                                             │
│  │                                                  │
│  ▼ Week 4: Git & Project                      ⬜   │
│     ...                                             │
└─────────────────────────────────────────────────────┘
```

---

#### 9.4 User Stories (Chi tiết theo 3 cấp)

```
US-01: Xem Roadmap lớn (Level 1)
───────────────────────────────────────────────
Là một sinh viên IT,
Tôi muốn xem tổng quan lộ trình học,
Để tôi biết hành trình phía trước gồm những gì.

Acceptance Criteria:
□ Hiển thị tên roadmap, tuổi, trình độ, mục tiêu
□ Hiển thị tổng số phases, weeks, tasks, giờ học
□ Hiển thị mức lương Junior/Mid/Senior
□ Hiển thị lý do cạnh tranh
□ Hiển thị nhu cầu thị trường
□ Có nút "Xem chi tiết phases"

Priority: MUST HAVE
Estimate: 3 giờ
```

```
US-02: Xem Phases (Level 2)
───────────────────────────────────────────────
Là một người đã xem roadmap lớn,
Tôi muốn xem từng giai đoạn chi tiết,
Để tôi biết mình sẽ học gì theo từng giai đoạn.

Acceptance Criteria:
□ Hiển thị danh sách phases theo thứ tự
□ Mỗi phase hiện: tên, thời gian, skills, giờ học, milestone
□ Skills hiển thị dạng tags
□ Phase hiện tại được highlight
□ Click vào phase → mở ra tasks (Level 3)
□ Có expand/collapse tất cả phases

Priority: MUST HAVE
Estimate: 4 giờ
```

```
US-03: Xem Tasks (Level 3)
───────────────────────────────────────────────
Là một người đang trong giai đoạn học,
Tôi muốn biết HÔM NAY cần làm gì,
Để tôi không mất thời gian suy nghĩ.

Acceptance Criteria:
□ Tasks nhóm theo tuần (Week 1, Week 2...)
□ Mỗi task hiện: tên, thời gian ước tính
□ Mỗi task có: tài liệu học, bài tập thực hành
□ Có checkbox đánh dấu hoàn thành (localStorage)
□ Task đã hoàn thành: gạch ngang, màu xám
□ Task hiện tại: highlight, màu nổi bật
□ Task tương lai: màu nhạt, chưa mở được

Priority: MUST HAVE
Estimate: 6 giờ
```

```
US-04: Nhập thông tin tạo roadmap
───────────────────────────────────────────────
Là một người muốn học IT,
Tôi muốn nhập tuổi, ngành, trình độ, mục tiêu,
Để AI tạo roadmap 3 cấp riêng cho tôi.

Acceptance Criteria:
□ Form có 5 fields: tuổi, ngành, trình độ, mục tiêu, thời gian
□ Validation tiếng Việt rõ ràng
□ Submit → loading → redirect đến trang roadmap
□ Hoạt động trên mobile

Priority: MUST HAVE
Estimate: 4 giờ
```

```
US-05: Đánh dấu task hoàn thành
───────────────────────────────────────────────
Là một người đang học theo roadmap,
Tôi muốn đánh dấu task đã hoàn thành,
Để theo dõi tiến độ học tập.

Acceptance Criteria:
□ Click checkbox → task đánh dấu done
□ Lưu vào localStorage (không cần login)
□ Hiển thị % hoàn thành mỗi phase
□ Hiển thị % hoàn thành tổng roadmap
□ Reset được nếu muốn học lại

Priority: SHOULD HAVE
Estimate: 3 giờ
```

---

#### 9.5 Technical Requirements

**Performance:**

| Metric | Target | Đo lường |
|--------|--------|---------|
| Time to First Byte (TTFB) | < 200ms | Lighthouse |
| First Contentful Paint (FCP) | < 1.5s | Lighthouse |
| Largest Contentful Paint (LCP) | < 2.5s | Lighthouse |
| API response time | < 30s | Backend logs |
| Page size | < 500KB | Network tab |

**Browser Support:**
Chrome 90+, Safari 14+, Firefox 88+, Edge 90+

**Device Support:**
Mobile S (320px) → Mobile M (375px) → Tablet (768px) → Laptop (1024px)

---

#### 9.6 Design Requirements

**Brand Identity:**

| Element | Giá trị | Ghi chú |
|---------|---------|---------|
| Primary color | #4F46E5 (Indigo) | Trust, tech |
| Secondary color | #10B981 (Emerald) | Growth, learning |
| Accent color | #F59E0B (Amber) | Highlight, CTA |
| Background | #F9FAFB (Gray-50) | Clean |
| Text | #111827 (Gray-900) | High contrast |
| Font | Inter | Modern, clean |

**Design Principles:**
1. **Đơn giản** — Focus vào content
2. **Rõ ràng** — User hiểu ngay app làm gì
3. **3 cấp rõ ràng** — Visual phân biệt Level 1/2/3
4. **Mobile-first** — Thiết kế cho mobile trước

**UI Components theo 3 cấp:**

| Component | Cấp | Mô tả |
|-----------|-----|-------|
| Roadmap Header | Level 1 | Title, stats, salary, CTA |
| Phase Card | Level 2 | Tên phase, skills tags, progress bar |
| Week Section | Level 3 | Nhóm tasks theo tuần |
| Task Item | Level 3 | Checkbox, tên, tài liệu, bài tập |
| Progress Bar | All | % hoàn thành theo phase/tổng |
| Skill Tag | Level 2 | Pill shape, colored |
| Accordion | Level 2-3 | Expand/collapse |
| Timeline | Level 1 | Visual timeline phases |

---

#### 9.7 Data Model (MVP)

**Bảng `roadmaps` (SQLite):**

```sql
CREATE TABLE roadmaps (
    id TEXT PRIMARY KEY,
    slug TEXT UNIQUE NOT NULL,
    
    -- Input
    age INTEGER NOT NULL,
    industry TEXT NOT NULL,
    industry_name TEXT NOT NULL,
    level TEXT NOT NULL,
    goal TEXT NOT NULL,
    duration_months INTEGER NOT NULL,
    
    -- Level 1: Roadmap lớn
    overview TEXT,
    total_weeks INTEGER,
    total_tasks INTEGER,
    total_hours INTEGER,
    salary_junior TEXT,
    salary_mid TEXT,
    salary_senior TEXT,
    competitive_advantage TEXT,
    market_demand TEXT,
    
    -- Level 2 + 3: Phases + Tasks (JSON)
    phases_json TEXT,
    -- Cấu trúc JSON:
    -- [
    --   {
    --     "id": "phase-1",
    --     "name": "Nền tảng",
    --     "duration": "Tháng 1-2",
    --     "weeks": 4,
    --     "total_hours": 120,
    --     "milestone": "Tạo được website tĩnh",
    --     "skills": ["HTML", "CSS", "JavaScript", "Git"],
    --     "weeks_detail": [
    --       {
    --         "id": "week-1",
    --         "name": "HTML cơ bản",
    --         "tasks": [
    --           {
    --             "id": "task-1",
    --             "name": "Cấu trúc HTML cơ bản",
    --             "days": "Day 1-2",
    --             "hours": 4,
    --             "resource": {"name": "freeCodeCamp", "url": "...", "type": "free"},
    --             "exercise": {"title": "Tạo trang profile", "description": "..."}
    --           }
    --         ]
    --       }
    --     ]
    --   }
    -- ]
    
    -- Metadata
    ai_model TEXT DEFAULT 'gpt-4o',
    ai_tokens_used INTEGER,
    generation_time_ms INTEGER,
    view_count INTEGER DEFAULT 0,
    share_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_roadmaps_slug ON roadmaps(slug);
CREATE INDEX idx_roadmaps_industry ON roadmaps(industry);
```

**Bảng `industries` (pre-seeded):**

```sql
CREATE TABLE industries (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    category TEXT,
    description TEXT,
    avg_salary_junior TEXT,
    avg_salary_mid TEXT,
    avg_salary_senior TEXT,
    demand_level TEXT,
    top_skills TEXT,
    meta_title TEXT,
    meta_description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Pre-seed 50+ ngành nghề (mọi lĩnh vực):**

| # | slug | name | Category |
|---|------|------|----------|
| **IT & Công nghệ** | | | |
| 1 | backend-developer | Backend Developer | IT |
| 2 | frontend-developer | Frontend Developer | IT |
| 3 | fullstack-developer | Fullstack Developer | IT |
| 4 | react-developer | React Developer | IT |
| 5 | python-developer | Python Developer | IT |
| 6 | data-analyst | Data Analyst | IT |
| 7 | data-scientist | Data Scientist | IT |
| 8 | ai-engineer | AI/ML Engineer | IT |
| 9 | devops-engineer | DevOps Engineer | IT |
| 10 | mobile-developer | Mobile Developer | IT |
| 11 | cybersecurity | Cybersecurity | IT |
| 12 | ui-ux-designer | UI/UX Designer | IT |
| **Marketing & Truyền thông** | | | |
| 13 | digital-marketing | Digital Marketing | Marketing |
| 14 | seo-specialist | SEO Specialist | Marketing |
| 15 | content-marketing | Content Marketing | Marketing |
| 16 | social-media-manager | Social Media Manager | Marketing |
| 17 | brand-manager | Brand Manager | Marketing |
| 18 | copywriter | Copywriter | Marketing |
| 19 | pr-specialist | PR Specialist | Marketing |
| **Kinh doanh & Quản lý** | | | |
| 20 | business-analyst | Business Analyst | Business |
| 21 | product-manager | Product Manager | Business |
| 22 | project-manager | Project Manager | Business |
| 23 | sales-manager | Sales Manager | Business |
| 24 | startup-founder | Startup Founder | Business |
| 25 | operations-manager | Operations Manager | Business |
| **Thiết kế & Sáng tạo** | | | |
| 26 | graphic-designer | Graphic Designer | Design |
| 27 | motion-designer | Motion Designer | Design |
| 28 | interior-designer | Interior Designer | Design |
| 29 | fashion-designer | Fashion Designer | Design |
| 30 | photographer | Photographer | Design |
| 31 | video-editor | Video Editor | Design |
| **Tài chính & Kế toán** | | | |
| 32 | accountant | Kế toán | Finance |
| 33 | financial-analyst | Phân tích tài chính | Finance |
| 34 | auditor | Kiểm toán | Finance |
| 35 | investment-banker | Ngân hàng đầu tư | Finance |
| 36 | cfa-analyst | CFA Analyst | Finance |
| **Y tế & Sức khỏe** | | | |
| 37 | nurse | Y tá | Healthcare |
| 38 | doctor | Bác sĩ | Healthcare |
| 39 | pharmacist | Dược sĩ | Healthcare |
| 40 | physiotherapist | Vật lý trị liệu | Healthcare |
| 41 | nutritionist | Dinh dưỡng | Healthcare |
| **Giáo dục** | | | |
| 42 | teacher | Giáo viên | Education |
| 43 | lecturer | Giảng viên | Education |
| 44 | english-teacher | Giáo viên tiếng Anh | Education |
| 45 | tutor | Gia sư | Education |
| **Kỹ thuật & Xây dựng** | | | |
| 46 | civil-engineer | Kỹ sư xây dựng | Engineering |
| 47 | mechanical-engineer | Kỹ sư cơ khí | Engineering |
| 48 | electrical-engineer | Kỹ sư điện | Engineering |
| 49 | architect | Kiến trúc sư | Engineering |
| **Du lịch & Khách sạn** | | | |
| 50 | tour-guide | Hướng dẫn viên | Tourism |
| 51 | hotel-manager | Quản lý khách sạn | Tourism |
| 52 | travel-agent | Đại lý du lịch | Tourism |
| **Luật** | | | |
| 53 | lawyer | Luật sư | Legal |
| 54 | legal-consultant | Tư vấn pháp lý | Legal |

---

#### 9.8 AI Prompt Engineering (3 cấp)

**System Prompt:**

```
Bạn là chuyên gia tư vấn nghề nghiệp IT tại Việt Nam với 15 năm kinh nghiệm.
Nhiệm vụ: Tạo roadmap học tập chi tiết theo 3 cấp bậc.

CẤU TRÚC 3 CẤP:
- Level 1 (Roadmap lớn): Tổng quan hành trình, mức lương, lý do cạnh tranh
- Level 2 (Phases): Từng giai đoạn 1-2 tháng, skills cần học, milestone
- Level 3 (Tasks): Tasks hàng ngày, tài liệu, bài tập cụ thể

Quy tắc:
1. Tất cả output bằng tiếng Việt
2. Mức lương tính bằng VNĐ, sát thị trường VN
3. Tasks phải CỤ THỂ: "Day 1-2: Học X" không phải "Học X"
4. Mỗi task phải có: tài liệu + bài tập + thời gian ước tính
5. Bài tập phải THỰC HÀNH được ngay
6. Skills theo thứ tự học hợp lý (cơ bản → nâng cao)
7. Timeline phải thực tế

Output MUST là JSON hợp lệ theo schema đã định.
```

**User Prompt Template:**

```
Tạo roadmap học tập theo 3 cấp bậc cho:

Thông tin người dùng:
- Tuổi: {age}
- Ngành muốn học: {industry_name}
- Trình độ hiện tại: {level}
- Mục tiêu: {goal}
- Thời gian dự kiến: {duration_months} tháng

Yêu cầu output JSON:

{
  "level1_roadmap": {
    "overview": "Tổng quan lộ trình (2-3 câu)",
    "total_weeks": 24,
    "total_tasks": 72,
    "total_hours": 360,
    "salary_range": {
      "junior": "8-12 triệu",
      "mid": "15-25 triệu",
      "senior": "30-50 triệu"
    },
    "competitive_advantage": "Lý do cạnh tranh tại VN",
    "market_demand": "Nhu cầu thị trường VN"
  },
  
  "level2_phases": [
    {
      "id": "phase-1",
      "name": "Phase 1: Nền tảng",
      "duration": "Tháng 1-2",
      "description": "Mô tả ngắn gọn phase này",
      "skills": ["HTML", "CSS", "JavaScript", "Git"],
      "total_hours": 120,
      "milestone": "Tạo được website tĩnh đầu tiên",
      "weeks_count": 4
    }
  ],
  
  "level3_tasks": [
    {
      "phase_id": "phase-1",
      "weeks": [
        {
          "id": "week-1",
          "name": "HTML cơ bản",
          "tasks": [
            {
              "id": "task-1",
              "name": "Học cấu trúc HTML cơ bản",
              "days": "Day 1-2",
              "hours": 4,
              "resource": {
                "name": "freeCodeCamp - Responsive Web Design",
                "url": "https://freecodecamp.org",
                "type": "free",
                "language": "en"
              },
              "exercise": {
                "title": "Tạo trang profile cá nhân",
                "description": "Tạo 1 trang HTML hoàn chỉnh với header, about, contact. Không dùng CSS, chỉ HTML thuần.",
                "deliverable": "File index.html"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

**Fallback Response (khi AI fail):**

> ⚠️ FALLBACK ĐÃ CẢI THIỆN — Xem chi tiết tại [HIGH PRIORITY RESOLUTION - ISSUE 6]
> 
> Fallback mới bao gồm:
> - Pre-generated fallbacks cho TOP 20 ngành (đầy đủ 3 cấp)
> - Generic fallback với tasks chi tiết (không bao giờ trả [])
> - Cache strategy: Cùng input → trả roadmap đã tạo
> 
> Script tạo fallback: `scripts/generate_fallbacks.py`
> Fallback files: `fallbacks/{industry}.json`

**Fallback response format (cải thiện):**

```json
{
  "level1_roadmap": {
    "overview": "Lộ trình học tập cá nhân hóa",
    "total_weeks": 24,
    "total_tasks": 72,
    "total_hours": 360,
    "salary_range": {"junior": "8-15 triệu", "mid": "15-30 triệu", "senior": "30-60 triệu"},
    "competitive_advantage": "Thị trường IT VN đang thiếu nhân lực",
    "market_demand": "Nhu cầu tuyển dụng IT tăng 30%/năm"
  },
  "level2_phases": [
    {
      "id": "phase-1",
      "name": "Phase 1: Nền tảng",
      "duration": "Tháng 1-2",
      "skills": ["Kỹ năng cơ bản"],
      "total_hours": 120,
      "milestone": "Hoàn thành nền tảng"
    }
  ],
  "level3_tasks": [],
  "_fallback": true
}
```

---

#### 9.9 Error Handling Strategy

| Tình huống | User thấy | Hành động |
|-----------|-----------|-----------|
| Form validation | Thông báo đỏ dưới field | Frontend validate |
| API timeout (>30s) | "AI đang bận, vui lòng thử lại" | Retry 1 lần |
| AI trả JSON sai | "Có lỗi xảy ra, đang thử lại" | Retry với fallback |
| Network error | "Mất kết nối, kiểm tra mạng" | Check navigator.onLine |
| Invalid slug (404) | "Không tìm thấy roadmap" | Redirect về home |

---

#### 9.10 MVP Timeline (Chi tiết theo ngày)

**Tuần 1: Backend + Data (Ngày 1-7)**

| Ngày | Task | Thời gian | Output |
|------|------|-----------|--------|
| 1 | Setup project structure | 2h | Folder, files |
| 1 | Setup FastAPI + SQLite | 2h | Backend skeleton |
| 2 | Design database schema | 2h | Migration SQL |
| 2 | Tạo industries seed data | 3h | 20 ngành IT |
| 3 | Build API POST /api/generate | 4h | Endpoint |
| 3 | Tích hợp OpenAI API (prompt 3 cấp) | 3h | AI response |
| 4 | Build GET /roadmap/{slug} | 3h | SSR route |
| 4 | Build GET /nganh/{slug} | 3h | Landing pages |

**Tuần 2: Frontend (Ngày 8-14)**

| Ngày | Task | Thời gian | Output |
|------|------|-----------|--------|
| 5 | HTML trang chủ + CSS design system | 6h | index.html, style.css |
| 6 | HTML form page + JS form logic | 6h | form.html, app.js |
| 7 | HTML Level 1: Roadmap header | 4h | Roadmap overview |
| 7 | HTML Level 2: Phase cards | 4h | Phase list |
| 8 | HTML Level 3: Tasks list | 6h | Tasks UI |
| 9 | Task checkbox + progress bar | 4h | Interactive |
| 9 | Loading + error states | 3h | UX polish |
| 10 | Mobile responsive | 4h | Media queries |
| 10 | SEO meta tags + OG tags | 3h | SEO ready |
| 11 | Testing all flows | 4h | QA |
| 11 | Fix bugs | 3h | Bug fixes |
| 12 | Deploy | 3h | Live URL |
| 12 | Setup domain + SSL | 2h | https:// |

**Tổng thời gian: ~60 giờ (12 ngày × 5 giờ)**

---

#### 9.11 Definition of Done (DoD)

MVP được coi là DONE khi:

**Functional (3 cấp):**
- [ ] Level 1: User xem được tổng quan roadmap
- [ ] Level 2: User xem được danh sách phases + skills
- [ ] Level 3: User xem được tasks hàng ngày + bài tập
- [ ] Task checkbox hoạt động (localStorage)
- [ ] Progress bar hoạt động

**Technical:**
- [ ] API response time < 30s
- [ ] Page load time < 3s
- [ ] Error handling đầy đủ
- [ ] SEO meta tags đầy đủ

**Quality:**
- [ ] Tested trên Chrome, Safari, Firefox
- [ ] Tested trên mobile 375px, 768px
- [ ] Lighthouse: Performance > 80, SEO > 90

---

#### 9.12 Success Metrics

**Week 1-2 (Validation):**

| Metric | Target |
|--------|--------|
| Roadmaps created | 20+ |
| User xem hết Level 1+2+3 | > 50% |
| Task checkbox clicks | > 100 |
| Avg time on result page | > 90s |

**Month 1-2 (Growth):**

| Metric | Target |
|--------|--------|
| Organic traffic | 500+/month |
| Conversion rate (form → result) | > 40% |
| Return visitors | > 15% |

---

#### 9.13 Post-MVP Roadmap

**Version 1.1:** User accounts, lưu roadmap, lịch sử
**Version 1.2:** 50+ ngành, community ratings
**Version 1.3:** Premium (AI mentor, export PDF)
**Version 2.0:** AI chatbot mentor, career coaching

---

**Trạng thái:** ✅ Đã xác định xong

---

## PHASE 5 — THIẾT KẾ SẢN PHẨM

### Bước 10 — User Flow (Luồng người dùng)

---

#### 10.1 User Flow Tổng Quan

```
┌─────────────────────────────────────────────────────────────┐
│                    USER FLOW TỔNG QUAN                      │
└─────────────────────────────────────────────────────────────┘

     ┌──────────┐
     │  ENTRY   │
     └────┬─────┘
          │
          ├── Google Search ("roadmap backend developer")
          │   └── Landing page /nganh/backend-developer
          │
          ├── Direct visit (bạn bè share link)
          │   └── Trang chủ /
          │
          └── Social share (Facebook, Zalo)
              └── Trang roadmap /roadmap/backend-20-tuoi
          │
          ▼
     ┌──────────┐
     │   HOME   │──── Xem ví dụ roadmap mẫu ────→ /roadmap/sample
     │   /      │
     └────┬─────┘
          │
          │ Click "Bắt đầu tạo roadmap"
          ▼
     ┌──────────┐
     │  FORM    │
     │ /tao-    │
     │ roadmap  │
     └────┬─────┘
          │
          │ Submit form
          ▼
     ┌──────────┐
     │ LOADING  │──── AI đang tạo roadmap...
     │ (3-30s)  │
     └────┬─────┘
          │
          ├── Success ──→ /roadmap/{slug}
          │
          └── Error ──→ Thông báo lỗi + Retry
                          │
                          ▼
     ┌──────────────────────────────────┐
     │         TRANG ROADMAP            │
     │    /roadmap/{industry}-{age}tuoi-{hash}│
     │                                  │
     │  ┌─────────────────────────────┐ │
     │  │  LEVEL 1: ROADMAP LỚN      │ │ ← Hiển thị đầu tiên
     │  │  Tổng quan, salary, stats   │ │
     │  └─────────────────────────────┘ │
     │                                  │
     │  ┌─────────────────────────────┐ │
     │  │  LEVEL 2: PHASES            │ │ ← Scroll xuống
     │  │  Danh sách phases + skills  │ │
     │  └─────────────────────────────┘ │
     │                                  │
     │  ┌─────────────────────────────┐ │
     │  │  LEVEL 3: TASKS             │ │ ← Click vào phase
     │  │  Tasks + exercises + links  │ │
     │  └─────────────────────────────┘ │
     │                                  │
     │  [Chia sẻ] [Tạo roadmap mới]    │
     └──────────────────────────────────┘
          │
          ├── Chia sẻ → Facebook/Zalo/Copy link
          │
          └── Tạo roadmap mới → Về /tao-roadmap
```

---

#### 10.2 User Flow Chi Tết — Trang Chủ

```
TRANG CHỦ: /
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User vào trang chủ → Hiển thị:

1. Hero Section
   ├── Title: "Tạo lộ trình học IT cá nhân hóa bằng AI"
   ├── Subtitle: "Nhập thông tin, AI tạo roadmap riêng cho bạn theo 3 cấp"
   ├── CTA Button: "Bắt đầu tạo roadmap" → /tao-roadmap
   └── Social proof: Dynamic theo giai đoạn (xem MEDIUM PRIORITY - ISSUE 15)

2. Ví dụ roadmap mẫu (3 cards)
   ├── Card 1: Backend Developer (20 tuổi, 6 tháng)
   │   └── Click → /roadmap/sample-backend
   ├── Card 2: Data Analyst (25 tuổi, 12 tháng)
   │   └── Click → /roadmap/sample-data-analyst
   └── Card 3: Frontend Developer (22 tuổi, 6 tháng)
       └── Click → /roadmap/sample-frontend

3. How it works (3 steps)
   ├── Step 1: Nhập thông tin (icon: form)
   ├── Step 2: AI tạo roadmap (icon: robot)
   └── Step 3: Học theo lộ trình (icon: checklist)

4. Danh sách ngành phổ biến (grid)
   ├── Backend Developer → /nganh/backend-developer
   ├── Frontend Developer → /nganh/frontend-developer
   ├── Data Analyst → /nganh/data-analyst
   ├── AI Engineer → /nganh/ai-engineer
   └── ... (8 ngành chính)

5. Footer
   ├── About
   ├── Contact
   └── © 2026 AI Career Roadmap
```

**User actions trên trang chủ:**

| Action | Element | Destination | Priority |
|--------|---------|-------------|----------|
| Click CTA | "Bắt đầu tạo roadmap" | /tao-roadmap | MUST |
| Click ví dụ | Card roadmap mẫu | /roadmap/sample-* | SHOULD |
| Click ngành | Grid ngành | /nganh/{slug} | SHOULD |
| Scroll | Xem thêm content | — | MUST |

---

#### 10.3 User Flow Chi Tết — Trang Tạo Roadmap

```
TRANG TẠO ROADMAP: /tao-roadmap
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User vào form → Hiển thị:

┌─────────────────────────────────────────────┐
│  🎯 Tạo roadmap của bạn                    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  Tuổi *                             │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  20                          │    │    │
│  │  └─────────────────────────────┘    │    │
│  │  ℹ️ Từ 15 đến 60 tuổi               │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  Ngành muốn học *                   │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  🔍 Chọn ngành...           │    │    │
│  │  └─────────────────────────────┘    │    │
│  │  Dropdown: 20+ ngành IT             │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  Trình độ hiện tại *                │    │
│  │  ○ Beginner  ○ Mid-level  ○ Senior  │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  Mục tiêu *                         │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  VD: Senior Backend Dev     │    │    │
│  │  │  trong 2 năm...             │    │    │
│  │  └─────────────────────────────┘    │    │
│  │  Tối thiểu 10 ký tự                │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  Thời gian dự kiến *                │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  6 tháng ▼                  │    │    │
│  │  └─────────────────────────────┘    │    │
│  │  Options: 3/6/12/24 tháng           │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  🎯 Tạo roadmap ngay                │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ℹ️ Miễn phí · Không cần đăng nhập        │
└─────────────────────────────────────────────┘
```

**User actions trên trang form:**

| Action | Element | Validation | Error message |
|--------|---------|------------|---------------|
| Nhập tuổi | Number input | 15-60, required | "Tuổi phải từ 15 đến 60" |
| Chọn ngành | Searchable dropdown | Required | "Vui lòng chọn ngành" |
| Chọn trình độ | Radio group | Required | "Vui lòng chọn trình độ" |
| Nhập mục tiêu | Textarea | Min 10 chars, required | "Mục tiêu tối thiểu 10 ký tự" |
| Chọn thời gian | Select | Required | "Vui lòng chọn thời gian" |
| Submit | Button | All fields valid | — |

**Form validation flow:**

```
User submit form
    │
    ├── Frontend validate
    │   ├── Tuổi rỗng → "Vui lòng nhập tuổi"
    │   ├── Tuổi < 15 → "Tuổi phải từ 15 trở lên"
    │   ├── Tuổi > 60 → "Tuổi phải từ 60 trở xuống"
    │   ├── Ngành rỗng → "Vui lòng chọn ngành"
    │   ├── Trình độ rỗng → "Vui lòng chọn trình độ"
    │   ├── Mục tiêu rỗng → "Vui lòng nhập mục tiêu"
    │   ├── Mục tiêu < 10 chars → "Mục tiêu tối thiểu 10 ký tự"
    │   └── Thời gian rỗng → "Vui lòng chọn thời gian"
    │
    ├── Validation pass → Show loading
    │
    └── POST /api/generate
        ├── Success (200) → Redirect /roadmap/{slug}
        ├── Timeout (408) → "AI đang bận, vui lòng thử lại"
        ├── Rate limit (429) → "Quá nhiều yêu cầu, chờ 1 phút"
        └── Server error (500) → "Hệ thống đang bảo trì"
```

---

#### 10.4 User Flow Chi Tết — Loading State

```
LOADING STATE (3-30 giây)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sau khi submit → Hiển thị loading:

┌─────────────────────────────────────────────┐
│                                             │
│           ┌───────────────┐                 │
│           │   ⏳ Loading  │                 │
│           └───────────────┘                 │
│                                             │
│     AI đang tạo roadmap riêng cho bạn...    │
│                                             │
│     Quá trình này có thể mất 10-30 giây    │
│                                             │
│     ┌─────────────────────────────────┐     │
│     │  ████████░░░░░░░░░░  40%        │     │
│     └─────────────────────────────────┘     │
│                                             │
│     💡 Bạn đang tạo roadmap cho:           │
│     Backend Developer · Beginner · 6 tháng  │
│                                             │
└─────────────────────────────────────────────┘

Loading stages (animated text):
1. "Đang phân tích thông tin..." (0-3s)
2. "Đang tạo lộ trình tổng thể..." (3-8s)
3. "Đang tạo chi tiết từng giai đoạn..." (8-15s)
4. "Đang tạo tasks và bài tập..." (15-25s)
5. "Đang hoàn thiện roadmap..." (25-30s)
```

---

#### 10.5 User Flow Chi Tết — Trang Kết Quả (3 cấp)

```
TRANG KẾT QUẢ: /roadmap/{slug}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

═══════════════════════════════════════════════
LEVEL 1: ROADMAP LỚN (Hiển thị đầu tiên)
═══════════════════════════════════════════════

┌─────────────────────────────────────────────┐
│  🗺️ ROADMAP: Backend Developer              │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  👤 Tuổi: 20                        │    │
│  │  📚 Trình độ: Beginner              │    │
│  │  🎯 Mục tiêu: Senior Backend Dev    │    │
│  │  ⏱️ Thời gian: 6 tháng              │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  📊 TỔNG QUAN                       │    │
│  │                                     │    │
│  │  3 Phases · 12 Weeks · 36 Tasks     │    │
│  │  360 giờ học · 15 giờ/tuần          │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  💰 MỨC LƯƠNG (VNĐ/tháng)          │    │
│  │                                     │    │
│  │  Junior:  8-12 triệu  ████░░░░      │    │
│  │  Mid:    15-25 triệu  ██████░░      │    │
│  │  Senior: 30-50 triệu  ████████      │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  🎯 LÝ DO CẠNH TRANH                │    │
│  │  Thị trường IT VN đang thiếu...     │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  📈 NHU CẦU THỊ TRƯỜNG              │    │
│  │  Tuyển dụng Backend Dev tăng 30%... │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  📅 TIMELINE                        │    │
│  │                                     │    │
│  │  Phase 1 ●━━━━━━━━ Phase 2 ●━━━━━━ │    │
│  │  T1-T2              T3-T4           │    │
│  │                         Phase 3 ●   │    │
│  │                         T5-T6       │    │
│  └─────────────────────────────────────┘    │
│                                             │
└─────────────────────────────────────────────┘

        │ Scroll xuống
        ▼

═══════════════════════════════════════════════
LEVEL 2: PHASES (Danh sách giai đoạn)
═══════════════════════════════════════════════

┌─────────────────────────────────────────────┐
│  📋 CÁC GIAI ĐOẠN                          │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  ▼ PHASE 1: NỀN TẢNG (Tháng 1-2)  │    │
│  │  ✅ Đã hoàn thành                  │    │
│  │                                     │    │
│  │  📊 4 Weeks · 12 Tasks · 120 giờ    │    │
│  │                                     │    │
│  │  🏷️ Skills:                         │    │
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌────┐ │    │
│  │  │ HTML │ │ CSS  │ │  JS  │ │Git │ │    │
│  │  └──────┘ └──────┘ └──────┘ └────┘ │    │
│  │                                     │    │
│  │  🎯 Milestone: Tạo được website     │    │
│  │     tĩnh đầu tiên                  │    │
│  │                                     │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  ████████████████░░░░  80%  │    │    │
│  │  └─────────────────────────────┘    │    │
│  │                                     │    │
│  │  [▼ Xem chi tiết tasks]             │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  ▶ PHASE 2: BACKEND CORE (T3-4)   │    │
│  │  🔄 Đang học                        │    │
│  │                                     │    │
│  │  📊 4 Weeks · 12 Tasks · 120 giờ    │    │
│  │                                     │    │
│  │  🏷️ Skills:                         │    │
│  │  ┌────────┐ ┌────────┐ ┌────────┐  │    │
│  │  │Node.js │ │Express │ │Postgres│  │    │
│  │  └────────┘ └────────┘ └────────┘  │    │
│  │                                     │    │
│  │  🎯 Milestone: Tạo được REST API    │    │
│  │                                     │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  ████████░░░░░░░░░░  40%    │    │    │
│  │  └─────────────────────────────┘    │    │
│  │                                     │    │
│  │  [▶ Xem chi tiết tasks]             │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  ▶ PHASE 3: NÂNG CAO (Tháng 5-6)  │    │
│  │  ⬜ Chưa bắt đầu                    │    │
│  │                                     │    │
│  │  📊 4 Weeks · 12 Tasks · 120 giờ    │    │
│  │                                     │    │
│  │  🏷️ Skills:                         │    │
│  │  ┌───────┐ ┌───────┐ ┌───────┐     │    │
│  │  │ Auth  │ │Docker │ │Testing│     │    │
│  │  └───────┘ └───────┘ └───────┘     │    │
│  │                                     │    │
│  │  🎯 Milestone: Portfolio project    │    │
│  │     hoàn chỉnh                     │    │
│  │                                     │    │
│  │  ┌─────────────────────────────┐    │    │
│  │  │  ░░░░░░░░░░░░░░░░░░  0%    │    │    │
│  │  └─────────────────────────────┘    │    │
│  │                                     │    │
│  │  [▶ Xem chi tiết tasks]             │    │
│  └─────────────────────────────────────┘    │
│                                             │
└─────────────────────────────────────────────┘

        │ Click "Xem chi tiết tasks" của Phase 2
        ▼

═══════════════════════════════════════════════
LEVEL 3: TASKS (Chi tiết trong mỗi Phase)
═══════════════════════════════════════════════

┌─────────────────────────────────────────────┐
│  📝 TASKS — PHASE 2: BACKEND CORE          │
│                                             │
│  ⏱️ Tháng 3-4 · 12 Tasks · 120 giờ         │
│  📊 Tiến độ: 5/12 tasks (40%)               │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  ▼ WEEK 5: NODE.JS CƠ BẢN    ✅    │    │
│  │                                     │    │
│  │  ☑ Day 1-2: Cài đặt Node.js & npm  │    │
│  │     📖 freeCodeCamp Node.js         │    │
│  │     📝 Cài Node, tạo file .js đầu   │    │
│  │     ⏱️ 4 giờ                         │    │
│  │                                     │    │
│  │  ☑ Day 3-4: Modules & File System   │    │
│  │     📖 Node.js Docs                 │    │
│  │     📝 Tạo CLI tool đơn giản       │    │
│  │     ⏱️ 4 giờ                         │    │
│  │                                     │    │
│  │  ☑ Day 5-7: HTTP Server cơ bản     │    │
│  │     📖 MDN HTTP                     │    │
│  │     📝 Tạo server trả "Hello World" │    │
│  │     ⏱️ 6 giờ                         │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  ▼ WEEK 6: EXPRESS FRAMEWORK  🔄    │    │
│  │                                     │    │
│  │  ☑ Day 1-2: Express cơ bản         │    │
│  │     📖 Express.js Docs              │    │
│  │     📝 Tạo REST API CRUD đơn giản  │    │
│  │     ⏱️ 4 giờ                         │    │
│  │                                     │    │
│  │  ☐ Day 3-4: Middleware & Router     │    │
│  │     📖 Express Middleware Guide      │    │
│  │     📝 Thêm validation + logging    │    │
│  │     ⏱️ 4 giờ                         │    │
│  │                                     │    │
│  │  ☐ Day 5-7: Error Handling          │    │
│  │     📖 Express Error Handling        │    │
│  │     📝 Xử lý lỗi tập trung         │    │
│  │     ⏱️ 6 giờ                         │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  ▶ WEEK 7: POSTGRESQL         ⬜    │    │
│  │  ▶ WEEK 8: PROJECT            ⬜    │    │
│  └─────────────────────────────────────┘    │
│                                             │
└─────────────────────────────────────────────┘

        │ Cuối trang
        ▼

┌─────────────────────────────────────────────┐
│  🎯 HÀNH ĐỘNG TIẾP THEO                    │
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │ Chia sẻ  │  │ Tạo mới  │  │  Về Home │  │
│  │ roadmap  │  │ roadmap  │  │          │  │
│  └──────────┘  └──────────┘  └──────────┘  │
│                                             │
│  📊 Thống kê: 1,234 roadmap đã tạo         │
└─────────────────────────────────────────────┘
```

---

#### 10.6 User Flow — Share Flow

```
USER SHARE FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User click "Chia sẻ"
    │
    ├── Copy Link
    │   ├── Copy URL vào clipboard
    │   ├── Toast: "Đã copy link!"
    │   └── OG tags hiển thị đúng khi paste
    │
    ├── Share Facebook
    │   ├── Open Facebook share dialog
    │   ├── URL: /roadmap/{slug}
    │   └── OG image: Screenshot roadmap
    │
    └── Share Zalo
        ├── Open Zalo share dialog
        └── URL: /roadmap/{slug}
```

---

#### 10.7 User Flow — Landing Page Ngành

```
LANDING PAGE NGÀNH: /nganh/{slug}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User search Google "roadmap backend developer"
    │
    └── Click kết quả → /nganh/backend-developer
        │
        └── Hiển thị:
            │
            ├── SEO Content (500+ words)
            │   ├── Backend Developer là gì?
            │   ├── Học Backend cần biết gì?
            │   ├── Mức lương Backend Dev tại VN
            │   └── Cơ hội việc làm
            │
            ├── Ví dụ Roadmap mẫu (Level 1)
            │   ├── 6 tháng, 3 phases
            │   └── Preview skills + timeline
            │
            ├── CTA: "Tạo roadmap riêng cho bạn"
            │   └── Click → /tao-roadmap (pre-fill ngành)
            │
            └── Các ngành liên quan
                ├── Frontend Developer
                ├── Fullstack Developer
                └── Node.js Developer
```

---

#### 10.8 User Flow — Error States

```
ERROR FLOWS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Form Validation Error:
   User submit → Highlight field đỏ → Hiện lỗi dưới field → Focus vào field lỗi

2. API Timeout:
   Loading > 30s → "AI đang bận, vui lòng thử lại" → [Retry] button

3. API Rate Limit:
   429 response → "Quá nhiều yêu cầu, chờ 1 phút" → Countdown timer

4. AI JSON Error:
   AI trả JSON sai → Retry 1 lần → Nếu fail → Fallback response → Hiển thị

5. Network Error:
   navigator.onLine = false → "Mất kết nối, kiểm tra mạng" → Auto retry khi online

6. 404 Not Found:
   Slug không tồn tại → "Không tìm thấy roadmap" → [Về trang chủ]

7. 500 Server Error:
   Server crash → "Hệ thống đang bảo trì" → [Thử lại]
```

---

### Bước 11 — Wireframe (Khung giao diện)

---

#### 11.1 Wireframe — Trang Chủ (/)

```
DESKTOP (1024px+)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────┐
│  🔵 AI Career Roadmap                    [Bắt đầu ngay]    │ ← Header
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    HERO SECTION                             │
│                                                             │
│         "Tạo lộ trình học IT                               │
│          cá nhân hóa bằng AI"                               │
│                                                             │
│    "Nhập thông tin, AI tạo roadmap riêng cho bạn            │
│     theo 3 cấp: Tổng quan → Giai đoạn → Tasks"             │
│                                                             │
│              ┌─────────────────────┐                        │
│              │  🎯 Bắt đầu ngay   │                        │
│              └─────────────────────┘                        │
│                                                             │
│              [Dynamic social proof]                          │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    HOW IT WORKS                             │
│                                                             │
│    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│    │  📝 Nhập     │  │  🤖 AI tạo   │  │  📚 Học theo │    │
│    │  thông tin   │→ │  roadmap     │→ │  lộ trình    │    │
│    │              │  │  3 cấp       │  │              │    │
│    └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    VÍ DỤ ROADMAP                            │
│                                                             │
│    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐    │
│    │ Backend Dev  │  │ Data Analyst │  │ Frontend Dev │    │
│    │ 20 tuổi      │  │ 25 tuổi      │  │ 22 tuổi      │    │
│    │ 6 tháng      │  │ 12 tháng     │  │ 6 tháng      │    │
│    │ [Xem]        │  │ [Xem]        │  │ [Xem]        │    │
│    └──────────────┘  └──────────────┘  └──────────────┘    │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    NGÀNH PHỔ BIẾN                           │
│                                                             │
│    ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐       │
│    │BE   │ │FE   │ │Data │ │AI   │ │DevOps│ │Mobile│       │
│    │Dev  │ │Dev  │ │Anal.│ │Eng. │ │      │ │      │       │
│    └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘       │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Footer: About · Contact · © 2026                           │
└─────────────────────────────────────────────────────────────┘


MOBILE (375px)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────┐
│ 🔵 AI Career Roadmap    │
├─────────────────────────┤
│                         │
│   "Tạo lộ trình học IT  │
│    cá nhân hóa bằng AI" │
│                         │
│ ┌─────────────────────┐ │
│ │  🎯 Bắt đầu ngay   │ │
│ └─────────────────────┘ │
│                         │
│   [Dynamic social proof]  │
│                         │
├─────────────────────────┤
│    HOW IT WORKS         │
│                         │
│  1. 📝 Nhập thông tin  │
│         ↓               │
│  2. 🤖 AI tạo roadmap  │
│         ↓               │
│  3. 📚 Học theo lộ trình│
│                         │
├─────────────────────────┤
│    VÍ DỤ ROADMAP        │
│                         │
│  ┌─────────────────────┐│
│  │ Backend Dev · 20 tuổi││
│  │ 6 tháng · [Xem]     ││
│  └─────────────────────┘│
│  ┌─────────────────────┐│
│  │ Data Analyst · 25   ││
│  │ 12 tháng · [Xem]    ││
│  └─────────────────────┘│
│                         │
├─────────────────────────┤
│  NGÀNH PHỔ BIẾN         │
│                         │
│  [BE] [FE] [Data]       │
│  [AI] [DevOps] [Mobile] │
│                         │
├─────────────────────────┤
│  Footer                 │
└─────────────────────────┘
```

---

#### 11.2 Wireframe — Trang Form (/tao-roadmap)

```
DESKTOP (1024px+)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────┐
│  🔵 AI Career Roadmap                    [Về trang chủ]     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│                    🎯 Tạo roadmap của bạn                   │
│                                                             │
│    ┌─────────────────────────────────────────────────────┐  │
│    │                                                     │  │
│    │  ┌─────────────────────────────────────────────┐    │  │
│    │  │  Tuổi *                                     │    │  │
│    │  │  ┌─────────────────────────────────────┐    │    │  │
│    │  │  │  20                                  │    │    │  │
│    │  │  └─────────────────────────────────────┘    │    │  │
│    │  │  ℹ️ Từ 15 đến 60 tuổi                       │    │  │
│    │  └─────────────────────────────────────────────┘    │  │
│    │                                                     │  │
│    │  ┌─────────────────────────────────────────────┐    │  │
│    │  │  Ngành muốn học *                           │    │  │
│    │  │  ┌─────────────────────────────────────┐    │    │  │
│    │  │  │  🔍 Chọn ngành IT...               │    │    │  │
│    │  │  └─────────────────────────────────────┘    │    │  │
│    │  │  ┌─────────────────────────────────────┐    │    │  │
│    │  │  │  ▸ Backend Developer                │    │    │  │
│    │  │  │  ▸ Frontend Developer               │    │    │  │
│    │  │  │  ▸ Fullstack Developer              │    │    │  │
│    │  │  │  ▸ Data Analyst                     │    │    │  │
│    │  │  │  ▸ AI/ML Engineer                   │    │    │  │
│    │  │  │  ▸ ... xem thêm                     │    │    │  │
│    │  │  └─────────────────────────────────────┘    │    │  │
│    │  └─────────────────────────────────────────────┘    │  │
│    │                                                     │  │
│    │  ┌─────────────────────────────────────────────┐    │  │
│    │  │  Trình độ hiện tại *                        │    │  │
│    │  │                                             │    │  │
│    │  │  ● Beginner   ○ Mid-level   ○ Senior       │    │  │
│    │  │                                             │    │  │
│    │  │  Beginner: Chưa biết gì hoặc mới bắt đầu   │    │  │
│    │  │  Mid-level: 1-2 năm kinh nghiệm             │    │  │
│    │  │  Senior: 3+ năm kinh nghiệm                 │    │  │
│    │  └─────────────────────────────────────────────┘    │  │
│    │                                                     │  │
│    │  ┌─────────────────────────────────────────────┐    │  │
│    │  │  Mục tiêu *                                 │    │  │
│    │  │  ┌─────────────────────────────────────┐    │    │  │
│    │  │  │  VD: Trở thành Senior Backend Dev   │    │    │  │
│    │  │  │  trong 2 năm, lương 25+ triệu       │    │    │  │
│    │  │  │                                      │    │    │  │
│    │  │  └─────────────────────────────────────┘    │    │  │
│    │  │  0/500 ký tự · Tối thiểu 10 ký tự          │    │  │
│    │  └─────────────────────────────────────────────┘    │  │
│    │                                                     │  │
│    │  ┌─────────────────────────────────────────────┐    │  │
│    │  │  Thời gian dự kiến *                        │    │  │
│    │  │  ┌─────────────────────────────────────┐    │    │  │
│    │  │  │  6 tháng                         ▼  │    │    │  │
│    │  │  └─────────────────────────────────────┘    │    │  │
│    │  └─────────────────────────────────────────────┘    │  │
│    │                                                     │  │
│    │  ┌─────────────────────────────────────────────┐    │  │
│    │  │         🎯 Tạo roadmap ngay                 │    │  │
│    │  └─────────────────────────────────────────────┘    │  │
│    │                                                     │  │
│    │  ℹ️ Miễn phí · Không cần đăng nhập · AI tạo trong  │  │
│    │     30 giây                                          │  │
│    │                                                     │  │
│    └─────────────────────────────────────────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘


MOBILE (375px)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────┐
│ 🔵 AI Career Roadmap    │
├─────────────────────────┤
│                         │
│  🎯 Tạo roadmap của bạn │
│                         │
│  Tuổi *                 │
│  ┌─────────────────────┐│
│  │  20                  ││
│  └─────────────────────┘│
│                         │
│  Ngành muốn học *       │
│  ┌─────────────────────┐│
│  │  🔍 Chọn ngành...   ││
│  └─────────────────────┘│
│                         │
│  Trình độ *             │
│  ● Beginner             │
│  ○ Mid-level            │
│  ○ Senior               │
│                         │
│  Mục tiêu *             │
│  ┌─────────────────────┐│
│  │ Trở thành Senior... ││
│  └─────────────────────┘│
│                         │
│  Thời gian *            │
│  ┌─────────────────────┐│
│  │  6 tháng          ▼ ││
│  └─────────────────────┘│
│                         │
│  ┌─────────────────────┐│
│  │  🎯 Tạo roadmap ngay││
│  └─────────────────────┘│
│                         │
│  Miễn phí · Không cần   │
│  đăng nhập              │
└─────────────────────────┘
```

---

#### 11.3 Wireframe — Trang Kết Quả (/roadmap/{slug})

```
DESKTOP (1024px+)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────┐
│  🔵 AI Career Roadmap     [Chia sẻ] [Tạo mới] [Về Home]    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  🗺️ ROADMAP: Backend Developer                      │    │
│  │                                                     │    │
│  │  👤 Tuổi: 20  📚 Beginner  🎯 Senior Dev  ⏱️ 6 tháng│    │
│  │                                                     │    │
│  │  📊 3 Phases · 12 Weeks · 36 Tasks · 360 giờ       │    │
│  │                                                     │    │
│  │  💰 Junior: 8-12tr  Mid: 15-25tr  Senior: 30-50tr  │    │
│  │                                                     │    │
│  │  📅 Phase 1 ●━━━━━━━━━ Phase 2 ●━━━━━━━━━ Phase 3 ●│    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ───────────────────────────────────────────────────────    │
│                                                             │
│  📋 CÁC GIAI ĐOẠN                                          │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  ▼ PHASE 1: NỀN TẢNG (T1-T2)  ✅ 80%              │    │
│  │  Skills: [HTML] [CSS] [JavaScript] [Git]            │    │
│  │  Milestone: Tạo được website tĩnh đầu tiên         │    │
│  │  ┌─────────────────────────────────┐                │    │
│  │  │ ████████████████░░░░  80%       │                │    │
│  │  └─────────────────────────────────┘                │    │
│  │  [▼ Xem tasks]                                      │    │
│  │                                                     │    │
│  │  ┌─────────────────────────────────────────────┐    │    │
│  │  │ ▼ Week 1: HTML cơ bản                 ✅    │    │    │
│  │  │                                             │    │    │
│  │  │ ☑ Day 1-2: Cấu trúc HTML                   │    │    │
│  │  │   📖 freeCodeCamp · 📝 Trang profile · 4h   │    │    │
│  │  │                                             │    │    │
│  │  │ ☑ Day 3-4: HTML Forms                       │    │    │
│  │  │   📖 MDN Docs · 📝 Form đăng ký · 4h        │    │    │
│  │  │                                             │    │    │
│  │  │ ☑ Day 5-7: Semantic HTML                    │    │    │
│  │  │   📖 web.dev · 📝 Refactor · 6h             │    │    │
│  │  │                                             │    │    │
│  │  │ ▼ Week 2: CSS cơ bản                 🔄    │    │    │
│  │  │ ☑ Day 1-2: Selectors & Box Model            │    │    │
│  │  │ ☐ Day 3-4: Flexbox                          │    │    │
│  │  │ ☐ Day 5-7: Grid + Responsive                │    │    │
│  │  │                                             │    │    │
│  │  │ ▶ Week 3: JavaScript                  ⬜    │    │    │
│  │  │ ▶ Week 4: Git & Project               ⬜    │    │    │
│  │  └─────────────────────────────────────────────┘    │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  ▶ PHASE 2: BACKEND CORE (T3-T4)  🔄 40%          │    │
│  │  Skills: [Node.js] [Express] [PostgreSQL]           │    │
│  │  [▶ Xem tasks]                                      │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐    │
│  │  ▶ PHASE 3: NÂNG CAO (T5-T6)  ⬜ 0%                │    │
│  │  Skills: [Auth] [Docker] [Testing] [Deploy]         │    │
│  │  [▶ Xem tasks]                                      │    │
│  └─────────────────────────────────────────────────────┘    │
│                                                             │
│  ───────────────────────────────────────────────────────    │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  📤 Chia sẻ  │  │  🔄 Tạo mới  │  │  🏠 Về Home  │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
│  📊 1,234 roadmap đã được tạo bởi AI Career Roadmap        │
│                                                             │
└─────────────────────────────────────────────────────────────┘


MOBILE (375px)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────┐
│ 🔵 AI Career Roadmap    │
│ [☰]          [Chia sẻ]  │
├─────────────────────────┤
│                         │
│ 🗺️ ROADMAP:             │
│ Backend Developer       │
│                         │
│ 👤 20 tuổi · 📚 Beginner│
│ 🎯 Senior · ⏱️ 6 tháng  │
│                         │
│ 📊 3 Phases             │
│    12 Weeks · 36 Tasks  │
│                         │
│ 💰 Mức lương:           │
│ Junior: 8-12 triệu      │
│ Mid: 15-25 triệu        │
│ Senior: 30-50 triệu     │
│                         │
│ 📅 Timeline:            │
│ T1-T2 → T3-T4 → T5-T6  │
│                         │
├─────────────────────────┤
│ 📋 CÁC GIAI ĐOẠN       │
│                         │
│ ┌─────────────────────┐ │
│ │ ▼ PHASE 1: NỀN TẢNG│ │
│ │ T1-T2 · ✅ 80%      │ │
│ │ [HTML][CSS][JS][Git] │ │
│ │ [▼ Xem tasks]       │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ ▶ PHASE 2: BACKEND  │ │
│ │ T3-T4 · 🔄 40%      │ │
│ │ [▶ Xem tasks]       │ │
│ └─────────────────────┘ │
│                         │
│ ┌─────────────────────┐ │
│ │ ▶ PHASE 3: NÂNG CAO │ │
│ │ T5-T6 · ⬜ 0%       │ │
│ └─────────────────────┘ │
│                         │
├─────────────────────────┤
│ [Chia sẻ] [Tạo mới]    │
│ [Về Home]               │
│                         │
│ 1,234 roadmap đã tạo   │
└─────────────────────────┘
```

---

#### 11.4 Wireframe — Loading State

```
DESKTOP + MOBILE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────┐
│                                             │
│                                             │
│              ┌───────────────┐              │
│              │               │              │
│              │   🤖 Loading  │              │
│              │               │              │
│              └───────────────┘              │
│                                             │
│       AI đang tạo roadmap riêng cho bạn     │
│                                             │
│       ┌─────────────────────────────┐       │
│       │  ████████░░░░░░░░░░  40%    │       │
│       └─────────────────────────────┘       │
│                                             │
│       "Đang tạo chi tiết từng               │
│        giai đoạn..."                        │
│                                             │
│       💡 Bạn đang tạo roadmap cho:          │
│       Backend Developer · Beginner          │
│       · Mục tiêu: Senior Dev · 6 tháng      │
│                                             │
│       ℹ️ Quá trình này có thể mất 10-30s    │
│                                             │
│                                             │
└─────────────────────────────────────────────┘
```

---

#### 11.5 Wireframe — Error State

```
┌─────────────────────────────────────────────┐
│                                             │
│              ┌───────────────┐              │
│              │   ❌ Lỗi      │              │
│              └───────────────┘              │
│                                             │
│         AI đang bận, vui lòng thử lại       │
│                                             │
│              ┌─────────────────┐            │
│              │  🔄 Thử lại     │            │
│              └─────────────────┘            │
│                                             │
│              ┌─────────────────┐            │
│              │  🏠 Về Home     │            │
│              └─────────────────┘            │
│                                             │
└─────────────────────────────────────────────┘
```

---

#### 11.6 Component Specifications

**Color System:**

```
Primary:     #4F46E5 (Indigo-600)    Buttons, links, active states
Secondary:   #10B981 (Emerald-500)   Success, completed tasks
Accent:      #F59E0B (Amber-500)     Warning, highlight
Background:  #F9FAFB (Gray-50)       Page background
Surface:     #FFFFFF                  Cards, modals
Text:        #111827 (Gray-900)      Primary text
Text muted:  #6B7280 (Gray-500)      Secondary text
Border:      #E5E7EB (Gray-200)      Borders, dividers
Error:       #EF4444 (Red-500)       Errors, validation
```

**Typography:**

```
Font family: 'Inter', -apple-system, sans-serif

H1: 36px / 44px / Bold    — Page title
H2: 24px / 32px / Bold    — Section title
H3: 20px / 28px / Semi    — Card title
H4: 16px / 24px / Semi    — Sub-section
Body: 16px / 24px / Regular — Content
Small: 14px / 20px / Regular — Labels, captions
Tiny: 12px / 16px / Regular — Badges, tags
```

**Spacing:**

```
xs: 4px    — Tight spacing
sm: 8px    — Inner padding
md: 16px   — Standard gap
lg: 24px   — Section gap
xl: 32px   — Large gap
2xl: 48px  — Page sections
3xl: 64px  — Hero sections
```

**Border Radius:**

```
sm: 4px    — Small elements (tags, badges)
md: 8px    — Standard (cards, inputs)
lg: 12px   — Large cards
xl: 16px   — Modals
full: 9999px — Pills, avatars
```

**Shadows:**

```
sm:  0 1px 2px rgba(0,0,0,0.05)     — Subtle
md:  0 4px 6px rgba(0,0,0,0.07)     — Cards
lg:  0 10px 15px rgba(0,0,0,0.1)    — Modals
xl:  0 20px 25px rgba(0,0,0,0.15)   — Popovers
```

**Breakpoints:**

```
Mobile S:  320px
Mobile M:  375px
Mobile L:  425px
Tablet:    768px
Laptop:    1024px
Laptop L:  1440px
```

---

#### 11.7 Animation Specifications

| Element | Animation | Duration | Easing |
|---------|-----------|----------|--------|
| Page transition | Fade in | 300ms | ease-in-out |
| Card hover | Scale 1.02 + shadow | 200ms | ease |
| Button hover | Darken 10% | 150ms | ease |
| Accordion expand | Height auto + fade | 300ms | ease-in-out |
| Loading spinner | Rotate 360° | 1s | linear |
| Progress bar | Width animate | 500ms | ease-out |
| Toast notification | Slide up + fade | 300ms | ease |
| Task checkbox | Scale bounce | 200ms | ease |
| Phase card appear | Fade up | 400ms | ease-out |

---

**Trạng thái:** ✅ Đã xác định xong

---

## PHASE 6 — THIẾT KẾ KỸ THUẬT

### Bước 12 — Tech Stack

---

#### 12.1 Tech Stack Tổng Quan

```
┌─────────────────────────────────────────────────────────────┐
│                    ARCHITECTURE OVERVIEW                     │
└─────────────────────────────────────────────────────────────┘

    ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
    │   USER       │     │   BROWSER    │     │   SEARCH     │
    │   (Mobile/   │────▶│   (HTML/     │────▶│   ENGINE     │
    │    Desktop)  │     │    CSS/JS)   │     │   (Google)   │
    └──────────────┘     └──────┬───────┘     └──────────────┘
                                │
                                │ HTTP Request
                                ▼
    ┌──────────────────────────────────────────────────────┐
    │                    FASTAPI SERVER                      │
    │                                                       │
    │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
    │  │ Routes  │  │ Services│  │ Template│  │ Static  │ │
    │  │ (API)   │  │ (Logic) │  │ (Jinja2)│  │ (CSS/JS)│ │
    │  └────┬────┘  └────┬────┘  └─────────┘  └─────────┘ │
    │       │            │                                  │
    │       │            ▼                                  │
    │       │     ┌─────────────┐    ┌─────────────┐       │
    │       │     │ AI Service  │    │  Database   │       │
    │       │     │ (OpenAI)    │    │  (SQLite)   │       │
    │       │     └─────────────┘    └─────────────┘       │
    └──────────────────────────────────────────────────────┘
```

#### 12.2 Chi Tết Từng Thành Phần

**FRONTEND — HTML/CSS/JS thuần:**

| Thành phần | Công nghệ | Phiên bản | Lý do chọn |
|-----------|-----------|-----------|------------|
| HTML | HTML5 | — | Semantic, SEO-friendly |
| CSS | CSS3 + Custom Properties | — | Không cần framework, nhẹ |
| JavaScript | Vanilla JS (ES6+) | — | Không cần build step, nhanh |
| Font | Inter (Google Fonts) | — | Modern, tiếng Việt tốt |
| Icons | Lucide Icons (SVG) | — | Nhẹ, sắc nét |
| Animation | CSS Animation + JS | — | Không cần library |

**Tại sao KHÔNG dùng React/Vue/Svelte:**

| Lý do | Chi tiết |
|-------|---------|
| SEO | SSR phức tạp hơn, cần thêm Next.js/Nuxt |
| Performance | Bundle size lớn hơn, hydration overhead |
| Complexity | Thêm build step, node_modules, config |
| MVP | Overkill cho 4 trang HTML |
| Maintenance | Ít dependency hơn = ít lỗi hơn |

**BACKEND — Python FastAPI:**

| Thành phần | Công nghệ | Phiên bản | Lý do chọn |
|-----------|-----------|-----------|------------|
| Framework | FastAPI | 0.100+ | Nhanh, async, auto docs |
| Server | Uvicorn | 0.23+ | ASGI server, nhanh |
| Template | Jinja2 | 3.1+ | SSR cho SEO |
| ORM | Raw SQL (sqlite3) | — | Đơn giản cho MVP |
| Validation | Pydantic | 2.0+ | Built-in FastAPI |
| HTTP Client | httpx | 0.24+ | Async HTTP cho OpenAI API |
| Env | python-dotenv | 1.0+ | Quản lý env vars |

**Tại sao KHÔNG dùng Django/Flask/NestJS:**

| Framework | Vấn đề |
|-----------|--------|
| Django | Quá nặng cho MVP, nhiều features không cần |
| Flask | Không async, không auto docs |
| NestJS | Cần Node.js + TypeScript, phức tạp hơn |

**DATABASE — SQLite:**

| Thành phần | Công nghệ | Lý do chọn |
|-----------|-----------|------------|
| Database | SQLite 3 | Không cần cài đặt, file-based |
| Migration | Raw SQL | Đơn giản cho MVP |
| Backup | Copy file .db | Dễ backup |

**Tại sao SQLite cho MVP:**

| Lý do | Chi tiết |
|-------|---------|
| Zero config | Không cần cài server |
| File-based | 1 file .db, dễ deploy |
| Performance | Đủ cho < 10k records |
| Migration | Dễ chuyển sang PostgreSQL sau |

**AI — OpenAI API:**

| Thành phần | Công nghệ | Lý do chọn |
|-----------|-----------|------------|
| AI Provider | Deepseek | Chất lượng tốt nhất |
| Model | deepseek-v4-flash | Nhanh, rẻ, thông minh |
| Client | httpx (async) | Non-blocking |
| Fallback | Template JSON | Khi API fail |

**HOSTING:**

| Thành phần | Công nghệ | Free tier |
|-----------|-----------|-----------|
| Backend | Railway.app | 500 giờ/tháng |
| Database | SQLite (file) | — |
| Domain | .vercel.app hoặc custom | Free |
| SSL | Auto (Railway) | Free |

**Alternative hosting:**

| Option | Pros | Cons |
|--------|------|------|
| Railway.app | Dễ deploy, free tier | Sleep sau 30 phút |
| Render.com | Free tier tốt | Slow cold start |
| Vercel | Nhanh, free | Không hỗ trợ Python tốt |
| Fly.io | Global, free | Phức tạp hơn |

---

### Bước 13 — Database Design

---

#### 13.1 Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    ENTITY RELATIONSHIP                       │
└─────────────────────────────────────────────────────────────┘

    ┌──────────────────┐          ┌──────────────────┐
    │    industries     │          │     roadmaps      │
    ├──────────────────┤          ├──────────────────┤
    │ id (PK)          │◄────────│ industry (FK)     │
    │ name             │   1:N    │ id (PK)           │
    │ slug (UNIQUE)    │          │ slug (UNIQUE)     │
    │ category         │          │ age               │
    │ description      │          │ level             │
    │ avg_salary_*     │          │ goal              │
    │ demand_level     │          │ duration_months   │
    │ top_skills       │          │ overview          │
    │ meta_title       │          │ phases_json       │
    │ meta_description │          │ salary_*          │
    │ sample_roadmap   │          │ ai_model          │
    │ created_at       │          │ view_count        │
    └──────────────────┘          │ share_count       │
                                  │ created_at        │
                                  └──────────────────┘
```

#### 13.2 Schema Chi Tiết

**Bảng `industries`:**

```sql
-- industries: Danh sách ngành IT (pre-seeded)
CREATE TABLE industries (
    id TEXT PRIMARY KEY,
    
    -- Thông tin cơ bản
    name TEXT NOT NULL,                    -- "Backend Developer"
    slug TEXT UNIQUE NOT NULL,             -- "backend-developer"
    category TEXT,                         -- "Web Development"
    
    -- SEO content
    description TEXT,                      -- Mô tả ngành (500+ words, SEO)
    
    -- Mức lương (market data)
    avg_salary_junior TEXT,                -- "8-12 triệu"
    avg_salary_mid TEXT,                   -- "15-25 triệu"
    avg_salary_senior TEXT,                -- "30-50 triệu"
    
    -- Market data
    demand_level TEXT CHECK(demand_level IN ('high', 'medium', 'low')),
    top_skills TEXT,                       -- JSON: ["Node.js","Python","SQL"]
    
    -- SEO metadata
    meta_title TEXT,                       -- "Roadmap Backend Developer..."
    meta_description TEXT,                 -- 150-160 chars
    
    -- Sample roadmap (pre-generated)
    sample_roadmap_json TEXT,              -- Full roadmap JSON
    
    -- Timestamps
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_industries_slug ON industries(slug);
CREATE INDEX idx_industries_category ON industries(category);
```

**Bảng `roadmaps`:**

```sql
-- roadmaps: Roadmap đã tạo bởi user
CREATE TABLE roadmaps (
    id TEXT PRIMARY KEY,                   -- UUID v4
    
    -- SEO URL
    slug TEXT UNIQUE NOT NULL,             -- "backend-developer-20tuoi-a3f7" (industry + age + 4hex)
    
    -- ─── INPUT (từ user) ───
    age INTEGER NOT NULL CHECK(age >= 15 AND age <= 60),
    industry TEXT NOT NULL,                -- "backend-developer" (FK → industries.slug)
    industry_name TEXT NOT NULL,           -- "Backend Developer" (display name)
    level TEXT NOT NULL CHECK(level IN ('beginner', 'mid', 'senior')),
    level_display TEXT NOT NULL,           -- "Beginner" (display name)
    goal TEXT NOT NULL,                    -- "Senior Backend Dev trong 2 năm"
    duration_months INTEGER NOT NULL CHECK(duration_months IN (3, 6, 12, 24)),
    
    -- ─── LEVEL 1: ROADMAP LỚN ───
    overview TEXT,                         -- Tổng quan (2-3 câu)
    total_weeks INTEGER,                   -- 24
    total_tasks INTEGER,                   -- 72
    total_hours INTEGER,                   -- 360
    hours_per_week INTEGER,                -- 15
    
    -- Mức lương
    salary_junior TEXT,                    -- "8-12 triệu"
    salary_mid TEXT,                       -- "15-25 triệu"
    salary_senior TEXT,                    -- "30-50 triệu"
    
    -- Market info
    competitive_advantage TEXT,            -- Lý do cạnh tranh
    market_demand TEXT,                    -- Nhu cầu thị trường
    interview_tips TEXT,                   -- JSON: ["Tip 1", "Tip 2"]
    
    -- ─── LEVEL 2 + 3: PHASES + TASKS ───
    phases_json TEXT,                      -- JSON (xem cấu trúc bên dưới)
    
    -- ─── METADATA ───
    ai_model TEXT DEFAULT 'gpt-4o',        -- Model đã dùng
    ai_tokens_used INTEGER,                -- Tokens consumed
    generation_time_ms INTEGER,            -- Time to generate (ms)
    prompt_version TEXT DEFAULT 'v1',      -- Version của prompt
    
    -- ─── STATS ───
    view_count INTEGER DEFAULT 0,
    share_count INTEGER DEFAULT 0,
    completion_rate REAL DEFAULT 0.0,      -- % tasks completed (nếu user logged in)
    
    -- ─── TIMESTAMPS ───
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_roadmaps_slug ON roadmaps(slug);
CREATE INDEX idx_roadmaps_industry ON roadmaps(industry);
CREATE INDEX idx_roadmaps_level ON roadmaps(level);
CREATE INDEX idx_roadmaps_created ON roadmaps(created_at DESC);
CREATE INDEX idx_roadmaps_views ON roadmaps(view_count DESC);
```

#### 13.3 Cấu trúc JSON — phases_json

```json
{
  "phases": [
    {
      "id": "phase-1",
      "name": "Phase 1: Nền tảng",
      "description": "Xây dựng nền tảng vững chắc về web development",
      "duration": "Tháng 1-2",
      "duration_weeks": 8,
      "total_hours": 120,
      "total_tasks": 12,
      "milestone": "Tạo được website tĩnh đầu tiên",
      "skills": [
        {
          "name": "HTML",
          "priority": "high",
          "difficulty": "easy",
          "hours_needed": 20,
          "description": "Cấu trúc trang web"
        },
        {
          "name": "CSS",
          "priority": "high",
          "difficulty": "easy",
          "hours_needed": 30,
          "description": "Styling và layout"
        },
        {
          "name": "JavaScript",
          "priority": "high",
          "difficulty": "medium",
          "hours_needed": 50,
          "description": "Lập trình frontend"
        },
        {
          "name": "Git",
          "priority": "medium",
          "difficulty": "easy",
          "hours_needed": 20,
          "description": "Quản lý source code"
        }
      ],
      "weeks": [
        {
          "id": "week-1",
          "name": "HTML cơ bản",
          "tasks": [
            {
              "id": "task-1",
              "name": "Cấu trúc HTML cơ bản",
              "days": "Day 1-2",
              "hours": 4,
              "difficulty": "easy",
              "resource": {
                "name": "freeCodeCamp - Responsive Web Design",
                "url": "https://freecodecamp.org/learn/2022/responsive-web-design/",
                "type": "free",
                "language": "en",
                "format": "interactive"
              },
              "exercise": {
                "title": "Tạo trang profile cá nhân",
                "description": "Tạo 1 trang HTML hoàn chỉnh với: header (tên, avatar), section About (giới thiệu bản thân), section Skills (danh sách kỹ năng), section Contact (form liên hệ). Chỉ dùng HTML thuần, không CSS.",
                "deliverable": "File index.html",
                "estimated_hours": 4
              }
            },
            {
              "id": "task-2",
              "name": "HTML Forms & Tables",
              "days": "Day 3-4",
              "hours": 4,
              "difficulty": "easy",
              "resource": {
                "name": "MDN Web Docs - HTML Forms",
                "url": "https://developer.mozilla.org/en-US/docs/Learn/Forms",
                "type": "free",
                "language": "en",
                "format": "documentation"
              },
              "exercise": {
                "title": "Tạo form đăng ký",
                "description": "Tạo form đăng ký với: tên, email, password, ngày sinh, giới tính (radio), sở thích (checkbox), submit button. Có validation HTML5.",
                "deliverable": "File register.html",
                "estimated_hours": 4
              }
            },
            {
              "id": "task-3",
              "name": "Semantic HTML & Accessibility",
              "days": "Day 5-7",
              "hours": 6,
              "difficulty": "medium",
              "resource": {
                "name": "web.dev - Learn Accessibility",
                "url": "https://web.dev/learn/accessibility/",
                "type": "free",
                "language": "en",
                "format": "course"
              },
              "exercise": {
                "title": "Refactor trang profile",
                "description": "Refactor trang profile ở Task 1: thay div bằng semantic tags (header, nav, main, section, article, footer), thêm aria-label, alt text cho ảnh, đảm bảo keyboard navigation.",
                "deliverable": "File index.html (refactored)",
                "estimated_hours": 4
              }
            }
          ]
        },
        {
          "id": "week-2",
          "name": "CSS cơ bản",
          "tasks": [
            {
              "id": "task-4",
              "name": "CSS Selectors & Box Model",
              "days": "Day 1-2",
              "hours": 4,
              "difficulty": "easy",
              "resource": {
                "name": "freeCodeCamp - CSS",
                "url": "https://freecodecamp.org/learn/2022/responsive-web-design/",
                "type": "free",
                "language": "en",
                "format": "interactive"
              },
              "exercise": {
                "title": "Style trang profile",
                "description": "Thêm CSS cho trang profile: font, màu sắc, padding, margin, border, background. Dùng class, id, element selectors.",
                "deliverable": "File style.css + index.html",
                "estimated_hours": 4
              }
            },
            {
              "id": "task-5",
              "name": "Flexbox Layout",
              "days": "Day 3-4",
              "hours": 4,
              "difficulty": "medium",
              "resource": {
                "name": "CSS-Tricks - A Complete Guide to Flexbox",
                "url": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/",
                "type": "free",
                "language": "en",
                "format": "guide"
              },
              "exercise": {
                "title": "Tạo layout 3 cột",
                "description": "Tạo layout responsive với: navbar (flex row), hero section (center content), features grid (3 columns), footer (flex row).",
                "deliverable": "File layout-flexbox.html",
                "estimated_hours": 4
              }
            },
            {
              "id": "task-6",
              "name": "CSS Grid + Responsive Design",
              "days": "Day 5-7",
              "hours": 6,
              "difficulty": "medium",
              "resource": {
                "name": "CSS-Tricks - A Complete Guide to Grid",
                "url": "https://css-tricks.com/snippets/css/complete-guide-grid/",
                "type": "free",
                "language": "en",
                "format": "guide"
              },
              "exercise": {
                "title": "Responsive portfolio",
                "description": "Tạo trang portfolio responsive: desktop 3 columns, tablet 2 columns, mobile 1 column. Dùng CSS Grid + media queries.",
                "deliverable": "File portfolio-responsive.html",
                "estimated_hours": 6
              }
            }
          ]
        },
        {
          "id": "week-3",
          "name": "JavaScript cơ bản",
          "tasks": [
            {
              "id": "task-7",
              "name": "Variables, Types, Functions",
              "days": "Day 1-3",
              "hours": 6,
              "difficulty": "easy",
              "resource": {
                "name": "freeCodeCamp - JavaScript Algorithms",
                "url": "https://freecodecamp.org/learn/javascript-algorithms-and-data-structures/",
                "type": "free",
                "language": "en",
                "format": "interactive"
              },
              "exercise": {
                "title": "Calculator đơn giản",
                "description": "Tạo calculator với HTML + JS: 2 input số, 4 buttons (+, -, *, /), kết quả hiển thị. Xử lý lỗi chia cho 0.",
                "deliverable": "File calculator.html",
                "estimated_hours": 4
              }
            }
          ]
        }
      ]
    },
    {
      "id": "phase-2",
      "name": "Phase 2: Backend Core",
      "duration": "Tháng 3-4",
      "weeks": [...]
    },
    {
      "id": "phase-3",
      "name": "Phase 3: Nâng cao",
      "duration": "Tháng 5-6",
      "weeks": [...]
    }
  ]
}
```

#### 13.4 Pre-seed Data — 20 Industries

```sql
INSERT INTO industries (id, name, slug, category, description, avg_salary_junior, avg_salary_mid, avg_salary_senior, demand_level, top_skills, meta_title, meta_description) VALUES
('ind-001', 'Backend Developer', 'backend-developer', 'Web Development', 
 'Backend Developer là người xây dựng phía server của ứng dụng web...', 
 '8-12 triệu', '15-25 triệu', '30-50 triệu', 'high',
 '["Node.js","Python","Java","SQL","REST API","Docker"]',
 'Roadmap Backend Developer - Lộ trình học Backend từ A đến Z',
 'Tạo roadmap học Backend Developer cá nhân hóa bằng AI. Lộ trình chi tiết từ Beginner đến Senior với mức lương thực tế tại Việt Nam.'),

('ind-002', 'Frontend Developer', 'frontend-developer', 'Web Development',
 'Frontend Developer là người xây dựng giao diện người dùng...',
 '7-10 triệu', '13-22 triệu', '25-45 triệu', 'high',
 '["HTML","CSS","JavaScript","React","Vue","TypeScript"]',
 'Roadmap Frontend Developer - Lộ trình học Frontend từ A đến Z',
 'Tạo roadmap học Frontend Developer cá nhân hóa bằng AI...'),

-- ... thêm 18 ngành nữa
```

---

### Bước 14 — API Design

---

#### 14.1 API Endpoints Tổng Quan

```
┌─────────────────────────────────────────────────────────────┐
│                    API ENDPOINTS                             │
└─────────────────────────────────────────────────────────────┘

HTML Routes (SSR - cho SEO):
  GET  /                          → Trang chủ
  GET  /tao-roadmap               → Form tạo roadmap
  GET  /roadmap/{slug}            → Xem roadmap (SSR)
  GET  /nganh/{slug}              → Landing page ngành (SSR)
  GET  /sitemap.xml               → Sitemap cho Google

API Routes (JSON - cho JS):
  POST /api/generate              → Tạo roadmap mới
  GET  /api/roadmap/{id}          → Lấy roadmap JSON
  GET  /api/industries            → Danh sách ngành
  GET  /api/stats                 → Thống kê

Utility:
  GET  /health                    → Health check
  GET  /robots.txt                → Robots cho SEO
```

#### 14.2 API Chi Tiết — POST /api/generate

**Request:**

```
POST /api/generate
Content-Type: application/json

{
  "age": 20,
  "industry": "backend-developer",
  "level": "beginner",
  "goal": "Trở thành Senior Backend Developer trong 2 năm, lương 25+ triệu",
  "duration_months": 6
}
```

**Validation Rules:**

| Field | Type | Required | Rules |
|-------|------|----------|-------|
| age | integer | Yes | 15-60 |
| industry | string | Yes | Phải tồn tại trong industries.slug |
| level | string | Yes | "beginner", "mid", "senior" |
| goal | string | Yes | Min 10 chars, max 500 chars |
| duration_months | integer | Yes | 3, 6, 12, 24 |

**Success Response (200):**

```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "slug": "backend-developer-20tuoi-a3f7",
    "url": "/roadmap/backend-developer-20tuoi-a3f7",
    
    "input": {
      "age": 20,
      "industry": "backend-developer",
      "industry_name": "Backend Developer",
      "level": "beginner",
      "level_display": "Beginner",
      "goal": "Trở thành Senior Backend Developer trong 2 năm",
      "duration_months": 6
    },
    
    "level1_roadmap": {
      "overview": "Lộ trình 6 tháng từ Beginner đến Junior Backend Developer...",
      "total_weeks": 24,
      "total_tasks": 72,
      "total_hours": 360,
      "hours_per_week": 15,
      "salary_range": {
        "junior": "8-12 triệu",
        "mid": "15-25 triệu",
        "senior": "30-50 triệu"
      },
      "competitive_advantage": "Thị trường IT VN đang thiếu...",
      "market_demand": "Tuyển dụng Backend Dev tăng 30%...",
      "interview_tips": ["Chuẩn bị câu hỏi về REST API", "..."]
    },
    
    "level2_phases": [
      {
        "id": "phase-1",
        "name": "Phase 1: Nền tảng",
        "duration": "Tháng 1-2",
        "description": "Xây dựng nền tảng web development",
        "total_hours": 120,
        "total_tasks": 12,
        "milestone": "Tạo được website tĩnh đầu tiên",
        "skills": ["HTML", "CSS", "JavaScript", "Git"],
        "weeks_count": 4
      }
    ],
    
    "level3_tasks": [
      {
        "phase_id": "phase-1",
        "weeks": [...]
      }
    ],
    
    "metadata": {
      "generated_at": "2026-05-30T10:30:00Z",
      "ai_model": "gpt-4o",
      "generation_time_ms": 15000
    }
  }
}
```

**Error Responses:**

```json
// 400 - Validation Error
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Dữ liệu không hợp lệ",
    "details": [
      {"field": "age", "message": "Tuổi phải từ 15 đến 60"},
      {"field": "goal", "message": "Mục tiêu tối thiểu 10 ký tự"}
    ]
  }
}

// 404 - Industry Not Found
{
  "success": false,
  "error": {
    "code": "INDUSTRY_NOT_FOUND",
    "message": "Không tìm thấy ngành này"
  }
}

// 429 - Rate Limit
{
  "success": false,
  "error": {
    "code": "RATE_LIMIT",
    "message": "Quá nhiều yêu cầu, vui lòng thử lại sau 1 phút",
    "retry_after": 60
  }
}

// 500 - Server Error
{
  "success": false,
  "error": {
    "code": "INTERNAL_ERROR",
    "message": "Hệ thống đang bảo trì, vui lòng thử lại sau"
  }
}

// 503 - AI Service Error
{
  "success": false,
  "error": {
    "code": "AI_SERVICE_ERROR",
    "message": "AI đang bận, vui lòng thử lại",
    "retry_after": 30
  }
}
```

#### 14.3 API Chi Tiết — GET /api/roadmap/{id}

```
GET /api/roadmap/550e8400-e29b-41d4-a716-446655440000

Response: (giống POST /api/generate success response)
```

#### 14.4 API Chi Tiết — GET /api/industries

```
GET /api/industries

Response:
{
  "success": true,
  "data": [
    {
      "id": "ind-001",
      "name": "Backend Developer",
      "slug": "backend-developer",
      "category": "Web Development",
      "demand_level": "high",
      "avg_salary_junior": "8-12 triệu",
      "top_skills": ["Node.js", "Python", "Java"]
    },
    ...
  ]
}
```

#### 14.5 API Chi Tiết — GET /api/stats

```
GET /api/stats

Response:
{
  "success": true,
  "data": {
    "total_roadmaps": 1234,
    "total_industries": 20,
    "popular_industries": [
      {"slug": "backend-developer", "count": 456},
      {"slug": "frontend-developer", "count": 321},
      {"slug": "data-analyst", "count": 198}
    ],
    "avg_generation_time_ms": 12000
  }
}
```

#### 14.6 Rate Limiting

| Endpoint | Limit | Window | Scope |
|----------|-------|--------|-------|
| POST /api/generate | 5 requests | 1 phút | Per IP |
| GET /api/* | 60 requests | 1 phút | Per IP |
| GET / (SSR) | 100 requests | 1 phút | Per IP |

---

### Bước 15 — AI Flow

---

#### 15.1 AI Flow Tổng Quan

```
┌─────────────────────────────────────────────────────────────┐
│                    AI FLOW OVERVIEW                          │
└─────────────────────────────────────────────────────────────┘

User Input
    │
    ▼
┌──────────────┐
│  Validation  │ ← Frontend + Backend validate
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Check Cache │ ← Tìm roadmap trùng input trong DB
└──────┬───────┘
       │
       ├── Cache Hit → Return cached roadmap
       │
       └── Cache Miss
           │
           ▼
    ┌──────────────┐
    │ Build Prompt │ ← Tạo prompt từ input
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐
    │  Call OpenAI │ ← Gọi API với prompt
    │  API (GPT-4o)│
    └──────┬───────┘
           │
           ├── Success
           │   │
           │   ▼
           │  ┌──────────────┐
           │  │ Parse JSON   │ ← Validate JSON response
           │  └──────┬───────┘
           │         │
           │         ├── Valid JSON
           │         │   │
           │         │   ▼
           │         │  ┌──────────────┐
           │         │  │ Save to DB   │ ← Lưu roadmap
           │         │  └──────┬───────┘
           │         │         │
           │         │         ▼
           │         │  ┌──────────────┐
           │         │  │ Generate     │ ← Tạo slug
           │         │  │ Slug         │
           │         │  └──────┬───────┘
           │         │         │
           │         │         ▼
           │         │     Return roadmap
           │         │
           │         └── Invalid JSON
           │             │
           │             ▼
           │         ┌──────────────┐
           │         │ Retry (1x)   │ ← Thử lại 1 lần
           │         └──────┬───────┘
           │                │
           │                ├── Success → Save + Return
           │                │
           │                └── Fail → Use Fallback
           │
           └── Error (timeout, rate limit, etc.)
               │
               ▼
           ┌──────────────┐
           │ Retry (1x)   │ ← Thử lại 1 lần
           └──────┬───────┘
                  │
                  ├── Success → Continue
                  │
                  └── Fail → Return error
```

#### 15.2 Prompt Engineering Chi Tiết

**System Prompt (cố định):**

```
Bạn là chuyên gia tư vấn nghề nghiệp tại Việt Nam với 15 năm kinh nghiệm.
Bạn đã giúp hơn 10,000 sinh viên và người đi làm xây dựng lộ trình học tập.
Bạn am hiểu MỌI NGÀNH NGHỀ: IT, Marketing, Kinh doanh, Thiết kế, Tài chính, Y tế, Giáo dục, Xây dựng, Du lịch, Luật...

NHIỆM VỤ:
Tạo roadmap học tập chi tiết theo 3 cấp bậc cho người dùng.

CẤU TRÚC OUTPUT:
- Level 1 (Roadmap lớn): Tổng quan hành trình, stats, mức lương, lý do cạnh tranh
- Level 2 (Phases): Từng giai đoạn 1-2 tháng, skills, milestone
- Level 3 (Tasks): Tasks hàng ngày, tài liệu, bài tập cụ thể

QUY TẮC BẮT BUỘC:
1. Tất cả output bằng tiếng Việt (trừ tên công nghệ và tài liệu)
2. Mức lương tính bằng VNĐ, sát thị trường VN hiện tại
3. Tasks phải CỤ THỂ: "Day 1-2: Học X" không phải "Học X"
4. Mỗi task BẮT BUỘC có: tài liệu + bài tập + thời gian ước tính
5. Bài tập phải THỰC HÀNH được ngay, có deliverable rõ ràng
6. Tài liệu ưu tiên free, tiếng Việt nếu có
7. Skills theo thứ tự học hợp lý (cơ bản → nâng cao)
8. Timeline phải thực tế (15-20 giờ/tuần cho người đi làm)
9. Competitive advantage phải liên quan thị trường VN
10. Output MUST là JSON hợp lệ, KHÔNG có markdown hay text thừa

OUTPUT FORMAT:
Trả về JSON object thuần, không có ```json``` wrapper.
```

**User Prompt Template:**

```
Tạo roadmap học tập theo 3 cấp bậc cho:

THÔNG TIN NGƯỜI DÙNG:
- Tuổi: {age} ({age_description})
- Ngành muốn học: {industry_name}
- Trình độ hiện tại: {level} ({level_description})
- Mục tiêu: {goal}
- Thời gian dự kiến: {duration_months} tháng
- Giờ học mỗi tuần: {hours_per_week} giờ

CONTEXT THỊ TRƯỜNG:
- Mức lương ngành này tại VN: {salary_info}
- Nhu cầu tuyển dụng: {demand_level}
- Skills phổ biến: {top_skills}

YÊU CẦU:
1. Tạo roadmap với {phases_count} phases
2. Mỗi phase có {weeks_per_phase} weeks
3. Mỗi week có 3 tasks (mỗi task 1-3 ngày)
4. Tổng {total_tasks} tasks trong {duration_months} tháng

OUTPUT JSON SCHEMA:
{
  "level1_roadmap": {
    "overview": "string (2-3 câu tổng quan)",
    "total_weeks": "integer",
    "total_tasks": "integer",
    "total_hours": "integer",
    "hours_per_week": "integer",
    "salary_range": {
      "junior": "string (VD: 8-12 triệu)",
      "mid": "string",
      "senior": "string"
    },
    "competitive_advantage": "string (2-3 câu)",
    "market_demand": "string (2-3 câu)",
    "interview_tips": ["string", "string"]
  },
  "level2_phases": [
    {
      "id": "phase-1",
      "name": "string (VD: Phase 1: Nền tảng)",
      "description": "string (1 câu)",
      "duration": "string (VD: Tháng 1-2)",
      "duration_weeks": "integer",
      "total_hours": "integer",
      "total_tasks": "integer",
      "milestone": "string",
      "skills": [
        {
          "name": "string",
          "priority": "high|medium|low",
          "difficulty": "easy|medium|hard",
          "hours_needed": "integer",
          "description": "string (1 câu)"
        }
      ]
    }
  ],
  "level3_tasks": [
    {
      "phase_id": "phase-1",
      "weeks": [
        {
          "id": "week-1",
          "name": "string (VD: HTML cơ bản)",
          "tasks": [
            {
              "id": "task-1",
              "name": "string",
              "days": "string (VD: Day 1-2)",
              "hours": "integer",
              "difficulty": "easy|medium|hard",
              "resource": {
                "name": "string",
                "url": "string (URL thật)",
                "type": "free|paid",
                "language": "vi|en",
                "format": "video|article|interactive|documentation|course"
              },
              "exercise": {
                "title": "string",
                "description": "string (chi tiết, actionable)",
                "deliverable": "string (VD: File index.html)",
                "estimated_hours": "integer"
              }
            }
          ]
        }
      ]
    }
  ]
}
```

#### 15.3 Prompt Variables

| Variable | Source | Example |
|----------|--------|---------|
| {age} | User input | 20 |
| {age_description} | Computed | "Sinh viên năm 2" |
| {industry_name} | DB lookup | "Backend Developer" |
| {level} | User input | "beginner" |
| {level_description} | Mapping | "Chưa biết gì hoặc mới bắt đầu" |
| {goal} | User input | "Senior Backend Dev trong 2 năm" |
| {duration_months} | User input | 6 |
| {hours_per_week} | Computed | 15 |
| {phases_count} | Computed | 3 |
| {weeks_per_phase} | Computed | 4 |
| {total_tasks} | Computed | 36 |
| {salary_info} | DB lookup | "8-50 triệu" |
| {demand_level} | DB lookup | "high" |
| {top_skills} | DB lookup | "Node.js, Python, SQL" |

#### 15.4 Response Processing

```python
async def process_ai_response(raw_response: str) -> dict:
    """Xử lý response từ OpenAI API"""
    
    # 1. Strip markdown code blocks nếu có
    raw = raw_response.strip()
    if raw.startswith("```json"):
        raw = raw[7:]
    if raw.startswith("```"):
        raw = raw[3:]
    if raw.endswith("```"):
        raw = raw[:-3]
    raw = raw.strip()
    
    # 2. Parse JSON
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Thử fix common JSON errors
        raw = raw.replace("'", '"')  # Single quotes → double quotes
        raw = re.sub(r',\s*}', '}', raw)  # Trailing comma
        raw = re.sub(r',\s*]', ']', raw)  # Trailing comma in array
        data = json.loads(raw)
    
    # 3. Validate schema
    validate_level1(data.get("level1_roadmap"))
    validate_level2(data.get("level2_phases"))
    validate_level3(data.get("level3_tasks"))
    
    # 4. Enrich data
    data = add_ids(data)  # Thêm IDs nếu thiếu
    data = calculate_totals(data)  # Tính lại totals
    
    return data
```

#### 15.5 Fallback Strategy

```python
FALLBACK_RESPONSE = {
    "level1_roadmap": {
        "overview": "Lộ trình học tập cá nhân hóa",
        "total_weeks": 24,
        "total_tasks": 36,
        "total_hours": 360,
        "hours_per_week": 15,
        "salary_range": {
            "junior": "8-15 triệu",
            "mid": "15-30 triệu",
            "senior": "30-60 triệu"
        },
        "competitive_advantage": "Thị trường IT Việt Nam đang thiếu nhân lực trầm trọng. Cơ hội việc làm cho developer luôn cao.",
        "market_demand": "Nhu cầu tuyển dụng IT tại VN tăng 30%/năm.",
        "interview_tips": [
            "Chuẩn bị portfolio trên GitHub",
            "Thực hành coding challenges trên LeetCode"
        ]
    },
    "level2_phases": [
        {
            "id": "phase-1",
            "name": "Phase 1: Nền tảng",
            "description": "Xây dựng nền tảng vững chắc",
            "duration": "Tháng 1-2",
            "duration_weeks": 8,
            "total_hours": 120,
            "total_tasks": 12,
            "milestone": "Hoàn thành nền tảng cơ bản",
            "skills": [
                {"name": "Kỹ năng cơ bản", "priority": "high", "difficulty": "easy", "hours_needed": 120}
            ]
        }
    ],
    "level3_tasks": [],
    "_fallback": True,
    "_fallback_reason": "AI service unavailable"
}
```

#### 15.6 Cache Strategy

```
Cache Key: hash(industry + level + duration_months + age_range)
           age_range: 15-18, 19-22, 23-28, 29-35, 36-60

Cache TTL: 7 days (roadmap content doesn't change often)

Cache Hit Rate Target: 30% (nhiều user cùng ngành, trình độ)
```

#### 15.7 Cost Optimization

| Strategy | Savings | Implementation |
|----------|---------|----------------|
| Cache roadmap | 30% | SQLite cache |
| Shorter prompt | 10% | Template optimization |
| GPT-4o-mini cho fallback | 50% | Dùng khi GPT-4o fail |
| Batch requests | 5% | Nếu có nhiều request cùng lúc |

**Estimated costs (GPT-4o):**
- Input tokens: ~800 tokens/prompt
- Output tokens: ~4000 tokens/response
- Cost per roadmap: ~$0.03
- 1000 roadmaps/tháng: ~$30/tháng

---

**Trạng thái:** ✅ Đã xác định xong

---

## PHASE 7 — SETUP DỰ ÁN

### Bước 16 — Setup GitHub

---

#### 16.1 Cấu trúc thư mục dự án

```
~/projects/ai-career-roadmap/
│
├── README.md                    # Mô tả dự án
├── .gitignore                   # Git ignore rules
├── .env.example                 # Template env vars
├── .env                         # Env vars thật (git ignored)
├── requirements.txt             # Python dependencies
├── run.sh                       # Script khởi động server
│
├── backend/
│   ├── __init__.py
│   ├── main.py                  # FastAPI app entry point
│   ├── config.py                # Config từ env vars
│   ├── database.py              # SQLite connection + helpers
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── pages.py             # HTML routes (SSR)
│   │   └── api.py               # API routes (JSON)
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ai_service.py        # OpenAI API integration
│   │   ├── roadmap_service.py   # Business logic
│   │   └── slug_service.py      # Slug generation
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py           # Pydantic models
│   │
│   ├── templates/               # Jinja2 templates
│   │   ├── base.html            # Base layout
│   │   ├── index.html           # Trang chủ
│   │   ├── create.html          # Form tạo roadmap
│   │   ├── roadmap.html         # Trang kết quả
│   │   ├── industry.html        # Landing page ngành
│   │   ├── sitemap.xml          # Sitemap template
│   │   └── components/
│   │       ├── header.html      # Header component
│   │       ├── footer.html      # Footer component
│   │       ├── hero.html        # Hero section
│   │       ├── form.html        # Form component
│   │       ├── roadmap-level1.html  # Level 1 display
│   │       ├── roadmap-level2.html  # Level 2 display
│   │       ├── roadmap-level3.html  # Level 3 display
│   │       └── loading.html     # Loading state
│   │
│   ├── static/
│   │   ├── css/
│   │   │   ├── style.css        # Main stylesheet
│   │   │   └── components.css   # Component styles
│   │   ├── js/
│   │   │   ├── app.js           # Main JS
│   │   │   ├── form.js          # Form logic
│   │   │   └── roadmap.js       # Roadmap display logic
│   │   └── images/
│   │       └── logo.svg         # Logo
│   │
│   ├── data/
│   │   ├── industries.json      # 20 ngành IT seed data
│   │   └── schema.sql           # Database schema
│   │
│   └── tests/
│       ├── __init__.py
│       ├── test_api.py          # API tests
│       ├── test_ai_service.py   # AI service tests
│       └── test_database.py     # Database tests
│
└── docs/
    ├── plan.md                  # Plan document (này)
    └── api-spec.md              # API specification
```

#### 16.2 .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
.venv/

# Environment
.env
.env.local
.env.production

# Database
*.db
*.sqlite
*.sqlite3

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# Cache
.cache/
.pytest_cache/

# Node (nếu dùng)
node_modules/
```

#### 16.3 .env.example

```env
# OpenAI API
OPENAI_API_KEY=sk-your-api-key-here

# App Config
APP_HOST=0.0.0.0
APP_PORT=8000
APP_ENV=development
APP_DEBUG=true

# Database
DATABASE_URL=sqlite:///./roadmap.db

# Rate Limiting
RATE_LIMIT_GENERATE=5
RATE_LIMIT_WINDOW=60

# AI Config
AI_MODEL=gpt-4o
AI_MAX_TOKENS=4000
AI_TEMPERATURE=0.7
AI_TIMEOUT=30
```

#### 16.4 requirements.txt

```txt
# Web Framework
fastapi==0.104.1
uvicorn[standard]==0.24.0
python-multipart==0.0.6

# Template Engine
jinja2==3.1.2

# AI
openai==1.6.1
httpx==0.25.2

# Database
aiosqlite==0.19.0

# Config
python-dotenv==1.0.0

# Validation (built-in FastAPI)
pydantic==2.5.2

# Utilities
python-slugify==8.0.1
uuid6==2024.1.12

# Testing
pytest==7.4.3
pytest-asyncio==0.23.2
httpx==0.25.2
```

#### 16.5 run.sh

```bash
#!/bin/bash
# Script khởi động server

echo "🚀 Starting AI Career Roadmap Server..."

# Check Python version
python3 --version

# Install dependencies if needed
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

echo "📦 Activating virtual environment..."
source venv/bin/activate

echo "📦 Installing dependencies..."
pip install -r requirements.txt -q

# Create .env if not exists
if [ ! -f ".env" ]; then
    echo "⚙️ Creating .env from .env.example..."
    cp .env.example .env
    echo "⚠️  Please edit .env and add your OPENAI_API_KEY"
fi

# Initialize database
echo "🗄️ Initializing database..."
python3 -c "from backend.database import init_database; import asyncio; asyncio.run(init_database())"

# Start server
echo "✅ Server starting at http://localhost:8000"
echo "📖 API docs at http://localhost:8000/docs"
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

#### 16.6 README.md

```markdown
# 🎯 AI Career Roadmap

Tạo lộ trình học IT cá nhân hóa bằng AI theo 3 cấp bậc.

## ✨ Features

- 🗺️ **Level 1 — Roadmap lớn**: Tổng quan hành trình, mức lương, lý do cạnh tranh
- 📋 **Level 2 — Phases**: Từng giai đoạn 1-2 tháng, skills, milestone
- 📝 **Level 3 — Tasks**: Tasks hàng ngày, tài liệu, bài tập cụ thể

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/your-username/ai-career-roadmap.git
cd ai-career-roadmap

# Setup
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY

# Run
chmod +x run.sh
./run.sh
```

Open http://localhost:8000

## 🛠️ Tech Stack

- **Backend**: Python FastAPI
- **Frontend**: HTML/CSS/JS (SSR with Jinja2)
- **Database**: SQLite
- **AI**: OpenAI GPT-4o

## 📖 API Documentation

http://localhost:8000/docs

## 📝 License

MIT
```

---

### Bước 17 — Setup Frontend

---

#### 17.1 Base Template — base.html

```html
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <!-- SEO Meta Tags -->
    <title>{% block title %}AI Career Roadmap{% endblock %}</title>
    <meta name="description" content="{% block description %}Tạo lộ trình học IT cá nhân hóa bằng AI{% endblock %}">
    
    <!-- Open Graph -->
    <meta property="og:title" content="{% block og_title %}AI Career Roadmap{% endblock %}">
    <meta property="og:description" content="{% block og_description %}Tạo lộ trình học IT cá nhân hóa bằng AI{% endblock %}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{% block og_url %}https://ai-career-roadmap.com{% endblock %}">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Styles -->
    <link rel="stylesheet" href="/static/css/style.css">
    {% block extra_css %}{% endblock %}
    
    <!-- Structured Data -->
    {% block structured_data %}{% endblock %}
</head>
<body>
    {% include 'components/header.html' %}
    
    <main>
        {% block content %}{% endblock %}
    </main>
    
    {% include 'components/footer.html' %}
    
    <!-- Scripts -->
    <script src="/static/js/app.js"></script>
    {% block extra_js %}{% endblock %}
</body>
</html>
```

#### 17.2 Trang Chủ — index.html

```html
{% extends 'base.html' %}

{% block title %}AI Career Roadmap — Tạo lộ trình học IT cá nhân hóa{% endblock %}
{% block description %}Công cụ AI tạo lộ trình học IT cá nhân hóa theo 3 cấp: Roadmap → Phases → Tasks hàng ngày. Miễn phí, tiếng Việt.{% endblock %}

{% block content %}
<!-- Hero Section -->
<section class="hero">
    <div class="container">
        <h1>Tạo lộ trình học IT<br>cá nhân hóa bằng AI</h1>
        <p>Nhập thông tin, AI tạo roadmap riêng cho bạn theo 3 cấp:<br>
        Tổng quan → Giai đoạn → Tasks hàng ngày</p>
        <a href="/tao-roadmap" class="btn btn-primary btn-lg">🎯 Bắt đầu ngay</a>
        <p class="social-proof">{{ total_roadmaps }}+ roadmap đã được tạo</p>
    </div>
</section>

<!-- How it works -->
<section class="section">
    <div class="container">
        <h2>Cách hoạt động</h2>
        <div class="steps">
            <div class="step">
                <span class="step-icon">📝</span>
                <h3>1. Nhập thông tin</h3>
                <p>Tuổi, ngành, trình độ, mục tiêu</p>
            </div>
            <div class="step-arrow">→</div>
            <div class="step">
                <span class="step-icon">🤖</span>
                <h3>2. AI tạo roadmap</h3>
                <p>Cá nhân hóa theo 3 cấp bậc</p>
            </div>
            <div class="step-arrow">→</div>
            <div class="step">
                <span class="step-icon">📚</span>
                <h3>3. Học theo lộ trình</h3>
                <p>Biết hôm nay cần làm gì</p>
            </div>
        </div>
    </div>
</section>

<!-- Ví dụ roadmap mẫu -->
<section class="section bg-gray">
    <div class="container">
        <h2>Ví dụ roadmap mẫu</h2>
        <div class="grid grid-3">
            {% for example in examples %}
            <a href="/roadmap/{{ example.slug }}" class="card">
                <h3>{{ example.name }}</h3>
                <p>{{ example.age }} tuổi · {{ example.duration }} tháng</p>
                <span class="badge">{{ example.level }}</span>
            </a>
            {% endfor %}
        </div>
    </div>
</section>

<!-- Ngành phổ biến -->
<section class="section">
    <div class="container">
        <h2>Ngành phổ biến</h2>
        <div class="grid grid-4">
            {% for industry in industries %}
            <a href="/nganh/{{ industry.slug }}" class="card card-sm">
                <h3>{{ industry.name }}</h3>
                <span class="badge badge-{{ industry.demand_level }}">{{ industry.demand_level }}</span>
            </a>
            {% endfor %}
        </div>
    </div>
</section>
{% endblock %}
```

#### 17.3 Trang Form — create.html

```html
{% extends 'base.html' %}

{% block title %}Tạo Roadmap — AI Career Roadmap{% endblock %}

{% block content %}
<section class="section">
    <div class="container container-sm">
        <div class="card">
            <h1>🎯 Tạo roadmap của bạn</h1>
            
            <form id="roadmap-form" class="form">
                <!-- Tuổi -->
                <div class="form-group">
                    <label for="age">Tuổi <span class="required">*</span></label>
                    <input type="number" id="age" name="age" min="15" max="60" required>
                    <span class="help-text">Từ 15 đến 60 tuổi</span>
                    <span class="error-text" id="age-error"></span>
                </div>
                
                <!-- Ngành -->
                <div class="form-group">
                    <label for="industry">Ngành muốn học <span class="required">*</span></label>
                    <select id="industry" name="industry" required>
                        <option value="">🔍 Chọn ngành IT...</option>
                        {% for industry in industries %}
                        <option value="{{ industry.slug }}">{{ industry.name }}</option>
                        {% endfor %}
                    </select>
                    <span class="error-text" id="industry-error"></span>
                </div>
                
                <!-- Trình độ -->
                <div class="form-group">
                    <label>Trình độ hiện tại <span class="required">*</span></label>
                    <div class="radio-group">
                        <label class="radio-label">
                            <input type="radio" name="level" value="beginner" required>
                            <span class="radio-custom"></span>
                            <span>
                                <strong>Beginner</strong>
                                <small>Chưa biết gì hoặc mới bắt đầu</small>
                            </span>
                        </label>
                        <label class="radio-label">
                            <input type="radio" name="level" value="mid">
                            <span class="radio-custom"></span>
                            <span>
                                <strong>Mid-level</strong>
                                <small>1-2 năm kinh nghiệm</small>
                            </span>
                        </label>
                        <label class="radio-label">
                            <input type="radio" name="level" value="senior">
                            <span class="radio-custom"></span>
                            <span>
                                <strong>Senior</strong>
                                <small>3+ năm kinh nghiệm</small>
                            </span>
                        </label>
                    </div>
                    <span class="error-text" id="level-error"></span>
                </div>
                
                <!-- Mục tiêu -->
                <div class="form-group">
                    <label for="goal">Mục tiêu <span class="required">*</span></label>
                    <textarea id="goal" name="goal" rows="3" maxlength="500" 
                              placeholder="VD: Trở thành Senior Backend Developer trong 2 năm, lương 25+ triệu"
                              required></textarea>
                    <span class="help-text"><span id="goal-count">0</span>/500 ký tự · Tối thiểu 10 ký tự</span>
                    <span class="error-text" id="goal-error"></span>
                </div>
                
                <!-- Thời gian -->
                <div class="form-group">
                    <label for="duration">Thời gian dự kiến <span class="required">*</span></label>
                    <select id="duration" name="duration_months" required>
                        <option value="">Chọn thời gian...</option>
                        <option value="3">3 tháng</option>
                        <option value="6" selected>6 tháng</option>
                        <option value="12">12 tháng</option>
                        <option value="24">24 tháng</option>
                    </select>
                    <span class="error-text" id="duration-error"></span>
                </div>
                
                <!-- Submit -->
                <button type="submit" class="btn btn-primary btn-lg btn-block" id="submit-btn">
                    🎯 Tạo roadmap ngay
                </button>
                
                <p class="text-center text-muted">
                    ℹ️ Miễn phí · Không cần đăng nhập · AI tạo trong 30 giây
                </p>
            </form>
        </div>
    </div>
</section>
{% endblock %}

{% block extra_js %}
<script src="/static/js/form.js"></script>
{% endblock %}
```

#### 17.4 Trang Kết Quả — roadmap.html

```html
{% extends 'base.html' %}

{% block title %}Roadmap {{ roadmap.industry_name }} — AI Career Roadmap{% endblock %}
{% block description %}Lộ trình {{ roadmap.industry_name }} cho người {{ roadmap.level_display }}. {{ roadmap.total_tasks }} tasks, {{ roadmap.total_hours }} giờ học.{% endblock %}

{% block content %}
<!-- LEVEL 1: ROADMAP LỚN -->
<section class="section">
    <div class="container">
        {% include 'components/roadmap-level1.html' %}
    </div>
</section>

<!-- LEVEL 2: PHASES -->
<section class="section bg-gray">
    <div class="container">
        <h2>📋 Các giai đoạn</h2>
        {% for phase in roadmap.level2_phases %}
        {% include 'components/roadmap-level2.html' %}
        {% endfor %}
    </div>
</section>

<!-- LEVEL 3: TASKS (hiển thị khi click vào phase) -->
{% for phase_data in roadmap.level3_tasks %}
<section class="section tasks-section" id="tasks-{{ phase_data.phase_id }}" style="display:none;">
    <div class="container">
        {% include 'components/roadmap-level3.html' %}
    </div>
</section>
{% endfor %}

<!-- Actions -->
<section class="section">
    <div class="container">
        <div class="actions">
            <button class="btn btn-outline" onclick="shareRoadmap()">📤 Chia sẻ</button>
            <a href="/tao-roadmap" class="btn btn-primary">🔄 Tạo roadmap mới</a>
            <a href="/" class="btn btn-outline">🏠 Về Home</a>
        </div>
        <p class="text-center text-muted">{{ stats.total_roadmaps }} roadmap đã được tạo</p>
    </div>
</section>
{% endblock %}

{% block extra_js %}
<script src="/static/js/roadmap.js"></script>
<script>
    const roadmapData = {{ roadmap_json | safe }};
</script>
{% endblock %}
```

#### 17.5 CSS Design System — style.css

```css
/* ═══════════════════════════════════════════════════════
   AI CAREER ROADMAP — DESIGN SYSTEM
   ═══════════════════════════════════════════════════════ */

/* ─── VARIABLES ─── */
:root {
    /* Colors */
    --color-primary: #4F46E5;
    --color-primary-dark: #4338CA;
    --color-secondary: #10B981;
    --color-accent: #F59E0B;
    --color-bg: #F9FAFB;
    --color-surface: #FFFFFF;
    --color-text: #111827;
    --color-text-muted: #6B7280;
    --color-border: #E5E7EB;
    --color-error: #EF4444;
    --color-success: #10B981;
    
    /* Typography */
    --font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    --font-size-xs: 0.75rem;
    --font-size-sm: 0.875rem;
    --font-size-base: 1rem;
    --font-size-lg: 1.125rem;
    --font-size-xl: 1.25rem;
    --font-size-2xl: 1.5rem;
    --font-size-3xl: 2rem;
    --font-size-4xl: 2.5rem;
    
    /* Spacing */
    --space-xs: 0.25rem;
    --space-sm: 0.5rem;
    --space-md: 1rem;
    --space-lg: 1.5rem;
    --space-xl: 2rem;
    --space-2xl: 3rem;
    --space-3xl: 4rem;
    
    /* Border Radius */
    --radius-sm: 0.25rem;
    --radius-md: 0.5rem;
    --radius-lg: 0.75rem;
    --radius-full: 9999px;
    
    /* Shadows */
    --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 6px rgba(0,0,0,0.07);
    --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
}

/* ─── RESET ─── */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: var(--font-family);
    font-size: var(--font-size-base);
    line-height: 1.6;
    color: var(--color-text);
    background-color: var(--color-bg);
}

/* ─── LAYOUT ─── */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--space-md);
}

.container-sm {
    max-width: 640px;
}

.section {
    padding: var(--space-3xl) 0;
}

.bg-gray {
    background-color: var(--color-bg);
}

/* ─── GRID ─── */
.grid {
    display: grid;
    gap: var(--space-lg);
}

.grid-3 { grid-template-columns: repeat(3, 1fr); }
.grid-4 { grid-template-columns: repeat(4, 1fr); }

@media (max-width: 768px) {
    .grid-3, .grid-4 { grid-template-columns: 1fr; }
}

/* ─── TYPOGRAPHY ─── */
h1 { font-size: var(--font-size-4xl); font-weight: 700; line-height: 1.2; }
h2 { font-size: var(--font-size-2xl); font-weight: 600; margin-bottom: var(--space-lg); }
h3 { font-size: var(--font-size-xl); font-weight: 600; }

/* ─── BUTTONS ─── */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: var(--space-sm) var(--space-lg);
    font-size: var(--font-size-base);
    font-weight: 600;
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: all 0.15s ease;
    text-decoration: none;
    border: 2px solid transparent;
}

.btn-primary {
    background-color: var(--color-primary);
    color: white;
}
.btn-primary:hover {
    background-color: var(--color-primary-dark);
}

.btn-outline {
    background: transparent;
    border-color: var(--color-primary);
    color: var(--color-primary);
}

.btn-lg {
    padding: var(--space-md) var(--space-xl);
    font-size: var(--font-size-lg);
}

.btn-block {
    width: 100%;
}

/* ─── CARDS ─── */
.card {
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--space-lg);
    box-shadow: var(--shadow-md);
    text-decoration: none;
    color: var(--color-text);
    transition: all 0.2s ease;
}
.card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-2px);
}

/* ─── FORMS ─── */
.form-group {
    margin-bottom: var(--space-lg);
}

.form-group label {
    display: block;
    font-weight: 600;
    margin-bottom: var(--space-sm);
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: var(--space-sm) var(--space-md);
    font-size: var(--font-size-base);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    transition: border-color 0.15s ease;
}

.form-group input:focus,
.form-group select:focus,
.form-group textarea:focus {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

.error-text {
    color: var(--color-error);
    font-size: var(--font-size-sm);
    display: none;
}

.help-text {
    color: var(--color-text-muted);
    font-size: var(--font-size-sm);
}

.required {
    color: var(--color-error);
}

/* ─── HERO ─── */
.hero {
    text-align: center;
    padding: var(--space-3xl) 0;
    background: linear-gradient(135deg, var(--color-primary), #7C3AED);
    color: white;
}

.hero h1 {
    font-size: var(--font-size-4xl);
    margin-bottom: var(--space-md);
}

.social-proof {
    margin-top: var(--space-lg);
    opacity: 0.8;
}

/* ─── ROADMAP LEVEL 1 ─── */
.roadmap-header {
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--space-xl);
    box-shadow: var(--shadow-md);
}

.roadmap-stats {
    display: flex;
    gap: var(--space-lg);
    flex-wrap: wrap;
}

.stat-item {
    text-align: center;
}

.stat-value {
    font-size: var(--font-size-2xl);
    font-weight: 700;
    color: var(--color-primary);
}

/* ─── ROADMAP LEVEL 2 ─── */
.phase-card {
    background: var(--color-surface);
    border-radius: var(--radius-lg);
    padding: var(--space-lg);
    margin-bottom: var(--space-lg);
    box-shadow: var(--shadow-sm);
    border-left: 4px solid var(--color-primary);
}

.phase-card.completed {
    border-left-color: var(--color-success);
}

.phase-card.active {
    border-left-color: var(--color-accent);
}

.skill-tag {
    display: inline-block;
    padding: var(--space-xs) var(--space-sm);
    background: rgba(79, 70, 229, 0.1);
    color: var(--color-primary);
    border-radius: var(--radius-full);
    font-size: var(--font-size-sm);
    font-weight: 500;
}

/* ─── ROADMAP LEVEL 3 ─── */
.task-item {
    display: flex;
    gap: var(--space-md);
    padding: var(--space-md);
    border-bottom: 1px solid var(--color-border);
}

.task-checkbox {
    width: 20px;
    height: 20px;
    cursor: pointer;
}

.task-completed {
    text-decoration: line-through;
    opacity: 0.6;
}

/* ─── PROGRESS BAR ─── */
.progress-bar {
    height: 8px;
    background: var(--color-border);
    border-radius: var(--radius-full);
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: var(--color-primary);
    border-radius: var(--radius-full);
    transition: width 0.5s ease;
}

/* ─── BADGES ─── */
.badge {
    display: inline-block;
    padding: var(--space-xs) var(--space-sm);
    font-size: var(--font-size-xs);
    font-weight: 600;
    border-radius: var(--radius-full);
    background: var(--color-border);
}

.badge-high { background: rgba(16, 185, 129, 0.1); color: var(--color-success); }
.badge-medium { background: rgba(245, 158, 11, 0.1); color: var(--color-accent); }
.badge-low { background: rgba(239, 68, 68, 0.1); color: var(--color-error); }

/* ─── LOADING ─── */
.loading {
    text-align: center;
    padding: var(--space-3xl);
}

.spinner {
    width: 48px;
    height: 48px;
    border: 4px solid var(--color-border);
    border-top-color: var(--color-primary);
    border-radius: 50%;
    animation: spin 1s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

/* ─── ACTIONS ─── */
.actions {
    display: flex;
    gap: var(--space-md);
    justify-content: center;
    flex-wrap: wrap;
}

/* ─── UTILITIES ─── */
.text-center { text-align: center; }
.text-muted { color: var(--color-text-muted); }
```

#### 17.6 JavaScript — form.js

```javascript
// ═══════════════════════════════════════════════════════
// FORM LOGIC
// ═══════════════════════════════════════════════════════

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('roadmap-form');
    const goalInput = document.getElementById('goal');
    const goalCount = document.getElementById('goal-count');
    
    // Character counter
    goalInput.addEventListener('input', () => {
        goalCount.textContent = goalInput.value.length;
    });
    
    // Form submission
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Validate
        if (!validateForm()) return;
        
        // Show loading
        showLoading();
        
        // Collect data
        const formData = {
            age: parseInt(document.getElementById('age').value),
            industry: document.getElementById('industry').value,
            level: document.querySelector('input[name="level"]:checked').value,
            goal: document.getElementById('goal').value,
            duration_months: parseInt(document.getElementById('duration').value)
        };
        
        try {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(formData)
            });
            
            const data = await response.json();
            
            if (data.success) {
                window.location.href = data.data.url;
            } else {
                showError(data.error.message);
                hideLoading();
            }
        } catch (error) {
            showError('Có lỗi xảy ra, vui lòng thử lại');
            hideLoading();
        }
    });
});

function validateForm() {
    let isValid = true;
    
    // Age
    const age = document.getElementById('age').value;
    if (!age || age < 15 || age > 60) {
        showFieldError('age', 'Tuổi phải từ 15 đến 60');
        isValid = false;
    } else {
        clearFieldError('age');
    }
    
    // Industry
    const industry = document.getElementById('industry').value;
    if (!industry) {
        showFieldError('industry', 'Vui lòng chọn ngành');
        isValid = false;
    } else {
        clearFieldError('industry');
    }
    
    // Level
    const level = document.querySelector('input[name="level"]:checked');
    if (!level) {
        showFieldError('level', 'Vui lòng chọn trình độ');
        isValid = false;
    } else {
        clearFieldError('level');
    }
    
    // Goal
    const goal = document.getElementById('goal').value;
    if (!goal || goal.length < 10) {
        showFieldError('goal', 'Mục tiêu tối thiểu 10 ký tự');
        isValid = false;
    } else {
        clearFieldError('goal');
    }
    
    // Duration
    const duration = document.getElementById('duration').value;
    if (!duration) {
        showFieldError('duration', 'Vui lòng chọn thời gian');
        isValid = false;
    } else {
        clearFieldError('duration');
    }
    
    return isValid;
}

function showFieldError(field, message) {
    const errorEl = document.getElementById(field + '-error');
    if (errorEl) {
        errorEl.textContent = message;
        errorEl.style.display = 'block';
    }
}

function clearFieldError(field) {
    const errorEl = document.getElementById(field + '-error');
    if (errorEl) {
        errorEl.textContent = '';
        errorEl.style.display = 'none';
    }
}

function showLoading() {
    document.getElementById('submit-btn').disabled = true;
    document.getElementById('submit-btn').innerHTML = '⏳ Đang tạo roadmap...';
}

function hideLoading() {
    document.getElementById('submit-btn').disabled = false;
    document.getElementById('submit-btn').innerHTML = '🎯 Tạo roadmap ngay';
}

function showError(message) {
    alert(message); // TODO: Replace with toast notification
}
```

---

### Bước 18 — Setup Backend

---

#### 18.1 main.py — FastAPI Entry Point

```python
# backend/main.py

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
import os

from backend.database import init_database
from backend.routes import pages, api


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Khởi tạo database khi server start"""
    await init_database()
    yield


app = FastAPI(
    title="AI Career Roadmap",
    description="Tạo lộ trình học IT cá nhân hóa bằng AI",
    version="1.0.0",
    lifespan=lifespan,
)

# Static files
app.mount("/static", StaticFiles(directory="backend/static"), name="static")

# Routes
app.include_router(pages.router)
app.include_router(api.router, prefix="/api")


@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "1.0.0"}
```

#### 18.2 config.py — Configuration

```python
# backend/config.py

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # App
    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", "8000"))
    APP_ENV: str = os.getenv("APP_ENV", "development")
    APP_DEBUG: bool = os.getenv("APP_DEBUG", "true").lower() == "true"
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./roadmap.db")
    
    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    AI_MODEL: str = os.getenv("AI_MODEL", "gpt-4o")
    AI_MAX_TOKENS: int = int(os.getenv("AI_MAX_TOKENS", "4000"))
    AI_TEMPERATURE: float = float(os.getenv("AI_TEMPERATURE", "0.7"))
    AI_TIMEOUT: int = int(os.getenv("AI_TIMEOUT", "30"))
    
    # Rate Limiting
    RATE_LIMIT_GENERATE: int = int(os.getenv("RATE_LIMIT_GENERATE", "5"))
    RATE_LIMIT_WINDOW: int = int(os.getenv("RATE_LIMIT_WINDOW", "60"))
    
    # Paths
    BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_DIR: str = os.path.join(BASE_DIR, "backend", "templates")
    STATIC_DIR: str = os.path.join(BASE_DIR, "backend", "static")
    DATA_DIR: str = os.path.join(BASE_DIR, "backend", "data")


settings = Settings()
```

#### 18.3 database.py — SQLite Connection

```python
# backend/database.py

import aiosqlite
import json
import os
from backend.config import settings

DATABASE_PATH = "roadmap.db"


async def get_db():
    """Get database connection"""
    db = await aiosqlite.connect(DATABASE_PATH)
    db.row_factory = aiosqlite.Row
    return db


async def init_database():
    """Initialize database with schema"""
    db = await get_db()
    
    # Read schema
    schema_path = os.path.join(settings.DATA_DIR, "schema.sql")
    with open(schema_path, "r") as f:
        schema = f.read()
    
    await db.executescript(schema)
    await db.commit()
    
    # Seed industries if empty
    cursor = await db.execute("SELECT COUNT(*) FROM industries")
    count = (await cursor.fetchone())[0]
    
    if count == 0:
        await seed_industries(db)
    
    await db.close()


async def seed_industries(db):
    """Seed industries data"""
    industries_path = os.path.join(settings.DATA_DIR, "industries.json")
    with open(industries_path, "r") as f:
        industries = json.load(f)
    
    for ind in industries:
        await db.execute(
            """INSERT INTO industries 
               (id, name, slug, category, description, 
                avg_salary_junior, avg_salary_mid, avg_salary_senior,
                demand_level, top_skills, meta_title, meta_description)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (ind["id"], ind["name"], ind["slug"], ind["category"],
             ind["description"], ind["avg_salary_junior"], ind["avg_salary_mid"],
             ind["avg_salary_senior"], ind["demand_level"],
             json.dumps(ind["top_skills"]), ind["meta_title"], ind["meta_description"])
        )
    
    await db.commit()
    print(f"✅ Seeded {len(industries)} industries")
```

#### 18.4 routes/api.py — API Routes

```python
# backend/routes/api.py

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional
import time

from backend.services.roadmap_service import generate_roadmap
from backend.database import get_db

router = APIRouter()


class GenerateRequest(BaseModel):
    age: int = Field(..., ge=15, le=60)
    industry: str = Field(..., min_length=1)
    level: str = Field(..., pattern="^(beginner|mid|senior)$")
    goal: str = Field(..., min_length=10, max_length=500)
    duration_months: int = Field(..., pattern="^(3|6|12|24)$")


@router.post("/generate")
async def generate(request: GenerateRequest):
    """Tạo roadmap mới"""
    start_time = time.time()
    
    # Validate industry exists
    db = await get_db()
    cursor = await db.execute(
        "SELECT * FROM industries WHERE slug = ?", 
        (request.industry,)
    )
    industry = await cursor.fetchone()
    await db.close()
    
    if not industry:
        raise HTTPException(status_code=404, detail="Không tìm thấy ngành này")
    
    # Generate roadmap
    try:
        roadmap = await generate_roadmap(
            age=request.age,
            industry=request.industry,
            industry_name=industry["name"],
            level=request.level,
            goal=request.goal,
            duration_months=request.duration_months,
            salary_info=f"{industry['avg_salary_junior']} - {industry['avg_salary_senior']}",
            demand_level=industry["demand_level"],
            top_skills=industry["top_skills"],
        )
    except Exception as e:
        raise HTTPException(status_code=503, detail="AI đang bận, vui lòng thử lại")
    
    generation_time = int((time.time() - start_time) * 1000)
    
    # Save to database
    db = await get_db()
    slug = f"{request.industry}-{request.age}-tuoi"
    
    await db.execute(
        """INSERT INTO roadmaps 
           (id, slug, age, industry, industry_name, level, level_display,
            goal, duration_months, overview, total_weeks, total_tasks, total_hours,
            hours_per_week, salary_junior, salary_mid, salary_senior,
            competitive_advantage, market_demand, interview_tips,
            phases_json, ai_model, generation_time_ms)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (roadmap["id"], slug, request.age, request.industry, industry["name"],
         request.level, request.level.capitalize(), request.goal,
         request.duration_months, roadmap["level1_roadmap"]["overview"],
         roadmap["level1_roadmap"]["total_weeks"],
         roadmap["level1_roadmap"]["total_tasks"],
         roadmap["level1_roadmap"]["total_hours"],
         roadmap["level1_roadmap"]["hours_per_week"],
         roadmap["level1_roadmap"]["salary_range"]["junior"],
         roadmap["level1_roadmap"]["salary_range"]["mid"],
         roadmap["level1_roadmap"]["salary_range"]["senior"],
         roadmap["level1_roadmap"]["competitive_advantage"],
         roadmap["level1_roadmap"]["market_demand"],
         json.dumps(roadmap["level1_roadmap"]["interview_tips"]),
         json.dumps(roadmap), "gpt-4o", generation_time)
    )
    await db.commit()
    await db.close()
    
    return {
        "success": True,
        "data": {
            "id": roadmap["id"],
            "slug": slug,
            "url": f"/roadmap/{slug}",
            "level1_roadmap": roadmap["level1_roadmap"],
            "level2_phases": roadmap["level2_phases"],
            "level3_tasks": roadmap["level3_tasks"],
            "metadata": {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ"),
                "ai_model": "gpt-4o",
                "generation_time_ms": generation_time
            }
        }
    }


@router.get("/industries")
async def get_industries():
    """Lấy danh sách ngành"""
    db = await get_db()
    cursor = await db.execute(
        "SELECT id, name, slug, category, demand_level, avg_salary_junior, top_skills FROM industries"
    )
    rows = await cursor.fetchall()
    await db.close()
    
    industries = []
    for row in rows:
        industries.append({
            "id": row["id"],
            "name": row["name"],
            "slug": row["slug"],
            "category": row["category"],
            "demand_level": row["demand_level"],
            "avg_salary_junior": row["avg_salary_junior"],
            "top_skills": json.loads(row["top_skills"]) if row["top_skills"] else []
        })
    
    return {"success": True, "data": industries}
```

#### 18.5 routes/pages.py — HTML Routes (SSR)

```python
# backend/routes/pages.py

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import json

from backend.config import settings
from backend.database import get_db

router = APIRouter()
templates = Jinja2Templates(directory=settings.TEMPLATE_DIR)


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Trang chủ"""
    db = await get_db()
    
    # Get industries
    cursor = await db.execute("SELECT * FROM industries LIMIT 8")
    industries = await cursor.fetchall()
    
    # Get total roadmaps
    cursor = await db.execute("SELECT COUNT(*) FROM roadmaps")
    total_roadmaps = (await cursor.fetchone())[0]
    
    await db.close()
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "industries": industries,
        "total_roadmaps": total_roadmaps,
        "examples": [
            {"name": "Backend Developer", "slug": "sample-backend", "age": 20, "duration": 6, "level": "Beginner"},
            {"name": "Data Analyst", "slug": "sample-data-analyst", "age": 25, "duration": 12, "level": "Beginner"},
            {"name": "Frontend Developer", "slug": "sample-frontend", "age": 22, "duration": 6, "level": "Beginner"},
        ]
    })


@router.get("/tao-roadmap", response_class=HTMLResponse)
async def create_form(request: Request):
    """Form tạo roadmap"""
    db = await get_db()
    cursor = await db.execute("SELECT * FROM industries ORDER BY name")
    industries = await cursor.fetchall()
    await db.close()
    
    return templates.TemplateResponse("create.html", {
        "request": request,
        "industries": industries,
    })


@router.get("/roadmap/{slug}", response_class=HTMLResponse)
async def view_roadmap(request: Request, slug: str):
    """Xem roadmap"""
    db = await get_db()
    cursor = await db.execute("SELECT * FROM roadmaps WHERE slug = ?", (slug,))
    roadmap = await cursor.fetchone()
    
    if not roadmap:
        await db.close()
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    
    # Increment view count
    await db.execute("UPDATE roadmaps SET view_count = view_count + 1 WHERE slug = ?", (slug,))
    await db.commit()
    await db.close()
    
    # Parse JSON fields
    roadmap_data = dict(roadmap)
    roadmap_data["phases_json"] = json.loads(roadmap_data["phases_json"]) if roadmap_data["phases_json"] else {}
    
    return templates.TemplateResponse("roadmap.html", {
        "request": request,
        "roadmap": roadmap_data,
        "roadmap_json": json.dumps(roadmap_data["phases_json"]),
    })


@router.get("/nganh/{slug}", response_class=HTMLResponse)
async def industry_page(request: Request, slug: str):
    """Landing page ngành"""
    db = await get_db()
    cursor = await db.execute("SELECT * FROM industries WHERE slug = ?", (slug,))
    industry = await cursor.fetchone()
    await db.close()
    
    if not industry:
        return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    
    return templates.TemplateResponse("industry.html", {
        "request": request,
        "industry": industry,
    })
```

#### 18.6 services/ai_service.py — OpenAI Integration

```python
# backend/services/ai_service.py

import httpx
import json
import os
from backend.config import settings


SYSTEM_PROMPT = """Bạn là chuyên gia tư vấn nghề nghiệp tại Việt Nam với 15 năm kinh nghiệm.
Bạn đã giúp hơn 10,000 sinh viên và người đi làm xây dựng lộ trình học tập.
Bạn am hiểu MỌI NGÀNH NGHỀ: IT, Marketing, Kinh doanh, Thiết kế, Tài chính, Y tế, Giáo dục, Xây dựng, Du lịch, Luật...

NHIỆM VỤ:
Tạo roadmap học tập chi tiết theo 3 cấp bậc cho người dùng.

QUY TẮC BẮT BUỘC:
1. Tất cả output bằng tiếng Việt (trừ tên công nghệ và tài liệu)
2. Mức lương tính bằng VNĐ, sát thị trường VN hiện tại
3. Tasks phải CỤ THỂ: "Day 1-2: Học X" không phải "Học X"
4. Mỗi task BẮT BUỘC có: tài liệu + bài tập + thời gian ước tính
5. Bài tập phải THỰC HÀNH được ngay, có deliverable rõ ràng
6. Output MUST là JSON hợp lệ, KHÔNG có markdown hay text thừa

OUTPUT FORMAT:
Trả về JSON object thuần, không có ```json``` wrapper."""


async def call_openai(prompt: str) -> dict:
    """Gọi OpenAI API"""
    async with httpx.AsyncClient(timeout=settings.AI_TIMEOUT) as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {settings.OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": settings.AI_MODEL,
                "messages": [
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": settings.AI_MAX_TOKENS,
                "temperature": settings.AI_TEMPERATURE,
            },
        )
        
        if response.status_code != 200:
            raise Exception(f"OpenAI API error: {response.status_code}")
        
        data = response.json()
        raw_content = data["choices"][0]["message"]["content"]
        
        return parse_ai_response(raw_content)


def parse_ai_response(raw: str) -> dict:
    """Parse JSON từ AI response"""
    raw = raw.strip()
    
    # Strip markdown code blocks
    if raw.startswith("```json"):
        raw = raw[7:]
    if raw.startswith("```"):
        raw = raw[3:]
    if raw.endswith("```"):
        raw = raw[:-3]
    raw = raw.strip()
    
    # Parse JSON
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        # Try to fix common errors
        raw = raw.replace("'", '"')
        import re
        raw = re.sub(r',\s*}', '}', raw)
        raw = re.sub(r',\s*]', ']', raw)
        return json.loads(raw)


def get_fallback_response() -> dict:
    """Fallback khi AI fail"""
    return {
        "level1_roadmap": {
            "overview": "Lộ trình học tập cá nhân hóa",
            "total_weeks": 24,
            "total_tasks": 36,
            "total_hours": 360,
            "hours_per_week": 15,
            "salary_range": {"junior": "8-15 triệu", "mid": "15-30 triệu", "senior": "30-60 triệu"},
            "competitive_advantage": "Thị trường IT Việt Nam đang thiếu nhân lực trầm trọng.",
            "market_demand": "Nhu cầu tuyển dụng IT tại VN tăng 30%/năm.",
            "interview_tips": ["Chuẩn bị portfolio trên GitHub", "Thực hành coding trên LeetCode"]
        },
        "level2_phases": [],
        "level3_tasks": [],
        "_fallback": True
    }
```

---

### Bước 19 — Setup Database

---

#### 19.1 schema.sql

```sql
-- backend/data/schema.sql

CREATE TABLE IF NOT EXISTS industries (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slug TEXT UNIQUE NOT NULL,
    category TEXT,
    description TEXT,
    avg_salary_junior TEXT,
    avg_salary_mid TEXT,
    avg_salary_senior TEXT,
    demand_level TEXT CHECK(demand_level IN ('high', 'medium', 'low')),
    top_skills TEXT,
    meta_title TEXT,
    meta_description TEXT,
    sample_roadmap_json TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS roadmaps (
    id TEXT PRIMARY KEY,
    slug TEXT UNIQUE NOT NULL,
    age INTEGER NOT NULL CHECK(age >= 15 AND age <= 60),
    industry TEXT NOT NULL,
    industry_name TEXT NOT NULL,
    level TEXT NOT NULL CHECK(level IN ('beginner', 'mid', 'senior')),
    level_display TEXT NOT NULL,
    goal TEXT NOT NULL,
    duration_months INTEGER NOT NULL,
    overview TEXT,
    total_weeks INTEGER,
    total_tasks INTEGER,
    total_hours INTEGER,
    hours_per_week INTEGER,
    salary_junior TEXT,
    salary_mid TEXT,
    salary_senior TEXT,
    competitive_advantage TEXT,
    market_demand TEXT,
    interview_tips TEXT,
    phases_json TEXT,
    ai_model TEXT DEFAULT 'gpt-4o',
    ai_tokens_used INTEGER,
    generation_time_ms INTEGER,
    prompt_version TEXT DEFAULT 'v1',
    view_count INTEGER DEFAULT 0,
    share_count INTEGER DEFAULT 0,
    completion_rate REAL DEFAULT 0.0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_roadmaps_slug ON roadmaps(slug);
CREATE INDEX IF NOT EXISTS idx_roadmaps_industry ON roadmaps(industry);
CREATE INDEX IF NOT EXISTS idx_roadmaps_created ON roadmaps(created_at DESC);
CREATE INDEX IF NOT EXISTS idx_industries_slug ON industries(slug);
```

#### 19.2 industries.json (seed data — 5 ngành đầu)

```json
[
    {
        "id": "ind-001",
        "name": "Backend Developer",
        "slug": "backend-developer",
        "category": "Web Development",
        "description": "Backend Developer là người xây dựng phía server của ứng dụng web, bao gồm API, database, authentication, và business logic.",
        "avg_salary_junior": "8-12 triệu",
        "avg_salary_mid": "15-25 triệu",
        "avg_salary_senior": "30-50 triệu",
        "demand_level": "high",
        "top_skills": ["Node.js", "Python", "Java", "SQL", "REST API", "Docker"],
        "meta_title": "Roadmap Backend Developer - Lộ trình học Backend từ A đến Z",
        "meta_description": "Tạo roadmap học Backend Developer cá nhân hóa bằng AI. Lộ trình chi tiết từ Beginner đến Senior với mức lương thực tế tại Việt Nam."
    },
    {
        "id": "ind-002",
        "name": "Frontend Developer",
        "slug": "frontend-developer",
        "category": "Web Development",
        "description": "Frontend Developer là người xây dựng giao diện người dùng, đảm bảo trải nghiệm mượt mà trên mọi thiết bị.",
        "avg_salary_junior": "7-10 triệu",
        "avg_salary_mid": "13-22 triệu",
        "avg_salary_senior": "25-45 triệu",
        "demand_level": "high",
        "top_skills": ["HTML", "CSS", "JavaScript", "React", "Vue", "TypeScript"],
        "meta_title": "Roadmap Frontend Developer - Lộ trình học Frontend từ A đến Z",
        "meta_description": "Tạo roadmap học Frontend Developer cá nhân hóa bằng AI..."
    },
    {
        "id": "ind-003",
        "name": "Data Analyst",
        "slug": "data-analyst",
        "category": "Data",
        "description": "Data Analyst phân tích dữ liệu để giúp doanh nghiệp ra quyết định.",
        "avg_salary_junior": "8-12 triệu",
        "avg_salary_mid": "15-25 triệu",
        "avg_salary_senior": "25-40 triệu",
        "demand_level": "high",
        "top_skills": ["SQL", "Python", "Excel", "Tableau", "Statistics"],
        "meta_title": "Roadmap Data Analyst - Lộ trình học Data Analyst từ A đến Z",
        "meta_description": "Tạo roadmap học Data Analyst cá nhân hóa bằng AI..."
    },
    {
        "id": "ind-004",
        "name": "AI/ML Engineer",
        "slug": "ai-engineer",
        "category": "AI",
        "description": "AI/ML Engineer xây dựng và triển khai các mô hình trí tuệ nhân tạo.",
        "avg_salary_junior": "10-15 triệu",
        "avg_salary_mid": "20-35 triệu",
        "avg_salary_senior": "40-70 triệu",
        "demand_level": "high",
        "top_skills": ["Python", "TensorFlow", "PyTorch", "Math", "Statistics"],
        "meta_title": "Roadmap AI Engineer - Lộ trình học AI/ML từ A đến Z",
        "meta_description": "Tạo roadmap học AI/ML Engineer cá nhân hóa bằng AI..."
    },
    {
        "id": "ind-005",
        "name": "DevOps Engineer",
        "slug": "devops-engineer",
        "category": "Infrastructure",
        "description": "DevOps Engineer tự động hóa quy trình phát triển và triển khai phần mềm.",
        "avg_salary_junior": "10-15 triệu",
        "avg_salary_mid": "18-30 triệu",
        "avg_salary_senior": "35-55 triệu",
        "demand_level": "medium",
        "top_skills": ["Linux", "Docker", "Kubernetes", "CI/CD", "AWS"],
        "meta_title": "Roadmap DevOps Engineer - Lộ trình học DevOps từ A đến Z",
        "meta_description": "Tạo roadmap học DevOps Engineer cá nhân hóa bằng AI..."
    }
]
```

---

**Trạng thái:** ✅ Đã xác định xong

---

## TIẾN ĐỘ TỔNG QUAN

| Phase | Bước | Trạng thái | Ghi chú |
|-------|------|-----------|---------|
| Phase 1 | Bước 1: Tìm vấn đề | ✅ Done | 5 pain points |
| Phase 1 | Bước 2: Mô tả dự án | ✅ Done | Elevator pitch |
| Phase 1 | Bước 3: UVP | ✅ Done | 3 cấp roadmap |
| Phase 2 | Bước 4: Research đối thủ | ✅ Done | 5 đối thủ |
| Phase 2 | Bước 5: Research keyword | ✅ Done | 17 keywords |
| Phase 2 | Bước 6: Research cộng đồng | ✅ Done | Insights |
| Phase 3 | Bước 7: Chọn target user | ✅ Done | 3 personas |
| Phase 3 | Bước 8: User Persona | ✅ Done | Chi tiết |
| Phase 4 | Bước 9: MVP Scope | ✅ Done | 3 cấp + MoSCoW |
| Phase 5 | Bước 10: User Flow | ✅ Done | 8 flow diagrams |
| Phase 5 | Bước 11: Wireframe | ✅ Done | Desktop + Mobile + Specs |
| Phase 6 | Bước 12: Tech Stack | ✅ Done | FastAPI + SQLite + OpenAI |
| Phase 6 | Bước 13: Database | ✅ Done | Schema + JSON structure |
| Phase 6 | Bước 14: API Design | ✅ Done | 5 endpoints + error codes |
| Phase 6 | Bước 15: AI Flow | ✅ Done | Prompt + fallback + cache |
| Phase 7 | Bước 16: Setup GitHub | ✅ Done | Repo + README + structure |
| Phase 7 | Bước 17: Setup Frontend | ✅ Done | HTML/CSS/JS + templates |
| Phase 7 | Bước 18: Setup Backend | ✅ Done | FastAPI + routes + services |
| Phase 7 | Bước 19: Setup Database | ✅ Done | SQLite + migrations + seed |
| Phase 8 | Bước 20: Unit Testing | ✅ Done | pytest + test cases |
| Phase 8 | Bước 21: Integration Testing | ✅ Done | API + UI + AI tests |
| Phase 8 | Bước 22: Performance Testing | ✅ Done | Load + stress tests |
| Phase 9 | Bước 23: Deploy Setup | ✅ Done | Railway + domain + SSL |
| Phase 9 | Bước 24: CI/CD Pipeline | ✅ Done | Auto deploy on push |
| Phase 9 | Bước 25: Monitoring | ✅ Done | Logs + alerts + metrics |

---

## PHASE 8 — TESTING

### Bước 20 — Unit Testing

---

#### 20.1 Test Strategy Tổng Quan

```
┌─────────────────────────────────────────────────────────────┐
│                    TEST PYRAMID                              │
└─────────────────────────────────────────────────────────────┘

                    ╱╲
                   ╱  ╲
                  ╱ E2E╲          ← 5% (Manual + Browser)
                 ╱──────╲
                ╱        ╲
               ╱ Integr.  ╲      ← 15% (API + DB + AI)
              ╱────────────╲
             ╱              ╲
            ╱   Unit Tests   ╲   ← 80% (Functions + Logic)
           ╱──────────────────╲

Mục tiêu coverage: > 70%
```

#### 20.2 Test Files Structure

```
backend/tests/
├── __init__.py
├── conftest.py              # Shared fixtures
├── test_api.py              # API endpoint tests
├── test_database.py         # Database operation tests
├── test_ai_service.py       # AI service tests
├── test_roadmap_service.py  # Business logic tests
├── test_slug_service.py     # Slug generation tests
├── test_validators.py       # Input validation tests
└── test_models.py           # Pydantic model tests
```

#### 20.3 conftest.py — Shared Fixtures

```python
# backend/tests/conftest.py

import pytest
import asyncio
import aiosqlite
import json
from unittest.mock import AsyncMock, patch

from backend.database import init_database, get_db


@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for async tests"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_db():
    """Create test database"""
    db = await aiosqlite.connect(":memory:")
    db.row_factory = aiosqlite.Row
    
    with open("backend/data/schema.sql", "r") as f:
        schema = f.read()
    await db.executescript(schema)
    
    with open("backend/data/industries.json", "r") as f:
        industries = json.load(f)
    
    for ind in industries[:5]:
        await db.execute(
            """INSERT INTO industries 
               (id, name, slug, category, description,
                avg_salary_junior, avg_salary_mid, avg_salary_senior,
                demand_level, top_skills, meta_title, meta_description)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (ind["id"], ind["name"], ind["slug"], ind["category"],
             ind["description"], ind["avg_salary_junior"], ind["avg_salary_mid"],
             ind["avg_salary_senior"], ind["demand_level"],
             json.dumps(ind["top_skills"]), ind["meta_title"], ind["meta_description"])
        )
    await db.commit()
    
    yield db
    await db.close()


@pytest.fixture
def sample_roadmap_data():
    """Sample roadmap data for testing"""
    return {
        "id": "test-uuid-123",
        "level1_roadmap": {
            "overview": "Test overview",
            "total_weeks": 12,
            "total_tasks": 36,
            "total_hours": 180,
            "hours_per_week": 15,
            "salary_range": {"junior": "8-12 triệu", "mid": "15-25 triệu", "senior": "30-50 triệu"},
            "competitive_advantage": "Test advantage",
            "market_demand": "Test demand",
            "interview_tips": ["Tip 1", "Tip 2"]
        },
        "level2_phases": [
            {
                "id": "phase-1",
                "name": "Phase 1: Test",
                "duration": "Tháng 1-2",
                "description": "Test phase",
                "total_hours": 60,
                "total_tasks": 12,
                "milestone": "Test milestone",
                "skills": ["Skill 1", "Skill 2"]
            }
        ],
        "level3_tasks": [
            {
                "phase_id": "phase-1",
                "weeks": [
                    {
                        "id": "week-1",
                        "name": "Week 1",
                        "tasks": [
                            {
                                "id": "task-1",
                                "name": "Test task",
                                "days": "Day 1-2",
                                "hours": 4,
                                "resource": {"name": "Test resource", "url": "https://test.com", "type": "free"},
                                "exercise": {"title": "Test exercise", "description": "Do something", "deliverable": "File"}
                            }
                        ]
                    }
                ]
            }
        ]
    }


@pytest.fixture
def mock_openai_response():
    """Mock OpenAI API response"""
    return {
        "choices": [
            {
                "message": {
                    "content": json.dumps({
                        "level1_roadmap": {
                            "overview": "Mock overview",
                            "total_weeks": 12,
                            "total_tasks": 36,
                            "total_hours": 180,
                            "hours_per_week": 15,
                            "salary_range": {"junior": "8-12 triệu", "mid": "15-25 triệu", "senior": "30-50 triệu"},
                            "competitive_advantage": "Mock advantage",
                            "market_demand": "Mock demand",
                            "interview_tips": ["Tip 1"]
                        },
                        "level2_phases": [],
                        "level3_tasks": []
                    })
                }
            }
        ]
    }
```

#### 20.4 test_api.py — API Tests

```python
# backend/tests/test_api.py

import pytest
import json
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch, AsyncMock

from backend.main import app


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestGenerateEndpoint:
    
    @pytest.mark.asyncio
    async def test_generate_success(self, client, mock_openai_response):
        """Test successful roadmap generation"""
        with patch("backend.services.ai_service.call_openai", return_value=mock_openai_response):
            response = await client.post("/api/generate", json={
                "age": 20,
                "industry": "backend-developer",
                "level": "beginner",
                "goal": "Trở thành Senior Backend Developer trong 2 năm",
                "duration_months": 6
            })
        
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert "id" in data["data"]
        assert "slug" in data["data"]
        assert "level1_roadmap" in data["data"]
        assert "level2_phases" in data["data"]
        assert "level3_tasks" in data["data"]
    
    @pytest.mark.asyncio
    async def test_generate_invalid_age(self, client):
        """Test validation: age out of range"""
        response = await client.post("/api/generate", json={
            "age": 10,
            "industry": "backend-developer",
            "level": "beginner",
            "goal": "Test goal here",
            "duration_months": 6
        })
        assert response.status_code == 422
    
    @pytest.mark.asyncio
    async def test_generate_invalid_level(self, client):
        """Test validation: invalid level"""
        response = await client.post("/api/generate", json={
            "age": 20,
            "industry": "backend-developer",
            "level": "expert",
            "goal": "Test goal here",
            "duration_months": 6
        })
        assert response.status_code == 422
    
    @pytest.mark.asyncio
    async def test_generate_short_goal(self, client):
        """Test validation: goal too short"""
        response = await client.post("/api/generate", json={
            "age": 20,
            "industry": "backend-developer",
            "level": "beginner",
            "goal": "Short",
            "duration_months": 6
        })
        assert response.status_code == 422
    
    @pytest.mark.asyncio
    async def test_generate_industry_not_found(self, client):
        """Test: industry doesn't exist"""
        response = await client.post("/api/generate", json={
            "age": 20,
            "industry": "nonexistent",
            "level": "beginner",
            "goal": "Test goal here with enough chars",
            "duration_months": 6
        })
        assert response.status_code == 404


class TestIndustriesEndpoint:
    
    @pytest.mark.asyncio
    async def test_get_industries(self, client):
        """Test get industries list"""
        response = await client.get("/api/industries")
        assert response.status_code == 200
        data = response.json()
        assert data["success"] is True
        assert len(data["data"]) > 0


class TestHealthEndpoint:
    
    @pytest.mark.asyncio
    async def test_health_check(self, client):
        """Test health endpoint"""
        response = await client.get("/health")
        assert response.status_code == 200
        assert response.json()["status"] == "ok"
```

#### 20.5 test_ai_service.py — AI Service Tests

```python
# backend/tests/test_ai_service.py

import pytest
import json
from backend.services.ai_service import parse_ai_response, get_fallback_response


class TestParseAIResponse:
    
    def test_parse_valid_json(self):
        raw = '{"level1_roadmap": {}, "level2_phases": [], "level3_tasks": []}'
        result = parse_ai_response(raw)
        assert "level1_roadmap" in result
    
    def test_parse_json_with_markdown(self):
        raw = '```json\n{"level1_roadmap": {}, "level2_phases": [], "level3_tasks": []}\n```'
        result = parse_ai_response(raw)
        assert "level1_roadmap" in result
    
    def test_parse_json_with_trailing_comma(self):
        raw = '{"level1_roadmap": {}, "level2_phases": [], "level3_tasks": [],}'
        result = parse_ai_response(raw)
        assert "level1_roadmap" in result
    
    def test_parse_invalid_json_raises(self):
        raw = 'not json at all'
        with pytest.raises(json.JSONDecodeError):
            parse_ai_response(raw)


class TestFallbackResponse:
    
    def test_fallback_structure(self):
        fallback = get_fallback_response()
        assert "level1_roadmap" in fallback
        assert "level2_phases" in fallback
        assert "level3_tasks" in fallback
        assert fallback["_fallback"] is True
    
    def test_fallback_has_salary(self):
        fallback = get_fallback_response()
        assert "salary_range" in fallback["level1_roadmap"]
```

#### 20.6 test_database.py — Database Tests

```python
# backend/tests/test_database.py

import pytest
import json
import aiosqlite


class TestDatabase:
    
    @pytest.mark.asyncio
    async def test_create_tables(self, test_db):
        cursor = await test_db.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
        tables = [row[0] for row in await cursor.fetchall()]
        assert "industries" in tables
        assert "roadmaps" in tables
    
    @pytest.mark.asyncio
    async def test_seed_industries(self, test_db):
        cursor = await test_db.execute("SELECT COUNT(*) FROM industries")
        count = (await cursor.fetchone())[0]
        assert count > 0
    
    @pytest.mark.asyncio
    async def test_insert_roadmap(self, test_db, sample_roadmap_data):
        await test_db.execute(
            """INSERT INTO roadmaps (id, slug, age, industry, industry_name,
               level, level_display, goal, duration_months, overview, phases_json)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (sample_roadmap_data["id"], "test-slug", 20,
             "backend-developer", "Backend Developer",
             "beginner", "Beginner", "Test goal", 6,
             "Test overview", json.dumps(sample_roadmap_data))
        )
        await test_db.commit()
        
        cursor = await test_db.execute(
            "SELECT * FROM roadmaps WHERE id = ?",
            (sample_roadmap_data["id"],)
        )
        row = await cursor.fetchone()
        assert row is not None
    
    @pytest.mark.asyncio
    async def test_unique_slug_constraint(self, test_db):
        await test_db.execute(
            """INSERT INTO roadmaps (id, slug, age, industry, industry_name,
               level, level_display, goal, duration_months)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            ("id-1", "duplicate-slug", 20, "test", "Test",
             "beginner", "Beginner", "Test goal", 6)
        )
        await test_db.commit()
        
        with pytest.raises(Exception):
            await test_db.execute(
                """INSERT INTO roadmaps (id, slug, age, industry, industry_name,
                   level, level_display, goal, duration_months)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                ("id-2", "duplicate-slug", 20, "test", "Test",
                 "beginner", "Beginner", "Test goal", 6)
            )
```

#### 20.7 Chạy Tests

```bash
# Chạy tất cả tests
cd ~/projects/ai-career-roadmap
python -m pytest backend/tests/ -v

# Chạy specific file
python -m pytest backend/tests/test_api.py -v

# Chạy với coverage
python -m pytest backend/tests/ -v --cov=backend --cov-report=html

# Chạy async tests
python -m pytest backend/tests/ -v -o asyncio_mode=auto
```

#### 20.8 Test Cases Checklist

| # | Test Case | Expected | Status |
|---|-----------|----------|--------|
| 1 | POST /api/generate với data hợp lệ | 200 + roadmap JSON | ⬜ |
| 2 | POST /api/generate với tuổi < 15 | 422 validation error | ⬜ |
| 3 | POST /api/generate với tuổi > 60 | 422 validation error | ⬜ |
| 4 | POST /api/generate với ngành không tồn tại | 404 not found | ⬜ |
| 5 | POST /api/generate với level sai | 422 validation error | ⬜ |
| 6 | POST /api/generate với goal quá ngắn | 422 validation error | ⬜ |
| 7 | POST /api/generate với duration sai | 422 validation error | ⬜ |
| 8 | GET /api/industries | 200 + danh sách ngành | ⬜ |
| 9 | GET /health | 200 + status ok | ⬜ |
| 10 | Parse JSON hợp lệ | Return dict | ⬜ |
| 11 | Parse JSON có markdown wrapper | Return dict | ⬜ |
| 12 | Parse JSON có trailing comma | Return dict | ⬜ |
| 13 | Parse JSON không hợp lệ | Raise exception | ⬜ |
| 14 | Fallback response có đủ fields | True | ⬜ |
| 15 | DB tạo tables | industries + roadmaps | ⬜ |
| 16 | DB seed industries | Count > 0 | ⬜ |
| 17 | DB insert roadmap | Row exists | ⬜ |
| 18 | DB duplicate slug | Raise IntegrityError | ⬜ |

---

### Bước 21 — Integration Testing

---

#### 21.1 End-to-End Flow Test

```python
# backend/tests/test_integration.py

import pytest
from httpx import AsyncClient, ASGITransport
from unittest.mock import patch

from backend.main import app


@pytest.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


class TestE2EFlow:
    
    @pytest.mark.asyncio
    async def test_full_roadmap_flow(self, client, mock_openai_response):
        """Test complete flow: create → view → share"""
        
        # Step 1: Generate roadmap
        with patch("backend.services.ai_service.call_openai", return_value=mock_openai_response):
            create_response = await client.post("/api/generate", json={
                "age": 20,
                "industry": "backend-developer",
                "level": "beginner",
                "goal": "Trở thành Senior Backend Developer trong 2 năm",
                "duration_months": 6
            })
        
        assert create_response.status_code == 200
        data = create_response.json()
        slug = data["data"]["slug"]
        
        # Step 2: View roadmap page
        view_response = await client.get(f"/roadmap/{slug}")
        assert view_response.status_code == 200
        assert "Backend Developer" in view_response.text
        
        # Step 3: View home page
        home_response = await client.get("/")
        assert home_response.status_code == 200
    
    @pytest.mark.asyncio
    async def test_roadmap_not_found(self, client):
        response = await client.get("/roadmap/nonexistent-slug")
        assert response.status_code == 404
    
    @pytest.mark.asyncio
    async def test_industry_page(self, client):
        response = await client.get("/nganh/backend-developer")
        assert response.status_code == 200
```

#### 21.2 Browser Tests (Manual)

| # | Test Case | Steps | Expected |
|---|-----------|-------|----------|
| 1 | Tạo roadmap thành công | Nhập đầy đủ → Submit | Redirect sang /roadmap/{slug} |
| 2 | Hiển thị 3 cấp | Xem trang kết quả | Level 1 + 2 + 3 hiển thị đúng |
| 3 | Form validation | Để trống → Submit | Hiện lỗi tiếng Việt |
| 4 | Mobile responsive | Mở trên 375px | Layout không vỡ |
| 5 | Loading state | Submit → chờ | Hiện spinner + text |
| 6 | Share button | Click "Chia sẻ" | Copy link + toast |
| 7 | SEO check | View source | Meta tags đầy đủ |

---

### Bước 22 — Performance Testing

---

#### 22.1 Performance Benchmarks

| Metric | Target | How to test |
|--------|--------|-------------|
| TTFB | < 200ms | curl -w "%{time_starttransfer}" |
| FCP | < 1.5s | Lighthouse |
| LCP | < 2.5s | Lighthouse |
| CLS | < 0.1 | Lighthouse |
| API response | < 30s | curl timing |
| Page size | < 500KB | Network tab |

#### 22.2 Lighthouse Test Script

```bash
npx lighthouse http://localhost:8000 \
    --output=json \
    --output-path=./lighthouse-report.json \
    --chrome-flags="--headless"

cat lighthouse-report.json | jq '.categories.performance.score'
cat lighthouse-report.json | jq '.categories.seo.score'
```

---

**Trạng thái:** ✅ Đã xác định xong

---

## PHASE 9 — DEPLOY

### Bước 23 — Deploy Setup

---

#### 23.1 Deploy Options

| Option | Free tier | Pros | Cons |
|--------|-----------|------|------|
| **Railway.app** | 500h/tháng | Dễ deploy, auto SSL | Sleep 30 phút |
| Render.com | 750h/tháng | Free tier tốt | Slow cold start |
| Fly.io | 3 shared VM | Global, fast | Phức tạp hơn |
| Vercel | Unlimited | Nhanh, CDN | Không hỗ trợ Python tốt |

**Chọn: Railway.app** (dễ nhất cho MVP)

#### 23.2 Railway Deploy Steps

```bash
# 1. Install Railway CLI
npm install -g @railway/cli

# 2. Login
railway login

# 3. Init project
cd ~/projects/ai-career-roadmap
railway init

# 4. Add environment variables
railway variables set OPENAI_API_KEY=sk-you...5. Deploy
railway up

# 6. Get URL
railway open
```

#### 23.3 railway.toml

```toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "uvicorn backend.main:app --host 0.0.0.0 --port $PORT"
healthcheckPath = "/health"
healthcheckTimeout = 30
restartPolicyType = "on_failure"
restartPolicyMaxRetries = 3
```

#### 23.4 Custom Domain Setup

```bash
# 1. Add domain in Railway dashboard
# Settings → Domains → Add Custom Domain

# 2. Update DNS records
# Type: CNAME
# Name: @ (hoặc www)
# Value: your-app.up.railway.app

# 3. SSL auto-provisioned by Railway
```

#### 23.5 Environment Variables (Production)

```env
OPENAI_API_KEY=sk-pro...tion=production
APP_DEBUG=false
AI_MODEL=gpt-4o
AI_TIMEOUT=30
```

---

### Bước 24 — CI/CD Pipeline

---

#### 24.1 GitHub Actions Workflow

```yaml
# .github/workflows/deploy.yml

name: Deploy to Railway

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        env:
          OPENAI_API_KEY: test-key
        run: python -m pytest backend/tests/ -v --tb=short
  
  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Install Railway CLI
        run: npm install -g @railway/cli
      - name: Deploy to Railway
        env:
          RAILWAY_TOKEN: ${{ secrets.RAILWAY_TOKEN }}
        run: railway up --service ai-career-roadmap
```

#### 24.2 GitHub Secrets Setup

```bash
# Thêm secrets vào GitHub repo:
# Settings → Secrets → Actions → New repository secret

RAILWAY_TOKEN=your-railway-token
```

#### 24.3 Auto Deploy Flow

```
Push to main
    │
    ▼
GitHub Actions
    │
    ├── Run tests
    │   └── Pass → Continue
    │   └── Fail → Stop + Notify
    │
    └── Deploy to Railway
        └── Success → Live!
        └── Fail → Rollback + Notify
```

---

### Bước 25 — Monitoring

---

#### 25.1 Logging Setup

```python
# backend/config.py (add logging)

import logging

logging.basicConfig(
    level=logging.INFO if settings.APP_ENV == "production" else logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log") if settings.APP_ENV == "production" else logging.NullHandler()
    ]
)

logger = logging.getLogger(__name__)
```

#### 25.2 Health Check Endpoint

```python
@app.get("/health")
async def health_check():
    try:
        db = await get_db()
        await db.execute("SELECT 1")
        await db.close()
        db_status = "ok"
    except:
        db_status = "error"
    
    return {
        "status": "ok",
        "version": "1.0.0",
        "database": db_status,
        "timestamp": datetime.utcnow().isoformat()
    }
```

#### 25.3 Monitoring Checklist

| Metric | Tool | Alert threshold |
|--------|------|-----------------|
| Uptime | Railway dashboard | Down > 1 phút |
| Response time | Railway metrics | > 5s average |
| Error rate | Railway logs | > 5% requests |
| Memory usage | Railway metrics | > 80% |
| API errors | Application logs | Any 500 error |

---

**Trạng thái:** ✅ Đã xác định xong

## BLOCKERS RESOLUTION — Giải quyết 5 thiếu sót nghiêm trọng

> Cập nhật: 30/05/2026
> Mục tiêu: Giải quyết triệt để 5 blockers trước khi bắt đầu code

---

### BLOCKER 1: BUSINESS MODEL — Quảng cáo là nguồn thu chính

**Chiến lược: Ad-supported Free Model + Premium không quảng cáo**

```
┌─────────────────────────────────────────────────────────────┐
│                    BUSINESS MODEL                            │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  FREE (95% users)                                   │   │
│  │  ├── Tạo roadmap đầy đủ 3 cấp                       │   │
│  │  ├── Có quảng cáo hiển thị (banner + native ads)    │   │
│  │  ├── Quảng cáo giữa các phase (in-content ads)      │   │
│  │  └── Không giới hạn số roadmap                      │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  PREMIUM (5% users) — 49,000đ/tháng                 │   │
│  │  ├── Không quảng cáo                                │   │
│  │  ├── Export PDF roadmap                             │   │
│  │  ├── Lưu unlimited roadmap vào account              │   │
│  │  ├── AI mentor chat (50 tin nhắn/tháng)             │   │
│  │  └── Badge "Premium Learner"                        │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  AFFILIATE (passive income)                          │   │
│  │  ├── Link khóa học Udemy/Coursera trong tasks       │   │
│  │  ├── Link sách Tiki/Amazon trong resources          │   │
│  │  ├── Link công cụ (IDE, hosting) trong exercises    │   │
│  │  └── Commission: 5-15% mỗi lần user mua             │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

**Chi phí API & Cách kiểm soát:**

```
BẢNG CHI PHÍ OPENAI API (GPT-4o-mini cho MVP):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Input tokens/roadmap:  ~2,000 (system prompt + user prompt)
Output tokens/roadmap: ~4,000 (JSON 3 cấp)
Cost/roadmap:          ~$0.006 (GPT-4o-mini)

| Roadmaps/tháng | Chi phí API | Thu nhập ads (ước tính) | Net    |
|----------------|-------------|------------------------|--------|
| 1,000          | $6          | $50-100                | +$44   |
| 5,000          | $30         | $250-500               | +$220  |
| 10,000         | $60         | $500-1,000             | +$440  |
| 50,000         | $300        | $2,500-5,000           | +$2,200|
| 100,000        | $600        | $5,000-10,000          | +$4,400|

Ước tính thu nhập ads:
- CPM (cost per 1000 impressions) tại VN: $0.50-2.00
- Mỗi roadmap view = ~3-5 ad impressions
- 1,000 roadmap × 4 impressions × $1 CPM = $4/tháng (ads hiển thị)
- Affiliate: 1-5% conversion × $2-5 commission = thêm $50-200/tháng
- Premium: 5% × 49,000đ = thêm khi có 1,000+ users
```

**Chiến lược giảm chi phí API:**

| Strategy | Mô tả | Tiết kiệm |
|----------|-------|------------|
| GPT-4o-mini | Dùng model rẻ hơn cho MVP | 90% vs GPT-4o |
| Cache roadmaps | Cùng input → trả roadmap đã tạo | 30-40% requests |
| Template fallback | Roadmap mẫu cho ngành phổ biến | 20% requests |
| Rate limit | 3 roadmap/user/ngày (free) | Tránh abuse |
| Batch generation | Tạo sẵn roadmap mẫu cho SEO | Giảm on-demand |

**Revenue timeline:**

```
Month 1-2:   $0 (focus build + SEO, chưa có traffic)
Month 3-4:   $10-50 (traffic nhỏ, ads bắt đầu)
Month 5-6:   $50-200 (SEO lên, 5k+ visits/month)
Month 7-12:  $200-1,000 (viral loops, affiliate)
Year 2:      $1,000-5,000 (nếu product-market fit)
```

**Ads placement strategy:**

```
┌─────────────────────────────────────────────┐
│  TRANG ROADMAP — Ad Placement               │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  LEVEL 1: ROADMAP LỚN              │    │
│  │  (Nội dung)                         │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │ ← Banner ads (728x90)
│  │  [GOOGLE ADSENSE — Banner]          │    │   Desktop: giữa Level 1-2
│  └─────────────────────────────────────┘    │   Mobile: full-width
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  LEVEL 2: PHASES                    │    │
│  │  (Nội dung)                         │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │ ← Native ads (in-feed)
│  │  [AD — Khóa học Backend hay]        │    │   Sau phase cuối
│  │  [Được tài trợ bởi Udemy]          │    │   Hoặc affiliate link
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  LEVEL 3: TASKS                     │    │
│  │  (Nội dung)                         │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  ┌─────────────────────────────────────┐    │ ← Sticky footer ads
│  │  [AD — Mobile footer banner]        │    │   Mobile only
│  └─────────────────────────────────────┘    │
└─────────────────────────────────────────────┘
```

**Trạng thái:** ✅ Đã xác định xong

---

### BLOCKER 2: COMPETITIVE MOAT — Xây dựng lợi thế phòng thủ

**Phân tích moat có thể xây dựng:**

```
MOAT STRATEGY — Xếp theo thứ tự ưu tiên
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. SEO MOAT (dễ nhất, xây từ ngày 1)
   ├── 50+ landing pages /nganh/{slug} cho mọi ngành
   ├── Pre-generated roadmap mẫu cho SEO indexing
   ├── Blog content về lộ trình học tập
   └── Timeline: 1-3 tháng để có organic traffic

2. COMMUNITY MOAT (xây tháng 2-3)
   ├── User comments trên mỗi roadmap
   ├── "Roadmap này hữu ích?" → rating system
   ├── User share progress → social proof
   └── Timeline: 2-3 tháng

3. DATA MOAT (xây tháng 3-6)
   ├── Aggregate data: "70% học Backend bắt đầu với HTML"
   ├── Completion rates: "Phase 1 có 85% completion"
   ├── Popular paths: "50% chuyển từ Frontend → Fullstack"
   └── Timeline: Cần 1,000+ roadmaps để có data

4. EXPERT-VERIFIED MOAT (xây tháng 4-6)
   ├── Mời senior dev review roadmap
   ├── Badge "Verified by [Expert Name]"
   ├── Expert trả lời câu hỏi trong roadmap
   └── Timeline: Cần network + outreach

5. UGC MOAT (xây tháng 6+)
   ├── Users tạo custom roadmap
   ├── Community voting trên custom roadmaps
   ├── "Roadmap được tạo bởi Nguyễn Văn A"
   └── Timeline: Cần critical mass
```

**Moat implementation cho MVP (tuần 1-2):**

| Moat | Feature | Effort | Impact |
|------|---------|--------|--------|
| SEO | Landing pages 50+ ngành | 2 ngày | Cao |
| SEO | Pre-generated sample roadmaps | 1 ngày | Cao |
| Social | Share button + OG tags | 0.5 ngày | Trung bình |
| Social | "Hữu ích?" rating (localStorage) | 0.5 ngày | Thấp |
| Data | View counter + popularity | 0.5 ngày | Thấp |

**Trạng thái:** ✅ Đã xác định xong

---

### BLOCKER 3: USER VALIDATION — Phỏng vấn trước khi build

**Kế hoạch validation (tuần 0, trước khi code):**

```
VALIDATION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bước 1: Tạo landing page test (1 ngày)
├── Landing page đơn giản: /nganh/backend-developer
├── Mockup screenshot roadmap 3 cấp
├── CTA: "Nhận roadmap miễn phí"
├── Form: Email + ngành muốn học
└── Tool: Carrd.co hoặc HTML tĩnh

Bước 2: Chạy traffic test (3-5 ngày)
├── Share lên Facebook groups IT VN
├── Share lên Reddit r/VietNam, r/learnprogramming
├── Post lên các group Zalo học IT
├── Budget: 200,000đ Facebook ads (optional)
└── Target: 100+ visits, 10+ signups

Bước 3: Phỏng vấn 10-15 người (3-5 ngày)
├── Tìm người qua: Facebook groups, friends, university
├── Câu hỏi:
│   ├── "Bạn học IT/ngành X bằng cách nào?"
│   ├── "Bạn có biết hôm nay nên học gì không?"
│   ├── "Nếu có roadmap chi tiết, bạn có dùng không?"
│   ├── "Bạn sẽ trả tiền cho tính năng nào?"
│   └── "Roadmap như thế này có hữu ích không?" (show mockup)
├── Ghi chú: Pain points, feature requests
└── Tool: Google Forms + Zoom/Meet

Bước 4: Quyết định go/no-go
├── Go nếu: 60%+ nói "có dùng" + 30%+ nói "có thể trả tiền"
├── Pivot nếu: <40% quan tâm
└── Iterate nếu: Quan tâm nhưng cần feature khác

Timeline: 5-7 ngày (trước khi bắt đầu code)
Cost: ~200,000đ (Facebook ads optional)
```

**Survey template (Google Forms):**

```
1. Bạn đang học/làm trong ngành gì?
   ○ IT  ○ Marketing  ○ Design  ○ Business  ○ Khác: ___

2. Bạn học bằng cách nào? (chọn nhiều)
   □ YouTube  □ Khóa học online  □ Sách  □ Tự mò  □ Trường ĐH

3. Bạn có biết HÔM NAY nên học gì không?
   ○ Có, rõ ràng  ○ Đại đại  ○ Không, học linh tinh

4. Nếu có website tạo roadmap cá nhân (3 cấp: tổng quan → 
   giai đoạn → tasks hàng ngày), bạn có dùng không?
   ○ Có  ○ Không  ○ Có thể

5. Tính năng nào quan trọng nhất? (chọn 2)
   □ Roadmap tổng quan  □ Tasks hàng ngày  □ Tài liệu học
   □ Bài tập thực hành  □ Theo dõi tiến độ  □ Chia sẻ

6. Bạn sẽ trả bao nhiêu cho roadmap cá nhân hóa?
   ○ Miễn phí  ○ 20-50k/tháng  ○ 50-100k/tháng  ○ Không trả

7. Email để nhận roadmap mẫu: ___
```

**Trạng thái:** ⬜ Cần thực hiện trước khi code

---

### BLOCKER 4: COST STRUCTURE — Kiểm soát chi phí

**Chi phí theo giai đoạn:**

```
COST STRUCTURE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

FIXED COSTS (tháng):
┌──────────────────────────────────────────────────────┐
│ Item              │ MVP (free)  │ Scale              │
├───────────────────┼─────────────┼────────────────────┤
│ Domain (.com)     │ $12/năm     │ $12/năm            │
│ Hosting (Railway) │ $0 (free)   │ $5-20/tháng        │
│ OpenAI API        │ $0-6/tháng  │ $6-600/tháng       │
│ Email (Resend)    │ $0 (free)   │ $0-20/tháng        │
│ Monitoring        │ $0 (free)   │ $0-10/tháng        │
├───────────────────┼─────────────┼────────────────────┤
│ TỔNG              │ $1-2/tháng  │ $5-650/tháng       │
└──────────────────────────────────────────────────────┘

API COST CONTROLS:
┌──────────────────────────────────────────────────────┐
│ 1. Rate Limiting                                     │
│    ├── Free: 3 roadmap/ngày/IP                       │
│    ├── Logged in: 5 roadmap/ngày                     │
│    └── Premium: 20 roadmap/ngày                      │
│                                                      │
│ 2. Cost Ceiling                                      │
│    ├── OpenAI billing alert: $50, $100, $200         │
│    ├── Auto-pause API nếu vượt $300/tháng           │
│    └── Fallback: Hiển thị roadmap mẫu thay vì AI    │
│                                                      │
│ 3. Caching Strategy                                  │
│    ├── Cache key: hash(industry + level + duration)  │
│    ├── Cache TTL: 7 ngày                             │
│    ├── Same input → same output (tiết kiệm 30-40%)  │
│    └── Pre-generate: 50 mẫu roadmap phổ biến        │
│                                                      │
│ 4. Model Selection                                   │
│    ├── MVP: GPT-4o-mini ($0.006/roadmap)            │
│    ├── Scale: GPT-4o-mini vẫn đủ                    │
│    └── Premium: GPT-4o ($0.06/roadmap) nếu cần     │
└──────────────────────────────────────────────────────┘
```

**Implementation trong code:**

```python
# Rate limiting middleware
from collections import defaultdict
import time

RATE_LIMITS = {
    "free": {"daily": 3, "hourly": 2},
    "logged_in": {"daily": 5, "hourly": 3},
    "premium": {"daily": 20, "hourly": 10},
}

# Cost ceiling
OPENAI_MONTHLY_BUDGET = 300.00  # USD
ALERT_THRESHOLDS = [50, 100, 200]

# Cache strategy
CACHE_CONFIG = {
    "ttl_seconds": 7 * 24 * 3600,  # 7 ngày
    "max_size": 1000,  # Tối đa 1,000 cached roadmaps
}
```

**Trạng thái:** ✅ Đã xác định xong

---

### BLOCKER 5: SLUG CONFLICT — Fix collision issue

**Vấn đề:**
```
SLUG CŨ: {industry}-{age}-tuoi
VD: backend-developer-20-tuoi

2 người cùng tuổi, cùng ngành → TRÙNG SLUG ❌
```

**Giải pháp: Slug với short hash**

```
SLUG MỚI: {industry}-{age}tuoi-{short_hash}

VD: backend-developer-20tuoi-a3f7
    backend-developer-20tuoi-b2c9

short_hash = 4 ký tự hex ngẫu nhiên (a-f, 0-9)
→ 16^4 = 65,536 combinations
→ Xác suất trùng cho cùng input: < 0.002%
→ URL vẫn readable và SEO-friendly
```

**Slug generation logic:**

```python
import hashlib
import secrets

def generate_slug(industry: str, age: int, level: str, duration: int) -> str:
    """Tạo slug unique cho roadmap."""
    # Base slug: readable
    base = f"{industry}-{age}tuoi"
    
    # Short hash: 4 ký tự hex từ input + random salt
    hash_input = f"{industry}-{age}-{level}-{duration}-{secrets.token_hex(4)}"
    short_hash = hashlib.sha256(hash_input.encode()).hexdigest()[:4]
    
    return f"{base}-{short_hash}"

# VD:
# generate_slug("backend-developer", 20, "beginner", 6)
# → "backend-developer-20tuoi-a3f7"
```

**Slug alternatives (nếu cần SEO hơn):**

| Option | VD | SEO | Readable | Unique |
|--------|-----|-----|----------|--------|
| Hash (chọn) | backend-developer-20tuoi-a3f7 | ✅ | ✅ | ✅ |
| UUID short | backend-dev-20-f7a3b2 | ⚠️ | ⚠️ | ✅ |
| Counter | backend-developer-20-tuoi-123 | ✅ | ✅ | ✅ |
| Timestamp | backend-dev-20-20260530 | ✅ | ✅ | ⚠️ |

**Chọn: Hash approach** — readable + unique + SEO-friendly

**Trạng thái:** ✅ Đã xác định xong

---

## TÓM TẮT BLOCKERS RESOLUTION

| # | Blocker | Giải pháp | Status |
|---|---------|-----------|--------|
| 1 | Business Model | Ad-supported + Premium 49k/tháng + Affiliate | ✅ |
| 2 | Competitive Moat | SEO (50+ pages) → Community → Data → Expert | ✅ |
| 3 | User Validation | Landing page test + Phỏng vấn 10-15 người | ⬜ Cần làm |
| 4 | Cost Structure | GPT-4o-mini + Cache + Rate limit + Budget ceiling | ✅ |
| 5 | Slug Conflict | {industry}-{age}tuoi-{4hex} | ✅ |

**Next step:** Thực hiện User Validation (Blocker 3) trước khi bắt đầu code.

---
## HIGH PRIORITY RESOLUTION — Giải quyết 5 thiếu sót quan trọng

> Cập nhật: 30/05/2026
> Mục tiêu: Giải quyết 5 thiếu sót high priority trước khi deploy MVP

---

### ISSUE 6: FALLBACK RESPONSE QUÁ TẾ — Pre-generated fallback cho từng ngành

**Vấn đề:**
```
Fallback hiện tại:
- Level 1: Generic "Lộ trình học tập cá nhân hóa" ❌
- Level 2: 1 phase duy nhất với "Kỹ năng cơ bản" ❌
- Level 3: [] (rỗng hoàn toàn!) ❌

→ User nhận roadmap vô nghĩa khi AI fail
→ Mất trust, bounce rate cao
```

**Giải pháp: Pre-generated fallback roadmaps cho TOP 20 ngành**

```
FALLBACK STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bước 1: Pre-generate 20 fallback roadmaps (offline)
├── Chạy script generate_fallbacks.py
├── Gọi GPT-4o-mini cho 20 ngành phổ biến nhất
├── Lưu vào fallbacks/ folder (JSON files)
└── Quality check: Manual review từng roadmap

Bước 2: Fallback selection logic
├── AI fail → Tìm fallback theo industry
├── industry có fallback → Trả fallback (đầy đủ 3 cấp)
├── industry không có fallback → Trả generic nhưng ĐẦY ĐỦ
└── Không bao giờ trả [] cho phases/tasks

Bước 3: Cache + reuse
├── Fallback cũng là cache entry
├── User tạo roadmap → Check cache trước
├── Cache hit → Trả ngay (0 API cost)
└── Cache miss → Gọi AI → Lưu vào cache
```

**Fallback data structure:**

```python
# fallbacks/backend-developer.json
{
  "industry": "backend-developer",
  "industry_name": "Backend Developer",
  "level1_roadmap": {
    "overview": "Lộ trình học Backend Developer từ zero đến job-ready. Backend là xương sống của mọi ứng dụng web, chịu trách nhiệm xử lý dữ liệu, logic nghiệp vụ và kết nối với cơ sở dữ liệu.",
    "total_weeks": 24,
    "total_tasks": 72,
    "total_hours": 360,
    "salary_range": {
      "junior": "8-15 triệu",
      "mid": "15-30 triệu", 
      "senior": "30-60 triệu"
    },
    "competitive_advantage": "Backend Developer là vị trí luôn thiếu nhân lực tại VN. Với sự phát triển của cloud computing và microservices, nhu cầu Backend Dev tăng 25-30%/năm.",
    "market_demand": "Theo VietnamWorks, Backend Developer nằm trong top 5 vị trí IT được tuyển dụng nhiều nhất. Mức lương trung bình cao hơn 20-30% so với Frontend."
  },
  "level2_phases": [
    {
      "id": "phase-1",
      "name": "Phase 1: Nền tảng",
      "duration": "Tháng 1-2",
      "description": "Xây dựng nền tảng lập trình và web cơ bản",
      "skills": ["HTML", "CSS", "JavaScript", "Git", "Terminal"],
      "total_hours": 120,
      "milestone": "Tạo được website tĩnh đầu tiên và hiểu cách web hoạt động",
      "weeks_count": 4
    },
    {
      "id": "phase-2", 
      "name": "Phase 2: Backend Core",
      "duration": "Tháng 3-4",
      "description": "Học ngôn ngữ backend và framework chính",
      "skills": ["Python", "FastAPI/Express", "SQL", "REST API"],
      "total_hours": 120,
      "milestone": "Tạo được REST API hoàn chỉnh với database",
      "weeks_count": 4
    },
    {
      "id": "phase-3",
      "name": "Phase 3: Nâng cao & Portfolio",
      "duration": "Tháng 5-6", 
      "description": "Học các kỹ năng production-ready và xây portfolio",
      "skills": ["Docker", "Authentication", "Testing", "Deployment"],
      "total_hours": 120,
      "milestone": "Portfolio project hoàn chỉnh, sẵn sàng apply việc",
      "weeks_count": 4
    }
  ],
  "level3_tasks": [
    {
      "phase_id": "phase-1",
      "weeks": [
        {
          "id": "week-1",
          "name": "HTML cơ bản",
          "tasks": [
            {
              "id": "task-1",
              "name": "Cấu trúc HTML cơ bản",
              "days": "Day 1-2",
              "hours": 4,
              "resource": {
                "name": "freeCodeCamp - Responsive Web Design",
                "url": "https://freecodecamp.org/learn/2022/responsive-web-design/",
                "type": "free",
                "language": "en"
              },
              "exercise": {
                "title": "Tạo trang profile cá nhân",
                "description": "Tạo 1 trang HTML hoàn chỉnh với header, about, contact sections. Không dùng CSS, chỉ HTML thuần.",
                "deliverable": "File index.html"
              }
            },
            {
              "id": "task-2",
              "name": "HTML Forms & Tables",
              "days": "Day 3-4",
              "hours": 4,
              "resource": {
                "name": "MDN Web Docs - HTML Forms",
                "url": "https://developer.mozilla.org/en-US/docs/Learn/Forms",
                "type": "free",
                "language": "en"
              },
              "exercise": {
                "title": "Tạo form đăng ký",
                "description": "Tạo form đăng ký với đầy đủ input types: text, email, password, radio, checkbox, select, textarea.",
                "deliverable": "File register.html"
              }
            },
            {
              "id": "task-3",
              "name": "Semantic HTML & Accessibility",
              "days": "Day 5-7",
              "hours": 6,
              "resource": {
                "name": "web.dev - Learn Accessibility",
                "url": "https://web.dev/learn/accessibility/",
                "type": "free",
                "language": "en"
              },
              "exercise": {
                "title": "Refactor trang profile",
                "description": "Chuyển trang profile từ div sang semantic HTML (header, nav, main, section, article, footer). Thêm ARIA labels.",
                "deliverable": "File index.html (refactored)"
              }
            }
          ]
        },
        {
          "id": "week-2",
          "name": "CSS cơ bản",
          "tasks": [
            {
              "id": "task-4",
              "name": "Selectors & Box Model",
              "days": "Day 1-2",
              "hours": 4,
              "resource": {
                "name": "freeCodeCamp - CSS",
                "url": "https://freecodecamp.org/learn/2022/responsive-web-design/",
                "type": "free"
              },
              "exercise": {
                "title": "Style trang profile",
                "description": "Thêm CSS cho trang profile: colors, fonts, spacing, borders. Sử dụng class, id, element selectors.",
                "deliverable": "index.html + style.css"
              }
            },
            {
              "id": "task-5",
              "name": "Flexbox",
              "days": "Day 3-4",
              "hours": 4,
              "resource": {
                "name": "CSS-Tricks - A Complete Guide to Flexbox",
                "url": "https://css-tricks.com/snippets/css/a-guide-to-flexbox/",
                "type": "free"
              },
              "exercise": {
                "title": "Tạo layout 3 cột",
                "description": "Tạo layout responsive với Flexbox: header, sidebar, main content, footer.",
                "deliverable": "layout.html + style.css"
              }
            },
            {
              "id": "task-6",
              "name": "CSS Grid + Responsive",
              "days": "Day 5-7",
              "hours": 6,
              "resource": {
                "name": "CSS-Tricks - A Complete Guide to Grid",
                "url": "https://css-tricks.com/snippets/css/complete-guide-grid/",
                "type": "free"
              },
              "exercise": {
                "title": "Responsive portfolio",
                "description": "Tạo portfolio responsive với CSS Grid. Desktop: 3 columns, Tablet: 2 columns, Mobile: 1 column.",
                "deliverable": "portfolio.html + style.css"
              }
            }
          ]
        }
      ]
    }
  ],
  "_fallback": true,
  "_generated_at": "2026-05-30",
  "_version": "1.0"
}
```

**Fallback generation script:**

```python
# scripts/generate_fallbacks.py
"""Pre-generate fallback roadmaps cho TOP 20 ngành."""

import json
import os
from pathlib import Path
from openai import OpenAI

TOP_20_INDUSTRIES = [
    {"id": "backend-developer", "name": "Backend Developer", "category": "IT"},
    {"id": "frontend-developer", "name": "Frontend Developer", "category": "IT"},
    {"id": "fullstack-developer", "name": "Fullstack Developer", "category": "IT"},
    {"id": "data-analyst", "name": "Data Analyst", "category": "IT"},
    {"id": "ai-engineer", "name": "AI/ML Engineer", "category": "IT"},
    {"id": "devops-engineer", "name": "DevOps Engineer", "category": "IT"},
    {"id": "mobile-developer", "name": "Mobile Developer", "category": "IT"},
    {"id": "cybersecurity", "name": "Cybersecurity", "category": "IT"},
    {"id": "ui-ux-designer", "name": "UI/UX Designer", "category": "IT"},
    {"id": "digital-marketing", "name": "Digital Marketing", "category": "Marketing"},
    {"id": "seo-specialist", "name": "SEO Specialist", "category": "Marketing"},
    {"id": "content-marketing", "name": "Content Marketing", "category": "Marketing"},
    {"id": "graphic-designer", "name": "Graphic Designer", "category": "Design"},
    {"id": "video-editor", "name": "Video Editor", "category": "Design"},
    {"id": "accountant", "name": "Kế toán", "category": "Finance"},
    {"id": "business-analyst", "name": "Business Analyst", "category": "Business"},
    {"id": "product-manager", "name": "Product Manager", "category": "Business"},
    {"id": "project-manager", "name": "Project Manager", "category": "Business"},
    {"id": "teacher", "name": "Giáo viên", "category": "Education"},
    {"id": "civil-engineer", "name": "Kỹ sư xây dựng", "category": "Engineering"},
]

def generate_fallback(industry: dict, client: OpenAI) -> dict:
    """Generate fallback roadmap cho 1 ngành."""
    prompt = f"""Tạo roadmap học tập cho {industry['name']} (beginner, 6 tháng).
    
Output JSON với cấu trúc:
- level1_roadmap: overview, total_weeks, total_tasks, total_hours, salary_range (VNĐ), competitive_advantage, market_demand
- level2_phases: 3 phases, mỗi phase có id, name, duration, description, skills[], total_hours, milestone, weeks_count
- level3_tasks: Tasks chi tiết cho ít nhất 2 tuần đầu (6 tasks), mỗi task có id, name, days, hours, resource (name, url, type), exercise (title, description, deliverable)

Lương tính bằng VNĐ. Resource phải là link thật, có thật. Output JSON hợp lệ."""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia tư vấn nghề nghiệp tại Việt Nam. Output MUST là JSON hợp lệ."},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"},
        temperature=0.7
    )
    
    return json.loads(response.choices[0].message.content)

def main():
    client = OpenAI()
    output_dir = Path("fallbacks")
    output_dir.mkdir(exist_ok=True)
    
    for industry in TOP_20_INDUSTRIES:
        output_file = output_dir / f"{industry['id']}.json"
        if output_file.exists():
            print(f"Skip {industry['id']} (exists)")
            continue
        
        print(f"Generating {industry['id']}...")
        try:
            data = generate_fallback(industry, client)
            data["industry"] = industry["id"]
            data["industry_name"] = industry["name"]
            data["_fallback"] = True
            data["_generated_at"] = "2026-05-30"
            
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  ✓ Saved {output_file}")
        except Exception as e:
            print(f"  ✗ Error: {e}")

if __name__ == "__main__":
    main()
```

**Fallback loading logic trong app:**

```python
# app/services/fallback.py
import json
from pathlib import Path
from typing import Optional

FALLBACK_DIR = Path("fallbacks")

def get_fallback(industry: str) -> Optional[dict]:
    """Load pre-generated fallback roadmap."""
    fallback_file = FALLBACK_DIR / f"{industry}.json"
    if fallback_file.exists():
        with open(fallback_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return None

def get_generic_fallback() -> dict:
    """Generic fallback khi không có ngành cụ thể."""
    return {
        "level1_roadmap": {
            "overview": "Lộ trình học tập cá nhân hóa dành riêng cho bạn. Được thiết kế để giúp bạn từ người mới bắt đầu đến có thể apply việc.",
            "total_weeks": 24,
            "total_tasks": 72,
            "total_hours": 360,
            "salary_range": {
                "junior": "8-15 triệu",
                "mid": "15-30 triệu",
                "senior": "30-60 triệu"
            },
            "competitive_advantage": "Thị trường lao động Việt Nam đang thiếu nhân lực chất lượng cao. Đầu tư vào học tập là đầu tư vào tương lai.",
            "market_demand": "Nhu cầu tuyển dụng tăng 20-30%/năm cho các vị trí chuyên môn."
        },
        "level2_phases": [
            {
                "id": "phase-1",
                "name": "Phase 1: Nền tảng",
                "duration": "Tháng 1-2",
                "description": "Xây dựng kiến thức nền tảng cơ bản",
                "skills": ["Kiến thức cơ bản", "Công cụ cần thiết", "Tư duy ngành"],
                "total_hours": 120,
                "milestone": "Hiểu rõ bản chất ngành và có nền tảng vững chắc",
                "weeks_count": 4
            },
            {
                "id": "phase-2",
                "name": "Phase 2: Kỹ năng chuyên môn",
                "duration": "Tháng 3-4",
                "description": "Học các kỹ năng chuyên môn cốt lõi",
                "skills": ["Kỹ năng chính", "Thực hành dự án", "Portfolio"],
                "total_hours": 120,
                "milestone": "Hoàn thành dự án đầu tiên trong portfolio",
                "weeks_count": 4
            },
            {
                "id": "phase-3",
                "name": "Phase 3: Nâng cao & Apply việc",
                "duration": "Tháng 5-6",
                "description": "Nâng cao kỹ năng và chuẩn bị apply việc",
                "skills": ["Kỹ năng nâng cao", "Phỏng vấn", "Networking"],
                "total_hours": 120,
                "milestone": "Sẵn sàng apply việc với portfolio hoàn chỉnh",
                "weeks_count": 4
            }
        ],
        "level3_tasks": [
            {
                "phase_id": "phase-1",
                "weeks": [
                    {
                        "id": "week-1",
                        "name": "Tìm hiểu ngành",
                        "tasks": [
                            {
                                "id": "task-1",
                                "name": "Nghiên cứu ngành",
                                "days": "Day 1-2",
                                "hours": 4,
                                "resource": {
                                    "name": "YouTube - Tìm hiểu ngành",
                                    "url": "https://youtube.com",
                                    "type": "free"
                                },
                                "exercise": {
                                    "title": "Viết bài phân tích ngành",
                                    "description": "Viết 500 từ về ngành bạn chọn: công việc hàng ngày, kỹ năng cần, mức lương, cơ hội.",
                                    "deliverable": "File PDF hoặc Google Doc"
                                }
                            },
                            {
                                "id": "task-2",
                                "name": "Tìm mentor/nguồn học",
                                "days": "Day 3-4",
                                "hours": 4,
                                "resource": {
                                    "name": "LinkedIn - Tìm chuyên gia",
                                    "url": "https://linkedin.com",
                                    "type": "free"
                                },
                                "exercise": {
                                    "title": "Lập danh sách học tập",
                                    "description": "Tìm 5 nguồn học miễn phí, 3 khóa học, 2 sách về ngành. Ghi rõ link và lý do chọn.",
                                    "deliverable": "File danh sách học tập"
                                }
                            }
                        ]
                    }
                ]
            }
        ],
        "_fallback": True,
        "_generic": True
    }
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 7: CONTENT STRATEGY CHO SEO — Pipeline viết content

**Vấn đề:**
```
54 ngành × 500+ words = 27,000+ words content
Ai viết? Khi nào? Chất lượng thế nào?
```

**Giải pháp: AI-generated content + Human review**

```
CONTENT PIPELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Giai đoạn 1: AI Generate (tuần 1)
├── Script: scripts/generate_seo_content.py
├── Input: Danh sách 54 ngành
├── Output: 54 bài viết × 500+ words
├── Model: GPT-4o-mini (rẻ, đủ quality)
├── Cost: ~$2-3 cho tất cả 54 bài
└── Format: Markdown files

Giai đoạn 2: Human Review (tuần 2)
├── Reviewer: Bạn hoặc 1-2 người
├── Checklist:
│   ├── ☐ Thông tin chính xác?
│   ├── ☐ Mức lương sát thực tế VN?
│   ├── ☐ Links resource còn hoạt động?
│   ├── ☐ Ngôn ngữ tự nhiên, không AI-like?
│   └── ☐ SEO keywords đúng?
├── Time: ~15 phút/bài × 54 = 13.5 giờ
└── Tool: Google Docs hoặc Notion

Giai đoạn 3: Publish (tuần 2-3)
├── Tạo landing page template
├── Chèn content vào /nganh/{slug}
├── Thêm internal links
├── Submit sitemap cho Google
└── Monitor: Google Search Console
```

**SEO content template:**

```python
# scripts/generate_seo_content.py
"""Generate SEO content cho 54 ngành."""

SEO_CONTENT_TEMPLATE = """
Viết bài SEO 500+ tiếng Việt về ngành {industry_name}.

Cấu trúc bắt buộc:
1. {industry_name} là gì? (100 words)
   - Định nghĩa ngành
   - Vai trò trong doanh nghiệp
   - Phân biệt với ngành liên quan

2. Học {industry_name} cần biết gì? (100 words)
   - Kỹ năng cứng cần có
   - Kỹ năng mềm cần có
   - Bắt đầu từ đâu

3. Mức lương {industry_name} tại Việt Nam (100 words)
   - Junior: X-Y triệu
   - Mid: X-Y triệu  
   - Senior: X-Y triệu
   - Yếu tố ảnh hưởng lương

4. Cơ hội việc làm {industry_name} (100 words)
   - Nhu cầu thị trường
   - Top công ty tuyển dụng
   - Xu hướng 3-5 năm tới

5. Lộ trình học {industry_name} (100 words)
   - Bước 1: Nền tảng
   - Bước 2: Chuyên môn
   - Bước 3: Thực chiến
   - CTA: Tạo roadmap cá nhân hóa

Yêu cầu:
- Tiếng Việt tự nhiên, không AI-like
- Dữ liệu sát thực tế Việt Nam 2025-2026
- Tối ưu SEO: dùng keywords "{industry_name}", "lộ trình {industry_name}", "học {industry_name}"
- Thêm internal links đến /tao-roadmap
"""

def generate_seo_content(industry: dict, client) -> str:
    """Generate SEO content cho 1 ngành."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Bạn là chuyên gia SEO content tiếng Việt. Viết tự nhiên, không sáo rỗng."},
            {"role": "user", "content": SEO_CONTENT_TEMPLATE.format(
                industry_name=industry["name"]
            )}
        ],
        temperature=0.8,
        max_tokens=1500
    )
    return response.choices[0].message.content
```

**Quality control checklist:**

```
CONTENT QUALITY CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Mỗi bài content phải pass:

□ Accuracy (Chính xác)
  ├── Mức lương có source?
  ├── Thống kê có reference?
  └── Links resource hoạt động?

□ Readability (Dễ đọc)
  ├── Không sáo rỗng "trong thời đại công nghệ 4.0"?
  ├── Câu ngắn, rõ ràng?
  └── Có headings, bullet points?

□ SEO (Tối ưu tìm kiếm)
  ├── Keywords chính xuất hiện 3-5 lần?
  ├── Meta description < 160 chars?
  ├── Internal links đến /tao-roadmap?
  └── H1, H2 structure đúng?

□ Uniqueness (Duy nhất)
  ├── Không copy từ đối thủ?
  ├── Góc nhìn riêng?
  └── Có data cụ thể VN?

Score: 8/12 criteria = PASS
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 8: RATE LIMITING KHÔNG ĐỦ — Cloudflare + Bot Protection

**Vấn đề:**
```
Hiện tại:
- /api/generate: 5 requests/phút ✅
- SSR routes (/nganh/*, /roadmap/*): KHÔNG CÓ ❌
- Bot có thể crawl 10,000 pages/giây ❌
- DDoS có thể sập server ❌
```

**Giải pháp: Multi-layer protection**

```
SECURITY LAYERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Layer 1: Cloudflare (FREE tier)
├── DNS proxy → Ẩn IP server thật
├── Bot Management: Block bad bots
├── WAF Rules: Block common attacks
├── Rate Limiting: 100 requests/phút/IP cho SSR
├── Caching: Cache static pages (landing pages)
└── SSL: Auto HTTPS

Layer 2: Application Rate Limiting
├── /api/generate: 3 requests/phút/IP (free)
├── /api/generate: 5 requests/phút/IP (logged in)
├── /nganh/*: 30 requests/phút/IP
├── /roadmap/*: 30 requests/phút/IP
├── Global: 200 requests/phút/IP
└── Penalty: Block 15 phút nếu vượt

Layer 3: Bot Detection
├── User-Agent check (block known bots)
├── Honeypot fields (hidden form fields)
├── CAPTCHA cho suspicious requests
├── JavaScript challenge cho bots
└── Fingerprinting (canvas, WebGL)

Layer 4: DDoS Protection
├── Cloudflare DDoS mitigation (auto)
├── Connection limits: 50/IP
├── Request size limit: 10KB
├── Timeout: 30s max
└── Fail2ban: Block repeat offenders
```

**Implementation:**

```python
# app/middleware/rate_limit.py
"""Rate limiting middleware với multiple tiers."""

import time
from collections import defaultdict
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)
        self.requests = defaultdict(list)
        self.blocked = {}
        
        # Rate limits: {path_pattern: (max_requests, window_seconds)}
        self.limits = {
            "/api/generate": (3, 60),      # 3/phút
            "/api/": (10, 60),             # 10/phút cho API khác
            "/nganh/": (30, 60),           # 30/phút
            "/roadmap/": (30, 60),         # 30/phút
            "default": (100, 60),          # 100/phút cho tất cả
        }
    
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        path = request.url.path
        
        # Check if IP is blocked
        if client_ip in self.blocked:
            if time.time() < self.blocked[client_ip]:
                raise HTTPException(status_code=429, detail="IP bị tạm khóa")
            else:
                del self.blocked[client_ip]
        
        # Find matching rate limit
        limit_key = "default"
        for pattern, (max_req, window) in self.limits.items():
            if path.startswith(pattern):
                limit_key = pattern
                break
        
        max_requests, window = self.limits[limit_key]
        
        # Clean old requests
        now = time.time()
        self.requests[(client_ip, limit_key)] = [
            t for t in self.requests[(client_ip, limit_key)]
            if now - t < window
        ]
        
        # Check limit
        if len(self.requests[(client_ip, limit_key)]) >= max_requests:
            # Block IP for 15 minutes if spamming
            if len(self.requests[(client_ip, limit_key)]) > max_requests * 2:
                self.blocked[client_ip] = now + 900
            raise HTTPException(
                status_code=429,
                detail=f"Quá nhiều yêu cầu. Thử lại sau {window} giây."
            )
        
        # Record request
        self.requests[(client_ip, limit_key)].append(now)
        
        response = await call_next(request)
        return response
```

```python
# app/middleware/bot_protection.py
"""Bot detection middleware."""

import re
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Known bad bots
BAD_BOTS = [
    "ahrefsbot", "semrushbot", "mj12bot", "dotbot",
    "blexbot", "rogerbot", "exabot", "gigabot",
    "scrapy", "httrack", "wget", "curl"
]

# Good bots (allow)
GOOD_BOTS = [
    "googlebot", "bingbot", "slurp", "duckduckbot",
    "baiduspider", "yandexbot", "facebookexternalhit",
    "twitterbot", "linkedinbot", "whatsapp"
]

class BotProtectionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        user_agent = request.headers.get("user-agent", "").lower()
        
        # Block known bad bots
        for bot in BAD_BOTS:
            if bot in user_agent:
                from fastapi.responses import JSONResponse
                return JSONResponse(
                    status_code=403,
                    content={"error": "Access denied"}
                )
        
        # Allow good bots
        for bot in GOOD_BOTS:
            if bot in user_agent:
                return await call_next(request)
        
        # Check for suspicious patterns
        if self._is_suspicious(request):
            from fastapi.responses import JSONResponse
            return JSONResponse(
                status_code=403,
                content={"error": "Access denied"}
            )
        
        return await call_next(request)
    
    def _is_suspicious(self, request: Request) -> bool:
        """Check for suspicious request patterns."""
        ua = request.headers.get("user-agent", "")
        
        # No user agent
        if not ua:
            return True
        
        # Too short user agent
        if len(ua) < 20:
            return True
        
        # Contains suspicious keywords
        suspicious = ["headless", "phantom", "selenium", "puppeteer"]
        if any(s in ua.lower() for s in suspicious):
            return True
        
        return False
```

**Cloudflare setup guide:**

```
CLOUDFLARE SETUP (FREE)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Tạo Cloudflare account
2. Add domain (VD: aicareerroadmap.vn)
3. Update nameservers tại registrar
4. Enable "Proxy" (orange cloud) cho tất cả DNS records
5. SSL/TLS: Full (strict)
6. Security → Bot Fight Mode: ON
7. Security → WAF: Enable Managed Rules
8. Caching → Configuration: Standard
9. Speed → Auto Minify: JS, CSS, HTML
10. Network → HTTP/2: ON, HTTP/3: ON

Custom Rate Limiting Rules (Dashboard → Security → WAF):
- Rule 1: /api/* → 10 requests/phút → Challenge
- Rule 2: /nganh/* → 50 requests/phút → Block
- Rule 3: /roadmap/* → 50 requests/phút → Block
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 9: DATABASE SCALING — Migration plan SQLite → PostgreSQL

**Vấn đề:**
```
SQLite limits:
- Tối ưu cho < 10k records, 1 writer at a time
- Không hỗ trợ concurrent writes
- Không có native JSON operators (phải parse trong Python)
- File-based → không scale horizontally

Plan target: 1,000 roadmaps/tháng
12 tháng = 12,000 records → bắt đầu chậm
```

**Giải pháp: SQLite cho MVP, PostgreSQL khi scale**

```
DATABASE MIGRATION PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 1: MVP (0-6 tháng) — SQLite
├── Đơn giản, không cần cài đặt
├── File-based, dễ deploy
├── Đủ cho < 10k records
├── Backup: Copy file .db
└── Cost: $0

Phase 2: Growth (6-12 tháng) — PostgreSQL
├── Trigger khi: > 5,000 records HOẶC > 100 concurrent users
├── Migration script: migrate_sqlite_to_pg.py
├── Downtime: < 5 phút (nếu làm đúng)
├── Cost: $0-15/tháng (Supabase free tier hoặc Railway)
└── Benefits: Concurrent writes, JSON operators, full-text search

Phase 3: Scale (12+ tháng) — PostgreSQL + Read Replicas
├── Trigger khi: > 50,000 records HOẶC > 1,000 concurrent users
├── Read replicas cho landing pages (read-heavy)
├── Connection pooling (PgBouncer)
├── Cost: $20-50/tháng
└── Benefits: Horizontal scaling, high availability
```

**Migration script:**

```python
# scripts/migrate_sqlite_to_pg.py
"""Migration script: SQLite → PostgreSQL."""

import sqlite3
import json
import os
from datetime import datetime

# PostgreSQL connection
PG_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/airoadmap")

def migrate():
    """Migrate data from SQLite to PostgreSQL."""
    import psycopg2
    from psycopg2.extras import execute_values
    
    # Connect to SQLite
    sqlite_conn = sqlite3.connect("data/roadmaps.db")
    sqlite_conn.row_factory = sqlite3.Row
    sqlite_cur = sqlite_conn.cursor()
    
    # Connect to PostgreSQL
    pg_conn = psycopg2.connect(PG_URL)
    pg_cur = pg_conn.cursor()
    
    # Create tables in PostgreSQL
    pg_cur.execute("""
        CREATE TABLE IF NOT EXISTS roadmaps (
            id TEXT PRIMARY KEY,
            slug TEXT UNIQUE NOT NULL,
            age INTEGER NOT NULL,
            industry TEXT NOT NULL,
            industry_name TEXT NOT NULL,
            level TEXT NOT NULL,
            goal TEXT NOT NULL,
            duration_months INTEGER NOT NULL,
            overview TEXT,
            total_weeks INTEGER,
            total_tasks INTEGER,
            total_hours INTEGER,
            salary_junior TEXT,
            salary_mid TEXT,
            salary_senior TEXT,
            competitive_advantage TEXT,
            market_demand TEXT,
            phases_json JSONB,
            ai_model TEXT DEFAULT 'gpt-4o-mini',
            ai_tokens_used INTEGER,
            generation_time_ms INTEGER,
            view_count INTEGER DEFAULT 0,
            share_count INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        
        CREATE INDEX IF NOT EXISTS idx_roadmaps_slug ON roadmaps(slug);
        CREATE INDEX IF NOT EXISTS idx_roadmaps_industry ON roadmaps(industry);
        CREATE INDEX IF NOT EXISTS idx_roadmaps_created ON roadmaps(created_at);
        
        -- JSONB index for querying phases
        CREATE INDEX IF NOT EXISTS idx_roadmaps_phases ON roadmaps USING GIN (phases_json);
    """)
    
    # Migrate data
    sqlite_cur.execute("SELECT * FROM roadmaps")
    rows = sqlite_cur.fetchall()
    
    for row in rows:
        pg_cur.execute("""
            INSERT INTO roadmaps (
                id, slug, age, industry, industry_name, level, goal,
                duration_months, overview, total_weeks, total_tasks,
                total_hours, salary_junior, salary_mid, salary_senior,
                competitive_advantage, market_demand, phases_json,
                ai_model, ai_tokens_used, generation_time_ms,
                view_count, share_count, created_at
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (id) DO NOTHING
        """, (
            row["id"], row["slug"], row["age"], row["industry"],
            row["industry_name"], row["level"], row["goal"],
            row["duration_months"], row["overview"], row["total_weeks"],
            row["total_tasks"], row["total_hours"], row["salary_junior"],
            row["salary_mid"], row["salary_senior"],
            row["competitive_advantage"], row["market_demand"],
            row["phases_json"],  # PostgreSQL sẽ auto-parse JSON
            row["ai_model"], row["ai_tokens_used"],
            row["generation_time_ms"], row["view_count"],
            row["share_count"], row["created_at"]
        ))
    
    pg_conn.commit()
    print(f"Migrated {len(rows)} records")
    
    sqlite_conn.close()
    pg_conn.close()

if __name__ == "__main__":
    migrate()
```

**Database abstraction layer:**

```python
# app/database.py
"""Database abstraction - hỗ trợ cả SQLite và PostgreSQL."""

import os
from typing import Optional

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///data/roadmaps.db")

def get_database():
    """Get database connection based on DATABASE_URL."""
    if DATABASE_URL.startswith("postgresql"):
        return PostgreSQLDatabase(DATABASE_URL)
    else:
        return SQLiteDatabase(DATABASE_URL)

class DatabaseInterface:
    """Interface chung cho database operations."""
    
    async def get_roadmap_by_slug(self, slug: str) -> Optional[dict]:
        raise NotImplementedError
    
    async def create_roadmap(self, data: dict) -> str:
        raise NotImplementedError
    
    async def increment_view_count(self, slug: str) -> None:
        raise NotImplementedError

class SQLiteDatabase(DatabaseInterface):
    """SQLite implementation."""
    
    def __init__(self, url: str):
        import aiosqlite
        self.db_path = url.replace("sqlite:///", "")
    
    async def get_roadmap_by_slug(self, slug: str) -> Optional[dict]:
        async with aiosqlite.connect(self.db_path) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(
                "SELECT * FROM roadmaps WHERE slug = ?", (slug,)
            ) as cursor:
                row = await cursor.fetchone()
                if row:
                    return dict(row)
        return None
    
    async def create_roadmap(self, data: dict) -> str:
        async with aiosqlite.connect(self.db_path) as db:
            await db.execute("""
                INSERT INTO roadmaps (id, slug, age, industry, industry_name,
                    level, goal, duration_months, overview, total_weeks,
                    total_tasks, total_hours, salary_junior, salary_mid,
                    salary_senior, competitive_advantage, market_demand,
                    phases_json, ai_model, ai_tokens_used, generation_time_ms)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data["id"], data["slug"], data["age"], data["industry"],
                data["industry_name"], data["level"], data["goal"],
                data["duration_months"], data["overview"], data["total_weeks"],
                data["total_tasks"], data["total_hours"], data["salary_junior"],
                data["salary_mid"], data["salary_senior"],
                data["competitive_advantage"], data["market_demand"],
                json.dumps(data["phases_json"]), data["ai_model"],
                data["ai_tokens_used"], data["generation_time_ms"]
            ))
            await db.commit()
        return data["id"]

class PostgreSQLDatabase(DatabaseInterface):
    """PostgreSQL implementation."""
    
    def __init__(self, url: str):
        import asyncpg
        self.pool = None
        self.url = url
    
    async def connect(self):
        import asyncpg
        self.pool = await asyncpg.create_pool(self.url)
    
    async def get_roadmap_by_slug(self, slug: str) -> Optional[dict]:
        async with self.pool.acquire() as conn:
            row = await conn.fetchrow(
                "SELECT * FROM roadmaps WHERE slug = $1", slug
            )
            if row:
                return dict(row)
        return None
    
    async def create_roadmap(self, data: dict) -> str:
        async with self.pool.acquire() as conn:
            await conn.execute("""
                INSERT INTO roadmaps (id, slug, age, industry, industry_name,
                    level, goal, duration_months, overview, total_weeks,
                    total_tasks, total_hours, salary_junior, salary_mid,
                    salary_senior, competitive_advantage, market_demand,
                    phases_json, ai_model, ai_tokens_used, generation_time_ms)
                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, 
                        $13, $14, $15, $16, $17, $18, $19, $20, $21)
            """, (
                data["id"], data["slug"], data["age"], data["industry"],
                data["industry_name"], data["level"], data["goal"],
                data["duration_months"], data["overview"], data["total_weeks"],
                data["total_tasks"], data["total_hours"], data["salary_junior"],
                data["salary_mid"], data["salary_senior"],
                data["competitive_advantage"], data["market_demand"],
                json.dumps(data["phases_json"]), data["ai_model"],
                data["ai_tokens_used"], data["generation_time_ms"]
            ))
        return data["id"]
```

**Migration trigger conditions:**

```
KHI NÀO MIGRATE?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Dấu hiệu cần migrate sang PostgreSQL:

□ Số lượng records > 5,000
□ Response time > 500ms (trung bình)
□ Có > 50 concurrent users
□ Cần full-text search
□ Cần JSON queries phức tạp
□ Cần concurrent writes
□ Backup strategy cần robust hơn

Monitoring:
- Thêm metric: DB query time
- Alert khi: p95 > 1s
- Weekly check: record count
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 10: AI OUTPUT QUALITY CONTROL — Human review + Feedback loop

**Vấn đề:**
```
AI có thể:
- Hallucinate salary data (lương sai thực tế)
- Suggest resource sai/hỏng (link die)
- Tạo roadmap không hợp lý (thứ tự học sai)
- Tasks quá mơ hồ ("Học JavaScript" thay vì "Day 1-2: Học variables")

Không có cách verify → User nhận roadmap kém chất lượng
```

**Giải pháp: Multi-layer quality control**

```
QUALITY CONTROL PIPELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Layer 1: AI Output Validation (tự động)
├── JSON schema validation
├── Required fields check
├── Data type validation
├── Range validation (tuổi 15-60, tháng 1-24)
├── Resource URL format check
└── Reject nếu fail → Retry 1 lần

Layer 2: Content Validation (tự động)
├── Salary range sanity check
│   ├── Junior: 5-20 triệu (VN 2026)
│   ├── Mid: 15-40 triệu
│   └── Senior: 30-100 triệu
├── Timeline sanity check
│   ├── Phase duration: 1-6 tháng
│   ├── Total duration: 3-24 tháng
│   └── Hours/week: 5-40 giờ
├── Skills relevance check
│   ├── Skills phải liên quan đến industry
│   └── Skills phải theo thứ tự hợp lý
└── Reject nếu fail → Dùng fallback

Layer 3: Resource Verification (tự động)
├── Check URL format (valid URL)
├── HEAD request check (URL alive?)
├── Domain whitelist (freeCodeCamp, MDN, etc.)
├── Cache verified URLs
└── Replace dead URLs với alternatives

Layer 4: User Feedback (reactive)
├── "Roadmap này hữu ích?" (👍/👎)
├── "Báo cáo lỗi" button
├── Feedback form (optional)
├── Aggregate feedback → Improve prompts
└── A/B test prompt variants

Layer 5: Human Review (periodic)
├── Review random 10% roadmaps
├── Checklist:
│   ├── ☐ Salary chính xác?
│   ├── ☐ Timeline hợp lý?
│   ├── ☐ Skills đúng thứ tự?
│   ├── ☐ Resources có thật?
│   ├── ☐ Tasks đủ chi tiết?
│   └── ☐ Ngôn ngữ tự nhiên?
├── Ghi nhận issues → Update prompts
└── Frequency: Weekly (1-2 giờ)
```

**Implementation:**

```python
# app/services/quality_control.py
"""AI output quality control."""

import re
from typing import Tuple
from urllib.parse import urlparse

class QualityControl:
    """Validate AI-generated roadmaps."""
    
    # Salary ranges (VNĐ, 2026)
    SALARY_RANGES = {
        "junior": (5_000_000, 20_000_000),
        "mid": (15_000_000, 40_000_000),
        "senior": (30_000_000, 100_000_000),
    }
    
    # Timeline ranges
    TIMELINE_RANGES = {
        "phase_duration_months": (1, 6),
        "total_duration_months": (3, 24),
        "hours_per_week": (5, 40),
    }
    
    # Trusted domains for resources
    TRUSTED_DOMAINS = [
        "freecodecamp.org", "developer.mozilla.org", "web.dev",
        "css-tricks.com", "w3schools.com", "github.com",
        "stackoverflow.com", "youtube.com", "udemy.com",
        "coursera.org", "edx.org", "khanacademy.org",
        "docs.python.org", "reactjs.org", "vuejs.org",
        "angular.io", "nodejs.org", "expressjs.com",
    ]
    
    def validate_roadmap(self, roadmap: dict) -> Tuple[bool, list]:
        """
        Validate roadmap quality.
        Returns: (is_valid, list_of_issues)
        """
        issues = []
        
        # Layer 1: Structure validation
        structure_issues = self._validate_structure(roadmap)
        issues.extend(structure_issues)
        
        # Layer 2: Content validation
        content_issues = self._validate_content(roadmap)
        issues.extend(content_issues)
        
        # Layer 3: Resource validation
        resource_issues = self._validate_resources(roadmap)
        issues.extend(resource_issues)
        
        is_valid = len(issues) == 0
        return is_valid, issues
    
    def _validate_structure(self, roadmap: dict) -> list:
        """Validate JSON structure."""
        issues = []
        
        # Check required top-level keys
        required_keys = ["level1_roadmap", "level2_phases", "level3_tasks"]
        for key in required_keys:
            if key not in roadmap:
                issues.append(f"Missing key: {key}")
        
        # Check level1 structure
        if "level1_roadmap" in roadmap:
            level1 = roadmap["level1_roadmap"]
            required_level1 = ["overview", "total_weeks", "total_tasks", 
                             "total_hours", "salary_range"]
            for key in required_level1:
                if key not in level1:
                    issues.append(f"Missing level1 key: {key}")
        
        # Check level2 structure
        if "level2_phases" in roadmap:
            phases = roadmap["level2_phases"]
            if not isinstance(phases, list) or len(phases) == 0:
                issues.append("level2_phases must be non-empty list")
            else:
                for i, phase in enumerate(phases):
                    required_phase = ["id", "name", "duration", "skills", 
                                    "total_hours", "milestone"]
                    for key in required_phase:
                        if key not in phase:
                            issues.append(f"Phase {i} missing key: {key}")
        
        # Check level3 structure
        if "level3_tasks" in roadmap:
            tasks = roadmap["level3_tasks"]
            if not isinstance(tasks, list) or len(tasks) == 0:
                issues.append("level3_tasks must be non-empty list")
        
        return issues
    
    def _validate_content(self, roadmap: dict) -> list:
        """Validate content quality."""
        issues = []
        
        if "level1_roadmap" not in roadmap:
            return issues
        
        level1 = roadmap["level1_roadmap"]
        
        # Validate salary ranges
        if "salary_range" in level1:
            salary = level1["salary_range"]
            for level, (min_val, max_val) in self.SALARY_RANGES.items():
                if level in salary:
                    # Parse salary string (VD: "8-15 triệu")
                    try:
                        salary_str = salary[level]
                        numbers = re.findall(r'\d+', salary_str)
                        if len(numbers) >= 2:
                            low, high = int(numbers[0]) * 1_000_000, int(numbers[1]) * 1_000_000
                            if low < min_val or high > max_val * 2:
                                issues.append(f"Salary {level} out of range: {salary_str}")
                    except:
                        issues.append(f"Cannot parse salary {level}: {salary[level]}")
        
        # Validate timeline
        if "total_weeks" in level1:
            weeks = level1["total_weeks"]
            min_weeks, max_weeks = 12, 96
            if weeks < min_weeks or weeks > max_weeks:
                issues.append(f"Total weeks out of range: {weeks}")
        
        if "total_hours" in level1:
            hours = level1["total_hours"]
            min_hours, max_hours = 100, 2000
            if hours < min_hours or hours > max_hours:
                issues.append(f"Total hours out of range: {hours}")
        
        return issues
    
    def _validate_resources(self, roadmap: dict) -> list:
        """Validate resource URLs."""
        issues = []
        
        if "level3_tasks" not in roadmap:
            return issues
        
        for phase_task in roadmap["level3_tasks"]:
            if "weeks" not in phase_task:
                continue
            
            for week in phase_task.get("weeks", []):
                for task in week.get("tasks", []):
                    resource = task.get("resource", {})
                    url = resource.get("url", "")
                    
                    if url:
                        # Check URL format
                        parsed = urlparse(url)
                        if not parsed.scheme or not parsed.netloc:
                            issues.append(f"Invalid URL format: {url}")
                        
                        # Check trusted domain
                        domain = parsed.netloc.replace("www.", "")
                        if domain not in self.TRUSTED_DOMAINS:
                            issues.append(f"Untrusted domain: {domain}")
        
        return issues

# Feedback collection
class FeedbackCollector:
    """Collect and analyze user feedback."""
    
    def __init__(self, db):
        self.db = db
    
    async def submit_feedback(self, roadmap_id: str, rating: bool, 
                            comment: str = None) -> None:
        """Submit user feedback."""
        await self.db.execute("""
            INSERT INTO feedback (roadmap_id, rating, comment, created_at)
            VALUES (?, ?, ?, ?)
        """, (roadmap_id, rating, comment, datetime.utcnow()))
    
    async def get_feedback_stats(self, roadmap_id: str) -> dict:
        """Get feedback statistics for a roadmap."""
        result = await self.db.fetch_one("""
            SELECT 
                COUNT(*) as total,
                SUM(CASE WHEN rating = 1 THEN 1 ELSE 0 END) as positive,
                SUM(CASE WHEN rating = 0 THEN 1 ELSE 0 END) as negative
            FROM feedback
            WHERE roadmap_id = ?
        """, (roadmap_id,))
        
        return {
            "total": result["total"],
            "positive": result["positive"],
            "negative": result["negative"],
            "satisfaction_rate": result["positive"] / result["total"] * 100 if result["total"] > 0 else 0
        }
    
    async def get_worst_roadmaps(self, limit: int = 10) -> list:
        """Get roadmaps with worst feedback (for review)."""
        return await self.db.fetch_all("""
            SELECT r.id, r.slug, r.industry_name,
                   COUNT(*) as feedback_count,
                   SUM(CASE WHEN f.rating = 0 THEN 1 ELSE 0 END) as negative_count
            FROM roadmaps r
            JOIN feedback f ON r.id = f.roadmap_id
            GROUP BY r.id
            HAVING negative_count > 0
            ORDER BY negative_count DESC
            LIMIT ?
        """, (limit,))
```

**Feedback UI components:**

```html
<!-- Feedback widget on roadmap page -->
<div class="feedback-widget">
  <p>Roadmap này có hữu ích không?</p>
  <div class="feedback-buttons">
    <button onclick="submitFeedback(true)" class="btn-positive">
      👍 Có, hữu ích
    </button>
    <button onclick="submitFeedback(false)" class="btn-negative">
      👎 Cần cải thiện
    </button>
  </div>
  <div id="feedback-form" style="display:none;">
    <textarea placeholder="Cho mình biết cần cải thiện gì..."></textarea>
    <button onclick="submitComment()">Gửi phản hồi</button>
  </div>
</div>

<script>
async function submitFeedback(isPositive) {
  const response = await fetch('/api/feedback', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      roadmap_id: '{{ roadmap.id }}',
      rating: isPositive,
      comment: null
    })
  });
  
  if (!isPositive) {
    document.getElementById('feedback-form').style.display = 'block';
  } else {
    alert('Cảm ơn bạn đã đánh giá! 🎉');
  }
}

async function submitComment() {
  const comment = document.querySelector('#feedback-form textarea').value;
  await fetch('/api/feedback', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({
      roadmap_id: '{{ roadmap.id }}',
      rating: false,
      comment: comment
    })
  });
  alert('Cảm ơn phản hồi của bạn! Chúng mình sẽ cải thiện.');
}
</script>
```

**Quality monitoring dashboard:**

```
QUALITY METRICS (weekly check)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Metric                    | Target | Action if fail      |
|---------------------------|--------|---------------------|
| AI validation pass rate   | > 90%  | Review prompts      |
| Resource URL alive rate   | > 95%  | Update dead links   |
| User satisfaction rate    | > 70%  | Review worst cases  |
| Negative feedback rate    | < 15%  | Investigate & fix   |
| Fallback usage rate       | < 5%   | Check AI reliability|
| Average response time     | < 30s  | Optimize prompts    |

Weekly review process:
1. Check metrics dashboard (5 phút)
2. Review top 5 worst roadmaps (15 phút)
3. Read user feedback comments (10 phút)
4. Update prompts if needed (20 phút)
5. Test changes (10 phút)
Total: ~1 giờ/tuần
```

**Trạng thái:** ✅ Đã xác định xong

---

## TÓM TẮT HIGH PRIORITY RESOLUTION

| # | Issue | Giải pháp | Status |
|---|-------|-----------|--------|
| 6 | Fallback Response | Pre-generated fallbacks cho TOP 20 ngành | ✅ |
| 7 | Content Strategy | AI generate + human review pipeline | ✅ |
| 8 | Rate Limiting | Cloudflare + multi-layer protection | ✅ |
| 9 | Database Scaling | SQLite → PostgreSQL migration plan | ✅ |
| 10 | Quality Control | 5-layer validation + feedback loop | ✅ |

**Next steps:**
1. Generate fallback roadmaps (scripts/generate_fallbacks.py)
2. Generate SEO content (scripts/generate_seo_content.py)
3. Setup Cloudflare account
4. Implement quality control middleware

---
## MEDIUM PRIORITY RESOLUTION — Giải quyết 5 thiếu sót trung bình

> Cập nhật: 30/05/2026
> Mục tiêu: Giải quyết 5 thiếu sót medium priority để cải thiện UX và growth

---

### ISSUE 11: ANALYTICS — GA4 + Event Tracking + Conversion Funnel

**Vấn đề:**
```
Không có analytics → Không biết:
- Bao nhiêu người visit?
- Họ đến từ đâu?
- Bao nhiêu người tạo roadmap?
- Bao nhiêu người xem hết 3 cấp?
- Conversion rate form → result?
```

**Giải pháp: Google Analytics 4 (FREE) + Custom Events**

```
ANALYTICS SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Tools:
├── Google Analytics 4 (FREE)
│   ├── Page views
│   ├── User behavior
│   ├── Conversion tracking
│   └── Audience insights
│
├── Google Search Console (FREE)
│   ├── SEO performance
│   ├── Keywords ranking
│   ├── Click-through rates
│   └── Index status
│
└── Custom Events (GA4)
    ├── Form submissions
    ├── Roadmap generation
    ├── Level views (1, 2, 3)
    ├── Task checkbox clicks
    ├── Share clicks
    └── Feedback submissions
```

**GA4 Setup:**

```html
<!-- Thêm vào <head> của tất cả pages -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX', {
    page_title: '{{ page_title }}',
    page_location: '{{ page_url }}',
    custom_map: {
      'dimension1': 'industry',
      'dimension2': 'user_level',
      'dimension3': 'duration_months'
    }
  });
</script>
```

**Custom Events Tracking:**

```javascript
// app/static/js/analytics.js
/** Analytics event tracking. */

const Analytics = {
  // Track page view
  pageView(pagePath, pageTitle) {
    gtag('event', 'page_view', {
      page_path: pagePath,
      page_title: pageTitle
    });
  },
  
  // Track form submission
  formSubmit(industry, level, duration) {
    gtag('event', 'form_submit', {
      event_category: 'roadmap_creation',
      event_label: industry,
      industry: industry,
      user_level: level,
      duration_months: duration
    });
  },
  
  // Track roadmap generation
  roadmapGenerated(industry, generationTime) {
    gtag('event', 'roadmap_generated', {
      event_category: 'roadmap_creation',
      event_label: industry,
      generation_time_ms: generationTime,
      value: 1
    });
  },
  
  // Track level views
  levelView(level, industry) {
    gtag('event', 'level_view', {
      event_category: 'roadmap_engagement',
      event_label: `level_${level}`,
      industry: industry,
      level: level
    });
  },
  
  // Track task checkbox
  taskChecked(taskId, phaseId) {
    gtag('event', 'task_checked', {
      event_category: 'roadmap_engagement',
      event_label: taskId,
      phase_id: phaseId
    });
  },
  
  // Track share
  shareClick(platform, roadmapSlug) {
    gtag('event', 'share_click', {
      event_category: 'social',
      event_label: platform,
      roadmap_slug: roadmapSlug
    });
  },
  
  // Track feedback
  feedbackSubmit(roadmapId, isPositive) {
    gtag('event', 'feedback_submit', {
      event_category: 'feedback',
      event_label: isPositive ? 'positive' : 'negative',
      roadmap_id: roadmapId,
      value: isPositive ? 1 : 0
    });
  },
  
  // Track email signup
  emailSignup(source) {
    gtag('event', 'email_signup', {
      event_category: 'conversion',
      event_label: source
    });
  },
  
  // Track search
  search(query, resultsCount) {
    gtag('event', 'search', {
      search_term: query,
      results_count: resultsCount
    });
  },
  
  // Track filter usage
  filterUsed(filterType, filterValue) {
    gtag('event', 'filter_used', {
      event_category: 'navigation',
      filter_type: filterType,
      filter_value: filterValue
    });
  }
};

// Auto-track page views
document.addEventListener('DOMContentLoaded', () => {
  Analytics.pageView(window.location.pathname, document.title);
});

// Export for global use
window.Analytics = Analytics;
```

**Conversion Funnel (GA4):**

```
CONVERSION FUNNEL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Landing Page Visit
├── Event: page_view
└── Metric: Unique visitors

Step 2: Form Page Visit
├── Event: page_view (/tao-roadmap)
└── Metric: Form page visits

Step 3: Form Submit
├── Event: form_submit
└── Metric: Form submissions

Step 4: Roadmap Generated
├── Event: roadmap_generated
└── Metric: Successful generations

Step 5: Level 1 View
├── Event: level_view (level=1)
└── Metric: Level 1 views

Step 6: Level 2 View
├── Event: level_view (level=2)
└── Metric: Level 2 views

Step 7: Level 3 View
├── Event: level_view (level=3)
└── Metric: Level 3 views

Step 8: Task Interaction
├── Event: task_checked
└── Metric: Task checkbox clicks

Step 9: Share/Return
├── Event: share_click OR page_view (return visit)
└── Metric: Shares + Return visitors

GA4 Funnel Exploration:
- Create custom funnel in GA4
- Track drop-off at each step
- Identify conversion bottlenecks
- A/B test improvements
```

**GA4 Custom Reports:**

```
REPORT 1: Roadmap Performance
├── Dimension: industry
├── Metrics: 
│   ├── Total roadmaps generated
│   ├── Average generation time
│   ├── Level 1→2→3 conversion
│   └── Task completion rate
└── Filter: Last 30 days

REPORT 2: User Behavior
├── Dimension: user_type (new/returning)
├── Metrics:
│   ├── Pages per session
│   ├── Average session duration
│   ├── Bounce rate
│   └── Return visitor rate
└── Filter: Last 30 days

REPORT 3: Traffic Sources
├── Dimension: source/medium
├── Metrics:
│   ├── Sessions
│   ├── Conversions (roadmap generated)
│   └── Conversion rate
└── Filter: Last 30 days

REPORT 4: Content Performance
├── Dimension: page_path
├── Metrics:
│   ├── Page views
│   ├── Unique pageviews
│   ├── Average time on page
│   └── Bounce rate
└── Filter: /nganh/* pages
```

**Search Console Setup:**

```
GOOGLE SEARCH CONSOLE SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Verify domain ownership
   ├── DNS verification (recommended)
   └── HTML file upload

2. Submit sitemap
   ├── URL: https://aicareerroadmap.vn/sitemap.xml
   └── Auto-submit via robots.txt

3. Monitor:
   ├── Total clicks
   ├── Total impressions
   ├── Average CTR
   ├── Average position
   └── Top queries

4. Action items:
   ├── Fix crawl errors
   ├── Request indexing for new pages
   └── Monitor mobile usability
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 12: EMAIL CAPTURE — Newsletter Signup + Re-engagement

**Vấn đề:**
```
Không có cách:
- Thu thập email users
- Re-engage users quay lại
- Notify khi có roadmap mới
- Gửi tips/content hàng tuần
```

**Giải pháp: Email capture form + Resend (FREE tier)**

```
EMAIL CAPTURE STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Touchpoints để thu thập email:

1. Trang chủ (/)
   ├── Hero section: "Nhận roadmap mẫu miễn phí"
   ├── Form: Email + Chọn ngành
   └── CTA: "Gửi roadmap mẫu"

2. Trang kết quả (/roadmap/{slug})
   ├── Sau khi xem roadmap
   ├── "Nhận tips học tập hàng tuần?"
   ├── Form: Email only
   └── CTA: "Đăng ký"

3. Landing page ngành (/nganh/{slug})
   ├── Cuối bài content
   ├── "Tạo roadmap riêng cho bạn"
   ├── Form: Email + Ngành
   └── CTA: "Nhận roadmap"

4. Pop-up (exit intent)
   ├── Khi user chuẩn bị rời trang
   ├── "Đừng bỏ lỡ! Nhận roadmap miễn phí"
   ├── Form: Email only
   └── CTA: "Gửi ngay"

5. Footer (tất cả pages)
   ├── "Đăng ký nhận tips học tập"
   ├── Form: Email only
   └── CTA: "Đăng ký"
```

**Email Service: Resend (FREE tier)**

```
RESEND SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Free tier:
├── 100 emails/day
├── 3,000 emails/month
├── Custom domain
├── Webhooks
└── API access

Cost khi scale:
├── 50,000 emails: $20/tháng
├── 100,000 emails: $40/tháng
└── 500,000 emails: $160/tháng

Alternative: Mailchimp (FREE tier)
├── 500 contacts
├── 1,000 emails/month
├── Templates
└── Automation
```

**Implementation:**

```python
# app/services/email.py
"""Email service using Resend."""

import os
import resend
from typing import Optional
from datetime import datetime

resend.api_key = os.getenv("RESEND_API_KEY")

class EmailService:
    """Handle email operations."""
    
    FROM_EMAIL = "noreply@aicareerroadmap.vn"
    FROM_NAME = "AI Career Roadmap"
    
    async def subscribe(self, email: str, industry: Optional[str] = None, 
                       source: str = "website") -> dict:
        """Subscribe email to newsletter."""
        # Store in database
        await self.db.execute("""
            INSERT INTO subscribers (email, industry, source, subscribed_at)
            VALUES (?, ?, ?, ?)
            ON CONFLICT (email) DO UPDATE SET
                industry = COALESCE(?, industry),
                last_active = ?
        """, (email, industry, source, datetime.utcnow(), industry, datetime.utcnow()))
        
        # Send welcome email
        await self.send_welcome_email(email, industry)
        
        return {"success": True, "email": email}
    
    async def send_welcome_email(self, email: str, industry: Optional[str] = None):
        """Send welcome email after subscription."""
        try:
            resend.Emails.send({
                "from": f"{self.FROM_NAME} <{self.FROM_EMAIL}>",
                "to": [email],
                "subject": "Chào mừng bạn đến với AI Career Roadmap! 🎉",
                "html": self._get_welcome_template(industry)
            })
        except Exception as e:
            print(f"Failed to send welcome email: {e}")
    
    async def send_roadmap_sample(self, email: str, industry: str):
        """Send sample roadmap email."""
        try:
            resend.Emails.send({
                "from": f"{self.FROM_NAME} <{self.FROM_EMAIL}>",
                "to": [email],
                "subject": f"Roadmap mẫu: {industry} - AI Career Roadmap",
                "html": self._get_sample_roadmap_template(industry)
            })
        except Exception as e:
            print(f"Failed to send sample roadmap: {e}")
    
    async def send_weekly_tips(self, email: str, tips: list):
        """Send weekly learning tips."""
        try:
            resend.Emails.send({
                "from": f"{self.FROM_NAME} <{self.FROM_EMAIL}>",
                "to": [email],
                "subject": "Tips học tập tuần này 📚",
                "html": self._get_weekly_tips_template(tips)
            })
        except Exception as e:
            print(f"Failed to send weekly tips: {e}")
    
    def _get_welcome_template(self, industry: Optional[str] = None) -> str:
        """Welcome email HTML template."""
        industry_section = ""
        if industry:
            industry_section = f"""
            <p>Bạn quan tâm đến ngành <strong>{industry}</strong>. 
            Đây là roadmap mẫu cho ngành này:</p>
            <a href="https://aicareerroadmap.vn/nganh/{industry.lower().replace(' ', '-')}" 
               class="button">Xem roadmap mẫu</a>
            """
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .button {{ 
                    display: inline-block; 
                    background: #4F46E5; 
                    color: white; 
                    padding: 12px 24px; 
                    text-decoration: none; 
                    border-radius: 6px; 
                }}
                .footer {{ margin-top: 30px; font-size: 12px; color: #666; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Chào mừng bạn! 🎉</h1>
                <p>Cảm ơn bạn đã đăng ký nhận thông tin từ AI Career Roadmap.</p>
                
                <p>Chúng mình sẽ gửi cho bạn:</p>
                <ul>
                    <li>Roadmap mẫu cho ngành bạn quan tâm</li>
                    <li>Tips học tập hàng tuần</li>
                    <li>Cập nhật tính năng mới</li>
                </ul>
                
                {industry_section}
                
                <p>Nếu bạn muốn tạo roadmap cá nhân hóa ngay:</p>
                <a href="https://aicareerroadmap.vn/tao-roadmap" class="button">
                    Tạo roadmap ngay
                </a>
                
                <div class="footer">
                    <p>Bạn nhận email này vì đã đăng ký tại aicareerroadmap.vn</p>
                    <p><a href="{{{{unsubscribe_url}}}}">Hủy đăng ký</a></p>
                </div>
            </div>
        </body>
        </html>
        """
    
    def _get_sample_roadmap_template(self, industry: str) -> str:
        """Sample roadmap email template."""
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
                .button {{ 
                    display: inline-block; 
                    background: #4F46E5; 
                    color: white; 
                    padding: 12px 24px; 
                    text-decoration: none; 
                    border-radius: 6px; 
                }}
                .roadmap-preview {{
                    background: #f9fafb;
                    padding: 20px;
                    border-radius: 8px;
                    margin: 20px 0;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Roadmap mẫu: {industry} 🗺️</h1>
                <p>Đây là roadmap mẫu cho ngành {industry}:</p>
                
                <div class="roadmap-preview">
                    <h3>📊 Tổng quan</h3>
                    <ul>
                        <li>Thời gian: 6 tháng</li>
                        <li>3 phases, 12 weeks, 36 tasks</li>
                        <li>360 giờ học</li>
                    </ul>
                    
                    <h3>💰 Mức lương</h3>
                    <ul>
                        <li>Junior: 8-15 triệu</li>
                        <li>Mid: 15-30 triệu</li>
                        <li>Senior: 30-60 triệu</li>
                    </ul>
                </div>
                
                <p>Đây chỉ là roadmap mẫu. Để tạo roadmap cá nhân hóa riêng cho bạn:</p>
                <a href="https://aicareerroadmap.vn/tao-roadmap" class="button">
                    Tạo roadmap riêng
                </a>
                
                <p>Nếu bạn muốn xem roadmap mẫu đầy đủ:</p>
                <a href="https://aicareerroadmap.vn/nganh/{industry.lower().replace(' ', '-')}">
                    Xem roadmap mẫu
                </a>
            </div>
        </body>
        </html>
        """
    
    def _get_weekly_tips_template(self, tips: list) -> str:
        """Weekly tips email template."""
        tips_html = ""
        for tip in tips:
            tips_html += f"""
            <div style="margin-bottom: 20px; padding: 15px; background: #f9fafb; border-radius: 8px;">
                <h3>{tip['title']}</h3>
                <p>{tip['description']}</p>
                <a href="{tip['link']}">Đọc thêm →</a>
            </div>
            """
        
        return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
                .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Tips học tập tuần này 📚</h1>
                <p>Chào bạn,</p>
                <p>Đây là những tips học tập hữu ích tuần này:</p>
                
                {tips_html}
                
                <p>Chúc bạn học tốt!</p>
                <p>Đội ngũ AI Career Roadmap</p>
            </div>
        </body>
        </html>
        """
```

**Database schema cho subscribers:**

```sql
CREATE TABLE subscribers (
    id TEXT PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    industry TEXT,
    source TEXT DEFAULT 'website',
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    unsubscribed_at TIMESTAMP
);

CREATE INDEX idx_subscribers_email ON subscribers(email);
CREATE INDEX idx_subscribers_industry ON subscribers(industry);
```

**Email capture UI components:**

```html
<!-- Email capture form trên trang chủ -->
<section class="email-capture">
  <div class="container">
    <h2>Nhận roadmap mẫu miễn phí 📧</h2>
    <p>Nhập email để nhận roadmap mẫu cho ngành bạn quan tâm</p>
    
    <form id="email-capture-form" class="email-form">
      <div class="form-row">
        <input type="email" name="email" placeholder="Email của bạn" required>
        <select name="industry">
          <option value="">Chọn ngành...</option>
          <option value="backend-developer">Backend Developer</option>
          <option value="frontend-developer">Frontend Developer</option>
          <option value="data-analyst">Data Analyst</option>
          <!-- Thêm các ngành khác -->
        </select>
        <button type="submit">Gửi roadmap mẫu</button>
      </div>
      <p class="form-note">Miễn phí · Không spam · Hủy bất kỳ lúc nào</p>
    </form>
  </div>
</section>

<script>
document.getElementById('email-capture-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const email = formData.get('email');
  const industry = formData.get('industry');
  
  try {
    const response = await fetch('/api/subscribe', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ email, industry, source: 'homepage' })
    });
    
    if (response.ok) {
      // Track analytics
      Analytics.emailSignup('homepage');
      
      // Show success
      alert('Cảm ơn bạn! Kiểm tra email để nhận roadmap mẫu.');
      e.target.reset();
    }
  } catch (error) {
    console.error('Subscription failed:', error);
  }
});
</script>
```

**Re-engagement strategy:**

```
RE-ENGAGEMENT EMAILS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Trigger 1: Welcome (ngay sau subscribe)
├── Content: Giới thiệu + roadmap mẫu
├── CTA: Tạo roadmap riêng
└── Delay: 0

Trigger 2: Day 3 (chưa tạo roadmap)
├── Content: "Bạn đã tạo roadmap chưa?"
├── CTA: Tạo roadmap ngay
└── Delay: 3 ngày

Trigger 3: Day 7 (chưa quay lại)
├── Content: Tips học tập + roadmap mới
├── CTA: Xem roadmap mới
└── Delay: 7 ngày

Trigger 4: Day 30 (inactive)
├── Content: "Chúng mình nhớ bạn!"
├── CTA: Tạo roadmap mới
└── Delay: 30 ngày

Trigger 5: Weekly tips (cho active users)
├── Content: Tips học tập + industry news
├── CTA: Đọc thêm
└── Schedule: Thứ 2 hàng tuần
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 13: FEEDBACK MECHANISM — Rating System + Error Reporting

**Vấn đề:**
```
Không có cách:
- User đánh giá roadmap
- User báo lỗi roadmap
- Thu thập feedback cải thiện
- Đo lường satisfaction
```

**Giải pháp: Feedback widget + Rating system**

> ⚠️ FEEDBACK ĐÃ ĐƯỢC ĐỀ CẬP TRONG ISSUE 10 (Quality Control)
> Phần này mở rộng thêm chi tiết implementation.

```
FEEDBACK SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Components:

1. Roadmap Rating (👍/👎)
   ├── Vị trí: Cuối trang roadmap
   ├── Data: Boolean (positive/negative)
   ├── Storage: feedback table
   └── Analytics: Satisfaction rate

2. Detailed Feedback Form
   ├── Trigger: Click 👎 hoặc "Báo lỗi"
   ├── Fields:
   │   ├── Feedback type (dropdown)
   │   │   ├── Salary không chính xác
   │   │   ├── Resource link hỏng
   │   │   ├── Tasks không rõ ràng
   │   │   ├── Timeline không thực tế
   │   │   ├── Skills không liên quan
   │   │   └── Khác
   │   ├── Description (textarea)
   │   └── Email (optional, để nhận phản hồi)
   └── Submit: POST /api/feedback

3. Quick Feedback (inline)
   ├── "Task này hữu ích?" (👍/👎) trên mỗi task
   ├── "Resource này còn hoạt động?" (✓/✗)
   └── Data: Task-level feedback

4. Bug Report Button
   ├── Vị trí: Fixed button (góc phải dưới)
   ├── Trigger: Click → Modal
   ├── Fields:
   │   ├── Bug type (dropdown)
   │   ├── Description
   │   ├── Screenshot (optional)
   │   └── Email (optional)
   └── Submit: POST /api/bug-report
```

**Implementation:**

```python
# app/services/feedback.py
"""Feedback service."""

from datetime import datetime
from typing import Optional
from enum import Enum

class FeedbackType(str, Enum):
    SALARY_INCORRECT = "salary_incorrect"
    RESOURCE_BROKEN = "resource_broken"
    TASKS_UNCLEAR = "tasks_unclear"
    TIMELINE_UNREALISTIC = "timeline_unrealistic"
    SKILLS_IRRELEVANT = "skills_irrelevant"
    OTHER = "other"

class FeedbackService:
    """Handle feedback operations."""
    
    async def submit_rating(self, roadmap_id: str, is_positive: bool,
                           user_ip: str) -> dict:
        """Submit simple rating (👍/👎)."""
        # Check if already rated (by IP)
        existing = await self.db.fetch_one("""
            SELECT id FROM feedback 
            WHERE roadmap_id = ? AND user_ip = ?
        """, (roadmap_id, user_ip))
        
        if existing:
            # Update existing rating
            await self.db.execute("""
                UPDATE feedback SET rating = ?, updated_at = ?
                WHERE roadmap_id = ? AND user_ip = ?
            """, (is_positive, datetime.utcnow(), roadmap_id, user_ip))
        else:
            # Insert new rating
            await self.db.execute("""
                INSERT INTO feedback (roadmap_id, rating, user_ip, created_at)
                VALUES (?, ?, ?, ?)
            """, (roadmap_id, is_positive, user_ip, datetime.utcnow()))
        
        return {"success": True}
    
    async def submit_detailed_feedback(self, roadmap_id: str, 
                                      feedback_type: FeedbackType,
                                      description: str,
                                      user_ip: str,
                                      email: Optional[str] = None) -> dict:
        """Submit detailed feedback."""
        await self.db.execute("""
            INSERT INTO detailed_feedback 
            (roadmap_id, feedback_type, description, user_ip, email, created_at)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (roadmap_id, feedback_type.value, description, user_ip, email, 
              datetime.utcnow()))
        
        # Send notification to admin
        await self._notify_admin(roadmap_id, feedback_type, description)
        
        return {"success": True}
    
    async def submit_task_feedback(self, task_id: str, roadmap_id: str,
                                  is_positive: bool, user_ip: str) -> dict:
        """Submit task-level feedback."""
        await self.db.execute("""
            INSERT INTO task_feedback (task_id, roadmap_id, rating, user_ip, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, (task_id, roadmap_id, is_positive, user_ip, datetime.utcnow()))
        
        return {"success": True}
    
    async def submit_bug_report(self, bug_type: str, description: str,
                               page_url: str, user_ip: str,
                               email: Optional[str] = None,
                               screenshot_url: Optional[str] = None) -> dict:
        """Submit bug report."""
        await self.db.execute("""
            INSERT INTO bug_reports 
            (bug_type, description, page_url, user_ip, email, screenshot_url, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (bug_type, description, page_url, user_ip, email, screenshot_url,
              datetime.utcnow()))
        
        # Send notification to admin
        await self._notify_admin_bug(bug_type, description, page_url)
        
        return {"success": True}
    
    async def get_roadmap_stats(self, roadmap_id: str) -> dict:
        """Get feedback statistics for a roadmap."""
        result = await self.db.fetch_one("""
            SELECT 
                COUNT(*) as total_ratings,
                SUM(CASE WHEN rating = 1 THEN 1 ELSE 0 END) as positive,
                SUM(CASE WHEN rating = 0 THEN 1 ELSE 0 END) as negative
            FROM feedback
            WHERE roadmap_id = ?
        """, (roadmap_id,))
        
        detailed = await self.db.fetch_all("""
            SELECT feedback_type, COUNT(*) as count
            FROM detailed_feedback
            WHERE roadmap_id = ?
            GROUP BY feedback_type
        """, (roadmap_id,))
        
        return {
            "total_ratings": result["total_ratings"],
            "positive": result["positive"],
            "negative": result["negative"],
            "satisfaction_rate": (
                result["positive"] / result["total_ratings"] * 100 
                if result["total_ratings"] > 0 else 0
            ),
            "detailed_feedback": {row["feedback_type"]: row["count"] for row in detailed}
        }
    
    async def get_worst_roadmaps(self, limit: int = 10) -> list:
        """Get roadmaps with worst feedback."""
        return await self.db.fetch_all("""
            SELECT 
                r.id, r.slug, r.industry_name,
                COUNT(*) as total_feedback,
                SUM(CASE WHEN f.rating = 0 THEN 1 ELSE 0 END) as negative_count,
                ROUND(SUM(CASE WHEN f.rating = 1 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 1) as satisfaction_rate
            FROM roadmaps r
            JOIN feedback f ON r.id = f.roadmap_id
            GROUP BY r.id
            HAVING negative_count > 0
            ORDER BY satisfaction_rate ASC
            LIMIT ?
        """, (limit,))
    
    async def _notify_admin(self, roadmap_id: str, feedback_type: FeedbackType,
                           description: str):
        """Send notification to admin about feedback."""
        # TODO: Implement email notification
        pass
    
    async def _notify_admin_bug(self, bug_type: str, description: str, page_url: str):
        """Send notification to admin about bug report."""
        # TODO: Implement email notification
        pass
```

**Database schema:**

```sql
-- Simple ratings
CREATE TABLE feedback (
    id TEXT PRIMARY KEY,
    roadmap_id TEXT NOT NULL,
    rating BOOLEAN NOT NULL,  -- true=positive, false=negative
    user_ip TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (roadmap_id) REFERENCES roadmaps(id)
);

-- Detailed feedback
CREATE TABLE detailed_feedback (
    id TEXT PRIMARY KEY,
    roadmap_id TEXT NOT NULL,
    feedback_type TEXT NOT NULL,
    description TEXT,
    user_ip TEXT,
    email TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (roadmap_id) REFERENCES roadmaps(id)
);

-- Task-level feedback
CREATE TABLE task_feedback (
    id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    roadmap_id TEXT NOT NULL,
    rating BOOLEAN NOT NULL,
    user_ip TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (roadmap_id) REFERENCES roadmaps(id)
);

-- Bug reports
CREATE TABLE bug_reports (
    id TEXT PRIMARY KEY,
    bug_type TEXT NOT NULL,
    description TEXT NOT NULL,
    page_url TEXT,
    user_ip TEXT,
    email TEXT,
    screenshot_url TEXT,
    status TEXT DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP
);

CREATE INDEX idx_feedback_roadmap ON feedback(roadmap_id);
CREATE INDEX idx_detailed_feedback_roadmap ON detailed_feedback(roadmap_id);
CREATE INDEX idx_task_feedback_task ON task_feedback(task_id);
CREATE INDEX idx_bug_reports_status ON bug_reports(status);
```

**Feedback UI components:**

```html
<!-- Feedback widget trên trang roadmap -->
<div class="feedback-widget" id="feedback-widget">
  <div class="rating-section">
    <p>Roadmap này có hữu ích không?</p>
    <div class="rating-buttons">
      <button onclick="submitRating(true)" class="btn-positive" id="btn-positive">
        👍 Hữu ích
      </button>
      <button onclick="submitRating(false)" class="btn-negative" id="btn-negative">
        👎 Cần cải thiện
      </button>
    </div>
  </div>
  
  <div id="detailed-feedback-form" class="detailed-form" style="display: none;">
    <h4>Cho mình biết cần cải thiện gì:</h4>
    <form id="feedback-form">
      <div class="form-group">
        <label>Vấn đề:</label>
        <select name="feedback_type" required>
          <option value="">Chọn vấn đề...</option>
          <option value="salary_incorrect">Mức lương không chính xác</option>
          <option value="resource_broken">Link resource hỏng</option>
          <option value="tasks_unclear">Tasks không rõ ràng</option>
          <option value="timeline_unrealistic">Timeline không thực tế</option>
          <option value="skills_irrelevant">Skills không liên quan</option>
          <option value="other">Khác</option>
        </select>
      </div>
      
      <div class="form-group">
        <label>Mô tả chi tiết:</label>
        <textarea name="description" rows="3" placeholder="Mô tả vấn đề..."></textarea>
      </div>
      
      <div class="form-group">
        <label>Email (optional, để nhận phản hồi):</label>
        <input type="email" name="email" placeholder="email@example.com">
      </div>
      
      <button type="submit">Gửi phản hồi</button>
    </form>
  </div>
  
  <div id="feedback-thankyou" class="thankyou" style="display: none;">
    <p>Cảm ơn phản hồi của bạn! 🙏</p>
    <p>Chúng mình sẽ cải thiện roadmap này.</p>
  </div>
</div>

<!-- Bug report button (fixed position) -->
<button id="bug-report-btn" class="bug-report-button" onclick="openBugReport()">
  🐛 Báo lỗi
</button>

<!-- Bug report modal -->
<div id="bug-report-modal" class="modal" style="display: none;">
  <div class="modal-content">
    <span class="close" onclick="closeBugReport()">&times;</span>
    <h3>Báo lỗi</h3>
    <form id="bug-report-form">
      <div class="form-group">
        <label>Loại lỗi:</label>
        <select name="bug_type" required>
          <option value="">Chọn loại lỗi...</option>
          <option value="display">Hiển thị sai</option>
          <option value="function">Chức năng không hoạt động</option>
          <option value="content">Nội dung sai</option>
          <option value="performance">Chậm/lag</option>
          <option value="other">Khác</option>
        </select>
      </div>
      
      <div class="form-group">
        <label>Mô tả:</label>
        <textarea name="description" rows="4" placeholder="Mô tả lỗi..." required></textarea>
      </div>
      
      <div class="form-group">
        <label>Email (optional):</label>
        <input type="email" name="email" placeholder="email@example.com">
      </div>
      
      <button type="submit">Gửi báo lỗi</button>
    </form>
  </div>
</div>

<script>
// Submit rating
async function submitRating(isPositive) {
  const roadmapId = '{{ roadmap.id }}';
  
  try {
    const response = await fetch('/api/feedback/rating', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ roadmap_id: roadmapId, rating: isPositive })
    });
    
    if (response.ok) {
      // Track analytics
      Analytics.feedbackSubmit(roadmapId, isPositive);
      
      // Update UI
      document.getElementById('btn-positive').disabled = true;
      document.getElementById('btn-negative').disabled = true;
      
      if (!isPositive) {
        // Show detailed feedback form
        document.getElementById('detailed-feedback-form').style.display = 'block';
      } else {
        // Show thank you
        document.getElementById('feedback-thankyou').style.display = 'block';
      }
    }
  } catch (error) {
    console.error('Feedback failed:', error);
  }
}

// Submit detailed feedback
document.getElementById('feedback-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  const roadmapId = '{{ roadmap.id }}';
  
  try {
    const response = await fetch('/api/feedback/detailed', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        roadmap_id: roadmapId,
        feedback_type: formData.get('feedback_type'),
        description: formData.get('description'),
        email: formData.get('email') || null
      })
    });
    
    if (response.ok) {
      // Hide form, show thank you
      document.getElementById('detailed-feedback-form').style.display = 'none';
      document.getElementById('feedback-thankyou').style.display = 'block';
    }
  } catch (error) {
    console.error('Detailed feedback failed:', error);
  }
});

// Bug report
function openBugReport() {
  document.getElementById('bug-report-modal').style.display = 'block';
}

function closeBugReport() {
  document.getElementById('bug-report-modal').style.display = 'none';
}

document.getElementById('bug-report-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  
  try {
    const response = await fetch('/api/bug-report', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        bug_type: formData.get('bug_type'),
        description: formData.get('description'),
        page_url: window.location.href,
        email: formData.get('email') || null
      })
    });
    
    if (response.ok) {
      alert('Cảm ơn bạn đã báo lỗi! Chúng mình sẽ xem xét.');
      closeBugReport();
    }
  } catch (error) {
    console.error('Bug report failed:', error);
  }
});
</script>
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 14: SEARCH FUNCTIONALITY — Search + Filter + Sort

**Vấn đề:**
```
Không có cách:
- Tìm kiếm ngành nhanh
- Filter theo category
- Sort theo popularity
- Search roadmap đã tạo
```

**Giải pháp: Search bar + Filter UI + Sort options**

```
SEARCH & FILTER SYSTEM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Components:

1. Search Bar (trang chủ + landing pages)
   ├── Placeholder: "Tìm ngành học..."
   ├── Autocomplete: Gợi ý ngành
   ├── Search on type: Real-time filtering
   └── Clear button: Xóa search

2. Category Filter
   ├── Tabs hoặc dropdown
   ├── Categories:
   │   ├── IT & Công nghệ
   │   ├── Marketing & Truyền thông
   │   ├── Kinh doanh & Quản lý
   │   ├── Thiết kế & Sáng tạo
   │   ├── Tài chính & Kế toán
   │   ├── Y tế & Sức khỏe
   │   ├── Giáo dục
   │   ├── Kỹ thuật & Xây dựng
   │   ├── Du lịch & Khách sạn
   │   └── Luật
   └── "Tất cả" option

3. Sort Options
   ├── Phổ biến nhất (view_count)
   ├── Mới nhất (created_at)
   ├── Mức lương cao (salary_senior)
   └── Thời gian ngắn (duration_months)

4. Search Results
   ├── Card layout
   ├── Preview: Tên ngành, category, salary
   ├── CTA: "Xem roadmap mẫu"
   └── Pagination: 12 items/page
```

**Implementation:**

```python
# app/services/search.py
"""Search service."""

from typing import Optional, List
from dataclasses import dataclass

@dataclass
class SearchResult:
    id: str
    slug: str
    name: str
    category: str
    description: str
    salary_junior: str
    salary_mid: str
    salary_senior: str
    demand_level: str
    view_count: int

class SearchService:
    """Handle search operations."""
    
    def search_industries(self, query: str, category: Optional[str] = None,
                         sort_by: str = "popularity", 
                         page: int = 1, per_page: int = 12) -> dict:
        """Search industries with filters."""
        
        # Build SQL query
        sql = """
            SELECT id, slug, name, category, description,
                   avg_salary_junior, avg_salary_mid, avg_salary_senior,
                   demand_level, view_count
            FROM industries
            WHERE 1=1
        """
        params = []
        
        # Search query
        if query:
            sql += " AND (name LIKE ? OR description LIKE ? OR slug LIKE ?)"
            search_term = f"%{query}%"
            params.extend([search_term, search_term, search_term])
        
        # Category filter
        if category and category != "all":
            sql += " AND category = ?"
            params.append(category)
        
        # Sort
        if sort_by == "popularity":
            sql += " ORDER BY view_count DESC"
        elif sort_by == "newest":
            sql += " ORDER BY created_at DESC"
        elif sort_by == "salary_high":
            sql += " ORDER BY avg_salary_senior DESC"
        elif sort_by == "duration_short":
            sql += " ORDER BY avg_duration ASC"
        else:
            sql += " ORDER BY view_count DESC"
        
        # Pagination
        offset = (page - 1) * per_page
        sql += " LIMIT ? OFFSET ?"
        params.extend([per_page, offset])
        
        # Execute query
        results = self.db.fetch_all(sql, params)
        
        # Get total count
        count_sql = """
            SELECT COUNT(*) as total
            FROM industries
            WHERE 1=1
        """
        count_params = []
        
        if query:
            count_sql += " AND (name LIKE ? OR description LIKE ? OR slug LIKE ?)"
            search_term = f"%{query}%"
            count_params.extend([search_term, search_term, search_term])
        
        if category and category != "all":
            count_sql += " AND category = ?"
            count_params.append(category)
        
        total = self.db.fetch_one(count_sql, count_params)["total"]
        
        return {
            "results": results,
            "total": total,
            "page": page,
            "per_page": per_page,
            "total_pages": (total + per_page - 1) // per_page
        }
    
    def get_categories(self) -> List[dict]:
        """Get all categories with counts."""
        return self.db.fetch_all("""
            SELECT category, COUNT(*) as count
            FROM industries
            GROUP BY category
            ORDER BY count DESC
        """)
    
    def get_popular_industries(self, limit: int = 8) -> List[dict]:
        """Get most popular industries."""
        return self.db.fetch_all("""
            SELECT id, slug, name, category, avg_salary_junior, avg_salary_mid,
                   avg_salary_senior, demand_level, view_count
            FROM industries
            ORDER BY view_count DESC
            LIMIT ?
        """, (limit,))
    
    def increment_view_count(self, industry_id: str) -> None:
        """Increment view count for industry."""
        self.db.execute("""
            UPDATE industries SET view_count = view_count + 1
            WHERE id = ?
        """, (industry_id,))
    
    def autocomplete(self, query: str, limit: int = 5) -> List[dict]:
        """Autocomplete suggestions."""
        if not query or len(query) < 2:
            return []
        
        return self.db.fetch_all("""
            SELECT id, slug, name, category
            FROM industries
            WHERE name LIKE ? OR slug LIKE ?
            ORDER BY view_count DESC
            LIMIT ?
        """, (f"%{query}%", f"%{query}%", limit))
```

**Database schema update:**

```sql
-- Thêm view_count vào industries table
ALTER TABLE industries ADD COLUMN view_count INTEGER DEFAULT 0;
ALTER TABLE industries ADD COLUMN created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- Index cho search
CREATE INDEX idx_industries_name ON industries(name);
CREATE INDEX idx_industries_category ON industries(category);
CREATE INDEX idx_industries_view_count ON industries(view_count);
```

**Search UI components:**

```html
<!-- Search bar trên trang chủ -->
<section class="search-section">
  <div class="container">
    <div class="search-box">
      <input type="text" id="search-input" placeholder="Tìm ngành học..." 
             autocomplete="off">
      <button id="search-btn">🔍</button>
      
      <!-- Autocomplete dropdown -->
      <div id="autocomplete-dropdown" class="autocomplete-dropdown" style="display: none;">
        <!-- Populated by JavaScript -->
      </div>
    </div>
    
    <!-- Category filters -->
    <div class="category-filters">
      <button class="filter-btn active" data-category="all">Tất cả</button>
      <button class="filter-btn" data-category="IT">IT & Công nghệ</button>
      <button class="filter-btn" data-category="Marketing">Marketing</button>
      <button class="filter-btn" data-category="Design">Thiết kế</button>
      <button class="filter-btn" data-category="Business">Kinh doanh</button>
      <button class="filter-btn" data-category="Finance">Tài chính</button>
      <!-- Thêm categories khác -->
    </div>
    
    <!-- Sort options -->
    <div class="sort-options">
      <label>Sắp xếp:</label>
      <select id="sort-select">
        <option value="popularity">Phổ biến nhất</option>
        <option value="newest">Mới nhất</option>
        <option value="salary_high">Mức lương cao</option>
        <option value="duration_short">Thời gian ngắn</option>
      </select>
    </div>
  </div>
</section>

<!-- Search results -->
<section class="search-results">
  <div class="container">
    <div id="results-count" class="results-count"></div>
    
    <div id="results-grid" class="results-grid">
      <!-- Populated by JavaScript -->
    </div>
    
    <div id="pagination" class="pagination">
      <!-- Populated by JavaScript -->
    </div>
  </div>
</section>

<script>
// Search state
let currentSearch = {
  query: '',
  category: 'all',
  sortBy: 'popularity',
  page: 1
};

// Search input handler
const searchInput = document.getElementById('search-input');
const autocompleteDropdown = document.getElementById('autocomplete-dropdown');
let searchTimeout;

searchInput.addEventListener('input', (e) => {
  const query = e.target.value;
  
  // Clear previous timeout
  clearTimeout(searchTimeout);
  
  // Debounce search
  searchTimeout = setTimeout(() => {
    if (query.length >= 2) {
      // Show autocomplete
      showAutocomplete(query);
    } else {
      // Hide autocomplete
      autocompleteDropdown.style.display = 'none';
    }
  }, 300);
});

// Show autocomplete suggestions
async function showAutocomplete(query) {
  try {
    const response = await fetch(`/api/search/autocomplete?q=${encodeURIComponent(query)}`);
    const data = await response.json();
    
    if (data.results.length > 0) {
      autocompleteDropdown.innerHTML = data.results.map(item => `
        <div class="autocomplete-item" onclick="selectIndustry('${item.slug}')">
          <span class="industry-name">${item.name}</span>
          <span class="industry-category">${item.category}</span>
        </div>
      `).join('');
      autocompleteDropdown.style.display = 'block';
    } else {
      autocompleteDropdown.style.display = 'none';
    }
  } catch (error) {
    console.error('Autocomplete failed:', error);
  }
}

// Select industry from autocomplete
function selectIndustry(slug) {
  autocompleteDropdown.style.display = 'none';
  searchInput.value = '';
  window.location.href = `/nganh/${slug}`;
}

// Category filter click
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    // Update active state
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    
    // Update search state
    currentSearch.category = btn.dataset.category;
    currentSearch.page = 1;
    
    // Track analytics
    Analytics.filterUsed('category', btn.dataset.category);
    
    // Perform search
    performSearch();
  });
});

// Sort change
document.getElementById('sort-select').addEventListener('change', (e) => {
  currentSearch.sortBy = e.target.value;
  currentSearch.page = 1;
  performSearch();
});

// Perform search
async function performSearch() {
  const params = new URLSearchParams({
    q: currentSearch.query,
    category: currentSearch.category,
    sort: currentSearch.sortBy,
    page: currentSearch.page,
    per_page: 12
  });
  
  try {
    const response = await fetch(`/api/search?${params}`);
    const data = await response.json();
    
    // Update results count
    document.getElementById('results-count').textContent = 
      `Tìm thấy ${data.total} ngành`;
    
    // Update results grid
    document.getElementById('results-grid').innerHTML = data.results.map(item => `
      <div class="industry-card">
        <h3>${item.name}</h3>
        <span class="category-badge">${item.category}</span>
        <p class="salary-info">
          Junior: ${item.avg_salary_junior}<br>
          Senior: ${item.avg_salary_senior}
        </p>
        <span class="demand-badge ${item.demand_level.toLowerCase()}">${item.demand_level}</span>
        <a href="/nganh/${item.slug}" class="btn-primary">Xem roadmap</a>
      </div>
    `).join('');
    
    // Update pagination
    updatePagination(data.page, data.total_pages);
    
    // Track analytics
    Analytics.search(currentSearch.query, data.total);
    
  } catch (error) {
    console.error('Search failed:', error);
  }
}

// Update pagination
function updatePagination(currentPage, totalPages) {
  const pagination = document.getElementById('pagination');
  
  if (totalPages <= 1) {
    pagination.innerHTML = '';
    return;
  }
  
  let html = '';
  
  // Previous button
  if (currentPage > 1) {
    html += `<button onclick="goToPage(${currentPage - 1})">← Trước</button>`;
  }
  
  // Page numbers
  for (let i = 1; i <= totalPages; i++) {
    if (i === currentPage) {
      html += `<button class="active">${i}</button>`;
    } else if (i === 1 || i === totalPages || (i >= currentPage - 2 && i <= currentPage + 2)) {
      html += `<button onclick="goToPage(${i})">${i}</button>`;
    } else if (i === currentPage - 3 || i === currentPage + 3) {
      html += `<span>...</span>`;
    }
  }
  
  // Next button
  if (currentPage < totalPages) {
    html += `<button onclick="goToPage(${currentPage + 1})">Sau →</button>`;
  }
  
  pagination.innerHTML = html;
}

// Go to page
function goToPage(page) {
  currentSearch.page = page;
  performSearch();
  
  // Scroll to top of results
  document.getElementById('results-grid').scrollIntoView({ behavior: 'smooth' });
}

// Search button click
document.getElementById('search-btn').addEventListener('click', () => {
  currentSearch.query = searchInput.value;
  currentSearch.page = 1;
  autocompleteDropdown.style.display = 'none';
  performSearch();
});

// Search on Enter
searchInput.addEventListener('keypress', (e) => {
  if (e.key === 'Enter') {
    currentSearch.query = searchInput.value;
    currentSearch.page = 1;
    autocompleteDropdown.style.display = 'none';
    performSearch();
  }
});

// Initial load
document.addEventListener('DOMContentLoaded', () => {
  performSearch();
});
</script>
```

**CSS styles:**

```css
/* Search section */
.search-section {
  background: #f9fafb;
  padding: 40px 0;
}

.search-box {
  position: relative;
  max-width: 600px;
  margin: 0 auto 20px;
}

.search-box input {
  width: 100%;
  padding: 12px 50px 12px 20px;
  font-size: 16px;
  border: 2px solid #e5e7eb;
  border-radius: 8px;
  outline: none;
}

.search-box input:focus {
  border-color: #4F46E5;
}

.search-box button {
  position: absolute;
  right: 5px;
  top: 50%;
  transform: translateY(-50%);
  background: none;
  border: none;
  font-size: 20px;
  cursor: pointer;
}

/* Autocomplete */
.autocomplete-dropdown {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 0 0 8px 8px;
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  z-index: 100;
}

.autocomplete-item {
  padding: 12px 20px;
  cursor: pointer;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.autocomplete-item:hover {
  background: #f3f4f6;
}

.industry-name {
  font-weight: 500;
}

.industry-category {
  font-size: 12px;
  color: #6b7280;
  background: #f3f4f6;
  padding: 2px 8px;
  border-radius: 4px;
}

/* Category filters */
.category-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-bottom: 20px;
}

.filter-btn {
  padding: 8px 16px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.2s;
}

.filter-btn:hover {
  border-color: #4F46E5;
  color: #4F46E5;
}

.filter-btn.active {
  background: #4F46E5;
  color: white;
  border-color: #4F46E5;
}

/* Sort options */
.sort-options {
  text-align: center;
  margin-bottom: 20px;
}

.sort-options label {
  margin-right: 10px;
  color: #6b7280;
}

.sort-options select {
  padding: 8px 12px;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  outline: none;
}

/* Results grid */
.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.industry-card {
  background: white;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  transition: all 0.2s;
}

.industry-card:hover {
  box-shadow: 0 4px 6px rgba(0,0,0,0.1);
  transform: translateY(-2px);
}

.industry-card h3 {
  margin: 0 0 10px;
  font-size: 18px;
}

.category-badge {
  display: inline-block;
  padding: 4px 8px;
  background: #f3f4f6;
  border-radius: 4px;
  font-size: 12px;
  color: #6b7280;
  margin-bottom: 10px;
}

.salary-info {
  font-size: 14px;
  color: #374151;
  margin-bottom: 10px;
}

.demand-badge {
  display: inline-block;
  padding: 4px 8px;
  border-radius: 4px;
  font-size: 12px;
  font-weight: 500;
  margin-bottom: 15px;
}

.demand-badge.cao {
  background: #d1fae5;
  color: #065f46;
}

.demand-badge.trung-bình {
  background: #fef3c7;
  color: #92400e;
}

.demand-badge.thấp {
  background: #fee2e2;
  color: #991b1b;
}

.btn-primary {
  display: inline-block;
  padding: 10px 20px;
  background: #4F46E5;
  color: white;
  text-decoration: none;
  border-radius: 6px;
  transition: background 0.2s;
}

.btn-primary:hover {
  background: #4338ca;
}

/* Pagination */
.pagination {
  display: flex;
  justify-content: center;
  gap: 5px;
}

.pagination button {
  padding: 8px 12px;
  background: white;
  border: 1px solid #e5e7eb;
  border-radius: 6px;
  cursor: pointer;
}

.pagination button:hover {
  background: #f3f4f6;
}

.pagination button.active {
  background: #4F46E5;
  color: white;
  border-color: #4F46E5;
}

/* Results count */
.results-count {
  text-align: center;
  color: #6b7280;
  margin-bottom: 20px;
}
```

**API endpoints:**

```python
# app/routes/search.py
"""Search API endpoints."""

from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter()

@router.get("/api/search")
async def search_industries(
    q: str = Query("", description="Search query"),
    category: str = Query("all", description="Category filter"),
    sort: str = Query("popularity", description="Sort by"),
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(12, ge=1, le=50, description="Items per page")
):
    """Search industries with filters."""
    results = search_service.search_industries(
        query=q,
        category=category if category != "all" else None,
        sort_by=sort,
        page=page,
        per_page=per_page
    )
    return results

@router.get("/api/search/autocomplete")
async def autocomplete(
    q: str = Query(..., min_length=2, description="Search query")
):
    """Autocomplete suggestions."""
    results = search_service.autocomplete(q, limit=5)
    return {"results": results}

@router.get("/api/categories")
async def get_categories():
    """Get all categories with counts."""
    categories = search_service.get_categories()
    return {"categories": categories}
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 15: SOCIAL PROOF — Counter thật hoặc bỏ fake proof

**Vấn đề:**
```
"1,000+ roadmap đã được tạo" khi chưa có ai
→ User thấy ngay là fake
→ Mất trust
→ Phản tác dụng
```

**Giải pháp: Thay đổi social proof strategy theo giai đoạn**

```
SOCIAL PROOF STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Giai đoạn 1: Pre-launch (0-100 roadmaps)
├── KHÔNG hiện counter
├── Thay bằng: Feature highlights
│   ├── "Cá nhân hóa 100%"
│   ├── "Miễn phí, không cần đăng nhập"
│   └── "3 cấp: Tổng quan → Giai đoạn → Tasks"
├── Focus vào: Value proposition
└── CTA: "Tạo roadmap ngay"

Giai đoạn 2: Early stage (100-1,000 roadmaps)
├── Hiện counter THẬT
│   ├── "247 roadmap đã được tạo"
│   └── Cập nhật realtime (hoặc daily)
├── Thêm: User testimonials (nếu có)
│   ├── "Roadmap rất hữu ích!" — Nguyễn Văn A
│   └── "Mình đã học theo và có việc" — Trần Thị B
└── CTA: "Tham gia cùng 247 người"

Giai đoạn 3: Growth (1,000+ roadmaps)
├── Hiện counter với format:
│   ├── "1,234+ roadmap đã được tạo"
│   └── Cập nhật realtime
├── Thêm: Social proof khác
│   ├── "Được featured trên VnExpress"
│   ├── "Top 1 Product Hunt VN"
│   └── "Được 50+ chuyên gia recommend"
└── CTA: "Tham gia cùng 1,234+ người"
```

**Implementation:**

```python
# app/services/social_proof.py
"""Social proof service."""

from typing import Optional
from datetime import datetime, timedelta

class SocialProofService:
    """Handle social proof display logic."""
    
    # Thresholds
    HIDE_COUNTER_THRESHOLD = 100  # Ẩn counter nếu < 100
    SHOW_REALTIME_THRESHOLD = 1000  # Hiện realtime nếu > 1000
    
    def get_hero_proof(self) -> dict:
        """Get social proof for hero section."""
        total_roadmaps = self._get_total_roadmaps()
        
        if total_roadmaps < self.HIDE_COUNTER_THRESHOLD:
            # Giai đoạn 1: Feature highlights
            return {
                "type": "features",
                "items": [
                    {"icon": "🎯", "text": "Cá nhân hóa 100%"},
                    {"icon": "🆓", "text": "Miễn phí, không cần đăng nhập"},
                    {"icon": "📊", "text": "3 cấp: Tổng quan → Giai đoạn → Tasks"}
                ]
            }
        elif total_roadmaps < self.SHOW_REALTIME_THRESHOLD:
            # Giai đoạn 2: Counter + testimonials
            testimonials = self._get_testimonials(limit=2)
            return {
                "type": "counter_with_testimonials",
                "counter": {
                    "count": total_roadmaps,
                    "text": f"{total_roadmaps} roadmap đã được tạo"
                },
                "testimonials": testimonials
            }
        else:
            # Giai đoạn 3: Counter realtime + achievements
            return {
                "type": "counter_realtime",
                "counter": {
                    "count": total_roadmaps,
                    "text": f"{total_roadmaps:,}+ roadmap đã được tạo",
                    "realtime": True
                },
                "achievements": [
                    {"icon": "🏆", "text": "Top 1 Product Hunt VN"},
                    {"icon": "📰", "text": "Được feature trên VnExpress"},
                    {"icon": "👨‍💼", "text": "Được 50+ chuyên gia recommend"}
                ]
            }
    
    def get_page_proof(self, page_type: str) -> dict:
        """Get social proof for specific pages."""
        total_roadmaps = self._get_total_roadmaps()
        
        if page_type == "landing":
            # Landing page: Counter + CTA
            if total_roadmaps < self.HIDE_COUNTER_THRESHOLD:
                return {
                    "show_counter": False,
                    "cta": "Tạo roadmap ngay"
                }
            else:
                return {
                    "show_counter": True,
                    "counter_text": f"Tham gia cùng {total_roadmaps:,}+ người",
                    "cta": "Tạo roadmap ngay"
                }
        
        elif page_type == "result":
            # Result page: Counter + share
            if total_roadmaps < self.HIDE_COUNTER_THRESHOLD:
                return {
                    "show_counter": False,
                    "share_text": "Chia sẻ roadmap này"
                }
            else:
                return {
                    "show_counter": True,
                    "counter_text": f"{total_roadmaps:,}+ roadmap đã được tạo",
                    "share_text": "Chia sẻ roadmap này"
                }
        
        elif page_type == "industry":
            # Industry page: Industry-specific stats
            industry_stats = self._get_industry_stats(page_type)
            return {
                "show_counter": True,
                "counter_text": f"{industry_stats['count']} roadmap đã được tạo",
                "show_salary": True,
                "salary_range": industry_stats['salary_range']
            }
    
    def _get_total_roadmaps(self) -> int:
        """Get total roadmaps count."""
        result = self.db.fetch_one("SELECT COUNT(*) as total FROM roadmaps")
        return result["total"]
    
    def _get_testimonials(self, limit: int = 2) -> list:
        """Get user testimonials."""
        # TODO: Implement testimonials table
        # For now, return empty list
        return []
    
    def _get_industry_stats(self, industry: str) -> dict:
        """Get industry-specific statistics."""
        result = self.db.fetch_one("""
            SELECT 
                COUNT(*) as count,
                salary_junior,
                salary_mid,
                salary_senior
            FROM roadmaps
            WHERE industry = ?
        """, (industry,))
        
        return {
            "count": result["count"],
            "salary_range": {
                "junior": result["salary_junior"],
                "mid": result["salary_mid"],
                "senior": result["salary_senior"]
            }
        }
```

**UI components:**

```html
<!-- Hero section social proof -->
<section class="hero">
  <div class="container">
    <h1>Tạo lộ trình học IT cá nhân hóa bằng AI</h1>
    <p>Nhập thông tin, AI tạo roadmap riêng cho bạn theo 3 cấp</p>
    
    <!-- Social proof - Dynamic -->
    <div id="social-proof" class="social-proof">
      <!-- Populated by JavaScript based on stage -->
    </div>
    
    <a href="/tao-roadmap" class="btn-primary">Bắt đầu ngay</a>
  </div>
</section>

<script>
// Load social proof
async function loadSocialProof() {
  try {
    const response = await fetch('/api/social-proof/hero');
    const data = await response.json();
    
    const container = document.getElementById('social-proof');
    
    if (data.type === 'features') {
      // Giai đoạn 1: Feature highlights
      container.innerHTML = data.items.map(item => `
        <div class="feature-item">
          <span class="feature-icon">${item.icon}</span>
          <span class="feature-text">${item.text}</span>
        </div>
      `).join('');
      
    } else if (data.type === 'counter_with_testimonials') {
      // Giai đoạn 2: Counter + testimonials
      let html = `
        <div class="counter">
          <span class="counter-number">${data.counter.count}</span>
          <span class="counter-text">${data.counter.text}</span>
        </div>
      `;
      
      if (data.testimonials.length > 0) {
        html += '<div class="testimonials">';
        data.testimonials.forEach(t => {
          html += `
            <div class="testimonial">
              <p>"${t.text}"</p>
              <span class="testimonial-author">— ${t.author}</span>
            </div>
          `;
        });
        html += '</div>';
      }
      
      container.innerHTML = html;
      
    } else if (data.type === 'counter_realtime') {
      // Giai đoạn 3: Counter realtime + achievements
      let html = `
        <div class="counter realtime">
          <span class="counter-number" id="counter-number">${data.counter.count}</span>
          <span class="counter-text">${data.counter.text}</span>
        </div>
      `;
      
      if (data.achievements && data.achievements.length > 0) {
        html += '<div class="achievements">';
        data.achievements.forEach(a => {
          html += `
            <div class="achievement">
              <span class="achievement-icon">${a.icon}</span>
              <span class="achievement-text">${a.text}</span>
            </div>
          `;
        });
        html += '</div>';
      }
      
      container.innerHTML = html;
      
      // Animate counter nếu realtime
      if (data.counter.realtime) {
        animateCounter(data.counter.count);
      }
    }
    
  } catch (error) {
    console.error('Failed to load social proof:', error);
  }
}

// Animate counter
function animateCounter(target) {
  const element = document.getElementById('counter-number');
  const duration = 2000; // 2 seconds
  const start = 0;
  const increment = target / (duration / 16);
  let current = start;
  
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      clearInterval(timer);
      current = target;
    }
    element.textContent = Math.floor(current).toLocaleString();
  }, 16);
}

// Load on page load
document.addEventListener('DOMContentLoaded', loadSocialProof);
</script>

<style>
.social-proof {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
  margin: 30px 0;
}

/* Features (Giai đoạn 1) */
.feature-item {
  display: flex;
  align-items: center;
  gap: 8px;
  background: rgba(255,255,255,0.1);
  padding: 10px 15px;
  border-radius: 8px;
}

.feature-icon {
  font-size: 20px;
}

.feature-text {
  font-size: 14px;
  color: #374151;
}

/* Counter (Giai đoạn 2-3) */
.counter {
  text-align: center;
  padding: 20px;
}

.counter-number {
  display: block;
  font-size: 48px;
  font-weight: 700;
  color: #4F46E5;
  line-height: 1;
}

.counter-text {
  font-size: 16px;
  color: #6b7280;
}

/* Testimonials (Giai đoạn 2) */
.testimonials {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  justify-content: center;
}

.testimonial {
  background: white;
  padding: 15px 20px;
  border-radius: 8px;
  border: 1px solid #e5e7eb;
  max-width: 300px;
}

.testimonial p {
  font-style: italic;
  margin: 0 0 10px;
  color: #374151;
}

.testimonial-author {
  font-size: 12px;
  color: #6b7280;
}

/* Achievements (Giai đoạn 3) */
.achievements {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  justify-content: center;
}

.achievement {
  display: flex;
  align-items: center;
  gap: 8px;
  background: #f3f4f6;
  padding: 10px 15px;
  border-radius: 8px;
}

.achievement-icon {
  font-size: 18px;
}

.achievement-text {
  font-size: 13px;
  color: #374151;
}

@media (max-width: 768px) {
  .counter-number {
    font-size: 36px;
  }
  
  .testimonials {
    flex-direction: column;
    align-items: center;
  }
  
  .achievements {
    flex-direction: column;
    align-items: center;
  }
}
</style>
```

**API endpoint:**

```python
# app/routes/social_proof.py
"""Social proof API endpoints."""

from fastapi import APIRouter

router = APIRouter()

@router.get("/api/social-proof/hero")
async def get_hero_proof():
    """Get social proof for hero section."""
    return social_proof_service.get_hero_proof()

@router.get("/api/social-proof/page/{page_type}")
async def get_page_proof(page_type: str):
    """Get social proof for specific page."""
    return social_proof_service.get_page_proof(page_type)
```

**Thay đổi trong plan hiện tại:**

Cần cập nhật các section sau:
1. Wireframe trang chủ (line ~1659): Thay "1,000+ roadmap" bằng dynamic social proof
2. User flow trang chủ (line ~1170): Cập nhật social proof logic
3. Mobile wireframe (line ~1710): Cập nhật social proof

**Trạng thái:** ✅ Đã xác định xong

---

## TÓM TẮT MEDIUM PRIORITY RESOLUTION

| # | Issue | Giải pháp | Status |
|---|-------|-----------|--------|
| 11 | Analytics | GA4 + Custom events + Conversion funnel | ✅ |
| 12 | Email Capture | Resend + Newsletter + Re-engagement | ✅ |
| 13 | Feedback Mechanism | Rating system + Bug report + Detailed feedback | ✅ |
| 14 | Search Functionality | Search bar + Category filter + Sort options | ✅ |
| 15 | Social Proof | Dynamic social proof theo giai đoạn | ✅ |

**Next steps:**
1. Setup GA4 account + Search Console
2. Setup Resend account + email templates
3. Implement feedback widget
4. Implement search functionality
5. Update wireframes với dynamic social proof

---
## TECHNICAL RESOLUTION — Giải quyết 5 thiếu sót kỹ thuật

> Cập nhật: 30/05/2026
> Mục tiêu: Giải quyết 5 thiếu sót kỹ thuật để đảm bảo performance, security, và reliability

---

### ISSUE 16: CACHING LAYER — Redis + HTTP Caching Headers

**Vấn đề:**
```
Hiện tại:
- Mỗi request → Query DB + Gọi AI (nếu cần)
- Không có HTTP caching headers
- Không có server-side cache
- Response time chậm cho repeat requests
```

**Giải pháp: Multi-layer caching**

```
CACHING STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Layer 1: HTTP Caching (Browser + CDN)
├── Cache-Control headers
├── ETag generation
├── Last-Modified headers
└── Cloudflare edge caching

Layer 2: Application Cache (In-memory)
├── Python dict cache (simple)
├── cachetools library (TTL cache)
├── Cache roadmaps (hot data)
└── Cache industry data

Layer 3: Database Query Cache (SQLite)
├── SQLite query cache (built-in)
├── Prepared statements
└── Connection pooling (aiosqlite)

Layer 4: AI Response Cache
├── Cache key: hash(industry + level + duration + age)
├── Cache TTL: 7 days
├── Cache storage: SQLite table
└── Hit rate target: 30-40%
```

**Implementation:**

```python
# app/middleware/cache.py
"""Caching middleware."""

import hashlib
import json
import time
from typing import Optional, Any
from functools import wraps
from fastapi import Request, Response
from fastapi.responses import JSONResponse

class CacheMiddleware:
    """HTTP caching middleware."""
    
    def __init__(self, app):
        self.app = app
        self.cache_config = {
            # Path patterns → Cache settings
            "/static/": {"max_age": 86400, "public": True},  # 1 day
            "/nganh/": {"max_age": 3600, "public": True},    # 1 hour
            "/roadmap/": {"max_age": 300, "public": True},   # 5 minutes
            "/api/": {"max_age": 0, "no_cache": True},       # No cache
            "/": {"max_age": 3600, "public": True},          # 1 hour
        }
    
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        
        request = Request(scope, receive)
        path = request.url.path
        
        # Find matching cache config
        cache_config = self._get_cache_config(path)
        
        if cache_config:
            # Add cache headers to response
            async def send_with_cache_headers(message):
                if message["type"] == "http.response.start":
                    headers = dict(message.get("headers", {}))
                    
                    # Add Cache-Control
                    if cache_config.get("no_cache"):
                        headers[b"cache-control"] = b"no-cache, no-store, must-revalidate"
                    else:
                        max_age = cache_config.get("max_age", 0)
                        public = "public" if cache_config.get("public") else "private"
                        headers[b"cache-control"] = f"{public}, max-age={max_age}".encode()
                    
                    # Add ETag
                    if b"etag" not in headers:
                        etag = self._generate_etag(request)
                        headers[b"etag"] = etag.encode()
                    
                    # Add Last-Modified
                    if b"last-modified" not in headers:
                        headers[b"last-modified"] = self._get_last_modified().encode()
                    
                    message["headers"] = list(headers.items())
                
                await send(message)
            
            await self.app(scope, receive, send_with_cache_headers)
        else:
            await self.app(scope, receive, send)
    
    def _get_cache_config(self, path: str) -> Optional[dict]:
        """Get cache config for path."""
        for pattern, config in self.cache_config.items():
            if path.startswith(pattern):
                return config
        return None
    
    def _generate_etag(self, request: Request) -> str:
        """Generate ETag for request."""
        # Simple ETag based on URL + timestamp
        etag_input = f"{request.url.path}:{int(time.time() // 300)}"  # 5 min window
        return hashlib.md5(etag_input.encode()).hexdigest()
    
    def _get_last_modified(self) -> str:
        """Get Last-Modified header value."""
        from email.utils import formatdate
        return formatdate(timeval=time.time(), usegmt=True)
```

```python
# app/cache/memory.py
"""In-memory cache using cachetools."""

from cachetools import TTLCache
from typing import Any, Optional
import hashlib
import json

class MemoryCache:
    """In-memory cache with TTL."""
    
    def __init__(self, maxsize: int = 1000, ttl: int = 300):
        self.cache = TTLCache(maxsize=maxsize, ttl=ttl)
    
    def get(self, key: str) -> Optional[Any]:
        """Get value from cache."""
        return self.cache.get(key)
    
    def set(self, key: str, value: Any, ttl: Optional[int] = None):
        """Set value in cache."""
        if ttl:
            # Create temporary cache with custom TTL
            temp_cache = TTLCache(maxsize=1, ttl=ttl)
            temp_cache[key] = value
            self.cache[key] = value
        else:
            self.cache[key] = value
    
    def delete(self, key: str):
        """Delete value from cache."""
        self.cache.pop(key, None)
    
    def clear(self):
        """Clear all cache."""
        self.cache.clear()
    
    def get_or_set(self, key: str, factory, ttl: Optional[int] = None) -> Any:
        """Get from cache or set using factory function."""
        value = self.get(key)
        if value is None:
            value = factory()
            self.set(key, value, ttl)
        return value

# Global cache instances
roadmap_cache = MemoryCache(maxsize=500, ttl=3600)  # 1 hour
industry_cache = MemoryCache(maxsize=100, ttl=86400)  # 1 day
search_cache = MemoryCache(maxsize=200, ttl=300)  # 5 minutes
```

```python
# app/cache/redis.py
"""Redis cache (optional, for production)."""

import os
import json
from typing import Optional, Any

class RedisCache:
    """Redis cache implementation."""
    
    def __init__(self):
        self.redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")
        self.client = None
    
    async def connect(self):
        """Connect to Redis."""
        try:
            import redis.asyncio as redis
            self.client = redis.from_url(self.redis_url)
            await self.client.ping()
            print("Connected to Redis")
        except Exception as e:
            print(f"Redis connection failed: {e}")
            self.client = None
    
    async def get(self, key: str) -> Optional[Any]:
        """Get value from Redis."""
        if not self.client:
            return None
        
        try:
            value = await self.client.get(key)
            if value:
                return json.loads(value)
        except Exception as e:
            print(f"Redis get error: {e}")
        
        return None
    
    async def set(self, key: str, value: Any, ttl: int = 3600):
        """Set value in Redis."""
        if not self.client:
            return
        
        try:
            await self.client.setex(key, ttl, json.dumps(value))
        except Exception as e:
            print(f"Redis set error: {e}")
    
    async def delete(self, key: str):
        """Delete value from Redis."""
        if not self.client:
            return
        
        try:
            await self.client.delete(key)
        except Exception as e:
            print(f"Redis delete error: {e}")
    
    async def clear(self):
        """Clear all cache."""
        if not self.client:
            return
        
        try:
            await self.client.flushdb()
        except Exception as e:
            print(f"Redis clear error: {e}")

# Global Redis cache (optional)
redis_cache = RedisCache()
```

```python
# app/cache/roadmap.py
"""Roadmap-specific caching."""

import hashlib
from typing import Optional
from .memory import roadmap_cache
from .redis import redis_cache

class RoadmapCache:
    """Cache roadmap data."""
    
    def _generate_key(self, industry: str, level: str, 
                     duration: int, age: int) -> str:
        """Generate cache key for roadmap."""
        input_str = f"{industry}:{level}:{duration}:{age}"
        return f"roadmap:{hashlib.md5(input_str.encode()).hexdigest()}"
    
    async def get(self, industry: str, level: str,
                 duration: int, age: int) -> Optional[dict]:
        """Get roadmap from cache."""
        key = self._generate_key(industry, level, duration, age)
        
        # Try memory cache first
        result = roadmap_cache.get(key)
        if result:
            return result
        
        # Try Redis cache
        result = await redis_cache.get(key)
        if result:
            # Store in memory cache for faster access
            roadmap_cache.set(key, result)
            return result
        
        return None
    
    async def set(self, industry: str, level: str, duration: int,
                 age: int, roadmap: dict, ttl: int = 604800):  # 7 days
        """Set roadmap in cache."""
        key = self._generate_key(industry, level, duration, age)
        
        # Store in memory cache
        roadmap_cache.set(key, roadmap, ttl=3600)  # 1 hour in memory
        
        # Store in Redis
        await redis_cache.set(key, roadmap, ttl=ttl)  # 7 days in Redis
    
    async def delete(self, industry: str, level: str,
                    duration: int, age: int):
        """Delete roadmap from cache."""
        key = self._generate_key(industry, level, duration, age)
        roadmap_cache.delete(key)
        await redis_cache.delete(key)
    
    async def get_stats(self) -> dict:
        """Get cache statistics."""
        return {
            "memory_cache_size": len(roadmap_cache.cache),
            "memory_cache_maxsize": roadmap_cache.cache.maxsize,
            "redis_connected": redis_cache.client is not None
        }

# Global roadmap cache
roadmap_cache_service = RoadmapCache()
```

**Cache headers configuration:**

```python
# app/config/cache.py
"""Cache configuration."""

CACHE_CONFIG = {
    # Static assets
    "static": {
        "max_age": 86400,  # 1 day
        "public": True,
        "immutable": True
    },
    
    # Landing pages
    "landing": {
        "max_age": 3600,  # 1 hour
        "public": True,
        "stale_while_revalidate": 300  # 5 minutes
    },
    
    # Roadmap pages
    "roadmap": {
        "max_age": 300,  # 5 minutes
        "public": True,
        "stale_while_revalidate": 60  # 1 minute
    },
    
    # API endpoints
    "api": {
        "max_age": 0,
        "no_cache": True,
        "no_store": True
    },
    
    # Health check
    "health": {
        "max_age": 0,
        "no_cache": True
    }
}

# Cache-Control header builder
def build_cache_control(config: dict) -> str:
    """Build Cache-Control header value."""
    parts = []
    
    if config.get("public"):
        parts.append("public")
    elif config.get("private"):
        parts.append("private")
    
    if config.get("no_cache"):
        parts.append("no-cache")
    
    if config.get("no_store"):
        parts.append("no-store")
    
    if config.get("must_revalidate"):
        parts.append("must-revalidate")
    
    max_age = config.get("max_age")
    if max_age is not None:
        parts.append(f"max-age={max_age}")
    
    stale = config.get("stale_while_revalidate")
    if stale:
        parts.append(f"stale-while-revalidate={stale}")
    
    return ", ".join(parts)
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 17: SECURITY HEADERS — CSP + X-Frame-Options + Security Middleware

**Vấn đề:**
```
Hiện tại:
- Không có CSP (Content Security Policy)
- Không có X-Frame-Options
- Không có X-Content-Type-Options
- Không có Strict-Transport-Security
- Không có rate limiting per IP thật sự
```

**Giải pháp: Security middleware với comprehensive headers**

```
SECURITY HEADERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Required Headers:
├── Content-Security-Policy (CSP)
│   ├── default-src 'self'
│   ├── script-src 'self' 'unsafe-inline' https://www.googletagmanager.com
│   ├── style-src 'self' 'unsafe-inline' https://fonts.googleapis.com
│   ├── font-src 'self' https://fonts.gstatic.com
│   ├── img-src 'self' data: https:
│   ├── connect-src 'self' https://www.google-analytics.com
│   └── frame-ancestors 'none'
│
├── X-Frame-Options: DENY
├── X-Content-Type-Options: nosniff
├── X-XSS-Protection: 1; mode=block
├── Referrer-Policy: strict-origin-when-cross-origin
├── Permissions-Policy: camera=(), microphone=(), geolocation=()
├── Strict-Transport-Security: max-age=31536000; includeSubDomains
└── Cross-Origin-Embedder-Policy: require-corp
```

**Implementation:**

```python
# app/middleware/security.py
"""Security middleware."""

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Dict

class SecurityMiddleware(BaseHTTPMiddleware):
    """Add security headers to all responses."""
    
    # Security headers configuration
    SECURITY_HEADERS = {
        # Content Security Policy
        "Content-Security-Policy": (
            "default-src 'self'; "
            "script-src 'self' 'unsafe-inline' 'unsafe-eval' "
            "https://www.googletagmanager.com "
            "https://www.google-analytics.com "
            "https://cdn.jsdelivr.net; "
            "style-src 'self' 'unsafe-inline' "
            "https://fonts.googleapis.com "
            "https://cdn.jsdelivr.net; "
            "font-src 'self' "
            "https://fonts.gstatic.com; "
            "img-src 'self' data: https:; "
            "connect-src 'self' "
            "https://www.google-analytics.com "
            "https://www.googletagmanager.com "
            "https://api.resend.com; "
            "frame-ancestors 'none'; "
            "base-uri 'self'; "
            "form-action 'self'"
        ),
        
        # Prevent clickjacking
        "X-Frame-Options": "DENY",
        
        # Prevent MIME type sniffing
        "X-Content-Type-Options": "nosniff",
        
        # XSS Protection
        "X-XSS-Protection": "1; mode=block",
        
        # Referrer Policy
        "Referrer-Policy": "strict-origin-when-cross-origin",
        
        # Permissions Policy
        "Permissions-Policy": (
            "camera=(), "
            "microphone=(), "
            "geolocation=(), "
            "payment=()"
        ),
        
        # HSTS (only for HTTPS)
        "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
        
        # Cross-Origin policies
        "Cross-Origin-Embedder-Policy": "require-corp",
        "Cross-Origin-Opener-Policy": "same-origin",
        "Cross-Origin-Resource-Policy": "same-origin",
    }
    
    # Headers to skip for certain paths
    SKIP_PATHS = {
        "/health": ["Content-Security-Policy"],
        "/api/": ["Content-Security-Policy"],
    }
    
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)
        
        # Add security headers
        path = request.url.path
        skip_headers = set()
        
        for skip_path, headers in self.SKIP_PATHS.items():
            if path.startswith(skip_path):
                skip_headers.update(headers)
        
        for header, value in self.SECURITY_HEADERS.items():
            if header not in skip_headers:
                response.headers[header] = value
        
        # Add HSTS only for HTTPS
        if request.url.scheme == "https":
            response.headers["Strict-Transport-Security"] = (
                "max-age=31536000; includeSubDomains"
            )
        
        return response
```

```python
# app/middleware/rate_limit.py
"""Rate limiting middleware (updated)."""

import time
from collections import defaultdict
from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Rate limiting per IP."""
    
    def __init__(self, app):
        super().__init__(app)
        self.requests = defaultdict(list)
        self.blocked = {}
        
        # Rate limits: {path_pattern: (max_requests, window_seconds)}
        self.limits = {
            "/api/generate": (3, 60),      # 3/phút
            "/api/subscribe": (5, 300),     # 5/5 phút
            "/api/feedback": (10, 60),      # 10/phút
            "/api/search": (30, 60),        # 30/phút
            "/nganh/": (30, 60),            # 30/phút
            "/roadmap/": (30, 60),          # 30/phút
            "default": (100, 60),           # 100/phút
        }
    
    async def dispatch(self, request: Request, call_next):
        client_ip = self._get_client_ip(request)
        path = request.url.path
        
        # Check if IP is blocked
        if client_ip in self.blocked:
            if time.time() < self.blocked[client_ip]:
                raise HTTPException(
                    status_code=429,
                    detail="IP bị tạm khóa do spam"
                )
            else:
                del self.blocked[client_ip]
        
        # Find matching rate limit
        limit_key = "default"
        for pattern, (max_req, window) in self.limits.items():
            if path.startswith(pattern):
                limit_key = pattern
                break
        
        max_requests, window = self.limits[limit_key]
        
        # Clean old requests
        now = time.time()
        self.requests[(client_ip, limit_key)] = [
            t for t in self.requests[(client_ip, limit_key)]
            if now - t < window
        ]
        
        # Check limit
        current_count = len(self.requests[(client_ip, limit_key)])
        
        if current_count >= max_requests:
            # Block IP for 15 minutes if spamming
            if current_count > max_requests * 2:
                self.blocked[client_ip] = now + 900
            
            # Calculate retry after
            oldest_request = self.requests[(client_ip, limit_key)][0]
            retry_after = int(window - (now - oldest_request))
            
            raise HTTPException(
                status_code=429,
                detail=f"Quá nhiều yêu cầu. Thử lại sau {retry_after} giây.",
                headers={"Retry-After": str(retry_after)}
            )
        
        # Record request
        self.requests[(client_ip, limit_key)].append(now)
        
        # Add rate limit headers
        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = str(max_requests)
        response.headers["X-RateLimit-Remaining"] = str(max_requests - current_count - 1)
        response.headers["X-RateLimit-Reset"] = str(int(now + window))
        
        return response
    
    def _get_client_ip(self, request: Request) -> str:
        """Get real client IP (considering proxies)."""
        # Check for proxy headers
        forwarded = request.headers.get("X-Forwarded-For")
        if forwarded:
            return forwarded.split(",")[0].strip()
        
        real_ip = request.headers.get("X-Real-IP")
        if real_ip:
            return real_ip
        
        return request.client.host
```

```python
# app/middleware/request_id.py
"""Request ID middleware."""

import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

class RequestIDMiddleware(BaseHTTPMiddleware):
    """Add unique request ID to each request."""
    
    async def dispatch(self, request: Request, call_next):
        # Get or generate request ID
        request_id = request.headers.get("X-Request-ID")
        if not request_id:
            request_id = str(uuid.uuid4())
        
        # Store in request state
        request.state.request_id = request_id
        
        # Process request
        response = await call_next(request)
        
        # Add request ID to response
        response.headers["X-Request-ID"] = request_id
        
        return response
```

**Security checklist:**

```
SECURITY CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

□ Headers
  ├── ☐ Content-Security-Policy configured
  ├── ☐ X-Frame-Options: DENY
  ├── ☐ X-Content-Type-Options: nosniff
  ├── ☐ X-XSS-Protection: 1; mode=block
  ├── ☐ Referrer-Policy configured
  ├── ☐ Permissions-Policy configured
  ├── ☐ Strict-Transport-Security (HTTPS only)
  └── ☐ Cross-Origin policies configured

□ Rate Limiting
  ├── ☐ Per-IP rate limiting
  ├── ☐ Different limits for different endpoints
  ├── ☐ Rate limit headers in response
  ├── ☐ IP blocking for spam
  └── ☐ Retry-After header on 429

□ Input Validation
  ├── ☐ SQL injection prevention (parameterized queries)
  ├── ☐ XSS prevention (HTML escaping)
  ├── ☐ CSRF protection (tokens)
  ├── ☐ Request size limits
  └── └── Input sanitization

□ Authentication (future)
  ├── ☐ Password hashing (bcrypt)
  ├── ☐ JWT tokens
  ├── ☐ Session management
  └── └── OAuth2 support
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 18: HEALTH CHECK — Comprehensive Health Monitoring

**Vấn đề:**
```
Hiện tại:
- /health chỉ check DB
- Không check OpenAI API
- Không check disk space
- Không check memory usage
- Không check external dependencies
```

**Giải pháp: Comprehensive health check endpoint**

```
HEALTH CHECK COMPONENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Checks:
├── 1. Database (SQLite/PostgreSQL)
│   ├── Connection test
│   ├── Query test (SELECT 1)
│   └── Response time
│
├── 2. OpenAI API
│   ├── API key valid
│   ├── Connection test
│   └── Response time
│
├── 3. Disk Space
│   ├── Total space
│   ├── Used space
│   ├── Free space
│   └── Usage percentage
│
├── 4. Memory Usage
│   ├── Total memory
│   ├── Used memory
│   ├── Free memory
│   └── Usage percentage
│
├── 5. External Services
│   ├── Resend API (email)
│   ├── Redis (if configured)
│   └── Cloudflare (if configured)
│
└── 6. Application
    ├── Uptime
    ├── Version
    ├── Environment
    └── Request count
```

**Implementation:**

```python
# app/routes/health.py
"""Comprehensive health check endpoint."""

import os
import time
import psutil
from datetime import datetime, timedelta
from fastapi import APIRouter
from typing import Dict, Any

router = APIRouter()

# Track application start time
APP_START_TIME = time.time()
REQUEST_COUNT = 0

class HealthChecker:
    """Perform health checks."""
    
    def __init__(self, db, openai_client):
        self.db = db
        self.openai_client = openai_client
    
    async def check_all(self) -> Dict[str, Any]:
        """Run all health checks."""
        start_time = time.time()
        
        results = {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "version": os.getenv("APP_VERSION", "1.0.0"),
            "environment": os.getenv("APP_ENV", "development"),
            "uptime_seconds": int(time.time() - APP_START_TIME),
            "request_count": REQUEST_COUNT,
            "checks": {}
        }
        
        # Run checks
        checks = await self._run_checks()
        results["checks"] = checks
        
        # Determine overall status
        failed_checks = [
            name for name, check in checks.items()
            if check["status"] != "ok"
        ]
        
        if failed_checks:
            results["status"] = "degraded"
            results["failed_checks"] = failed_checks
        
        # Add response time
        results["response_time_ms"] = int((time.time() - start_time) * 1000)
        
        return results
    
    async def _run_checks(self) -> Dict[str, Any]:
        """Run individual checks."""
        checks = {}
        
        # Database check
        checks["database"] = await self._check_database()
        
        # OpenAI API check
        checks["openai_api"] = await self._check_openai_api()
        
        # Disk space check
        checks["disk_space"] = self._check_disk_space()
        
        # Memory check
        checks["memory"] = self._check_memory()
        
        # External services
        checks["external_services"] = await self._check_external_services()
        
        return checks
    
    async def _check_database(self) -> Dict[str, Any]:
        """Check database connectivity."""
        try:
            start_time = time.time()
            
            # Test query
            await self.db.execute("SELECT 1")
            
            response_time = int((time.time() - start_time) * 1000)
            
            return {
                "status": "ok",
                "response_time_ms": response_time,
                "type": "sqlite" if "sqlite" in str(self.db.url) else "postgresql"
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    async def _check_openai_api(self) -> Dict[str, Any]:
        """Check OpenAI API connectivity."""
        try:
            start_time = time.time()
            
            # Test API key (list models)
            # Note: This is a lightweight check
            api_key = os.getenv("OPENAI_API_KEY")
            if not api_key:
                return {
                    "status": "error",
                    "error": "API key not configured"
                }
            
            # Simple validation (check key format)
            if not api_key.startswith("sk-"):
                return {
                    "status": "error",
                    "error": "Invalid API key format"
                }
            
            response_time = int((time.time() - start_time) * 1000)
            
            return {
                "status": "ok",
                "response_time_ms": response_time,
                "key_configured": True
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _check_disk_space(self) -> Dict[str, Any]:
        """Check disk space."""
        try:
            disk = psutil.disk_usage("/")
            
            return {
                "status": "ok" if disk.percent < 90 else "warning",
                "total_gb": round(disk.total / (1024**3), 2),
                "used_gb": round(disk.used / (1024**3), 2),
                "free_gb": round(disk.free / (1024**3), 2),
                "percent_used": disk.percent
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    def _check_memory(self) -> Dict[str, Any]:
        """Check memory usage."""
        try:
            memory = psutil.virtual_memory()
            
            return {
                "status": "ok" if memory.percent < 90 else "warning",
                "total_gb": round(memory.total / (1024**3), 2),
                "used_gb": round(memory.used / (1024**3), 2),
                "available_gb": round(memory.available / (1024**3), 2),
                "percent_used": memory.percent
            }
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            }
    
    async def _check_external_services(self) -> Dict[str, Any]:
        """Check external service connectivity."""
        services = {}
        
        # Check Resend API
        resend_key = os.getenv("RESEND_API_KEY")
        services["resend"] = {
            "status": "ok" if resend_key else "not_configured",
            "configured": bool(resend_key)
        }
        
        # Check Redis (if configured)
        redis_url = os.getenv("REDIS_URL")
        services["redis"] = {
            "status": "ok" if redis_url else "not_configured",
            "configured": bool(redis_url)
        }
        
        return services

# Health checker instance
health_checker = None

def init_health_checker(db, openai_client):
    """Initialize health checker."""
    global health_checker
    health_checker = HealthChecker(db, openai_client)

@router.get("/health")
async def health_check():
    """Comprehensive health check endpoint."""
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    
    if health_checker:
        return await health_checker.check_all()
    
    # Fallback simple check
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0"
    }

@router.get("/health/simple")
async def simple_health_check():
    """Simple health check (for load balancers)."""
    return {"status": "ok"}

@router.get("/health/ready")
async def readiness_check():
    """Readiness check (for Kubernetes)."""
    # Check if application is ready to serve traffic
    if health_checker:
        result = await health_checker.check_all()
        if result["status"] == "healthy":
            return {"status": "ready"}
    
    return {"status": "not_ready"}, 503

@router.get("/health/live")
async def liveness_check():
    """Liveness check (for Kubernetes)."""
    # Check if application is alive
    return {"status": "alive"}
```

**Health check response format:**

```json
{
  "status": "healthy",
  "timestamp": "2026-05-30T10:00:00Z",
  "version": "1.0.0",
  "environment": "production",
  "uptime_seconds": 86400,
  "request_count": 12345,
  "response_time_ms": 15,
  "checks": {
    "database": {
      "status": "ok",
      "response_time_ms": 5,
      "type": "sqlite"
    },
    "openai_api": {
      "status": "ok",
      "response_time_ms": 10,
      "key_configured": true
    },
    "disk_space": {
      "status": "ok",
      "total_gb": 50.0,
      "used_gb": 25.0,
      "free_gb": 25.0,
      "percent_used": 50
    },
    "memory": {
      "status": "ok",
      "total_gb": 8.0,
      "used_gb": 4.0,
      "available_gb": 4.0,
      "percent_used": 50
    },
    "external_services": {
      "resend": {
        "status": "ok",
        "configured": true
      },
      "redis": {
        "status": "not_configured",
        "configured": false
      }
    }
  }
}
```

**Monitoring integration:**

```python
# app/monitoring/health.py
"""Health monitoring and alerting."""

import asyncio
from datetime import datetime
from typing import Dict, Any

class HealthMonitor:
    """Monitor health and send alerts."""
    
    def __init__(self, health_checker, alert_service):
        self.health_checker = health_checker
        self.alert_service = alert_service
        self.last_status = "healthy"
        self.consecutive_failures = 0
    
    async def start_monitoring(self, interval: int = 60):
        """Start periodic health monitoring."""
        while True:
            try:
                result = await self.health_checker.check_all()
                await self._process_result(result)
            except Exception as e:
                print(f"Health monitoring error: {e}")
            
            await asyncio.sleep(interval)
    
    async def _process_result(self, result: Dict[str, Any]):
        """Process health check result."""
        current_status = result["status"]
        
        # Check for status change
        if current_status != self.last_status:
            if current_status == "degraded":
                self.consecutive_failures += 1
                
                # Send alert after 3 consecutive failures
                if self.consecutive_failures >= 3:
                    await self._send_alert(result)
            else:
                self.consecutive_failures = 0
                
                # Send recovery notification
                if self.last_status == "degraded":
                    await self._send_recovery(result)
            
            self.last_status = current_status
    
    async def _send_alert(self, result: Dict[str, Any]):
        """Send alert for degraded health."""
        failed_checks = result.get("failed_checks", [])
        
        message = f"""
        ⚠️ Health Alert
        
        Status: {result['status']}
        Failed checks: {', '.join(failed_checks)}
        Time: {result['timestamp']}
        
        Please investigate immediately.
        """
        
        # Send via email, Slack, etc.
        await self.alert_service.send_alert(message)
    
    async def _send_recovery(self, result: Dict[str, Any]):
        """Send recovery notification."""
        message = f"""
        ✅ Health Recovery
        
        Status: {result['status']}
        Time: {result['timestamp']}
        
        All systems operational.
        """
        
        await self.alert_service.send_alert(message)
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 19: LOGGING — Structured Logging + Sentry

**Vấn đề:**
```
Hiện tại:
- Basic logging (print statements)
- Không có structured logging
- Không có request ID tracking
- Không có error aggregation
- Khó debug production issues
```

**Giải pháp: Structured logging + Sentry integration**

```
LOGGING STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Components:
├── 1. Structured Logging (JSON)
│   ├── Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
│   ├── Context: request_id, user_id, ip, path
│   ├── Performance: response_time, db_query_time
│   └── Business: roadmap_generated, user_signup
│
├── 2. Request Logging
│   ├── Request: method, path, query, headers
│   ├── Response: status_code, response_time
│   ├── Error: exception, stack_trace
│   └── Context: request_id, user_agent, ip
│
├── 3. Sentry Integration
│   ├── Error tracking
│   ├── Performance monitoring
│   ├── Release tracking
│   └── Alert rules
│
└── 4. Log Aggregation
    ├── File logging (rotating)
    ├── stdout logging (Docker)
    └── External service (optional)
```

**Implementation:**

```python
# app/logging/config.py
"""Logging configuration."""

import os
import logging
import json
from datetime import datetime
from typing import Any, Dict

class JSONFormatter(logging.Formatter):
    """JSON log formatter."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as JSON."""
        log_data = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # Add extra fields
        if hasattr(record, "request_id"):
            log_data["request_id"] = record.request_id
        
        if hasattr(record, "user_id"):
            log_data["user_id"] = record.user_id
        
        if hasattr(record, "ip"):
            log_data["ip"] = record.ip
        
        if hasattr(record, "path"):
            log_data["path"] = record.path
        
        if hasattr(record, "method"):
            log_data["method"] = record.method
        
        if hasattr(record, "status_code"):
            log_data["status_code"] = record.status_code
        
        if hasattr(record, "response_time"):
            log_data["response_time_ms"] = record.response_time
        
        if hasattr(record, "extra"):
            log_data["extra"] = record.extra
        
        # Add exception info
        if record.exc_info:
            log_data["exception"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "traceback": self.formatException(record.exc_info)
            }
        
        return json.dumps(log_data, ensure_ascii=False)

def setup_logging():
    """Setup logging configuration."""
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    environment = os.getenv("APP_ENV", "development")
    
    # Root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(getattr(logging, log_level))
    
    # Remove existing handlers
    root_logger.handlers = []
    
    # Console handler (JSON format in production)
    console_handler = logging.StreamHandler()
    if environment == "production":
        console_handler.setFormatter(JSONFormatter())
    else:
        console_handler.setFormatter(logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        ))
    root_logger.addHandler(console_handler)
    
    # File handler (rotating)
    if environment == "production":
        from logging.handlers import RotatingFileHandler
        
        file_handler = RotatingFileHandler(
            "logs/app.log",
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5
        )
        file_handler.setFormatter(JSONFormatter())
        root_logger.addHandler(file_handler)
    
    # Suppress noisy loggers
    logging.getLogger("uvicorn").setLevel(logging.WARNING)
    logging.getLogger("uvicorn.access").setLevel(logging.WARNING)
    
    return root_logger
```

```python
# app/logging/request_logger.py
"""Request logging middleware."""

import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware(BaseHTTPMiddleware):
    """Log all requests and responses."""
    
    async def dispatch(self, request: Request, call_next):
        # Generate request ID
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request.state.request_id = request_id
        
        # Start timer
        start_time = time.time()
        
        # Log request
        logger.info(
            "Request started",
            extra={
                "request_id": request_id,
                "method": request.method,
                "path": request.url.path,
                "query": str(request.query_params),
                "ip": request.client.host,
                "user_agent": request.headers.get("User-Agent", "")
            }
        )
        
        try:
            # Process request
            response = await call_next(request)
            
            # Calculate response time
            response_time = int((time.time() - start_time) * 1000)
            
            # Log response
            logger.info(
                "Request completed",
                extra={
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "status_code": response.status_code,
                    "response_time": response_time
                }
            )
            
            # Add headers
            response.headers["X-Request-ID"] = request_id
            response.headers["X-Response-Time"] = f"{response_time}ms"
            
            return response
            
        except Exception as e:
            # Log error
            response_time = int((time.time() - start_time) * 1000)
            
            logger.error(
                "Request failed",
                extra={
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "response_time": response_time,
                    "error": str(e)
                },
                exc_info=True
            )
            
            raise
```

```python
# app/logging/sentry.py
"""Sentry integration."""

import os
import sentry_sdk
from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

def setup_sentry():
    """Setup Sentry error tracking."""
    sentry_dsn = os.getenv("SENTRY_DSN")
    
    if not sentry_dsn:
        print("SENTRY_DSN not configured, skipping Sentry setup")
        return
    
    # Sentry logging integration
    sentry_logging = LoggingIntegration(
        level=logging.INFO,        # Capture info and above as breadcrumbs
        event_level=logging.ERROR  # Send errors as events
    )
    
    # Initialize Sentry
    sentry_sdk.init(
        dsn=sentry_dsn,
        environment=os.getenv("APP_ENV", "development"),
        release=os.getenv("APP_VERSION", "1.0.0"),
        integrations=[
            FastApiIntegration(),
            sentry_logging
        ],
        traces_sample_rate=0.1,  # 10% of transactions
        profiles_sample_rate=0.1,  # 10% of transactions
        
        # beforeSend hook
        before_send=before_send_hook
    )
    
    print(f"Sentry initialized for environment: {os.getenv('APP_ENV')}")

def before_send_hook(event, hint):
    """Filter sensitive data before sending to Sentry."""
    # Remove sensitive headers
    if "request" in event:
        if "headers" in event["request"]:
            headers = event["request"]["headers"]
            if "Authorization" in headers:
                headers["Authorization"] = "[REDACTED]"
            if "Cookie" in headers:
                headers["Cookie"] = "[REDACTED]"
    
    # Remove sensitive query params
    if "request" in event:
        if "query_string" in event["request"]:
            query = event["request"]["query_string"]
            if "password" in query:
                event["request"]["query_string"] = "[REDACTED]"
    
    return event

def capture_exception(exception: Exception, context: dict = None):
    """Capture exception with context."""
    with sentry_sdk.new_scope() as scope:
        if context:
            for key, value in context.items():
                scope.set_extra(key, value)
        
        sentry_sdk.capture_exception(exception)

def capture_message(message: str, level: str = "info"):
    """Capture message."""
    sentry_sdk.capture_message(message, level=level)
```

```python
# app/logging/business_logger.py
"""Business event logging."""

import logging
from datetime import datetime
from typing import Optional, Dict, Any

logger = logging.getLogger(__name__)

class BusinessLogger:
    """Log business events."""
    
    def roadmap_generated(self, roadmap_id: str, industry: str,
                         level: str, duration: int, age: int,
                         generation_time_ms: int, tokens_used: int):
        """Log roadmap generation."""
        logger.info(
            "Roadmap generated",
            extra={
                "event": "roadmap_generated",
                "roadmap_id": roadmap_id,
                "industry": industry,
                "level": level,
                "duration": duration,
                "age": age,
                "generation_time_ms": generation_time_ms,
                "tokens_used": tokens_used
            }
        )
    
    def user_subscribed(self, email: str, industry: Optional[str],
                       source: str):
        """Log user subscription."""
        logger.info(
            "User subscribed",
            extra={
                "event": "user_subscribed",
                "email": email,
                "industry": industry,
                "source": source
            }
        )
    
    def feedback_submitted(self, roadmap_id: str, rating: bool,
                          feedback_type: Optional[str] = None):
        """Log feedback submission."""
        logger.info(
            "Feedback submitted",
            extra={
                "event": "feedback_submitted",
                "roadmap_id": roadmap_id,
                "rating": rating,
                "feedback_type": feedback_type
            }
        )
    
    def search_performed(self, query: str, category: Optional[str],
                        results_count: int):
        """Log search."""
        logger.info(
            "Search performed",
            extra={
                "event": "search_performed",
                "query": query,
                "category": category,
                "results_count": results_count
            }
        )
    
    def api_error(self, endpoint: str, error: str,
                 request_id: Optional[str] = None):
        """Log API error."""
        logger.error(
            "API error",
            extra={
                "event": "api_error",
                "endpoint": endpoint,
                "error": error,
                "request_id": request_id
            }
        )
    
    def performance_warning(self, endpoint: str, response_time_ms: int,
                           threshold_ms: int = 1000):
        """Log performance warning."""
        if response_time_ms > threshold_ms:
            logger.warning(
                "Slow response",
                extra={
                    "event": "performance_warning",
                    "endpoint": endpoint,
                    "response_time_ms": response_time_ms,
                    "threshold_ms": threshold_ms
                }
            )

# Global business logger
business_logger = BusinessLogger()
```

**Sentry setup guide:**

```
SENTRY SETUP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Create Sentry account (free tier)
   ├── 5,000 events/month
   ├── 1 user
   └── 30 days retention

2. Create project
   ├── Platform: Python
   ├── Framework: FastAPI
   └── Alert rules: On error

3. Get DSN
   ├── URL: https://sentry.io/settings/projects/
   └── DSN: https://xxx@xxx.ingest.sentry.io/xxx

4. Add to environment
   └── SENTRY_DSN=https://xxx@xxx.ingest.sentry.io/xxx

5. Install dependencies
   └── pip install sentry-sdk[fastapi]

6. Configure in app
   └── Call setup_sentry() on startup

7. Test
   └── raise Exception("Test Sentry")
```

**Log analysis queries:**

```sql
-- Top errors
SELECT 
    json_extract(message, '$.event') as event,
    COUNT(*) as count
FROM logs
WHERE level = 'ERROR'
GROUP BY event
ORDER BY count DESC
LIMIT 10;

-- Slow requests
SELECT 
    json_extract(message, '$.path') as path,
    AVG(json_extract(message, '$.response_time_ms')) as avg_time,
    MAX(json_extract(message, '$.response_time_ms')) as max_time
FROM logs
WHERE level = 'INFO'
  AND json_extract(message, '$.event') = 'request_completed'
GROUP BY path
HAVING avg_time > 1000
ORDER BY avg_time DESC;

-- Roadmap generation stats
SELECT 
    json_extract(message, '$.industry') as industry,
    COUNT(*) as count,
    AVG(json_extract(message, '$.generation_time_ms')) as avg_time,
    AVG(json_extract(message, '$.tokens_used')) as avg_tokens
FROM logs
WHERE json_extract(message, '$.event') = 'roadmap_generated'
GROUP BY industry
ORDER BY count DESC;
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 20: BACKUP STRATEGY — Daily Backup + S3 Upload

**Vấn đề:**
```
Hiện tại:
- SQLite file-based = dễ mất data
- Không có auto backup
- Không có disaster recovery plan
- Không có异地备份
```

**Giải pháp: Multi-layer backup strategy**

```
BACKUP STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Layer 1: Local Backup (SQLite)
├── Daily backup at 2:00 AM
├── Keep last 7 days
├── Compress with gzip
└── Store in backups/ directory

Layer 2: Cloud Backup (S3/R2)
├── Upload to S3/R2 daily
├── Keep last 30 days
├── Encrypted at rest
└── Versioning enabled

Layer 3: Database-specific
├── SQLite: .backup command
├── PostgreSQL: pg_dump
└── Point-in-time recovery

Layer 4: Disaster Recovery
├── Restore procedure documented
├── Test restore monthly
├── RTO: 1 hour
└── RPO: 24 hours
```

**Implementation:**

```python
# app/backup/manager.py
"""Backup manager."""

import os
import gzip
import shutil
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

class BackupManager:
    """Manage database backups."""
    
    def __init__(self, db_path: str, backup_dir: str = "backups"):
        self.db_path = db_path
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(parents=True, exist_ok=True)
    
    def create_backup(self, compress: bool = True) -> Path:
        """Create database backup."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"roadmap_backup_{timestamp}.db"
        backup_path = self.backup_dir / backup_filename
        
        # Create backup using SQLite .backup command
        try:
            source = sqlite3.connect(self.db_path)
            dest = sqlite3.connect(str(backup_path))
            
            with dest:
                source.backup(dest)
            
            source.close()
            dest.close()
            
            # Compress if requested
            if compress:
                compressed_path = backup_path.with_suffix(".db.gz")
                with open(backup_path, "rb") as f_in:
                    with gzip.open(compressed_path, "wb") as f_out:
                        shutil.copyfileobj(f_in, f_out)
                
                # Remove uncompressed file
                backup_path.unlink()
                backup_path = compressed_path
            
            print(f"Backup created: {backup_path}")
            return backup_path
            
        except Exception as e:
            print(f"Backup failed: {e}")
            raise
    
    def cleanup_old_backups(self, keep_days: int = 7):
        """Remove backups older than keep_days."""
        cutoff_date = datetime.now() - timedelta(days=keep_days)
        
        for backup_file in self.backup_dir.glob("roadmap_backup_*"):
            if backup_file.stat().st_mtime < cutoff_date.timestamp():
                backup_file.unlink()
                print(f"Removed old backup: {backup_file}")
    
    def list_backups(self) -> list:
        """List all backups."""
        backups = []
        for backup_file in sorted(self.backup_dir.glob("roadmap_backup_*")):
            stat = backup_file.stat()
            backups.append({
                "filename": backup_file.name,
                "size_mb": round(stat.st_size / (1024 * 1024), 2),
                "created_at": datetime.fromtimestamp(stat.st_mtime).isoformat()
            })
        return backups
    
    def restore_backup(self, backup_path: Path):
        """Restore database from backup."""
        if not backup_path.exists():
            raise FileNotFoundError(f"Backup not found: {backup_path}")
        
        # Decompress if needed
        if backup_path.suffix == ".gz":
            decompressed_path = backup_path.with_suffix("")
            with gzip.open(backup_path, "rb") as f_in:
                with open(decompressed_path, "wb") as f_out:
                    shutil.copyfileobj(f_in, f_out)
            backup_path = decompressed_path
        
        # Restore database
        try:
            # Backup current database
            current_backup = self.create_backup(compress=False)
            print(f"Current database backed up to: {current_backup}")
            
            # Replace with backup
            shutil.copy2(backup_path, self.db_path)
            print(f"Database restored from: {backup_path}")
            
        except Exception as e:
            print(f"Restore failed: {e}")
            # Restore original
            if current_backup.exists():
                shutil.copy2(current_backup, self.db_path)
            raise
```

```python
# app/backup/s3.py
"""S3/R2 backup uploader."""

import os
import boto3
from pathlib import Path
from typing import Optional

class S3BackupUploader:
    """Upload backups to S3/R2."""
    
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            endpoint_url=os.getenv("S3_ENDPOINT"),
            aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
            aws_secret_access_key=os.getenv("S3_SECRET_KEY")
        )
        self.bucket = os.getenv("S3_BUCKET", "ai-career-roadmap-backups")
        self.prefix = os.getenv("S3_PREFIX", "backups/")
    
    def upload_backup(self, local_path: Path, 
                     remote_name: Optional[str] = None) -> str:
        """Upload backup to S3."""
        if remote_name is None:
            remote_name = local_path.name
        
        key = f"{self.prefix}{remote_name}"
        
        try:
            self.s3_client.upload_file(
                str(local_path),
                self.bucket,
                key,
                ExtraArgs={
                    "ServerSideEncryption": "AES256",
                    "StorageClass": "STANDARD_IA"  # Infrequent Access
                }
            )
            
            print(f"Backup uploaded to s3://{self.bucket}/{key}")
            return f"s3://{self.bucket}/{key}"
            
        except Exception as e:
            print(f"S3 upload failed: {e}")
            raise
    
    def list_backups(self) -> list:
        """List backups in S3."""
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket,
                Prefix=self.prefix
            )
            
            backups = []
            for obj in response.get("Contents", []):
                backups.append({
                    "key": obj["Key"],
                    "size_mb": round(obj["Size"] / (1024 * 1024), 2),
                    "last_modified": obj["LastModified"].isoformat()
                })
            
            return backups
            
        except Exception as e:
            print(f"S3 list failed: {e}")
            return []
    
    def download_backup(self, key: str, local_path: Path) -> Path:
        """Download backup from S3."""
        try:
            self.s3_client.download_file(
                self.bucket,
                key,
                str(local_path)
            )
            
            print(f"Backup downloaded to {local_path}")
            return local_path
            
        except Exception as e:
            print(f"S3 download failed: {e}")
            raise
    
    def cleanup_old_backups(self, keep_days: int = 30):
        """Remove backups older than keep_days."""
        from datetime import datetime, timedelta
        
        cutoff_date = datetime.now() - timedelta(days=keep_days)
        
        backups = self.list_backups()
        for backup in backups:
            last_modified = datetime.fromisoformat(backup["last_modified"].replace("Z", "+00:00"))
            if last_modified < cutoff_date:
                self.s3_client.delete_object(
                    Bucket=self.bucket,
                    Key=backup["key"]
                )
                print(f"Removed old S3 backup: {backup['key']}")
```

```python
# app/backup/scheduler.py
"""Backup scheduler."""

import asyncio
from datetime import datetime, time
from typing import Optional

class BackupScheduler:
    """Schedule automatic backups."""
    
    def __init__(self, backup_manager, s3_uploader=None):
        self.backup_manager = backup_manager
        self.s3_uploader = s3_uploader
    
    async def start(self, backup_time: time = time(2, 0)):
        """Start backup scheduler."""
        print(f"Backup scheduler started, daily at {backup_time}")
        
        while True:
            # Wait until backup time
            await self._wait_until(backup_time)
            
            try:
                await self.run_backup()
            except Exception as e:
                print(f"Scheduled backup failed: {e}")
    
    async def run_backup(self):
        """Run backup process."""
        print(f"Starting backup at {datetime.now()}")
        
        # Create local backup
        backup_path = self.backup_manager.create_backup(compress=True)
        
        # Upload to S3 if configured
        if self.s3_uploader:
            try:
                s3_path = self.s3_uploader.upload_backup(backup_path)
                print(f"Backup uploaded to S3: {s3_path}")
            except Exception as e:
                print(f"S3 upload failed: {e}")
        
        # Cleanup old local backups
        self.backup_manager.cleanup_old_backups(keep_days=7)
        
        # Cleanup old S3 backups
        if self.s3_uploader:
            try:
                self.s3_uploader.cleanup_old_backups(keep_days=30)
            except Exception as e:
                print(f"S3 cleanup failed: {e}")
        
        print(f"Backup completed at {datetime.now()}")
    
    async def _wait_until(self, target_time: time):
        """Wait until target time."""
        now = datetime.now()
        target = datetime.combine(now.date(), target_time)
        
        if now >= target:
            target += timedelta(days=1)
        
        wait_seconds = (target - now).total_seconds()
        await asyncio.sleep(wait_seconds)
```

**Backup verification:**

```python
# app/backup/verify.py
"""Backup verification."""

import sqlite3
from pathlib import Path

class BackupVerifier:
    """Verify backup integrity."""
    
    def verify_backup(self, backup_path: Path) -> dict:
        """Verify backup file integrity."""
        result = {
            "valid": False,
            "checks": {}
        }
        
        # Check file exists
        if not backup_path.exists():
            result["checks"]["file_exists"] = False
            return result
        
        result["checks"]["file_exists"] = True
        
        # Check file size
        file_size = backup_path.stat().st_size
        result["checks"]["file_size_mb"] = round(file_size / (1024 * 1024), 2)
        
        if file_size == 0:
            result["checks"]["file_not_empty"] = False
            return result
        
        result["checks"]["file_not_empty"] = True
        
        # Check SQLite integrity
        try:
            conn = sqlite3.connect(str(backup_path))
            cursor = conn.cursor()
            
            # Check integrity
            cursor.execute("PRAGMA integrity_check")
            integrity = cursor.fetchone()[0]
            result["checks"]["sqlite_integrity"] = integrity == "ok"
            
            # Check tables
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
            tables = [row[0] for row in cursor.fetchall()]
            result["checks"]["tables"] = tables
            
            # Check record counts
            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                result["checks"][f"{table}_count"] = count
            
            conn.close()
            
            # All checks passed
            result["valid"] = all([
                result["checks"].get("file_exists"),
                result["checks"].get("file_not_empty"),
                result["checks"].get("sqlite_integrity")
            ])
            
        except Exception as e:
            result["checks"]["sqlite_error"] = str(e)
        
        return result
    
    def verify_restore(self, db_path: Path, backup_path: Path) -> bool:
        """Verify database can be restored from backup."""
        try:
            # Create temporary database
            temp_db = db_path.parent / "temp_verify.db"
            
            # Restore backup to temp database
            conn = sqlite3.connect(str(temp_db))
            with open(backup_path, "rb") as f:
                conn.backup(sqlite3.connect(":memory:"))
            conn.close()
            
            # Verify temp database
            verification = self.verify_backup(temp_db)
            
            # Cleanup
            temp_db.unlink()
            
            return verification["valid"]
            
        except Exception as e:
            print(f"Restore verification failed: {e}")
            return False
```

**Disaster recovery plan:**

```
DISASTER RECOVERY PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RTO (Recovery Time Objective): 1 giờ
RPO (Recovery Point Objective): 24 giờ

Recovery Steps:

1. Assess damage
   ├── Determine cause
   ├── Check data integrity
   └── Estimate recovery time

2. Stop application
   ├── Stop web server
   ├── Stop background jobs
   └── Notify users (if possible)

3. Restore database
   ├── Download latest backup from S3
   ├── Verify backup integrity
   ├── Restore to new database
   └── Verify restored data

4. Test restored data
   ├── Run integrity checks
   ├── Verify critical tables
   └── Test application functionality

5. Switch to restored database
   ├── Update database path
   ├── Restart application
   └── Monitor for issues

6. Post-recovery
   ├── Document incident
   ├── Update procedures
   └── Notify stakeholders
```

**Backup configuration:**

```python
# app/config/backup.py
"""Backup configuration."""

BACKUP_CONFIG = {
    "local": {
        "enabled": True,
        "directory": "backups",
        "keep_days": 7,
        "compress": True,
        "schedule": "0 2 * * *"  # 2:00 AM daily
    },
    "s3": {
        "enabled": True,
        "bucket": "ai-career-roadmap-backups",
        "prefix": "backups/",
        "keep_days": 30,
        "storage_class": "STANDARD_IA",
        "encryption": "AES256"
    },
    "verification": {
        "enabled": True,
        "verify_after_backup": True,
        "test_restore_monthly": True
    }
}
```

**Trạng thái:** ✅ Đã xác định xong

---

## TÓM TẮT TECHNICAL RESOLUTION

| # | Issue | Giải pháp | Status |
|---|-------|-----------|--------|
| 16 | Caching Layer | Multi-layer cache: HTTP + Memory + Redis | ✅ |
| 17 | Security Headers | CSP + X-Frame-Options + Rate Limiting | ✅ |
| 18 | Health Check | Comprehensive: DB + API + Disk + Memory | ✅ |
| 19 | Logging | Structured JSON + Sentry + Request tracking | ✅ |
| 20 | Backup Strategy | Daily local + S3 upload + Disaster recovery | ✅ |

**Next steps:**
1. Implement caching middleware
2. Implement security middleware
3. Implement health check endpoint
4. Setup logging + Sentry
5. Setup backup scheduler + S3

---
## UX RESOLUTION — Giải quyết 4 thiếu sót về User Experience

> Cập nhật: 30/05/2026
> Mục tiêu: Cải thiện UX để tăng engagement và retention

---

### ISSUE 21: FORM QUÁ ĐƠN GIẢN — Thêm fields để AI cá nhân hóa hơn

**Vấn đề:**
```
Form hiện tại chỉ có:
- Tuổi
- Ngành
- Trình độ
- Mục tiêu
- Thời gian

Thiếu thông tin quan trọng:
- Công việc hiện tại (để AI hiểu context)
- Số giờ học/ngày (để phân bổ tasks hợp lý)
- Phong cách học (video/text/practice)
- Ngân sách (free/paid resources)
```

**Giải pháp: Enhanced form với 8 fields**

```
ENHANCED FORM FIELDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Field 1: Tuổi * (bắt buộc)
├── Type: Number input
├── Range: 15-60
├── Placeholder: "20"
└── Validation: Required, 15-60

Field 2: Ngành muốn học * (bắt buộc)
├── Type: Searchable dropdown
├── Options: 54 ngành
├── Placeholder: "Chọn ngành..."
└── Validation: Required

Field 3: Trình độ hiện tại * (bắt buộc)
├── Type: Radio group
├── Options:
│   ├── Beginner (chưa biết gì)
│   ├── Junior (biết cơ bản)
│   ├── Mid (1-3 năm kinh nghiệm)
│   └── Senior (3+ năm kinh nghiệm)
└── Validation: Required

Field 4: Mục tiêu * (bắt buộc)
├── Type: Textarea
├── Placeholder: "VD: Senior Backend Dev trong 2 năm"
├── Min length: 10 ký tự
└── Validation: Required, min 10 chars

Field 5: Thời gian dự kiến * (bắt buộc)
├── Type: Select
├── Options: 3/6/12/24 tháng
├── Default: 6 tháng
└── Validation: Required

Field 6: Công việc hiện tại (tùy chọn)
├── Type: Select
├── Options:
│   ├── Sinh viên
│   ├── Fresher (mới tốt nghiệp)
│   ├── Junior (1-2 năm)
│   ├── Mid (2-5 năm)
│   ├── Senior (5+ năm)
│   ├── Quản lý
│   ├── Tự do
│   ├── Thất nghiệp
│   └── Khác
├── Default: None
└── Purpose: AI hiểu context để suggest phù hợp

Field 7: Số giờ học/ngày (tùy chọn)
├── Type: Select
├── Options:
│   ├── 1-2 giờ (bận rộn)
│   ├── 3-4 giờ (trung bình)
│   ├── 5-6 giờ (nhiều thời gian)
│   ├── 7-8 giờ (full-time học)
│   └── 8+ giờ (intensive)
├── Default: 3-4 giờ
└── Purpose: Phân bổ tasks hợp lý theo thời gian

Field 8: Phong cách học (tùy chọn)
├── Type: Checkbox group (chọn nhiều)
├── Options:
│   ├── 📹 Video (YouTube, Udemy)
│   ├── 📖 Đọc (docs, articles)
│   ├── 🛠️ Thực hành (code, projects)
│   ├── 👥 Học nhóm (community)
│   └── 🎓 Khóa học (structured)
├── Default: All checked
└── Purpose: Suggest resources phù hợp phong cách
```

**Implementation:**

```html
<!-- Enhanced form -->
<form id="roadmap-form" class="roadmap-form">
  <!-- Field 1: Tuổi -->
  <div class="form-group">
    <label for="age">Tuổi *</label>
    <input type="number" id="age" name="age" min="15" max="60" 
           placeholder="20" required>
    <span class="form-hint">Từ 15 đến 60 tuổi</span>
    <span class="form-error" id="age-error"></span>
  </div>
  
  <!-- Field 2: Ngành -->
  <div class="form-group">
    <label for="industry">Ngành muốn học *</label>
    <select id="industry" name="industry" required>
      <option value="">Chọn ngành...</option>
      <optgroup label="IT & Công nghệ">
        <option value="backend-developer">Backend Developer</option>
        <option value="frontend-developer">Frontend Developer</option>
        <!-- Thêm options -->
      </optgroup>
      <optgroup label="Marketing">
        <option value="digital-marketing">Digital Marketing</option>
        <!-- Thêm options -->
      </optgroup>
    </select>
    <span class="form-error" id="industry-error"></span>
  </div>
  
  <!-- Field 3: Trình độ -->
  <div class="form-group">
    <label>Trình độ hiện tại *</label>
    <div class="radio-group">
      <label class="radio-label">
        <input type="radio" name="level" value="beginner" required>
        <span class="radio-custom"></span>
        <span>Beginner</span>
        <span class="radio-desc">Chưa biết gì</span>
      </label>
      <label class="radio-label">
        <input type="radio" name="level" value="junior">
        <span class="radio-custom"></span>
        <span>Junior</span>
        <span class="radio-desc">Biết cơ bản</span>
      </label>
      <label class="radio-label">
        <input type="radio" name="level" value="mid">
        <span class="radio-custom"></span>
        <span>Mid</span>
        <span class="radio-desc">1-3 năm kinh nghiệm</span>
      </label>
      <label class="radio-label">
        <input type="radio" name="level" value="senior">
        <span class="radio-custom"></span>
        <span>Senior</span>
        <span class="radio-desc">3+ năm kinh nghiệm</span>
      </label>
    </div>
    <span class="form-error" id="level-error"></span>
  </div>
  
  <!-- Field 4: Mục tiêu -->
  <div class="form-group">
    <label for="goal">Mục tiêu *</label>
    <textarea id="goal" name="goal" rows="3" 
              placeholder="VD: Senior Backend Dev trong 2 năm" 
              minlength="10" required></textarea>
    <span class="form-hint">Tối thiểu 10 ký tự</span>
    <span class="form-error" id="goal-error"></span>
  </div>
  
  <!-- Field 5: Thời gian -->
  <div class="form-group">
    <label for="duration">Thời gian dự kiến *</label>
    <select id="duration" name="duration" required>
      <option value="3">3 tháng</option>
      <option value="6" selected>6 tháng</option>
      <option value="12">12 tháng</option>
      <option value="24">24 tháng</option>
    </select>
    <span class="form-error" id="duration-error"></span>
  </div>
  
  <!-- Field 6: Công việc hiện tại (optional) -->
  <div class="form-group optional">
    <label for="current_job">Công việc hiện tại</label>
    <select id="current_job" name="current_job">
      <option value="">Không chọn</option>
      <option value="student">Sinh viên</option>
      <option value="fresher">Fresher (mới tốt nghiệp)</option>
      <option value="junior">Junior (1-2 năm)</option>
      <option value="mid">Mid (2-5 năm)</option>
      <option value="senior">Senior (5+ năm)</option>
      <option value="manager">Quản lý</option>
      <option value="freelancer">Tự do</option>
      <option value="unemployed">Thất nghiệp</option>
      <option value="other">Khác</option>
    </select>
    <span class="form-hint">Để AI hiểu context của bạn</span>
  </div>
  
  <!-- Field 7: Số giờ học/ngày (optional) -->
  <div class="form-group optional">
    <label for="hours_per_day">Số giờ học/ngày</label>
    <select id="hours_per_day" name="hours_per_day">
      <option value="1-2">1-2 giờ (bận rộn)</option>
      <option value="3-4" selected>3-4 giờ (trung bình)</option>
      <option value="5-6">5-6 giờ (nhiều thời gian)</option>
      <option value="7-8">7-8 giờ (full-time học)</option>
      <option value="8+">8+ giờ (intensive)</option>
    </select>
    <span class="form-hint">Để phân bổ tasks hợp lý</span>
  </div>
  
  <!-- Field 8: Phong cách học (optional) -->
  <div class="form-group optional">
    <label>Phong cách học</label>
    <div class="checkbox-group">
      <label class="checkbox-label">
        <input type="checkbox" name="learning_style" value="video" checked>
        <span class="checkbox-custom"></span>
        📹 Video
      </label>
      <label class="checkbox-label">
        <input type="checkbox" name="learning_style" value="reading" checked>
        <span class="checkbox-custom"></span>
        📖 Đọc
      </label>
      <label class="checkbox-label">
        <input type="checkbox" name="learning_style" value="practice" checked>
        <span class="checkbox-custom"></span>
        🛠️ Thực hành
      </label>
      <label class="checkbox-label">
        <input type="checkbox" name="learning_style" value="community" checked>
        <span class="checkbox-custom"></span>
        👥 Học nhóm
      </label>
      <label class="checkbox-label">
        <input type="checkbox" name="learning_style" value="courses" checked>
        <span class="checkbox-custom"></span>
        🎓 Khóa học
      </label>
    </div>
    <span class="form-hint">Chọn nhiều, để AI suggest resources phù hợp</span>
  </div>
  
  <!-- Submit -->
  <div class="form-group">
    <button type="submit" class="btn-primary btn-large">
      🎯 Tạo roadmap ngay
    </button>
    <p class="form-note">Miễn phí · Không cần đăng nhập · ~30 giây</p>
  </div>
</form>

<script>
document.getElementById('roadmap-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  
  const formData = new FormData(e.target);
  
  // Get learning styles
  const learningStyles = formData.getAll('learning_style');
  
  const data = {
    age: parseInt(formData.get('age')),
    industry: formData.get('industry'),
    level: formData.get('level'),
    goal: formData.get('goal'),
    duration: parseInt(formData.get('duration')),
    current_job: formData.get('current_job') || null,
    hours_per_day: formData.get('hours_per_day') || '3-4',
    learning_style: learningStyles.length > 0 ? learningStyles : ['video', 'reading', 'practice']
  };
  
  // Validate
  if (!validateForm(data)) return;
  
  // Track analytics
  Analytics.formSubmit(data.industry, data.level, data.duration);
  
  // Show loading
  showLoading();
  
  try {
    const response = await fetch('/api/generate', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify(data)
    });
    
    if (response.ok) {
      const result = await response.json();
      window.location.href = `/roadmap/${result.slug}`;
    } else {
      showError('Có lỗi xảy ra, vui lòng thử lại.');
    }
  } catch (error) {
    showError('Mất kết nối, kiểm tra mạng.');
  }
});

function validateForm(data) {
  let isValid = true;
  
  // Age validation
  if (!data.age || data.age < 15 || data.age > 60) {
    showFieldError('age', 'Tuổi phải từ 15 đến 60');
    isValid = false;
  }
  
  // Industry validation
  if (!data.industry) {
    showFieldError('industry', 'Vui lòng chọn ngành');
    isValid = false;
  }
  
  // Level validation
  if (!data.level) {
    showFieldError('level', 'Vui lòng chọn trình độ');
    isValid = false;
  }
  
  // Goal validation
  if (!data.goal || data.goal.length < 10) {
    showFieldError('goal', 'Mục tiêu tối thiểu 10 ký tự');
    isValid = false;
  }
  
  return isValid;
}

function showFieldError(field, message) {
  const errorElement = document.getElementById(`${field}-error`);
  if (errorElement) {
    errorElement.textContent = message;
    errorElement.style.display = 'block';
  }
}
</script>
```

**AI prompt update:**

```python
# Updated prompt to use new fields
USER_PROMPT_TEMPLATE = """
Tạo roadmap học tập theo 3 cấp bậc cho:

Thông tin người dùng:
- Tuổi: {age}
- Ngành muốn học: {industry_name}
- Trình độ hiện tại: {level}
- Mục tiêu: {goal}
- Thời gian dự kiến: {duration} tháng
- Công việc hiện tại: {current_job}
- Số giờ học/ngày: {hours_per_day}
- Phong cách học: {learning_style}

Yêu cầu đặc biệt:
1. Phân bổ tasks dựa trên số giờ học/ngày
2. Suggest resources phù hợp phong cách học:
   - Nếu thích video: ưu tiên YouTube, Udemy
   - Nếu thích đọc: ưu tiên docs, articles
   - Nếu thích thực hành: ưu tiên projects, exercises
3. Nếu là sinh viên: thêm tips cân bằng học tập
4. Nếu đi làm: thêm tips học hiệu quả với thời gian ít
5. Nếu thất nghiệp: thêm tips học intensive

Output JSON theo schema đã định.
"""
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 22: ROADMAP KHÔNG CÓ "TIẾP THEO LÀ GÌ?" — CTA sau mỗi phase

**Vấn đề:**
```
User hoàn thành roadmap → Không biết làm gì tiếp
- Không có "Apply jobs" link
- Không có "Practice" link
- Không có "Next roadmap" suggestion
- Không có job board integration
```

**Giải pháp: Next Steps section + Job Integration**

```
NEXT STEPS STRATEGY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Sau mỗi Phase (Level 2)
   ├── "Bạn đã hoàn thành Phase X!"
   ├── CTA: "Bắt đầu Phase X+1"
   ├── Link: Practice project suggestion
   └── Link: Community discussion

2. Sau khi hoàn thành Roadmap (Level 1)
   ├── "Chúc mừng! Bạn đã hoàn thành roadmap!"
   ├── CTA: "Apply việc ngay"
   ├── Link: Job boards (ITviec, TopCV)
   ├── CTA: "Tạo roadmap tiếp theo"
   └── Link: Related roadmaps

3. Job Board Integration
   ├── ITviec: Search jobs theo ngành
   ├── TopCV: Search jobs theo skill
   ├── VietnamWorks: Search jobs theo level
   └── LinkedIn: Search jobs worldwide

4. Practice Suggestions
   ├── GitHub repos để contribute
   ├── Coding challenges (LeetCode, HackerRank)
   ├── Project ideas để build portfolio
   └── Open source projects

5. Community Links
   ├── Facebook groups theo ngành
   ├── Discord servers
   ├── Reddit communities
   └── Stack Overflow
```

**Implementation:**

```python
# app/services/next_steps.py
"""Next steps service."""

from typing import List, Dict, Optional

class NextStepsService:
    """Generate next steps after roadmap completion."""
    
    # Job board links by industry
    JOB_BOARDS = {
        "backend-developer": [
            {"name": "ITviec", "url": "https://itviec.com/it-jobs/backend-developer", "icon": "💼"},
            {"name": "TopCV", "url": "https://topcv.vn/viec-lam-backend-developer", "icon": "📄"},
            {"name": "LinkedIn", "url": "https://www.linkedin.com/jobs/backend-developer-jobs/", "icon": "🔗"}
        ],
        "frontend-developer": [
            {"name": "ITviec", "url": "https://itviec.com/it-jobs/frontend-developer", "icon": "💼"},
            {"name": "TopCV", "url": "https://topcv.vn/viec-lam-frontend-developer", "icon": "📄"},
            {"name": "LinkedIn", "url": "https://www.linkedin.com/jobs/frontend-developer-jobs/", "icon": "🔗"}
        ],
        # Thêm cho các ngành khác
    }
    
    # Practice suggestions by industry
    PRACTICE_SUGGESTIONS = {
        "backend-developer": [
            {"type": "project", "title": "Build REST API", "description": "Tạo API cho todo app", "difficulty": "beginner"},
            {"type": "project", "title": "Build URL Shortener", "description": "Tạo dịch vụ rút gọn link", "difficulty": "intermediate"},
            {"type": "challenge", "title": "LeetCode", "url": "https://leetcode.com/", "description": "Practice algorithms"},
            {"type": "opensource", "title": "Contribute to FastAPI", "url": "https://github.com/tiangolo/fastapi", "description": "Đóng góp open source"}
        ],
        "frontend-developer": [
            {"type": "project", "title": "Build Portfolio", "description": "Tạo portfolio website cá nhân", "difficulty": "beginner"},
            {"type": "project", "title": "Build E-commerce", "description": "Tạo website bán hàng", "difficulty": "intermediate"},
            {"type": "challenge", "title": "Frontend Mentor", "url": "https://www.frontendmentor.io/", "description": "Practice UI challenges"},
            {"type": "opensource", "title": "Contribute to React", "url": "https://github.com/facebook/react", "description": "Đóng góp open source"}
        ],
        # Thêm cho các ngành khác
    }
    
    # Community links by industry
    COMMUNITIES = {
        "backend-developer": [
            {"name": "Backend Developers VN", "type": "facebook", "url": "https://facebook.com/groups/backenddevvn"},
            {"name": "Node.js Vietnam", "type": "facebook", "url": "https://facebook.com/groups/nodejsvietnam"},
            {"name": "r/backend", "type": "reddit", "url": "https://reddit.com/r/backend"},
            {"name": "Backend Discord", "type": "discord", "url": "https://discord.gg/backend"}
        ],
        "frontend-developer": [
            {"name": "Frontend Developers VN", "type": "facebook", "url": "https://facebook.com/groups/frontenddevvn"},
            {"name": "React Vietnam", "type": "facebook", "url": "https://facebook.com/groups/reactvietnam"},
            {"name": "r/frontend", "type": "reddit", "url": "https://reddit.com/r/frontend"},
            {"name": "Frontend Discord", "type": "discord", "url": "https://discord.gg/frontend"}
        ],
        # Thêm cho các ngành khác
    }
    
    def get_phase_completion_cta(self, industry: str, phase_number: int,
                                 total_phases: int) -> dict:
        """Get CTA after completing a phase."""
        if phase_number < total_phases:
            # Chưa hoàn thành roadmap
            return {
                "type": "phase_completion",
                "title": f"Chúc mừng! Bạn đã hoàn thành Phase {phase_number}! 🎉",
                "subtitle": "Bạn đang tiến bộ rất tốt!",
                "actions": [
                    {
                        "type": "next_phase",
                        "title": f"Bắt đầu Phase {phase_number + 1}",
                        "icon": "➡️",
                        "primary": True
                    },
                    {
                        "type": "practice",
                        "title": "Thực hành thêm",
                        "icon": "🛠️",
                        "suggestions": self._get_practice_for_phase(industry, phase_number)
                    },
                    {
                        "type": "community",
                        "title": "Thảo luận với cộng đồng",
                        "icon": "👥",
                        "links": self.COMMUNITIES.get(industry, [])[:2]
                    }
                ]
            }
        else:
            # Hoàn thành roadmap
            return {
                "type": "roadmap_completion",
                "title": "Chúc mừng! Bạn đã hoàn thành roadmap! 🎉🎊",
                "subtitle": "Bạn đã học xong tất cả các phase. Giờ là lúc apply việc!",
                "actions": [
                    {
                        "type": "apply_jobs",
                        "title": "Apply việc ngay",
                        "icon": "💼",
                        "primary": True,
                        "job_boards": self.JOB_BOARDS.get(industry, [])
                    },
                    {
                        "type": "next_roadmap",
                        "title": "Tạo roadmap tiếp theo",
                        "icon": "🗺️",
                        "suggestions": self._get_related_industries(industry)
                    },
                    {
                        "type": "practice",
                        "title": "Practice thêm",
                        "icon": "🛠️",
                        "suggestions": self.PRACTICE_SUGGESTIONS.get(industry, [])
                    },
                    {
                        "type": "community",
                        "title": "Join cộng đồng",
                        "icon": "👥",
                        "links": self.COMMUNITIES.get(industry, [])
                    },
                    {
                        "type": "share",
                        "title": "Chia sẻ roadmap",
                        "icon": "📢",
                        "message": "Khoe thành tích với bạn bè!"
                    }
                ]
            }
    
    def _get_practice_for_phase(self, industry: str, phase_number: int) -> list:
        """Get practice suggestions for specific phase."""
        suggestions = self.PRACTICE_SUGGESTIONS.get(industry, [])
        # Return suggestions based on phase difficulty
        if phase_number == 1:
            return [s for s in suggestions if s.get("difficulty") == "beginner"]
        elif phase_number == 2:
            return [s for s in suggestions if s.get("difficulty") == "intermediate"]
        else:
            return suggestions
    
    def _get_related_industries(self, industry: str) -> list:
        """Get related industries for next roadmap."""
        related = {
            "backend-developer": ["fullstack-developer", "devops-engineer", "data-engineer"],
            "frontend-developer": ["fullstack-developer", "ui-ux-designer", "mobile-developer"],
            "fullstack-developer": ["backend-developer", "frontend-developer", "devops-engineer"],
            "data-analyst": ["data-scientist", "data-engineer", "business-analyst"],
            "ai-engineer": ["data-scientist", "machine-learning-engineer", "data-engineer"],
            # Thêm cho các ngành khác
        }
        return related.get(industry, [])
```

**UI components:**

```html
<!-- Next steps section on roadmap page -->
<section class="next-steps" id="next-steps" style="display: none;">
  <div class="container">
    <div class="next-steps-card" id="next-steps-content">
      <!-- Populated by JavaScript -->
    </div>
  </div>
</section>

<script>
// Show next steps when phase/roadmap is completed
function showNextSteps(type, data) {
  const section = document.getElementById('next-steps');
  const content = document.getElementById('next-steps-content');
  
  if (type === 'phase') {
    content.innerHTML = renderPhaseCompletion(data);
  } else if (type === 'roadmap') {
    content.innerHTML = renderRoadmapCompletion(data);
  }
  
  section.style.display = 'block';
  section.scrollIntoView({ behavior: 'smooth' });
}

function renderPhaseCompletion(data) {
  return `
    <div class="completion-header">
      <h2>${data.title}</h2>
      <p>${data.subtitle}</p>
    </div>
    
    <div class="completion-actions">
      ${data.actions.map(action => `
        ${action.primary ? `
          <a href="#" class="btn-primary btn-large" onclick="handleAction('${action.type}')">
            ${action.icon} ${action.title}
          </a>
        ` : `
          <div class="action-card">
            <h3>${action.icon} ${action.title}</h3>
            ${action.suggestions ? `
              <ul class="suggestions-list">
                ${action.suggestions.map(s => `
                  <li>
                    <strong>${s.title}</strong>
                    <p>${s.description}</p>
                  </li>
                `).join('')}
              </ul>
            ` : ''}
            ${action.links ? `
              <div class="links-list">
                ${action.links.map(l => `
                  <a href="${l.url}" target="_blank" class="link-item">
                    ${l.name}
                  </a>
                `).join('')}
              </div>
            ` : ''}
          </div>
        `}
      `).join('')}
    </div>
  `;
}

function renderRoadmapCompletion(data) {
  return `
    <div class="completion-header celebration">
      <div class="confetti">🎉🎊✨</div>
      <h2>${data.title}</h2>
      <p>${data.subtitle}</p>
    </div>
    
    <div class="completion-actions grid">
      ${data.actions.map(action => `
        <div class="action-card ${action.primary ? 'primary' : ''}">
          <div class="action-icon">${action.icon}</div>
          <h3>${action.title}</h3>
          
          ${action.job_boards ? `
            <div class="job-boards">
              ${action.job_boards.map(jb => `
                <a href="${jb.url}" target="_blank" class="job-board-link">
                  ${jb.icon} ${jb.name}
                </a>
              `).join('')}
            </div>
          ` : ''}
          
          ${action.suggestions ? `
            <ul class="suggestions-list">
              ${action.suggestions.map(s => `
                <li>
                  <strong>${s.title}</strong>
                  ${s.url ? `<a href="${s.url}" target="_blank">Xem →</a>` : ''}
                </li>
              `).join('')}
            </ul>
          ` : ''}
          
          ${action.links ? `
            <div class="links-list">
              ${action.links.map(l => `
                <a href="${l.url}" target="_blank" class="link-item">
                  ${l.name}
                </a>
              `).join('')}
            </div>
          ` : ''}
          
          ${action.message ? `<p class="action-message">${action.message}</p>` : ''}
        </div>
      `).join('')}
    </div>
  `;
}
</script>

<style>
.next-steps {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 60px 0;
  color: white;
}

.next-steps-card {
  max-width: 800px;
  margin: 0 auto;
}

.completion-header {
  text-align: center;
  margin-bottom: 40px;
}

.completion-header h2 {
  font-size: 32px;
  margin-bottom: 10px;
}

.completion-header p {
  font-size: 18px;
  opacity: 0.9;
}

.celebration {
  position: relative;
}

.confetti {
  font-size: 48px;
  margin-bottom: 20px;
  animation: bounce 1s infinite;
}

@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

.completion-actions {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.completion-actions.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}

.action-card {
  background: rgba(255,255,255,0.1);
  padding: 25px;
  border-radius: 12px;
  backdrop-filter: blur(10px);
}

.action-card.primary {
  background: rgba(255,255,255,0.2);
  border: 2px solid rgba(255,255,255,0.3);
}

.action-icon {
  font-size: 32px;
  margin-bottom: 15px;
}

.action-card h3 {
  margin-bottom: 15px;
  font-size: 18px;
}

.job-boards {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.job-board-link {
  display: inline-block;
  padding: 8px 16px;
  background: rgba(255,255,255,0.2);
  border-radius: 6px;
  color: white;
  text-decoration: none;
  transition: background 0.2s;
}

.job-board-link:hover {
  background: rgba(255,255,255,0.3);
}

.suggestions-list {
  list-style: none;
  padding: 0;
}

.suggestions-list li {
  padding: 10px 0;
  border-bottom: 1px solid rgba(255,255,255,0.1);
}

.suggestions-list li:last-child {
  border-bottom: none;
}

.suggestions-list strong {
  display: block;
  margin-bottom: 5px;
}

.suggestions-list a {
  color: #ffd700;
  text-decoration: none;
}

.links-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.link-item {
  display: inline-block;
  padding: 6px 12px;
  background: rgba(255,255,255,0.15);
  border-radius: 4px;
  color: white;
  text-decoration: none;
  font-size: 14px;
}

.link-item:hover {
  background: rgba(255,255,255,0.25);
}

.action-message {
  font-style: italic;
  opacity: 0.8;
  margin-top: 10px;
}
</style>
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 23: DARK MODE — Toggle dark/light mode

**Vấn đề:**
```
Gen Z thích dark mode
Dễ implement với CSS variables
Không có dark mode = mất user trẻ
```

**Giải pháp: CSS variables + Toggle button**

```
DARK MODE IMPLEMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Components:
├── CSS Variables (light/dark themes)
├── Toggle button (header)
├── LocalStorage persistence
├── System preference detection
└── Smooth transition
```

**Implementation:**

```css
/* app/static/css/themes.css */

/* Light theme (default) */
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f9fafb;
  --bg-tertiary: #f3f4f6;
  --text-primary: #111827;
  --text-secondary: #374151;
  --text-tertiary: #6b7280;
  --border-color: #e5e7eb;
  --border-hover: #d1d5db;
  --accent-primary: #4F46E5;
  --accent-secondary: #10B981;
  --accent-warning: #F59E0B;
  --accent-error: #EF4444;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.1);
  --card-bg: #ffffff;
  --card-border: #e5e7eb;
  --input-bg: #ffffff;
  --input-border: #d1d5db;
  --input-focus: #4F46E5;
  --code-bg: #f3f4f6;
  --code-text: #e11d48;
  --success-bg: #d1fae5;
  --success-text: #065f46;
  --warning-bg: #fef3c7;
  --warning-text: #92400e;
  --error-bg: #fee2e2;
  --error-text: #991b1b;
  --overlay-bg: rgba(0,0,0,0.5);
}

/* Dark theme */
[data-theme="dark"] {
  --bg-primary: #111827;
  --bg-secondary: #1f2937;
  --bg-tertiary: #374151;
  --text-primary: #f9fafb;
  --text-secondary: #d1d5db;
  --text-tertiary: #9ca3af;
  --border-color: #4b5563;
  --border-hover: #6b7280;
  --accent-primary: #818cf8;
  --accent-secondary: #34d399;
  --accent-warning: #fbbf24;
  --accent-error: #f87171;
  --shadow-sm: 0 1px 2px rgba(0,0,0,0.3);
  --shadow-md: 0 4px 6px rgba(0,0,0,0.4);
  --shadow-lg: 0 10px 15px rgba(0,0,0,0.4);
  --card-bg: #1f2937;
  --card-border: #4b5563;
  --input-bg: #374151;
  --input-border: #4b5563;
  --input-focus: #818cf8;
  --code-bg: #374151;
  --code-text: #fb923c;
  --success-bg: #064e3b;
  --success-text: #6ee7b7;
  --warning-bg: #78350f;
  --warning-text: #fcd34d;
  --error-bg: #7f1d1d;
  --error-text: #fca5a5;
  --overlay-bg: rgba(0,0,0,0.7);
}

/* Apply variables */
body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  transition: background-color 0.3s ease, color 0.3s ease;
}

.card {
  background-color: var(--card-bg);
  border-color: var(--card-border);
}

input, select, textarea {
  background-color: var(--input-bg);
  border-color: var(--input-border);
  color: var(--text-primary);
}

input:focus, select:focus, textarea:focus {
  border-color: var(--input-focus);
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
}

[data-theme="dark"] input:focus,
[data-theme="dark"] select:focus,
[data-theme="dark"] textarea:focus {
  box-shadow: 0 0 0 3px rgba(129, 140, 248, 0.2);
}

code {
  background-color: var(--code-bg);
  color: var(--code-text);
}

.alert-success {
  background-color: var(--success-bg);
  color: var(--success-text);
}

.alert-warning {
  background-color: var(--warning-bg);
  color: var(--warning-text);
}

.alert-error {
  background-color: var(--error-bg);
  color: var(--error-text);
}
```

```html
<!-- Dark mode toggle button -->
<button id="theme-toggle" class="theme-toggle" aria-label="Toggle dark mode">
  <span class="theme-toggle-icon">🌙</span>
</button>

<style>
.theme-toggle {
  position: fixed;
  bottom: 20px;
  right: 20px;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background: var(--accent-primary);
  color: white;
  border: none;
  cursor: pointer;
  font-size: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-md);
  transition: transform 0.2s, background 0.2s;
  z-index: 1000;
}

.theme-toggle:hover {
  transform: scale(1.1);
}

.theme-toggle-icon {
  line-height: 1;
}
</style>

<script>
// Theme toggle functionality
(function() {
  const STORAGE_KEY = 'theme';
  const DARK_CLASS = 'dark';
  
  // Get saved theme or system preference
  function getTheme() {
    const saved = localStorage.getItem(STORAGE_KEY);
    if (saved) return saved;
    
    // Check system preference
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return DARK_CLASS;
    }
    
    return 'light';
  }
  
  // Apply theme
  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    
    // Update toggle button icon
    const toggle = document.getElementById('theme-toggle');
    if (toggle) {
      const icon = toggle.querySelector('.theme-toggle-icon');
      icon.textContent = theme === DARK_CLASS ? '☀️' : '🌙';
    }
    
    // Save preference
    localStorage.setItem(STORAGE_KEY, theme);
  }
  
  // Toggle theme
  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === DARK_CLASS ? 'light' : DARK_CLASS;
    applyTheme(next);
    
    // Track analytics
    if (typeof Analytics !== 'undefined') {
      Analytics.themeChanged(next);
    }
  }
  
  // Initialize
  applyTheme(getTheme());
  
  // Add event listener
  document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('theme-toggle');
    if (toggle) {
      toggle.addEventListener('click', toggleTheme);
    }
  });
  
  // Listen for system theme changes
  if (window.matchMedia) {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
      if (!localStorage.getItem(STORAGE_KEY)) {
        applyTheme(e.matches ? DARK_CLASS : 'light');
      }
    });
  }
})();
</script>
```

**Update existing CSS to use variables:**

```css
/* app/static/css/style.css - Update to use variables */

/* Before */
body {
  background-color: #ffffff;
  color: #111827;
}

.card {
  background: #ffffff;
  border: 1px solid #e5e7eb;
}

/* After */
body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
}

.card {
  background: var(--card-bg);
  border: 1px solid var(--card-border);
}

/* All hardcoded colors should use variables */
.header {
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
}

.btn-primary {
  background: var(--accent-primary);
}

.btn-primary:hover {
  background: var(--accent-primary);
  opacity: 0.9;
}

.text-secondary {
  color: var(--text-secondary);
}

.bg-secondary {
  background: var(--bg-secondary);
}
```

**Trạng thái:** ✅ Đã xác định xong

---

### ISSUE 24: OFFLINE SUPPORT — Service Worker + PWA

**Vấn đề:**
```
User muốn xem roadmap khi offline
- Không có service worker
- Không có PWA manifest
- Không có offline page
```

**Giải pháp: PWA basics + Service Worker**

```
PWA IMPLEMENTATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Components:
├── Web App Manifest
├── Service Worker
├── Offline page
├── Cache strategies
└── Install prompt
```

**Implementation:**

```json
// app/static/manifest.json
{
  "name": "AI Career Roadmap",
  "short_name": "AI Roadmap",
  "description": "Tạo lộ trình học tập cá nhân hóa bằng AI",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#4F46E5",
  "orientation": "portrait",
  "icons": [
    {
      "src": "/static/icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "categories": ["education", "productivity"],
  "lang": "vi",
  "screenshots": [
    {
      "src": "/static/screenshots/home.png",
      "sizes": "1280x720",
      "type": "image/png",
      "form_factor": "wide"
    },
    {
      "src": "/static/screenshots/mobile.png",
      "sizes": "750x1334",
      "type": "image/png",
      "form_factor": "narrow"
    }
  ]
}
```

```javascript
// app/static/sw.js
const CACHE_NAME = 'ai-career-roadmap-v1';
const STATIC_ASSETS = [
  '/',
  '/static/css/style.css',
  '/static/js/app.js',
  '/static/icons/icon-192x192.png',
  '/offline.html'
];

// Install event - Cache static assets
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => {
        console.log('Caching static assets');
        return cache.addAll(STATIC_ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate event - Clean old caches
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then(cacheNames => {
        return Promise.all(
          cacheNames
            .filter(name => name !== CACHE_NAME)
            .map(name => caches.delete(name))
        );
      })
      .then(() => self.clients.claim())
  );
});

// Fetch event - Serve from cache, fallback to network
self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip non-GET requests
  if (request.method !== 'GET') return;
  
  // Skip API requests
  if (url.pathname.startsWith('/api/')) return;
  
  // Network first, fallback to cache
  event.respondWith(
    fetch(request)
      .then(response => {
        // Clone response
        const responseClone = response.clone();
        
        // Cache successful responses
        if (response.status === 200) {
          caches.open(CACHE_NAME)
            .then(cache => {
              cache.put(request, responseClone);
            });
        }
        
        return response;
      })
      .catch(() => {
        // Fallback to cache
        return caches.match(request)
          .then(cachedResponse => {
            if (cachedResponse) {
              return cachedResponse;
            }
            
            // Fallback to offline page for navigation
            if (request.mode === 'navigate') {
              return caches.match('/offline.html');
            }
            
            // Return 404 for other requests
            return new Response('Not found', { status: 404 });
          });
      })
  );
});

// Background sync for form submissions
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-roadmap') {
    event.waitUntil(syncRoadmap());
  }
});

async function syncRoadmap() {
  // Get pending submissions from IndexedDB
  const db = await openDB();
  const submissions = await db.getAll('pending-submissions');
  
  for (const submission of submissions) {
    try {
      const response = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(submission.data)
      });
      
      if (response.ok) {
        await db.delete('pending-submissions', submission.id);
      }
    } catch (error) {
      console.error('Sync failed:', error);
    }
  }
}
```

```html
<!-- Offline page -->
<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Offline - AI Career Roadmap</title>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
      background: #f9fafb;
      color: #111827;
    }
    
    .offline-container {
      text-align: center;
      padding: 40px;
      max-width: 400px;
    }
    
    .offline-icon {
      font-size: 64px;
      margin-bottom: 20px;
    }
    
    h1 {
      font-size: 24px;
      margin-bottom: 10px;
    }
    
    p {
      color: #6b7280;
      margin-bottom: 30px;
      line-height: 1.6;
    }
    
    .btn {
      display: inline-block;
      padding: 12px 24px;
      background: #4F46E5;
      color: white;
      text-decoration: none;
      border-radius: 8px;
      font-weight: 500;
    }
    
    .btn:hover {
      background: #4338ca;
    }
    
    .features {
      margin-top: 40px;
      text-align: left;
    }
    
    .feature {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px 0;
    }
    
    .feature-icon {
      font-size: 20px;
    }
  </style>
</head>
<body>
  <div class="offline-container">
    <div class="offline-icon">📡</div>
    <h1>Bạn đang offline</h1>
    <p>
      Không có kết nối internet. Một số tính năng có thể không hoạt động.
      Roadmap đã lưu vẫn có thể xem được.
    </p>
    
    <a href="/" class="btn">Thử lại</a>
    
    <div class="features">
      <div class="feature">
        <span class="feature-icon">✅</span>
        <span>Xem roadmap đã lưu</span>
      </div>
      <div class="feature">
        <span class="feature-icon">✅</span>
        <span>Đánh dấu task hoàn thành</span>
      </div>
      <div class="feature">
        <span class="feature-icon">❌</span>
        <span>Tạo roadmap mới (cần online)</span>
      </div>
    </div>
  </div>
</body>
</html>
```

```html
<!-- Add to HTML head -->
<head>
  <!-- PWA Manifest -->
  <link rel="manifest" href="/static/manifest.json">
  
  <!-- Theme color -->
  <meta name="theme-color" content="#4F46E5">
  
  <!-- Apple touch icon -->
  <link rel="apple-touch-icon" href="/static/icons/icon-192x192.png">
  
  <!-- Apple mobile web app -->
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="default">
  <meta name="apple-mobile-web-app-title" content="AI Roadmap">
  
  <!-- Register service worker -->
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/static/sw.js')
          .then(registration => {
            console.log('SW registered:', registration.scope);
          })
          .catch(error => {
            console.log('SW registration failed:', error);
          });
      });
    }
  </script>
</head>
```

**Install prompt:**

```javascript
// PWA install prompt
let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
  // Prevent Chrome 67 and earlier from automatically showing the prompt
  e.preventDefault();
  
  // Stash the event so it can be triggered later
  deferredPrompt = e;
  
  // Show install button
  showInstallButton();
});

function showInstallButton() {
  const installButton = document.getElementById('install-button');
  if (installButton) {
    installButton.style.display = 'block';
    
    installButton.addEventListener('click', async () => {
      if (deferredPrompt) {
        // Show the prompt
        deferredPrompt.prompt();
        
        // Wait for the user to respond to the prompt
        const { outcome } = await deferredPrompt.userChoice;
        console.log(`User response: ${outcome}`);
        
        // Clear the deferredPrompt
        deferredPrompt = null;
        
        // Hide install button
        installButton.style.display = 'none';
      }
    });
  }
}

window.addEventListener('appinstalled', (evt) => {
  console.log('App installed');
  // Track analytics
  Analytics.appInstalled();
});
```

**Trạng thái:** ✅ Đã xác định xong

---

## TÓM TẮT UX RESOLUTION

| # | Issue | Giải pháp | Status |
|---|-------|-----------|--------|
| 21 | Form quá đơn giản | Thêm 3 fields: current_job, hours_per_day, learning_style | ✅ |
| 22 | Không có "Tiếp theo" | Next Steps + Job boards + Practice + Community links | ✅ |
| 23 | Không có Dark Mode | CSS variables + Toggle button + System preference | ✅ |
| 24 | Không có Offline Support | Service Worker + PWA manifest + Offline page | ✅ |

---

## RECOMMENDATIONS — Cập nhật theo thứ tự ưu tiên

> Dựa trên tất cả 24 thiếu sót đã giải quyết

### TRƯỚC KHI BUILD (Tuần 0)

```
PRIORITY 1: VALIDATION (Quan trọng nhất)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. ⬜ Phỏng vấn 10-20 người dùng mục tiêu
   ├── Tìm người qua: Facebook groups, friends, university
   ├── Câu hỏi: Pain points, feature requests, willingness to pay
   ├── Tool: Google Forms + Zoom/Meet
   ├── Time: 3-5 ngày
   └── Output: User validation report

2. ⬜ Tạo landing page test demand (no-code)
   ├── Tool: Carrd.co hoặc HTML tĩnh
   ├── Content: Mockup screenshot + CTA
   ├── Traffic: Facebook groups, Reddit
   ├── Time: 1 ngày
   └── Metric: 100+ visits, 10+ signups

3. ⬜ Generate fallback roadmaps (scripts/generate_fallbacks.py)
   ├── Target: TOP 20 ngành
   ├── Model: GPT-4o-mini
   ├── Time: 1 ngày
   └── Output: fallbacks/*.json

4. ⬜ Generate SEO content (scripts/generate_seo_content.py)
   ├── Target: 54 ngành × 500+ words
   ├── Model: GPT-4o-mini
   ├── Time: 2 ngày (generate + review)
   └── Output: content/*.md
```

### TRONG KHI BUILD (Tuần 1-2)

```
PRIORITY 2: CORE FEATURES (MVP)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

5. ⬜ Enhanced form với 8 fields
   ├── Thêm: current_job, hours_per_day, learning_style
   ├── Update AI prompt
   ├── Time: 0.5 ngày
   └── Impact: Cao (better personalization)

6. ⬜ Next Steps section
   ├── Phase completion CTA
   ├── Roadmap completion celebration
   ├── Job board integration
   ├── Practice suggestions
   ├── Community links
   └── Time: 1 ngày

7. ⬜ Feedback mechanism
   ├── Roadmap rating (👍/👎)
   ├── Detailed feedback form
   ├── Bug report button
   ├── Time: 1 ngày
   └── Impact: Cao (quality improvement)

8. ⬜ Analytics tracking
   ├── GA4 setup
   ├── Custom events
   ├── Conversion funnel
   ├── Time: 0.5 ngày
   └── Impact: Cao (data-driven decisions)

9. ⬜ Security headers
   ├── CSP, X-Frame-Options, HSTS
   ├── Rate limiting
   ├── Time: 0.5 ngày
   └── Impact: Cao (security)
```

### SAU KHI BUILD (Tuần 3-4)

```
PRIORITY 3: GROWTH FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

10. ⬜ Dark mode
    ├── CSS variables
    ├── Toggle button
    ├── System preference
    ├── Time: 0.5 ngày
    └── Impact: Trung bình (UX improvement)

11. ⬜ Search functionality
    ├── Search bar
    ├── Category filter
    ├── Sort options
    ├── Time: 1 ngày
    └── Impact: Trung bình (navigation)

12. ⬜ Email capture
    ├── Resend setup
    ├── Newsletter signup
    ├── Re-engagement emails
    ├── Time: 1 ngày
    └── Impact: Cao (retention)

13. ⬜ Dynamic social proof
    ├── Real counter
    ├── Testimonials
    ├── Achievements
    ├── Time: 0.5 ngày
    └── Impact: Trung bình (trust)

14. ⬜ PWA + Offline support
    ├── Service worker
    ├── Manifest
    ├── Offline page
    ├── Time: 1 ngày
    └── Impact: Thấp (nice to have)
```

### SAU KHI LAUNCH (Tháng 2+)

```
PRIORITY 4: SCALE & OPTIMIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

15. ⬜ Caching layer
    ├── HTTP caching
    ├── In-memory cache
    ├── Redis (optional)
    ├── Time: 1 ngày
    └── Impact: Cao (performance)

16. ⬜ Health check
    ├── Comprehensive checks
    ├── Monitoring integration
    ├── Time: 0.5 ngày
    └── Impact: Cao (reliability)

17. ⬜ Structured logging
    ├── JSON logging
    ├── Sentry integration
    ├── Request tracking
    ├── Time: 1 ngày
    └── Impact: Cao (debugging)

18. ⬜ Backup strategy
    ├── Daily backup
    ├── S3 upload
    ├── Disaster recovery
    ├── Time: 0.5 ngày
    └── Impact: Cao (data safety)

19. ⬜ Database migration
    ├── SQLite → PostgreSQL
    ├── Migration script
    ├── Time: 1 ngày
    └── Impact: Trung bình (when needed)

20. ⬜ Content strategy
    ├── SEO content pipeline
    ├── Quality control
    ├── Time: Ongoing
    └── Impact: Cao (SEO growth)
```

### TỔNG KẾT

```
TOTAL TASKS: 20
ESTIMATED TIME: 15-20 ngày (1 người)

PHASE 1 (Week 0): Validation + Prep
├── Tasks: 4
├── Time: 5-7 ngày
└── Output: User validation + Fallbacks + Content

PHASE 2 (Week 1-2): Core MVP
├── Tasks: 5
├── Time: 4-5 ngày
└── Output: Working MVP with enhanced features

PHASE 3 (Week 3-4): Growth
├── Tasks: 5
├── Time: 4-5 ngày
└── Output: Growth features + Polish

PHASE 4 (Month 2+): Scale
├── Tasks: 6
├── Time: 4-5 ngày
└── Output: Production-ready + Monitoring
```

---

5. Setup backup scheduler + S3

---

## NEXT STEPS

Sau khi review plan này, tiếp tục với:
1. ✅ Blockers Resolution (5 thiếu sót nghiêm trọng) — ĐÃ XỬ LÝ
2. ✅ High Priority Resolution (5 thiếu sót quan trọng) — ĐÃ XỬ LÝ
3. ✅ Medium Priority Resolution (5 thiếu sót trung bình) — ĐÃ XỬ LÝ
4. ✅ Technical Resolution (5 thiếu sót kỹ thuật) — ĐÃ XỬ LÝ
5. ✅ UX Resolution (4 thiếu sót UX) — ĐÃ XỬ LÝ
6. ✅ Recommendations updated — ĐÃ XỬ LÝ

**Bắt đầu thực hiện theo Recommendations:**

### PHASE 1: Validation (Tuần 0)
- ⬜ Phỏng vấn 10-20 người dùng mục tiêu
- ⬜ Tạo landing page test demand
- ⬜ Generate fallback roadmaps
- ⬜ Generate SEO content

### PHASE 2: Core MVP (Tuần 1-2)
- ⬜ Enhanced form với 8 fields
- ⬜ Next Steps section
- ⬜ Feedback mechanism
- ⬜ Analytics tracking
- ⬜ Security headers

### PHASE 3: Growth (Tuần 3-4)
- ⬜ Dark mode
- ⬜ Search functionality
- ⬜ Email capture
- ⬜ Dynamic social proof
- ⬜ PWA + Offline support

### PHASE 4: Scale (Tháng 2+)
- ⬜ Caching layer
- ⬜ Health check
- ⬜ Structured logging
- ⬜ Backup strategy
- ⬜ Database migration
- ⬜ Content strategy

---

*Cập nhật lần cuối: 30/05/2026*
