from docx import Document

file_path = r"C:\Users\97541\Downloads\day_07+数据结构之集合与元组[习题答案].docx"
doc = Document(file_path)

print("Day7答案文件内容:")
for i, para in enumerate(doc.paragraphs, 1):
    text = para.text.strip()
    if text:
        print(f"{i:3d}: {text}")