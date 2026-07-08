from docx import Document

file_path = r"C:\Users\97541\Downloads\day_12+函数2[习题答案].docx"
doc = Document(file_path)

print("=== Day12答案文件内容 ===")
for i, para in enumerate(doc.paragraphs[:80], 1):
    text = para.text.strip()
    if text:
        print(f"{i:3d}: [{text[:80]}]")