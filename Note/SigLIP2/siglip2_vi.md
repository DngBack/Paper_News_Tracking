# Giới thiệu SigLIP 2

Bài báo giới thiệu **SigLIP 2**, một họ mới của các bộ mã hóa ngôn ngữ-thị giác đa ngôn ngữ, được phát triển dựa trên mô hình SigLIP ban đầu. SigLIP 2 tích hợp nhiều kỹ thuật phát triển độc lập vào một quy trình huấn luyện thống nhất, bao gồm:

- Tiền huấn luyện dựa trên tạo chú thích
- Các tổn thất tự giám sát (tự chưng cất, dự đoán mặt nạ)
- Quản lý dữ liệu trực tuyến

## 🔹 Những điểm nổi bật của SigLIP 2

### ✅ Bộ mã hóa ngôn ngữ-thị giác đa ngôn ngữ mạnh mẽ

Hiệu suất vượt trội trên các tác vụ ngôn ngữ-thị giác tập trung vào tiếng Anh, đồng thời đạt kết quả xuất sắc trên các tiêu chuẩn đánh giá đa ngôn ngữ chỉ với một mô hình duy nhất.

### ✅ Đặc trưng dày đặc

Tích hợp các tổn thất tự giám sát và tổn thất dựa trên bộ giải mã, giúp cải thiện các đặc trưng dày đặc và hiệu suất trên các bài toán định vị.

### ✅ Tương thích ngược

Được thiết kế để **tương thích ngược** với SigLIP bằng cách sử dụng cùng một kiến trúc.

### ✅ Tỷ lệ khung hình gốc và độ phân giải linh hoạt

Bao gồm một biến thể **NaFlex** hỗ trợ nhiều độ phân giải và bảo toàn tỷ lệ khung hình gốc của hình ảnh.

### ✅ Mô hình nhỏ mạnh mẽ

Tối ưu hóa hiệu suất của các mô hình nhỏ hơn bằng cách sử dụng các kỹ thuật chưng cất thông qua quản lý dữ liệu chủ động.

## 🚀 Hiệu suất và quy mô

Các mô hình **SigLIP 2** vượt trội so với các phiên bản **SigLIP** trước đó ở mọi quy mô, đặc biệt là trong các năng lực cốt lõi như:

- **Phân loại zero-shot**
- **Truy xuất hình ảnh-văn bản**
- **Hiệu suất chuyển giao cho các mô hình Ngôn ngữ-Thị giác (VLMs)**

Quy trình huấn luyện mới giúp **cải thiện các nhiệm vụ định vị và dự đoán dày đặc**. Các mô hình được huấn luyện trên một tập dữ liệu đa dạng hơn, có áp dụng **kỹ thuật giảm thiểu sai lệch**, giúp cải thiện khả năng hiểu đa ngôn ngữ và nâng cao tính công bằng.

## 📌 Kích thước mô hình

Các điểm kiểm tra mô hình được phát hành với **bốn kích thước**:

| Mô hình    | Số tham số |
| ---------- | ---------- |
| **ViT-B**  | 86M        |
| **L**      | 303M       |
| **So400m** | 400M       |
| **g**      | 1B         |
