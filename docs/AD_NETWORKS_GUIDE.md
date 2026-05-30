# HƯỚNG DẪN ĐĂNG KÝ AD NETWORKS CHO AI CAREER ROADMAP

## 1. PROPELLERADS (Khuyến nghị #1)

### Bước 1: Đăng ký
1. Vào: https://propellerads.com/publishers/
2. Click "Sign Up" hoặc "Join Now"
3. Điền:
   - Email: ngovan960@gmail.com
   - Password: (tạo password mạnh)
   - Website: https://roadmap-ai.onrender.com
   - Country: Vietnam
4. Click "Register"
5. Verify email (check inbox)

### Bước 2: Add Site
1. Login vào dashboard
2. Click "Sites" → "Add Site"
3. Nhập URL: https://roadmap-ai.onrender.com
4. Chọn Category: Education / Learning
5. Click "Add"
6. Verify site (thêm meta tag vào <head>)

### Bước 3: Tạo Ad Zone
1. Click vào site vừa add
2. Click "New Ad Zone"
3. Chọn format:
   - "In-Page Push" (recommended - clean ads)
   - Hoặc "OnClick" (popunder - RPM cao hơn)
4. Copy ad code

### Bước 4: Chèn code vào website
1. Mở backend/templates/base.html
2. Chèn code trước </head> hoặc </body>
3. Deploy lại lên Render

### Bước 5: Kiếm tiền!
- Dashboard xem earnings
- Min payout: $5
- Payment: PayPal, Wire, USDT

---

## 2. ADSTERRA (Khuyến nghị #2)

### Bước 1: Đăng ký
1. Vào: https://adsterra.com/
2. Click "Sign Up" → "Publisher"
3. Điền:
   - Email
   - Password
   - Website: https://roadmap-ai.onrender.com
   - Category: Education
4. Click "Register"
5. Verify email

### Bước 2: Add Site
1. Dashboard → "Sites" → "Add Site"
2. Nhập URL
3. Chọn ad format
4. Wait approve (24h)

### Bước 3: Tạo Ad Unit
1. Click "Ad Units" → "Create"
2. Chọn: "Social Bar" (best for clean look)
3. Copy code
4. Chèn vào website

### Bước 4: Verify
1. Quay lại Adsterra dashboard
2. Click "Verify" trên site
3. Ads sẽ hiện ngay

---

## 3. MONETAG (Alternative)

### Bước 1: Đăng ký
1. Vào: https://monetag.com/
2. Click "Sign Up"
3. Điền thông tin
4. Verify email

### Bước 2: Add Site
1. Dashboard → "Sites"
2. Add: https://roadmap-ai.onrender.com
3. Choose format: "SmartLink" hoặc "Push"

### Bước 3: Get Code
1. Copy ad code
2. Chèn vào website
3. Deploy

---

## SO SÁNH ĐỂ CHỌN

| Feature | PropellerAds | Adsterra | Monetag |
|---------|--------------|----------|---------|
| Approval | Instant | 24h | Instant |
| Min Payout | $5 | $5 | $5 |
| Payment | PayPal, USDT | PayPal, USDT | PayPal, USDT |
| Best Format | In-Page Push | Social Bar | SmartLink |
| Anti-AdBlock | ✅ | ✅ | ✅ |
| RPM (VN) | $0.5-2 | $0.5-3 | $0.5-3 |

**KHUYẾN NGHỊ:** Bắt đầu với PropellerAds (instant approval)

---

## CÁCH CHÈN CODE VÀO WEBSITE

### File: backend/templates/base.html

Thêm trước </head>:

```html
<!-- PropellerAds In-Page Push -->
<script>
  (function(d,z,s){s.src='//'+d+'/400/'+z;try{(document.body||document.documentElement).appendChild(s)}catch(e){}})('domainname.com',5432836,document.createElement('script'));
</script>
```

Hoặc Adsterra Social Bar:

```html
<!-- Adsterra Social Bar -->
<script>
  (function(d, id) {
    if (d.getElementById(id)) return;
    var s = d.createElement('script');
    s.id = id;
    s.src = 'https://js.adsterra.com/adsterra.js';
    (document.head || document.body).appendChild(s);
  })(document, 'adsterra-script');
</script>
```
