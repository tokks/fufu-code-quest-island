from docx import Document

file_path = r"C:\Users\97541\Downloads\day_03+转义字符,布尔类型和None类型,逻辑判断,编码格式[习题答案].docx"
doc = Document(file_path)

print("=== Day3答案文件完整内容 ===")
for i, para in enumerate(doc.paragraphs, 1):
    text = para.text.strip()
    if text:
        print(f"{i:3d}: [{text[:100]}]")