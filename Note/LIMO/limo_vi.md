# **Các kết quả chính của dự án LIMO (Less is More for Reasoning)**

## **1. Độ chính xác cao với lượng dữ liệu tối thiểu**

- LIMO đạt **57,1%** độ chính xác trên bộ đánh giá **AIME** và **94,8%** trên bộ **MATH** chỉ với **817 mẫu huấn luyện**.
- Điều này chứng minh rằng khả năng suy luận toán học phức tạp có thể được khai thác với số lượng ví dụ rất ít.
- LIMO chỉ sử dụng **1% dữ liệu huấn luyện** so với các phương pháp trước đây nhưng vẫn đạt hiệu suất vượt trội.

## **2. Khả năng tổng quát hóa ngoài phân phối** (_Out-of-Distribution Generalization_)

- LIMO đạt **mức cải thiện tuyệt đối 40,5% trên 10 bộ đánh giá đa dạng**.
- Vượt trội so với các mô hình được huấn luyện trên lượng dữ liệu lớn hơn gấp 100 lần.
- Thách thức quan điểm rằng tinh chỉnh có giám sát chủ yếu dẫn đến ghi nhớ thay vì tổng quát hóa.

## **3. Hiệu suất vượt trội so với các tập dữ liệu lớn hơn**

- Bộ dữ liệu tinh lọc gồm **817 bài toán** giúp LIMO đạt **72,8% độ chính xác**.
- Cao hơn các mô hình được huấn luyện trên tập dữ liệu lớn như **NuminaMath-100k** và **OpenThoughts-114k**.
- Điều này chứng minh rằng **chất lượng dữ liệu quan trọng hơn số lượng dữ liệu**.

## **4. Ảnh hưởng của chất lượng chuỗi lập luận**

- Các mô hình được huấn luyện trên chuỗi suy luận chất lượng cao nhất (_L5_) đạt hiệu suất cao nhất trên **AIME24** và **MATH500**.
- Hiệu suất giảm dần theo từng cấp chất lượng thấp hơn.
- Khoảng cách giữa _L5_ và _L1_:
  - **15 điểm phần trăm** trên AIME24.
  - **12 điểm phần trăm** trên MATH500.

## **5. Ảnh hưởng của chất lượng câu hỏi**

- Mô hình được huấn luyện trên bộ dữ liệu có độ thử thách cao hơn sẽ có khả năng suy luận tốt hơn.
- Việc chỉ thay đổi cách chọn bài toán giúp tăng **16% độ chính xác** trên AIME2024.

## **6. Tầm quan trọng của nền tảng tiền huấn luyện**

- Việc lựa chọn mô hình tiền huấn luyện có ảnh hưởng lớn đến hiệu suất suy luận.
- LIMO được xây dựng trên **Qwen2.5-32B-Instruct**, vượt trội hơn phiên bản tiền nhiệm:
  - **AIME2024**: Tăng **47,1 điểm phần trăm** so với **Qwen1.5-32B-Instruct**.
  - **MATH500**: Tăng **34,4 điểm phần trăm** so với **Qwen1.5-32B-Instruct**.

## **7. Hiệu suất tổng thể cao nhất**

- LIMO đạt **trung bình 72,1%** trên tất cả các bộ đánh giá, vượt trội so với:
  - **OpenAI-o1-preview**: 67,8%.
  - **QwQ-32B-Preview**: 66,4%.
  - Và các baseline khác.

## **8. Phân tích định tính**

- LIMO thể hiện khả năng **tự phản biện mạnh mẽ** và **tạo ra các chuỗi lập luận dài** (_long chain-of-thought_).
- Có khả năng **tự kiểm tra phát biểu của mình** và **xác minh các phép toán đã thực hiện**.

# **Các đóng góp chính của dự án LIMO (Less is More for Reasoning)**

## **1. Giả thuyết LIMO (_LIMO Hypothesis_)**

- Bài báo giới thiệu và thiết lập giả thuyết **LIMO**, cho thấy rằng **khả năng suy luận phức tạp có thể được khai thác chỉ với một lượng dữ liệu nhỏ đáng kinh ngạc** (chỉ vài trăm ví dụ).
- Bằng cách tận dụng **kiến thức toán học phong phú** trong các mô hình tiền huấn luyện và **chuỗi lập luận chi tiết**, LIMO **thách thức các giả định về quy luật mở rộng (_scaling laws_) trong các tác vụ suy luận**.
- Giả thuyết LIMO cho rằng **khả năng suy luận nâng cao có thể xuất hiện trong các mô hình nền tảng chỉ với một số ít các ví dụ được tổ chức chính xác**, dựa trên hai yếu tố:
  - **Kiến thức tiền huấn luyện** đã có sẵn trong không gian tham số của mô hình.
  - **Chất lượng của chuỗi lập luận**, giúp phân rã các vấn đề phức tạp thành các bước logic chi tiết.

## **2. Hiệu quả dữ liệu (_Data Efficiency_)**

- LIMO chứng minh rằng có thể đạt **độ chính xác cao với lượng dữ liệu huấn luyện tối thiểu**.
- Ví dụ:
  - **57,1% độ chính xác trên AIME**.
  - **94,8% độ chính xác trên MATH**.
  - Chỉ sử dụng **817 mẫu huấn luyện**, tương đương **1% dữ liệu** so với các phương pháp trước đây.

## **3. Khả năng tổng quát hóa ngoài phân phối (_Out-of-Distribution Generalization_)**

- LIMO thể hiện khả năng **tổng quát hóa mạnh mẽ**, đạt **mức cải thiện tuyệt đối 40,5% trên 10 bộ đánh giá khác nhau**.
- Hiệu suất vượt trội so với các mô hình được huấn luyện trên lượng dữ liệu lớn hơn **100 lần**.

## **4. Xác định các yếu tố quan trọng (_Identification of Critical Factors_)**

- Dự án xác định **các yếu tố cốt lõi** để khai thác khả năng suy luận hiệu quả, đặc biệt là:
  - **Sự kết hợp giữa kiến thức tiền huấn luyện và khả năng mở rộng tính toán tại thời điểm suy luận**.

## **5. Bằng chứng thực nghiệm có hệ thống (_Systematic Empirical Evidence_)**

- LIMO cung cấp **bằng chứng thực nghiệm có hệ thống**, thách thức các giả định hiện tại về **quy luật mở rộng trong tác vụ suy luận**.
- Chứng minh rằng lợi ích của phương pháp này **không chỉ giới hạn trong tập huấn luyện mà còn tổng quát tốt trên các bài toán ngoài phân phối**.

## **6. Phát hành mã nguồn mở (_Open-Source Release_)**

- Các tác giả công bố **một bộ công cụ mã nguồn mở đầy đủ**, bao gồm:
  - **Mô hình đã tinh chỉnh**.
  - **Pipeline đánh giá**.
  - **Mã huấn luyện**.
  - **Bộ dữ liệu được tuyển chọn kỹ lưỡng**.
- Điều này tạo điều kiện thuận lợi cho **nghiên cứu có hệ thống về hiệu quả dữ liệu trong suy luận phức tạp** và đảm bảo **khả năng tái lập kết quả**.

## **7. Tuyển chọn dữ liệu chất lượng cao (_High-Quality Data Curation_)**

- Bài báo nhấn mạnh **tầm quan trọng của chất lượng dữ liệu** hơn là số lượng.
- LIMO giới thiệu **một phương pháp hệ thống** để xây dựng bộ dữ liệu tối thiểu với các câu hỏi được thiết kế nhằm **khai thác quá trình suy luận mở rộng** và các lời giải thể hiện **tiến trình logic rõ ràng**.

## **8. Chất lượng chuỗi lập luận (_Reasoning Chain Quality_)**

- Mô hình được huấn luyện trên **chuỗi lập luận chất lượng cao** đạt hiệu suất tốt hơn đáng kể.

## **9. Chất lượng câu hỏi (_Question Quality_)**

- Mô hình được huấn luyện trên **tập dữ liệu có độ thử thách cao hơn** thể hiện **khả năng suy luận vượt trội**.

---

# **Xây dựng tập dữ liệu và huấn luyện mô hình LIMO**

## **1. Xây dựng tập dữ liệu**

### **Xác thực giả thuyết LIMO (_LIMO Hypothesis Validation_)**

- Quá trình xây dựng tập dữ liệu dựa trên **Giả thuyết LIMO** (_Less-Is-More Reasoning_), cho rằng **khả năng suy luận phức tạp có thể xuất hiện thông qua một số ít nhưng được tổ chức chính xác các ví dụ về quá trình tư duy** trong các mô hình nền tảng có kiến thức miền được mã hóa toàn diện trong quá trình tiền huấn luyện.
- Giả thuyết này dựa trên:
  - **Sự hiện diện của kiến thức tiên quyết** trong không gian tham số của mô hình.
  - **Chất lượng của chuỗi lập luận**, giúp phân rã các vấn đề phức tạp thành các bước logic chi tiết.

### **Mục tiêu**

- Xây dựng một tập dữ liệu **tối thiểu nhưng chất lượng cao**, có khả năng **khai thác hiệu quả khả năng suy luận vốn có của mô hình**.

### **Lựa chọn câu hỏi**

- **Tiêu chí lựa chọn**:

  - **Độ khó**: Ưu tiên các bài toán **thử thách cao**, đòi hỏi chuỗi lập luận phức tạp và tích hợp kiến thức.
  - **Tính tổng quát**: Ưu tiên các bài toán **khác biệt đáng kể so với dữ liệu huấn luyện của mô hình**.
  - **Độ đa dạng kiến thức**: Bao gồm nhiều lĩnh vực và khái niệm toán học khác nhau.

- **Quy trình lọc nhiều giai đoạn**:
  - **Bắt đầu với hàng chục triệu bài toán** từ nhiều tập dữ liệu có sẵn.
  - **Lọc sơ bộ độ khó**:
    - Dùng mô hình **Qwen2.5-Math-7B-Instruct** để loại bỏ các bài toán mà mô hình này có thể giải chính xác trong **vài lần thử**.
  - **Lọc chuyên sâu**:
    - Các bài toán còn lại được đánh giá bằng **các mô hình suy luận tiên tiến nhất**.
    - Chỉ giữ lại các bài toán mà **ngay cả những mô hình mạnh nhất cũng chỉ đạt tỷ lệ thành công dưới một ngưỡng nhất định**.
  - **Lựa chọn chiến lược**:
    - Cân bằng sự đại diện giữa các **lĩnh vực toán học** và các **mức độ phức tạp khác nhau**.
    - **Tránh sự trùng lặp khái niệm**.
  - **Kết quả**:
    - Thu được **817 bài toán được tuyển chọn kỹ lưỡng**.

### **Xây dựng chuỗi lập luận (_Reasoning Chain Construction_)**

- **Chiến lược tuyển chọn lời giải**:
  - Thu thập lời giải chính thức (nếu có), bổ sung bằng lời giải từ **chuyên gia con người** và **chuyên gia AI**.
  - Sử dụng các **mô hình suy luận tiên tiến** để tạo ra **các cách giải đa dạng**.
  - Áp dụng kỹ thuật **tự chưng cất (_self-distillation_)**, tạo ra các biến thể mô hình để sinh ra thêm các phản hồi cho bài toán.
  - **Lọc các phản hồi** theo tiêu chí chính xác để xây dựng **tập lời giải hợp lệ ban đầu**.
  - **Phân tích sâu các lời giải đã lọc** thông qua đánh giá hợp tác.
  - **Xác định các đặc điểm quan trọng của chuỗi lập luận chất lượng cao**:
    - **Cấu trúc tổ chức tối ưu**.
    - **Hệ thống hỗ trợ tư duy hiệu quả**.
    - **Quá trình xác minh chặt chẽ**.
  - **Áp dụng kết hợp lọc theo quy tắc và hỗ trợ từ mô hình ngôn ngữ lớn (LLM)** để chọn ra các lời giải chất lượng cao.
  - **Kết quả**:
    - Xây dựng tập dữ liệu gồm **các bộ ba (q, r, a)**, trong đó **mỗi chuỗi lập luận đều đạt tiêu chí chất lượng**.

---

## **2. Huấn luyện mô hình**

### **Mô hình nền tảng**

- **Mô hình cơ sở**: **Qwen2.5-32B-Instruct** được tinh chỉnh bằng **fine-tuning có giám sát (SFT)** trên tập dữ liệu LIMO.

### **Giao thức huấn luyện**

- Áp dụng **fine-tuning toàn bộ tham số** với tối ưu hóa **DeepSpeed ZeRO-3** và **FlashAttention-2**.
- Giới hạn độ dài chuỗi tối đa **16.384 tokens**.
- Sau quá trình huấn luyện với **chỉ vài trăm mẫu dữ liệu SFT**, mô hình có thể **tích hợp các tác vụ meta-reasoning vào một chuỗi suy luận thống nhất**.
