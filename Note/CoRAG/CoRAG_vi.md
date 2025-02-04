# CoRAG: Chain-of-Retrieval Augmented Generation

Bài báo đề xuất CoRAG, một phương pháp huấn luyện mô hình RAG giúp cải thiện khả năng xử lý truy vấn phức tạp bằng cách thực hiện chuỗi truy xuất nhiều bước thay vì chỉ một lần như cách truyền thống. Để huấn luyện CoRAG, nhóm tác giả sử dụng rejection sampling để tạo ra các chuỗi truy xuất trung gian, giúp mô hình học hỏi hiệu quả hơn từ dữ liệu.

CoRAG đạt kết quả xuất sắc trên nhiều benchmark, đặc biệt trong bài toán hỏi-đáp nhiều bước, với mức cải thiện hơn 10 điểm EM score so với baseline. Trên bộ KILT benchmark, CoRAG lập kỷ lục hiệu suất mới trên nhiều nhiệm vụ yêu cầu kiến thức sâu. Nghiên cứu này cũng cung cấp các phân tích chi tiết về cách CoRAG mở rộng quy mô, tạo nền tảng cho các mô hình RAG trong tương lai.
