from docx import Document

file_path = r"C:\Users\97541\Downloads\day_12+函数2[习题答案].docx"
doc = Document(file_path)

content = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        content.append(text)

for i in range(36, 100):
    if i < len(content):
        print(f"{i+1:3d}: [{content[i][:80]}]")