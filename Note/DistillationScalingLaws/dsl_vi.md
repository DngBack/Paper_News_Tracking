# **Quy luật mở rộng của Distillation (Distillation Scaling Laws)**

## **Giới thiệu**

Quy luật mở rộng của Distillation giúp ước tính hiệu suất của mô hình học sinh sau khi được distillation. Dựa trên ngân sách tính toán (compute budget) và cách phân bổ giữa mô hình giáo viên và mô hình học sinh, quy luật này giúp cộng đồng nghiên cứu tạo ra các mô hình mạnh mẽ hơn với chi phí suy luận (inference) và chi phí tính toán suốt vòng đời thấp hơn.

## **Những phát hiện chính**

### **1. Quy luật mở rộng của Distillation**

- Một trong những đóng góp quan trọng của nghiên cứu là quy luật mở rộng giúp ước tính hiệu suất của mô hình học sinh.
- Quy luật này dựa trên ngân sách tính toán và cách phân bổ tài nguyên giữa mô hình giáo viên và học sinh.
- Điều này giúp tối ưu hóa compute để tạo ra các mô hình có hiệu suất cao hơn với chi phí tính toán thấp hơn.

### **2. Công thức tối ưu hóa compute**

- Bài báo cung cấp các chiến lược tối ưu hóa compute để áp dụng distillation hiệu quả.
- Các chiến lược này giúp xác định cách phân bổ compute cho cả mô hình giáo viên và học sinh nhằm đạt hiệu suất tối đa.

### **3. Khi nào Distillation vượt trội?**

Distillation hiệu quả hơn so với tiền huấn luyện có giám sát (supervised pretraining) trong một số điều kiện nhất định:

#### **Nhiều mô hình học sinh hoặc đã có mô hình giáo viên**

- Nếu có nhiều mô hình học sinh cần distillation hoặc đã có sẵn một mô hình giáo viên phù hợp, distillation có thể vượt trội hơn so với học có giám sát.
- Lợi thế này duy trì đến một mức compute nhất định, liên quan đến kích thước mô hình học sinh.

#### **Trường hợp tốt nhất**

- Trong kịch bản tối ưu, distillation có thể vượt trội so với học có giám sát, được thể hiện qua sự khác biệt về entropy chéo (cross-entropy) giữa hai phương pháp.

### **4. Khi nào nên sử dụng học có giám sát?**

- Nếu mục tiêu là huấn luyện một mô hình học sinh duy nhất và mô hình giáo viên cũng cần được huấn luyện từ đầu, thì học có giám sát sẽ hiệu quả hơn distillation.

### **5. Vai trò của mô hình giáo viên**

- Entropy chéo của giáo viên là yếu tố quyết định chính đến entropy chéo của học sinh.
- Do đó, kích thước giáo viên và số lượng token có thể không cần phải là trục tìm kiếm chính trong tối ưu hóa.

### **6. Compute hoặc token cố định**

- Bài báo phân tích các kịch bản trong đó compute hoặc số lượng token bị giới hạn để xác định khi nào distillation có lợi hơn so với học có giám sát.

### **7. Hiệu suất tính toán**

- Distillation có thể tiết kiệm compute và dữ liệu hơn so với học có giám sát khi tạo ra một mô hình mong muốn.

### **8. Lựa chọn siêu tham số**

- Distillation thuần túy với hệ số trộn (λ) = 1 và nhiệt độ (τ) = 1 mang lại hiệu suất ổn định trên nhiều kích thước mô hình.
