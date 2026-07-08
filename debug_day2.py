import os
from docx import Document

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

day_str = "02"

for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx") and "习题答案" not in filename:
        if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
            print(f"文件名: {filename}")
            doc = Document(os.path.join(DOWNLOADS_DIR, filename))
            print("\n文档内容:")
            for i, para in enumerate(doc.paragraphs):
                text = para.text.strip()
                if text:
                    print(f"{i}: '{text}'")
            break