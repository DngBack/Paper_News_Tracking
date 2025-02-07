# CoRAG: Chain-of-Retrieval Augmented Generation

Bài báo giới thiệu Chain-of-Retrieval Augmented Generation (CoRAG), một phương pháp đào tạo các mô hình có khả năng truy xuất và lập luận thông tin liên quan theo nhiều bước trước khi đưa ra câu trả lời cuối cùng. Dưới đây là bản tóm tắt các khía cạnh chính của bài báo:
Vấn đề cốt lõi:

- Các hệ thống Retrieval-Augmented Generation (RAG) truyền thống thường chỉ thực hiện một bước truy xuất trước khi tạo phản hồi. Điều này có thể hạn chế, đặc biệt đối với các truy vấn phức tạp đòi hỏi nhiều bước suy luận.
- Các mô hình truy xuất, sử dụng biểu diễn vector có kích thước cố định để đạt hiệu quả, có thể gặp khó khăn với các truy vấn phức tạp.
- Thường không rõ thông tin nào nên được truy xuất ban đầu cho các tác vụ suy luận đa bước.
  Giải pháp đề xuất: CoRAG
- CoRAG cho phép mô hình tự động điều chỉnh lại truy vấn dựa trên trạng thái hiện tại của quá trình suy luận, truy xuất thông tin một cách lặp đi lặp lại.
- Khung này được thiết kế để mô phỏng quá trình giải quyết vấn đề của con người, nơi thông tin được tìm kiếm một cách lặp đi lặp lại.
- CoRAG được đào tạo để truy xuất thông tin một cách rõ ràng theo từng bước, thay vì chỉ dựa vào khả năng học trong ngữ cảnh.
  Đào tạo CoRAG:
- Rejection Sampling: Bài báo sử dụng rejection sampling để tự động tạo ra các chuỗi truy xuất trung gian, là các chuỗi truy vấn phụ và câu trả lời phụ.
  - Một mô hình ngôn ngữ (LLM) tạo ra các truy vấn phụ dựa trên truy vấn gốc và các truy vấn phụ và câu trả lời phụ trước đó.
  - Một công cụ truy xuất văn bản tìm các tài liệu liên quan cho mỗi truy vấn phụ, và một LLM tạo ra các câu trả lời phụ tương ứng.
  - Quá trình lặp lại cho đến khi đạt đến độ dài chuỗi tối đa hoặc câu trả lời khớp với câu trả lời cuối cùng chính xác.
  - Chuỗi truy xuất có điểm log-likelihood cao nhất được chọn để tăng cường bộ dữ liệu chỉ có QA gốc.
- Tinh chỉnh: Các mô hình ngôn ngữ nguồn mở được tinh chỉnh trên các tập dữ liệu tăng cường bằng cách sử dụng các mục tiêu dự đoán token tiếp theo tiêu chuẩn. Mô hình được đào tạo trên ba tác vụ: dự đoán truy vấn phụ tiếp theo, dự đoán câu trả lời phụ và dự đoán câu trả lời cuối cùng.
  Chiến lược giải mã tại thời điểm kiểm thử:
- Bài báo khám phá các chiến lược giải mã khác nhau để quản lý sự đánh đổi giữa hiệu suất và chi phí tính toán tại thời điểm kiểm thử. Các chiến lược này kiểm soát mức tiêu thụ token và tần suất các cuộc gọi của trình truy xuất.
  - Greedy Decoding: Tạo ra các truy vấn phụ và câu trả lời phụ một cách tuần tự bằng cách sử dụng giải mã tham lam.
  - Best-of-N Sampling: Lấy mẫu N chuỗi truy xuất và chọn chuỗi tốt nhất để tạo ra câu trả lời cuối cùng, dựa trên điểm phạt.
  - Tree Search: Sử dụng một biến thể tìm kiếm theo chiều rộng với các lần triển khai chuỗi truy xuất.
    Kết quả thực nghiệm:
- CoRAG vượt trội đáng kể so với các baseline mạnh trong các tác vụ trả lời câu hỏi (QA) đa bước.
- Mô hình đạt được hiệu suất tối tân trên benchmark KILT trên nhiều tác vụ chuyên sâu về tri thức.
- Hiệu suất của CoRAG tăng lên khi tăng tính toán tại thời điểm kiểm thử (chuỗi truy xuất dài hơn), theo một mối quan hệ log-tuyến tính gần đúng giữa mức tiêu thụ token và hiệu suất mô hình.
- Khung này thể hiện sự mạnh mẽ đối với các trình truy xuất có chất lượng khác nhau.
- CoRAG có thể phân tách hiệu quả các truy vấn phức tạp và thực hiện việc cải cách truy vấn linh hoạt để cải thiện chất lượng của các phản hồi được tạo ra.
  Những phát hiện và phân tích chính:
- Đào tạo lặp đi lặp lại: Việc lấy mẫu từ chối lặp đi lặp lại, trong đó mô hình CoRAG đã được đào tạo được sử dụng để tạo ra các tập chuỗi truy xuất mới, cho thấy kết quả hỗn hợp, cho thấy rằng các LLM được điều chỉnh theo hướng dẫn đã tạo ra các chuỗi truy xuất chất lượng cao.
- Tổng quát hóa yếu thành mạnh: Việc sử dụng LLM yếu hơn để tạo chuỗi truy xuất và LLM mạnh hơn để đào tạo là một chiến lược khả thi.
- Chuỗi truy xuất: Cơ chế chuỗi truy xuất có lợi nhất cho các câu hỏi đa bước phức tạp; đối với các câu hỏi đơn giản hơn, lợi ích là không đáng kể.
- Học cách dừng: Mô hình có thể học cách dừng truy xuất thông tin tại thời điểm kiểm thử, điều này có thể tiết kiệm token với chi phí làm giảm hiệu suất.
- Bài báo cũng phân tích tác động của các yếu tố khác nhau như các trình truy xuất khác nhau, kích thước lấy mẫu từ chối và nhiệt độ lấy mẫu đối với hiệu suất của mô hình.

Nhìn chung, CoRAG là một phương pháp đầy hứa hẹn để cải thiện tính chính xác và độ tin cậy của các hệ thống RAG bằng cách cho phép các mô hình suy luận và truy xuất thông tin một cách lặp đi lặp lại.
