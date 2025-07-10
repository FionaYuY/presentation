#!/usr/bin/env python3
import pdfplumber
import sys

def read_pdf(file_path):
    """讀取PDF檔案內容"""
    try:
        with pdfplumber.open(file_path) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n\n"
            return full_text
    except Exception as e:
        print(f"讀取PDF時發生錯誤: {e}")
        return None

if __name__ == "__main__":
    pdf_path = "員工自評表.pdf"
    content = read_pdf(pdf_path)
    if content:
        print(content)
    else:
        print("無法讀取PDF檔案") 