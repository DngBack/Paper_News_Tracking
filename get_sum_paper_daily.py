import os
import datetime
from summaries_paper import summarize, format_to_markdown_en, extract_text_from_pdf

def read_and_delete_pdfs(folder_path: str) -> dict:
    """
    Reads all PDF files in a given folder, extracts their text, 
    and deletes them after reading.

    Args:
        folder_path (str): The path to the folder containing PDF files.

    Returns:
        dict: A dictionary where keys are filenames and values are extracted text.
    """
    pdf_texts = {}
    
    # Lấy ngày hiện tại theo định dạng YYMMDD
    today_str = datetime.datetime.now().strftime("%y%m%d")

    # Định nghĩa thư mục và tệp lưu Markdown
    save_folder = os.path.join("Note", today_str)
    os.makedirs(save_folder, exist_ok=True)

    # Lặp qua tất cả các file trong thư mục
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            
            text_pdf = extract_text_from_pdf(pdf_path=pdf_path)
            summarize_texts = summarize(text=text_pdf)
            summarize_texts = format_to_markdown_en(sum_text_simple=summarize_texts)
            # Tạo đường dẫn file Markdown riêng cho từng PDF
            md_filename = os.path.splitext(filename)[0] + ".md"  # Đổi đuôi .pdf thành .md
            md_file_path = os.path.join(save_folder, md_filename)

            # Ghi nội dung vào file Markdown
            with open(md_file_path, "w", encoding="utf-8") as md_file:
                md_file.write(f"# Summary of {filename}\n\n{summarize_texts}\n")
            
            # Xoá file sau khi đọc xong
            os.remove(pdf_path)
    
    return pdf_texts

read_and_delete_pdfs("temp_pdfs")
