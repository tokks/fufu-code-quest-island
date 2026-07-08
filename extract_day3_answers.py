from docx import Document
import re

file_path = r"C:\Users\97541\Downloads\day_03+转义字符,布尔类型和None类型,逻辑判断,编码格式[习题答案].docx"
doc = Document(file_path)

content = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        content.append(text)

print("=== Day3答案文件内容 ===")
for i, line in enumerate(content[:100], 1):
    choice_match = re.search(r'(答案|解答)[：:]?\s*([ABCDE])', line)
    if choice_match:
        print(f"{i:3d}: [{line}] --> 答案: {choice_match.group(2)}")
    elif "参考答案" in line or "参考代码" in line:
        print(f"{i:3d}: [{line}] --> 编程题答案开始")
    else:
        print(f"{i:3d}: [{line}]")