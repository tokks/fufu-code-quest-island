import re
from docx import Document

file_path = r"C:\Users\97541\Downloads\day_07+数据结构之集合与元组[习题答案].docx"
doc = Document(file_path)

content = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        content.append(text)

answers = []
i = 0
while i < len(content):
    line = content[i]
    
    choice_match = re.search(r'(答案|解答)[：:]?\s*([ABCDE])', line)
    if choice_match:
        answer = choice_match.group(2)
        answers.append({'type': 'choice', 'answer': answer, 'line': line})
        i += 1
        continue
    
    if "参考答案" in line or "参考代码" in line:
        i += 1
        code_lines = []
        while i < len(content):
            code_line = content[i]
            if code_line.endswith('？') or code_line.endswith('?') or code_line.endswith('：') and len(code_lines) > 0:
                break
            if "选择题" in code_line or "编程题" in code_line or "实战题" in code_line:
                break
            if re.search(r'(答案|解答)[：:]?\s*[ABCDE]', code_line):
                break
            if code_line.strip():
                code_lines.append(code_line)
            i += 1
        if code_lines:
            answers.append({'type': 'code', 'answer': code_lines[:5], 'line': line})
        continue
    
    i += 1

print(f"提取到 {len(answers)} 个答案")
for ans in answers[:20]:
    print(f"  [{ans['type']}] {ans['answer']}")