import json
import re
import os
from docx import Document

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

def parse_docx(file_path):
    doc = Document(file_path)
    content = []
    for para in doc.paragraphs:
        try:
            text = para.text.strip()
            if text:
                content.append(text)
        except:
            pass
    return content

def find_answer_file(day_num):
    day_str = str(day_num)
    day_str2 = day_str.zfill(2)
    
    for filename in os.listdir(DOWNLOADS_DIR):
        if filename.endswith(".docx"):
            lower_name = filename.lower()
            has_day = f"day_{day_str2}" in lower_name or f"day_{day_str}" in lower_name or \
                      f"day{day_str2}" in lower_name or f"day{day_str}" in lower_name
            
            if has_day and ("习题答案" in filename or "参考答案" in filename):
                return os.path.join(DOWNLOADS_DIR, filename)
    return None

def extract_code_answers(content):
    code_answers = []
    i = 0
    
    while i < len(content):
        line = content[i]
        
        if "参考答案" in line or "参考代码" in line or "答案：" in line:
            i += 1
            code_lines = []
            in_code = True
            
            while i < len(content):
                code_line = content[i]
                
                if re.match(r'^\d+\.\s*', code_line) and len(code_lines) > 5:
                    break
                
                if "选择题" in code_line or "编程题" in code_line or "实战题" in code_line:
                    break
                
                if "解析" in code_line and len(code_lines) > 5:
                    break
                
                if re.search(r'(答案|解答)[：:]?\s*[ABCDE]', code_line):
                    break
                
                if code_line.strip():
                    code_lines.append(code_line)
                i += 1
            
            if code_lines:
                code_answers.append('\n'.join(code_lines))
            continue
        
        if line.startswith('#') or line.startswith('def ') or line.startswith('print(') or \
           line.startswith('for ') or line.startswith('if ') or line.startswith('while ') or \
           line.startswith('class ') or line.startswith('import ') or line.startswith('from ') or \
           line.startswith('return ') or line.startswith('='):
            code_lines = [line]
            i += 1
            while i < len(content):
                code_line = content[i]
                
                if re.match(r'^\d+\.\s*', code_line):
                    break
                
                if "选择题" in code_line or "编程题" in code_line or "实战题" in code_line:
                    break
                
                if re.search(r'(答案|解答)[：:]?\s*[ABCDE]', code_line):
                    break
                
                if code_line.strip():
                    code_lines.append(code_line)
                i += 1
            
            if len(code_lines) > 1:
                code_answers.append('\n'.join(code_lines))
            else:
                i += 1
            continue
        
        i += 1
    
    return code_answers

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

days_with_missing = [3, 7, 12, 14, 15, 18]

for day in days_with_missing:
    answer_path = find_answer_file(day)
    if not answer_path:
        print(f"Day {day}: 未找到答案文件")
        continue
    
    content = parse_docx(answer_path)
    code_answers = extract_code_answers(content)
    
    day_questions = [q for q in questions if q['day'] == day]
    missing_code = sum(1 for q in day_questions if q['type'] == 'code' and not q.get('answer'))
    
    print(f"\nDay {day}: 编程题{missing_code}题缺失, 提取到{len(code_answers)}个编程答案")
    
    code_idx = 0
    for q in day_questions:
        if q['type'] == 'code' and not q.get('answer'):
            if code_idx < len(code_answers):
                q['answer'] = code_answers[code_idx]
                code_idx += 1

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("\n=== 更新后的答案缺失情况 ===")
for day in days_with_missing:
    day_questions = [q for q in questions if q['day'] == day]
    missing_count = sum(1 for q in day_questions if not q.get('answer'))
    print(f"Day {day}: 缺失{missing_count}题")