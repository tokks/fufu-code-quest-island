from docx import Document
import re

file_path = r"C:\Users\97541\Downloads\day_10+字典,深拷贝与浅拷贝,列表推导式-习题.docx"
doc = Document(file_path)

print("=== Day10习题文件格式分析 ===")
for i, para in enumerate(doc.paragraphs[:80], 1):
    text = para.text.strip()
    if text:
        is_q = False
        if re.match(r'第\s*\d+\s*题[：:]', text):
            is_q = True
        elif re.match(r'\d+\.\s*', text):
            is_q = True
        elif text.endswith('？') or text.endswith('?'):
            is_q = True
        print(f"{i:3d}: [{text}] {'<-- 题目' if is_q else ''}")