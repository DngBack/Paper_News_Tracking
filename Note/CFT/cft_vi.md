# Critique Fine-Tuning (CFT) – Điều Chỉnh Tinh Chỉnh Phê Bình

**Critique Fine-Tuning (CFT)** là một chiến lược huấn luyện mô hình ngôn ngữ tập trung vào việc học cách phê bình các phản hồi nhiễu thay vì chỉ đơn thuần bắt chước những phản hồi đúng. Cách tiếp cận này được lấy cảm hứng từ quá trình học tập của con người, nhấn mạnh vào tư duy phản biện và phân tích sâu hơn.

## Các khía cạnh chính của CFT

- Mô hình học cách đưa ra đánh giá đối với các phản hồi nhiễu, bao gồm việc **xác định lỗi sai, đề xuất cải thiện và xác minh tính chính xác**.
- CFT huấn luyện mô hình để phê bình một cặp truy vấn – phản hồi, **tối đa hóa xác suất** $P(c|[x; y])$, trong đó **c** là lời phê bình được gán nhãn cho cặp truy vấn – phản hồi **[x; y]**.
- CFT đã cho thấy **sự cải thiện ổn định** so với **Supervised Fine-Tuning (SFT)** trên các bài kiểm tra toán học với nhiều mô hình nền tảng khác nhau. **CFT có thể vượt trội hơn các mô hình SFT từ 4–10 điểm tuyệt đối**.
- CFT có thể **đạt hiệu suất tương đương với các phương pháp học tăng cường (RL)** nhưng **tiêu tốn ít tài nguyên tính toán hơn**.
- Các nghiên cứu **ablation studies** cho thấy CFT có **khả năng chống chịu tốt** với **nguồn phản hồi nhiễu và mô hình đánh giá giáo viên**.

## Phương pháp thực nghiệm

Để kiểm chứng hiệu quả của CFT, các tác giả đã xây dựng một **bộ dữ liệu 50.000 mẫu** từ **WebInstruct**, sử dụng **GPT-4o** để tạo ra các lời phê bình dưới dạng:

\[
([truy vấn; phản hồi nhiễu], phê bình)
\]

Các tập dữ liệu được sử dụng cho CFT **bao gồm nhiều chủ đề hơn nhưng có kích thước nhỏ hơn**, cho thấy **tính hiệu quả trong việc nâng cao khả năng suy luận của LLMs**.  
Mục tiêu huấn luyện là **nối câu hỏi $x$ và phản hồi nhiễu $y$ làm đầu vào**, sau đó tối ưu hóa tham số mô hình để tạo ra lời phê bình $c$.

## Kết quả thí nghiệm

Các thí nghiệm đã so sánh **CFT với nhiều phương pháp SFT khác nhau** trên **ba mô hình nền tảng kích thước 7B** bằng các bài kiểm tra suy luận toán học.  
**Kết quả:**

✅ CFT **liên tục vượt trội** hơn so với tất cả các phương pháp SFT trên các mô hình khác nhau.  
✅ CFT **có tốc độ hội tụ nhanh hơn** với **ít dữ liệu huấn luyện hơn**.
