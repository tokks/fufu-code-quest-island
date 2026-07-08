from docx import Document

doc = Document(r"C:\Users\97541\Downloads\day_01+Python基本概念和pycharm的使用[习题答案].docx")

for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    if text:
        print(f"{i}: {text}")