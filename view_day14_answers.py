from docx import Document

file_path = r"C:\Users\97541\Downloads\day_14+面向对象[习题答案].docx"
doc = Document(file_path)

content = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        content.append(text)

for i in range(min(80, len(content))):
    print(f"{i+1:3d}: [{content[i][:80]}]")