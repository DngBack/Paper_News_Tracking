# ThinkSmarternotHarder: AdaptiveReasoningwith Inference AwareOptimization

Yu và cộng sự (2025) giải quyết thách thức của các mô hình ngôn ngữ lớn khi sử dụng chuỗi suy luận quá dài cho các bài toán toán học đơn giản. Họ giới thiệu Inference Budget-Constrained Policy Optimization (IBPO), một thuật toán tối ưu hóa việc phân bổ ngân sách suy luận dựa trên độ khó của truy vấn. IBPO tinh chỉnh mô hình để hiểu độ phức tạp của vấn đề và phân bổ tài nguyên một cách hợp lý, giúp cải thiện hiệu suất trên các bài toán toán học.

Nghiên cứu cho thấy IBPO giúp mô hình đạt hiệu quả sử dụng token tốt hơn và tuân thủ ràng buộc, đồng thời phân bổ ngân sách suy luận một cách linh hoạt. Các nhà nghiên cứu đã phát triển IBPO từ góc độ tối ưu hóa, dẫn đến một bản cập nhật SFT có trọng số đơn giản dựa trên các nguyên tắc tối ưu hóa chính sách có ràng buộc. Kết quả cho thấy tiềm năng của IBPO trong việc cân bằng giữa độ chính xác và chi phí tính toán trong các mô hình ngôn ngữ lớn (LLM).

Bài báo giải quyết một số vấn đề quan trọng liên quan đến suy luận trong các mô hình ngôn ngữ lớn (LLMs):

Hành vi đơn chế độ (uni-modal) trong các mô hình suy luận chuỗi dài: Các mô hình tiên tiến có xu hướng sử dụng chuỗi suy luận dài một cách không cần thiết ngay cả đối với các truy vấn đơn giản, dẫn đến chi phí suy luận cao và gia tăng dấu chân carbon.

Nhu cầu tối ưu hóa độ dài suy luận theo truy vấn: Bài báo đề xuất một cách tiếp cận giúp mô hình suy luận hoạt động theo hành vi đa chế độ (multi-modal), trong đó độ dài chuỗi suy luận được tự động điều chỉnh dựa trên độ phức tạp của truy vấn.

Cân bằng giữa độ chính xác và chi phí token: Mục tiêu của nghiên cứu là nâng cao hiệu suất sử dụng token, đảm bảo mô hình đạt được độ chính xác cao nhất với mức tiêu thụ token tối ưu.

Tối ưu hóa phân bổ tài nguyên: Bài báo đề cập đến bài toán kiểm soát việc phân bổ phản hồi có độ dài khác nhau, hướng đến tối ưu hóa hiệu suất suy luận mà không lãng phí tài nguyên tính toán.

Đáp ứng ràng buộc và phân bổ ngân sách suy luận: Nghiên cứu đề xuất một phương pháp giúp mô hình tuân thủ các ràng buộc ngân sách suy luận và phân bổ ngân sách động nhằm ưu tiên tài nguyên cho các bài toán có độ phức tạp cao hơn.

Thiết kế thuật toán: Xây dựng bài toán dưới dạng một vấn đề RL có ràng buộc với giới hạn phân bổ tài nguyên, đồng thời trình bày cách dẫn xuất thuật toán IBPO từ góc độ tối ưu hóa, dẫn đến một phương pháp cập nhật SFT có trọng số theo từng bước lặp.

Triển khai thực tế: Cung cấp chi tiết về cách triển khai thuật toán IBPO, bao gồm việc lựa chọn thuật toán cơ sở (Constraint Generative Policy Optimization - CGPO) và thiết kế hàm thưởng. Hàm thưởng được xác định là reward margin, tức là lợi thế phần thưởng của nhóm G so với tất cả các nhóm khác.

Các thuật ngữ, xây dựng G+ & quy trình huấn luyện: Giải thích cách tạo phản hồi mở rộng, bao gồm Sequential Voting (SV) và Adaptive Sequential Voting (ASV). SV chỉ tạo phản hồi trong tập G+, trong khi ASV xuất ra hỗn hợp các phản hồi thuộc
𝑦
∈
𝐺
∘
y∈G
∘
và
𝑦
∈
𝐺

- y∈G
- . Phần này cũng trình bày về tập dữ liệu và quy trình huấn luyện sử dụng trong thí nghiệm.

Đánh giá IBPO với OPTIuB: Trình bày kết quả thực nghiệm của IBPO, thể hiện khả năng tuân thủ ràng buộc và phân bổ ngân sách suy luận một cách linh hoạt. Các tiêu chí đánh giá bao gồm cải thiện tuyệt đối, hiệu suất, tuân thủ ràng buộc và phân bổ ngân sách.

Kết luận & thảo luận: Tổng kết lại khung IBPO và những lợi ích của nó, bao gồm khả năng tuân thủ ràng buộc và phân bổ ngân sách suy luận động. Phần này cũng thảo luận về những hạn chế, ứng dụng rộng hơn và hướng phát triển trong tương lai.

Phụ lục:
Ví dụ phản hồi: Cung cấp ví dụ về phản hồi của ASV-IuB-50%, bao gồm các trường hợp có sử dụng voting và không sử dụng voting.
Tích lũy batch: Đưa ra cách triển khai tích lũy batch của Thuật toán 1 để giảm bớt vấn đề giới hạn tài nguyên tính toán.
Giải MILP: Trình bày cách sử dụng trình giải MILP trong SciPy để tối ưu hóa bài toán lập trình tuyến tính nguyên trong batch.
Xây dựng dữ liệu: Mô tả chi tiết các tập dữ liệu sử dụng, bao gồm Qsdpo, Agolden sdpo, Qmath, và Asample math.
Siêu tham số: Liệt kê các siêu tham số được sử dụng trong các thí nghiệm.
Thảo luận thêm: Bao gồm các thảo luận sâu hơn về ràng buộc ngân sách và CGPO trên DRL với LLaMA.
Bài báo kết luận rằng khung IBPO giúp mô hình tuân thủ ràng buộc và phân bổ ngân sách suy luận một cách linh hoạt, từ đó cải thiện hiệu suất và hiệu quả trong việc giải quyết các bài toán toán học.
