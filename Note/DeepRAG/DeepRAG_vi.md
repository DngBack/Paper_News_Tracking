### DeepRAG: Suy nghĩ từng bước trước khi truy xuất cho các mô hình ngôn ngữ lớn

Bài báo _"DeepRAG: Thinking to Retrieval Step by Step for Large Language Models"_ giới thiệu một framework có tên **DeepRAG**, nhằm cải thiện khả năng suy luận và độ chính xác của các mô hình ngôn ngữ lớn (**LLMs**) trong truy xuất kết hợp sinh văn bản (**Retrieval-Augmented Generation - RAG**). Framework này giải quyết các thách thức về **phân rã nhiệm vụ kém hiệu quả** và **truy xuất dư thừa**, vốn có thể tạo ra nhiễu và làm giảm chất lượng phản hồi.

DeepRAG mô hình hóa **quá trình suy luận có hỗ trợ truy xuất** như một **Quá trình Quyết định Markov (MDP)**, cho phép truy xuất một cách chiến lược và thích ứng.

---

## **Các thành phần chính của DeepRAG**

### 1. Truyện truy xuất (Retrieval Narrative)

- Đảm bảo luồng truy xuất có cấu trúc và thích ứng bằng cách tạo ra các **truy vấn con** dựa trên thông tin đã truy xuất trước đó.
- Giúp chia nhỏ các truy vấn phức tạp thành các truy vấn con dễ xử lý hơn.

### 2. Quyết định nguyên tử (Atomic Decisions)

- Xác định **động** liệu có nên truy xuất thông tin bên ngoài hay chỉ dựa vào kiến thức **nội tại** của LLM cho từng truy vấn con.
- Giúp tránh truy xuất không cần thiết, từ đó **cải thiện chất lượng sinh văn bản và giảm độ trễ suy luận**.

---

## **Cách DeepRAG hoạt động**

DeepRAG thực hiện quy trình gồm **ba bước**:

### 1. Tìm kiếm theo cây nhị phân (Binary Tree Search)

- Xây dựng **cây nhị phân** cho từng truy vấn con, **khám phá** các nhánh dựa trên kiến thức **nội tại** hoặc kiến thức từ **nguồn bên ngoài**.
- Phương pháp này giúp tổng hợp dữ liệu cho **học bắt chước (imitation learning)** và **hiệu chỉnh ranh giới kiến thức** của LLM.

### 2. Học bắt chước (Imitation Learning)

- Trích xuất **quá trình suy luận** giúp đạt được câu trả lời chính xác với chi phí truy xuất tối thiểu.
- Điều chỉnh mô hình để **cải thiện quyết định kết thúc**, **ra quyết định nguyên tử**, **nâng cao khả năng phân rã truy vấn**, và **tạo ra câu trả lời trung gian chính xác**.

### 3. Chuỗi hiệu chỉnh (Chain of Calibration)

- **Hiệu chỉnh kiến thức nội tại** của LLM bằng cách tối ưu từng quyết định nguyên tử.
- Tổng hợp **dữ liệu ưu tiên** để xác định **khi nào cần truy xuất**, sau đó **tinh chỉnh (fine-tune)** LLM với dữ liệu này.

---

## **Mô hình MDP trong DeepRAG**

DeepRAG coi quá trình suy luận như một **MDP**, được định nghĩa bởi bộ tứ **(S, A, P, R)**:

- **Trạng thái (S):** Đại diện cho **giải pháp một phần** của câu hỏi ban đầu tại từng bước.
- **Hành động (A):** Gồm hai quyết định phụ:
  - **Quyết định kết thúc** (tiếp tục hay dừng suy luận).
  - **Quyết định nguyên tử** (truy xuất thông tin bên ngoài hay dựa vào kiến thức nội tại).
- **Chuyển đổi trạng thái (P):** Cập nhật trạng thái dựa trên hành động đã thực hiện (tạo truy vấn con tiếp theo hoặc kết thúc quá trình).
- **Phần thưởng (R):** Đánh giá **tính đúng đắn của câu trả lời** và **chi phí truy xuất**, chỉ áp dụng khi câu trả lời cuối cùng được tạo ra.

---

## **Thí nghiệm và Kết quả**

DeepRAG được thử nghiệm trên **năm bộ dữ liệu truy vấn mở** gồm:

- **HotpotQA, 2WikiMultihopQA, PopQA, CAG**, và **WebQuestions**.

Kết quả thực nghiệm cho thấy DeepRAG **vượt trội hơn các phương pháp hiện có**, đạt **độ chính xác cao hơn 21,99%** trong khi vẫn cải thiện **hiệu suất truy xuất**.

Phân tích sâu hơn chỉ ra rằng quyết định truy xuất của DeepRAG có mối tương quan chặt chẽ hơn với **kiến thức nội tại của LLM**, giúp hiệu chỉnh **ranh giới kiến thức** một cách hiệu quả hơn.

---

## **Truy xuất kết hợp sinh thích ứng (Adaptive Retrieval-Augmented Generation)**

DeepRAG thuộc nhóm phương pháp **RAG thích ứng**, nhằm tối ưu hóa **hiệu suất và độ chính xác** của truy xuất thông tin.

Các phương pháp hiện có bao gồm:

- **Phương pháp dựa trên phân loại (classifier-based methods)**
- **Phương pháp dựa trên độ tin cậy (confidence-based methods)**
- **Phương pháp dựa trên LLM (LLM-based methods)**

DeepRAG **khác biệt** khi tận dụng **khả năng sinh văn bản vốn có** của LLM để **khám phá ranh giới kiến thức**, **không cần thêm tham số** hay **các thước đo độ không chắc chắn không đáng tin cậy**.

---

## **Suy luận trong Truy xuất Kết hợp Sinh (RAG Reasoning)**

DeepRAG đóng góp vào xu hướng tích hợp **khả năng suy luận** vào RAG.

Không giống các phương pháp khác dựa nhiều vào **truy xuất mở rộng** hoặc **mô hình suy luận lớn**, DeepRAG cung cấp một **giải pháp end-to-end**, cho phép **bất kỳ mô hình nào cũng có thể suy nghĩ từng bước về việc truy xuất khi cần**.

---

## **Ranh giới Kiến thức (Knowledge Boundary)**

LLMs thường gặp khó khăn trong việc **phân biệt rõ ràng** giữa **những gì nó biết** và **những gì nó không biết**.

DeepRAG giải quyết vấn đề này bằng cách **khám phá ranh giới kiến thức** trong thiết lập RAG, giúp LLM **tự nhận thức được giới hạn của mình** và **đưa ra quyết định truy xuất thông tin phù hợp**.
