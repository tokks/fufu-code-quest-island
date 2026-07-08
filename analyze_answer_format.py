from docx import Document
import re

file_path = r"C:\Users\97541\Downloads\day_07+数据结构之集合与元组[习题答案].docx"
doc = Document(file_path)

print("=== Day7答案文件详细分析 ===")
for i, para in enumerate(doc.paragraphs, 1):
    text = para.text.strip()
    if text:
        is_answer = bool(re.search(r'[答解]案[：:]?\s*([ABCDE])', text))
        is_code_answer = "参考答案" in text or "参考代码" in text
        is_question = text.endswith('？') or text.endswith('?') or text.endswith('：')
        
        print(f"{i:3d}: [{text[:80]}]")
        if is_answer:
            print(f"   --> 选择题答案")
        if is_code_answer:
            print(f"   --> 编程题答案开始")
        if is_question:
            print(f"   --> 题目")