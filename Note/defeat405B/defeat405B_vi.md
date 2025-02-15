# Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling

## Phiên Bản Tiếng Việt

Bài báo **"Can 1B LLM Surpass 405B LLM? Rethinking Compute-Optimal Test-Time Scaling"** nghiên cứu cách các mô hình ngôn ngữ nhỏ (LLM) có thể vượt trội hơn các mô hình lớn bằng cách sử dụng **compute-optimal test-time scaling (TTS)**. TTS là một phương pháp cải thiện hiệu suất của LLM bằng cách phân bổ nhiều tài nguyên tính toán hơn trong giai đoạn suy luận. Bài báo này tập trung vào hai câu hỏi chính:

1. Làm thế nào để tối ưu hóa việc mở rộng tính toán trong quá trình suy luận trên các mô hình chính sách khác nhau, mô hình thưởng theo quá trình (Process Reward Models - PRMs), và các mức độ khó của bài toán?
2. Việc mở rộng tính toán có thể cải thiện hiệu suất của LLM đến mức nào trên các nhiệm vụ phức tạp? Liệu các mô hình nhỏ có thể vượt qua các mô hình lớn nhờ phương pháp này không?

## Các Khái Niệm và Phương Pháp Chính

- **Test-Time Scaling (TTS):** Cải thiện khả năng suy luận của LLM bằng cách phân bổ thêm tài nguyên tính toán trong quá trình suy luận. Có hai loại TTS:
  - **Internal TTS:** Huấn luyện LLM suy nghĩ chậm lại bằng phương pháp **Chain-of-Thought (CoT)** dài.
  - **External TTS:** Cải thiện suy luận thông qua phương pháp lấy mẫu hoặc tìm kiếm với một LLM cố định. Thách thức là tối ưu hóa tài nguyên tính toán cho từng bài toán.
- **Process Reward Models (PRMs):** Hướng dẫn quá trình sinh văn bản và chọn câu trả lời cuối cùng, giúp mở rộng tính toán trong quá trình suy luận. PRMs hoạt động như bộ kiểm tra trong TTS.
- **Compute-Optimal TTS:** Tối ưu hóa việc phân bổ tài nguyên tính toán cho từng bài toán. Chiến lược này phụ thuộc nhiều vào mô hình chính sách, PRM, và độ khó của bài toán.
- **Mô hình chính sách (Policy Models):** LLM tạo ra lời giải.
- **Markov Decision Process (MDP):** Bài toán suy luận được mô hình hóa như một MDP, gồm các thành phần \((S, A, P, R, \gamma)\), trong đó:
  - \(S\) là không gian trạng thái,
  - \(A\) là không gian hành động,
  - \(P\) là hàm chuyển đổi trạng thái,
  - \(R\) là hàm thưởng,
  - \(\gamma\) là hệ số chiết khấu.
- **Best-of-N (BoN):** Mô hình chính sách tạo ra \(N\) câu trả lời, sau đó sử dụng phương pháp chấm điểm và bỏ phiếu để chọn kết quả cuối cùng.
- **Beam Search:** Mô hình chính sách tạo ra từng bước giải, bộ kiểm tra chọn các bước tốt nhất để tiếp tục tìm kiếm cho đến khi đạt độ sâu tối đa hoặc gặp token kết thúc.
- **Diverse Verifier Tree Search (DVTS):** Mở rộng beam search bằng cách chia quá trình tìm kiếm thành các cây con, mỗi cây được khám phá độc lập bằng beam search.
- **Reward-Aware Compute-Optimal TTS:** Chiến lược kết hợp hàm thưởng vào khung TTS tối ưu hóa tính toán, giúp TTS thích ứng với mô hình chính sách, prompt và hàm thưởng, tạo ra một khung làm việc tổng quát hơn cho TTS.

## Thí Nghiệm và Kết Quả

Bài báo thực hiện các thí nghiệm trên tập dữ liệu **MATH-500** và **AIME24**, sử dụng PRMs có kích thước từ **1.5B** đến **72B** tham số và mô hình chính sách có kích thước từ **0.5B** đến **72B** tham số. Các kết quả chính bao gồm:

- Chiến lược **compute-optimal TTS** phụ thuộc rất nhiều vào mô hình chính sách, PRM và độ khó của bài toán.
- Mô hình nhỏ có thể vượt qua mô hình lớn bằng compute-optimal TTS. Ví dụ, một LLM **3B** có thể vượt qua một LLM **405B**.
- Phương pháp TTS tối ưu phụ thuộc vào PRM được sử dụng. **BoN** tốt hơn các chiến lược khác khi dùng PRM **Math-Shepherd** và **RLHFlow**, trong khi các phương pháp dựa trên tìm kiếm hoạt động tốt hơn với PRM **Skywork** và **Qwen2.5-Math**.
- Phương pháp TTS tối ưu phụ thuộc vào mô hình chính sách. Với mô hình nhỏ, các phương pháp tìm kiếm tốt hơn BoN, trong khi với mô hình lớn, BoN hiệu quả hơn.
- Phương pháp TTS tối ưu khác nhau tùy theo độ khó của bài toán. Với mô hình nhỏ, BoN tốt hơn cho bài toán dễ, trong khi beam search tốt hơn cho bài toán khó.
- **PRMs có xu hướng thiên vị theo độ dài bước giải.** Dữ liệu huấn luyện của **RLHFlow-PRM-Deepseek-8B** dài hơn so với **RLHFlow-PRM-Mistral-8B**, dẫn đến thiên vị với các đầu ra dài hơn.
- **PRMs nhạy cảm với phương pháp bỏ phiếu.** **Skywork-PRM-7B** hoạt động tốt hơn với **PRM-Vote** so với **PRM-Max**, trong khi **Qwen2.5-Math-PRM-7B** không quá nhạy cảm với phương pháp bỏ phiếu.

## Ảnh Hưởng của Compute-Optimal TTS

- **Cải thiện hiệu suất:** **Llama-3.2-3B-Instruct** với compute-optimal TTS vượt trội hơn **Llama-3.1-405B-Instruct** trên **MATH-500** và **AIME24**.
- **Tăng hiệu quả:** Compute-optimal TTS có thể hiệu quả hơn so với phương pháp bỏ phiếu đa số (majority voting) và cải thiện đáng kể khả năng suy luận so với CoT.
- **So sánh với phương pháp Long-CoT:** **TTS với Qwen2.5-7B-Instruct** vượt trội hơn **rStar-Math, Eurus-2, SimpleRL**, và **Satori** trên cả **MATH-500** và **AIME24**.

## Hạn Chế và Hướng Phát Triển Tương Lai

Bài báo chỉ ra một số hạn chế và hướng phát triển trong tương lai:

- Mở rộng TTS sang các nhiệm vụ khác như lập trình và hóa học.
- Khám phá các phương pháp hiệu quả hơn cho compute-optimal TTS.
