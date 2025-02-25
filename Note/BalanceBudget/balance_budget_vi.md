# Tối ưu hóa phân bổ dữ liệu giữa SFT và PFT trong hậu huấn luyện LLMs

Bài báo này nghiên cứu cách phân bổ tối ưu một ngân sách dữ liệu huấn luyện cố định giữa **Supervised Finetuning (SFT)** và **Preference Finetuning (PFT)** trong giai đoạn hậu huấn luyện (post-training) các mô hình ngôn ngữ lớn (**LLMs**). Nghiên cứu đánh giá sự đánh đổi giữa hai phương pháp trên nhiều bài toán khác nhau, các kích thước mô hình khác nhau và các mức chi phí gán nhãn dữ liệu khác nhau.

## 🔑 Những phát hiện chính

- **SFT hiệu quả hơn trong môi trường dữ liệu hạn chế** (dưới **1.000 mẫu**).
- **Khi dữ liệu huấn luyện tăng lên, việc kết hợp cả SFT và PFT thường đạt hiệu suất tối ưu**, với tỷ trọng dữ liệu **PFT ngày càng cao**.
- **Bỏ qua hoàn toàn SFT và chỉ áp dụng PFT lên mô hình gốc dẫn đến hiệu suất kém**, đây được gọi là vấn đề **"khởi động lạnh" (cold start)**, đặc biệt rõ ràng với các bài toán như **toán học**.
- **Chỉ cần một lượng nhỏ dữ liệu SFT (<10% ngân sách) có thể giải quyết hiệu quả vấn đề cold start**, giúp cải thiện đáng kể hiệu suất trên các **benchmark phân tích**.

## 📌 Vai trò của SFT trong PFT

Bài báo đặt câu hỏi liệu **SFT có thực sự cần thiết trước khi áp dụng PFT hay không**. Kết quả cho thấy:

- **Áp dụng trực tiếp PFT lên mô hình gốc chỉ mang lại cải thiện hạn chế**, đặc biệt với các mô hình nhỏ.
- **SFT giúp mô hình thích nghi với định dạng đầu ra mong muốn**, tạo ra một điểm khởi đầu tốt hơn cho quá trình tinh chỉnh **PFT bằng phương pháp DPO**.
- Điều này đặc biệt quan trọng với các bài toán như **toán học**, nơi việc **định dạng đầu ra** đóng vai trò quan trọng trong hiệu suất mô hình.

## 💰 Ảnh hưởng của chi phí gán nhãn dữ liệu

Bài báo cũng phân tích cách tối ưu hóa phân bổ dữ liệu khi **chi phí gán nhãn giữa SFT và PFT khác nhau**.

- Do **các tập dữ liệu mã nguồn mở không có thông tin chi phí rõ ràng**, nhóm nghiên cứu sử dụng dữ liệu tổng hợp tạo ra từ **GPT-4o** để ước tính chi phí này.
- **Trong hầu hết các trường hợp, việc đầu tư một phần ngân sách vào SFT trước khi chuyển sang PFT mang lại hiệu suất tối ưu, bất kể chi phí gán nhãn cụ thể**.

## ⚙️ Cấu hình thử nghiệm

Nghiên cứu sử dụng các mô hình thuộc họ:

- **Llama3.1-8B**
- **Qwen2.5-7B**

Thực hiện tinh chỉnh cả **SFT và PFT** trong **2 epoch**.  
**LoRA** được áp dụng để tối ưu hiệu suất huấn luyện.

### 🔬 Bốn tác vụ chính được đánh giá:

1. **Helpfulness** (mức độ hữu ích)
2. **Summarization** (tóm tắt)
3. **Instruction Following** (làm theo hướng dẫn)
4. **Grade School Mathematics** (toán tiểu học)

📌 **Bảng 1 và 2 trong bài báo cung cấp thông tin chi tiết về các tập dữ liệu dùng trong huấn luyện và các tiêu chí đánh giá.**
