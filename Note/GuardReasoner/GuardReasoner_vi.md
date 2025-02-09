# GuardReasoner: Towards Reasoning-based LLM Safeguard

GuardReasoner là một cơ chế bảo vệ mới được thiết kế để nâng cao tính an toàn của các mô hình ngôn ngữ lớn (LLM) bằng cách trang bị cho chúng khả năng suy luận. Khi LLM ngày càng được triển khai trong các ứng dụng quan trọng về an toàn, việc đảm bảo độ tin cậy và khả năng kiểm chứng của chúng trở thành yếu tố thiết yếu. Các phương pháp bảo vệ truyền thống thường thiếu khả năng suy luận qua các tình huống phức tạp, hạn chế hiệu quả của chúng. GuardReasoner giải quyết vấn đề này bằng cách hướng dẫn mô hình bảo vệ học cách suy luận, từ đó cải thiện hiệu suất, khả năng giải thích và tính tổng quát hóa.

Cách hoạt động của GuardReasoner:
Tạo bộ dữ liệu:

GuardReasoner sử dụng bộ dữ liệu GuardReasonerTrain, bao gồm khoảng 127.000 mẫu và 460.000 bước suy luận chi tiết.
Bộ dữ liệu này được tổng hợp bằng cách sử dụng các mô hình tiên tiến như GPT-4o để tạo ra các quy trình suy luận toàn diện.
Huấn luyện tinh chỉnh có giám sát dựa trên suy luận (R-SFT - Reasoning Supervised Fine-Tuning):

Mô hình bảo vệ được huấn luyện trên dữ liệu suy luận tổng hợp để phát triển khả năng suy luận cơ bản.
Quá trình này được áp dụng cho các mô hình nền tảng có kích thước khác nhau, chẳng hạn như LLaMA 3.2 1B, 3B và LLaMA 3.1 8B, phù hợp với các nhu cầu ứng dụng khác nhau.
Tối ưu hóa ưu tiên mẫu khó trực tiếp (HS-DPO - Hard Sample Direct Preference Optimization):

Giai đoạn này giúp cải thiện khả năng suy luận của mô hình bằng cách tạo nhiều đầu ra kèm theo các bước suy luận cho mỗi đầu vào.
Các đầu ra đúng và suy luận đi kèm sẽ được sử dụng làm ví dụ tích cực, trong khi các đầu ra sai sẽ làm ví dụ tiêu cực.
Cách tiếp cận này giúp mô hình tập trung vào các trường hợp khó, qua đó nâng cao kỹ năng suy luận.
Nhờ các giai đoạn trên, GuardReasoner không chỉ cải thiện hiệu suất của LLM trong các nhiệm vụ quan trọng về an toàn mà còn tăng cường khả năng giải thích bằng cách cung cấp suy luận rõ ràng cho từng quyết định. Hơn nữa, bằng cách tập trung vào các trường hợp phức tạp và tinh vi trong quá trình huấn luyện, mô hình có khả năng tổng quát hóa tốt hơn, giúp nó thích ứng với nhiều tình huống khác nhau.

Các thử nghiệm trên 13 bộ dữ liệu đánh giá khác nhau trong 3 nhiệm vụ bảo vệ cho thấy GuardReasoner có hiệu suất vượt trội. Đặc biệt, phiên bản GuardReasoner 8B vượt qua GPT-4o+CoT với 5,74% điểm F1 và cao hơn LLaMA Guard 3 8B tới 20,84% điểm F1 trung bình, cho thấy tính hiệu quả trong việc tăng cường an toàn cho LLM.

GuardReasoner, bao gồm dữ liệu, mã nguồn và các mô hình (1B, 3B, 8B), đã được công khai trên GitHub để mọi người có thể khám phá và sử dụng.
