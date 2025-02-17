# **RSD (Reward-Guided Speculative Decoding)**

**RSD cải thiện hiệu suất suy luận của mô hình ngôn ngữ lớn (LLM) bằng cách kết hợp một mô hình nháp nhẹ với một mô hình mục tiêu mạnh hơn, sử dụng hàm phần thưởng để hướng dẫn lựa chọn đầu ra tại mỗi bước.**

## **1. Mô hình Nháp và Mô hình Mục Tiêu**

RSD sử dụng hai mô hình:

- **Mô hình nháp (Draft Model):** Một mô hình nhỏ, nhanh chóng để tạo các bước ứng viên.
- **Mô hình mục tiêu (Target Model):** Một mô hình lớn hơn, đáng tin cậy hơn, được dùng để xác minh và tinh chỉnh dự đoán.

## **2. Hàm Phần Thưởng**

- Hàm phần thưởng \( r(y*i | z_i) \) đánh giá chất lượng của từng bước \( y_i \) trong chuỗi \( y*{1:i} \) dựa trên lời nhắc \( x \).
- Giá trị phần thưởng cao hơn có nghĩa là đầu ra của mô hình có nhiều khả năng phù hợp với phản hồi mong muốn.

## **3. Lựa Chọn Thích Ứng**

- Không giống như **Speculative Decoding** truyền thống vốn duy trì tính không thiên vị nghiêm ngặt, RSD sử dụng tín hiệu phần thưởng để chọn lọc các đầu ra có giá trị cao thay vì loại bỏ các token không khớp ngay lập tức.

## **4. Các Bước của Thuật Toán RSD**

1. **Tạo Bước Nháp:** Mô hình nháp tạo một bước ứng viên \( \hat{y}\_i \).
2. **Tính Toán Phần Thưởng:** Hàm phần thưởng \( r(y_i | z_i) \) đánh giá chất lượng của bước này.
3. **Áp Dụng Tiêu Chí Chấp Nhận:**
   - Nếu \( r*i \) đạt tiêu chí \( A*\omega(r_i) \), \( \hat{y}\_i \) được giữ lại.
   - Nếu không, mô hình mục tiêu \( M \) tạo một bước mới.
4. **Lấy Mẫu từ Phân Phối Hỗn Hợp:**
   - Các bước được chấp nhận đến từ \( P_m \) (mô hình nháp).
   - Các bước bị từ chối đến từ \( P_M \) (mô hình mục tiêu).
5. **Lặp Lại Đến Khi Kết Thúc:** Quá trình tiếp tục đến khi xuất hiện token kết thúc (EOS) hoặc đạt độ dài tối đa \( N \).

## **5. Pha Trộn Động với Các Hàm Trọng Số**

RSD định nghĩa một phân phối \( P\_{RSD} \) là sự pha trộn động giữa mô hình nháp (\( P_m \)) và mô hình mục tiêu (\( P_M \)):

\[
P\_{RSD}(y_i | z_i) = w(y_i | z_i) P_m(y_i | z_i) + v(y_i | z_i) P_M(y_i | z_i)
\]

Trong đó:

- **\( w(\cdot) \) và \( v(\cdot) \)** là các hàm trọng số điều chỉnh dựa trên chất lượng đầu ra \( y_i | z_i \).
- **\( v(y_i | z_i) = \nu \)** với \( \nu \) là một hằng số đảm bảo mô hình mục tiêu luôn có vai trò dự phòng.
- **\( w(y_i | z_i) = \omega r(y_i | z_i) = \omega(r(y_i | z_i)) \)**, trong đó \( \omega(\cdot) \) ánh xạ phần thưởng thành mức độ tin cậy đối với \( P_m \).

## **6. Hành Vi của Hàm Trọng Số**

- **Khi \( r(y_i | z_i) \) cao:**
  - \( \omega(r(y_i | z_i)) \to 1 \), \( P_m \) chiếm ưu thế.
  - Hệ thống tin tưởng vào mô hình nháp để tiết kiệm tài nguyên.
- **Khi \( r(y_i | z_i) \) thấp:**
  - \( \omega(r(y_i | z_i)) \to 0 \), \( P_M \) chiếm ưu thế.
  - Mô hình mục tiêu xử lý các đầu ra chất lượng thấp để đảm bảo độ chính xác.

## **7. Trọng Số Tối Ưu**

Hàm trọng số tối ưu để tối đa hóa phần thưởng là **hàm bước nhị phân**:

\[
\omega*r(y|z) =
\begin{cases}
1, & \text{nếu } r(y|z) \geq \delta*\gamma(z) \\  
0, & \text{nếu } r(y|z) < \delta\_\gamma(z)
\end{cases}
\]

Trong đó \( \delta\_\gamma(z) \) là ngưỡng tối ưu.

## **8. Mô Hình Phần Thưởng Quá Trình (PRMs)**

- RSD sử dụng **Skywork-o1-Open-PRM** làm **Mô hình Phần thưởng Quá trình (PRM)**.
- Điểm phần thưởng dao động từ 0 đến 1, với điểm cao hơn biểu thị chất lượng tốt hơn.
- PRM được gọi tại mỗi bước suy luận để đánh giá chất lượng bước đó.

## **9. Tóm Tắt**

RSD điều chỉnh linh hoạt thời điểm sử dụng mô hình lớn hơn, giúp **giảm đáng kể số phép tính không cần thiết trong khi vẫn duy trì hoặc cải thiện chất lượng** so với các phương pháp suy luận truyền thống.

Sự cân bằng giữa **chi phí và chất lượng** này đặc biệt quan trọng trong các ứng dụng quy mô lớn, nơi **hiệu suất và độ chính xác** đều là yếu tố then chốt.
