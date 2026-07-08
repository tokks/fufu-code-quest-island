from docx import Document

doc = Document(r"C:\Users\97541\Downloads\day_04+条件判断,运算与优先级,and和or[习题].docx")

for i, para in enumerate(doc.paragraphs):
    text = para.text.strip()
    if text:
        print(f"{i}: {text}")