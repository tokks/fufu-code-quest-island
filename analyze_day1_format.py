from docx import Document
import re

file_path = r"C:\Users\97541\Downloads\day_01+Python编程基础之环境搭建与语法入门[习题].docx"
doc = Document(file_path)

print("=== Day1习题文件格式分析 ===")
for i, para in enumerate(doc.paragraphs[:50], 1):
    text = para.text.strip()
    if text:
        print(f"{i:3d}: [{text}]")