### s1: Phương pháp mở rộng tính toán đơn giản trong quá trình kiểm tra

Bài báo _"s1: Simple Test-Time Scaling"_ giới thiệu một phương pháp cải thiện **khả năng suy luận của các mô hình ngôn ngữ (LMs)** bằng cách **tăng cường lượng tính toán tại thời điểm kiểm tra**. Các tác giả, **Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, và Emmanuel Candès**, tập trung vào việc đạt được **hiệu suất suy luận mạnh mẽ** và **hành vi mở rộng hợp lý trong quá trình kiểm tra**.

Ý tưởng cốt lõi là **huấn luyện mô hình ngôn ngữ** trên một **tập dữ liệu nhỏ nhưng được chọn lọc cẩn thận**, sau đó sử dụng một kỹ thuật gọi là **"ép ngân sách" (budget forcing)** để kiểm soát lượng tính toán trong quá trình kiểm tra.

---

## **Thành phần chính của s1**

### 1. Chọn lọc tập dữ liệu

- **Tạo tập dữ liệu s1K** gồm **1.000 câu hỏi** kèm theo quá trình suy luận.
- Các câu hỏi được chọn dựa trên **ba tiêu chí**: **chất lượng, độ khó và tính đa dạng**.
- Ban đầu có **59.029 câu hỏi từ 16 nguồn đa dạng**, bao gồm **NuminaMATH, bài toán AIME lịch sử, OlympicArena, OmniMath và AGIEval**.
- Tạo thêm **hai tập dữ liệu mới: s1-prob và s1-teasers**.
- Lọc còn **1.000 mẫu** dựa trên **chất lượng, độ khó và tính đa dạng**.
- Phân loại câu hỏi theo **lĩnh vực cụ thể** bằng **Claude 3.5 Sonnet** theo **hệ thống phân loại toán học MSC**.

### 2. Ép Ngân Sách (Budget Forcing)

- **Kiểm soát tính toán tại thời điểm kiểm tra** bằng cách **kết thúc sớm hoặc kéo dài** quá trình suy luận.
- Nếu mô hình tạo ra nhiều **token suy luận** hơn mức mong muốn, nó sẽ **tự động kết thúc** bằng cách chèn một **dấu hiệu kết thúc suy luận**.
- Để **kéo dài quá trình suy luận**, **dấu hiệu kết thúc suy luận bị ẩn đi**, và từ **"Wait"** được chèn vào, khuyến khích mô hình tiếp tục suy luận.

### 3. Huấn luyện và Đánh giá Mô hình

- Mô hình **Qwen2.5-32B-Instruct** được **tinh chỉnh** trên **s1K dataset**.
- Được đánh giá trên **ba bộ dữ liệu**: **AIME24, MATH500 và GPQA Diamond**.
- **s1-32B được huấn luyện trong 26 phút trên 16 NVIDIA H100 GPUs**.

---

## **Kết luận và Hạn chế**

- **Suy luận hiệu quả với số mẫu nhỏ**: **s1-32B** đạt hiệu suất cạnh tranh với các **mô hình đóng như OpenAI’s o1-preview**.
- **Khả năng suy luận tiềm ẩn** có thể được **kích hoạt bằng tinh chỉnh trên tập dữ liệu nhỏ, chất lượng cao**.
- **Hạn chế mở rộng tại thời điểm kiểm tra**: Bị giới hạn bởi **cửa sổ ngữ cảnh của mô hình**.
- **Giải pháp**: Sử dụng **các phương pháp mở rộng song song**, như **bỏ phiếu đa số** hoặc **tìm kiếm theo cây**.
