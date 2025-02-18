# Satori: Mô hình LLM 7B với khả năng suy luận nâng cao

Satori là một mô hình ngôn ngữ lớn (LLM) 7B cải thiện khả năng suy luận thông qua tìm kiếm tự hồi quy. Nó sử dụng cơ chế **Chuỗi Hành Động-Suy Nghĩ** (_Chain-of-Action-Thought - COAT_), cho phép thực hiện nhiều hành động meta trong quá trình giải quyết vấn đề, chẳng hạn như phản ánh về các bước trước đó hoặc khám phá các giải pháp thay thế.

## 🔹 Các đặc điểm chính của Satori:

- **🧠 Mô hình huấn luyện:**  
  Satori sử dụng quy trình huấn luyện hai giai đoạn:

  1. **Tinh chỉnh định dạng (Format Tuning - FT):** Giúp nội hóa phương thức suy luận COAT.
  2. **Tự cải thiện bằng học tăng cường (RL):** Cải thiện khả năng suy luận thông qua tự tối ưu hóa.

- **⚡ Hiệu suất:**  
  Mô hình có khả năng **tự tìm kiếm hồi quy**, không cần hướng dẫn bên ngoài, với **sự giám sát tối thiểu** và **quy mô tự cải thiện lớn**.

- **📈 Hiệu quả:**  
  Satori thể hiện **hiệu suất vượt trội** trong các bài toán suy luận toán học, **tốt hơn các mô hình hướng dẫn trên cùng nền tảng**.

- **🌍 Tính tổng quát:**

  - Chuyển đổi tốt sang các tác vụ **ngoài miền huấn luyện**.
  - Thể hiện khả năng **tự phản tư** và **tự khám phá**.

- **🔗 Suy luận COAT:**

  - Được huấn luyện với **định dạng suy luận COAT**.
  - Vượt trội hơn so với các mô hình sử dụng **Chuỗi Suy Nghĩ (Chain-of-Thought - CoT)**.

- **🔄 Tự sửa lỗi:**

  - Có khả năng **tự sửa lỗi mạnh mẽ hơn** so với các mô hình không có giai đoạn huấn luyện RL.

- **📊 Khả năng mở rộng theo thời gian thực nghiệm:**

  - Thông qua huấn luyện RL, mô hình **cải thiện hiệu suất bằng cách dành nhiều thời gian hơn cho suy luận**.

- **♻️ Cải thiện lặp lại:**
  - Có thể đạt được **sự gia tăng hiệu suất liên tục** thông qua quá trình **cải thiện lặp lại**.

---

## 🔹 Khung huấn luyện của Satori bao gồm:

### 🔧 1. **Tinh chỉnh định dạng (Format Tuning - FT)**

- Giai đoạn tinh chỉnh quy mô nhỏ giúp **điều chỉnh một LLM tiền huấn luyện** trên một tập dữ liệu nhỏ gồm các quy trình suy luận.
- Giúp mô hình làm quen với **các token hành động meta**.

### 🤖 2. **Tổng hợp dữ liệu đa tác nhân (Multi-Agent Data Synthesis)**

Khung tổng hợp dữ liệu đa tác nhân sử dụng **ba LLM** để xây dựng các quy trình suy luận chất lượng cao:

1. **Bộ tạo (Generator)**
   - Tạo ra nhiều con đường suy luận cho một bài toán đầu vào.
2. **Bộ phê bình (Critic)**
   - Đánh giá mức độ chính xác của các con đường suy luận, cung cấp phản hồi.
3. **Mô hình thưởng (Reward Model)**
   - Gán điểm số và chọn ra con đường **hiệu quả nhất**.

### 🔄 3. **Khởi động lại và khám phá (Restart and Explore - RAE)**

- Lấy cảm hứng từ **Go-Explore**, giúp mô hình:
  - **Khởi động lại từ các bước trung gian**, kể cả những điểm **thất bại trước đó**.
  - **Tập trung vào sửa lỗi** thay vì làm lại từ đầu.
  - **Khuyến khích khám phá sâu hơn** với phần thưởng phụ.

### 🎯 4. **Thiết kế phần thưởng (Reward Design)**

Satori sử dụng **mức độ chính xác làm phần thưởng chính** và bổ sung phần thưởng phụ:

- **🏆 Phần thưởng dựa trên quy tắc**
  - Đánh giá **mức độ chính xác của câu trả lời cuối cùng**.
- **📊 Thưởng theo mức độ ưu tiên (Preference Bonuses)**
  - Một **Mô hình Kết quả (Outcome Reward Model - ORM)** được huấn luyện bằng **Bradley-Terry (BT)** để đánh giá **các quy trình suy luận**, gán giá trị cao hơn cho những quy trình **chính xác hơn**.

### 🚀 5. **Cải thiện lặp lại (Iterative Self-Improvement)**

- Sau mỗi vòng **huấn luyện RL**, kiến thức tối ưu hiện tại được **chưng cất vào mô hình nền** thông qua **tinh chỉnh có giám sát (SFT)**.

---

## 📊 **Hiệu suất thực nghiệm của Satori**

- Đạt **hiệu suất hàng đầu** trên các **bài kiểm tra suy luận toán học**.
- Thể hiện **khả năng tổng quát mạnh mẽ** đối với các **tác vụ ngoài miền**.
- **Vượt trội hơn mô hình** `Qwen-2.5-Math-7B-Instruct` (một mô hình chuyên về toán học trên cùng nền tảng) **mặc dù yêu cầu ít giám sát hơn**.

---
