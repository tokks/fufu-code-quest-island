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

def extract_all_answers(content):
    answers = []
    i = 0
    
    while i < len(content):
        line = content[i]
        
        match1 = re.search(r'[（(]\s*([ABCDE])\s*[）)]', line)
        if match1:
            answers.append({'type': 'choice', 'answer': match1.group(1)})
            i += 1
            continue
        
        match2 = re.search(r'(答案|解答)[：:]?\s*([ABCDE])', line)
        if match2:
            answers.append({'type': 'choice', 'answer': match2.group(2)})
            i += 1
            continue
        
        match3 = re.search(r'解析[：:]?\s*([ABCDE])', line)
        if match3:
            answers.append({'type': 'choice', 'answer': match3.group(1)})
            i += 1
            continue
        
        if "参考答案" in line or "参考代码" in line:
            i += 1
            code_lines = []
            while i < len(content):
                code_line = content[i]
                
                if re.match(r'\d+\.\s*', code_line) and len(code_lines) > 10:
                    break
                
                if "选择题" in code_line or "编程题" in code_line or "实战题" in code_line:
                    break
                
                if re.search(r'(答案|解答|解析)[：:]?\s*[ABCDE]', code_line):
                    break
                
                if code_line.strip():
                    code_lines.append(code_line)
                i += 1
            if code_lines:
                answers.append({'type': 'code', 'answer': '\n'.join(code_lines)})
            continue
        
        i += 1
    
    return answers

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

days_with_missing = [3, 7, 12, 14, 15, 18]

for day in days_with_missing:
    answer_path = find_answer_file(day)
    if not answer_path:
        print(f"Day {day}: 未找到答案文件")
        continue
    
    content = parse_docx(answer_path)
    answers = extract_all_answers(content)
    
    day_questions = [q for q in questions if q['day'] == day]
    missing_count = sum(1 for q in day_questions if not q.get('answer'))
    
    print(f"\nDay {day}: {len(day_questions)}题, 缺失{missing_count}题, 提取到{len(answers)}个答案")
    
    choice_idx = 0
    code_idx = 0
    
    for q in day_questions:
        if q.get('answer'):
            continue
        
        if q['type'] == 'choice':
            if choice_idx < len(answers) and answers[choice_idx]['type'] == 'choice':
                q['answer'] = answers[choice_idx]['answer']
                choice_idx += 1
        else:
            if code_idx < len(answers) and answers[code_idx]['type'] == 'code':
                q['answer'] = answers[code_idx]['answer']
                code_idx += 1

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("\n=== 更新后的答案缺失情况 ===")
for day in days_with_missing:
    day_questions = [q for q in questions if q['day'] == day]
    missing_count = sum(1 for q in day_questions if not q.get('answer'))
    print(f"Day {day}: 缺失{missing_count}题")