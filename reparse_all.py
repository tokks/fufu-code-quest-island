import os
import json
import re
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

def is_question(line):
    if line.endswith('？') or line.endswith('?') or line.endswith('：') or line.endswith(':'):
        return True
    if re.match(r'第\s*\d+\s*题[：:]', line):
        return True
    return False

def parse_day(day_num):
    day_str = str(day_num)
    exercise_path = None
    answer_path = None

    for filename in os.listdir(DOWNLOADS_DIR):
        if filename.endswith(".docx"):
            has_day = f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower()
            is_exercise = "习题答案" not in filename and "参考答案" not in filename
            is_answer = "习题答案" in filename or "参考答案" in filename
            
            if has_day and is_exercise:
                exercise_path = os.path.join(DOWNLOADS_DIR, filename)
            elif has_day and is_answer:
                answer_path = os.path.join(DOWNLOADS_DIR, filename)

    if not exercise_path:
        print(f'Day {day_num}: 未找到习题文件')
        return []

    exercise_content = parse_docx(exercise_path)
    
    if answer_path:
        answer_content = parse_docx(answer_path)
    else:
        answer_content = []

    questions = []
    i = 0
    current_section = None

    while i < len(exercise_content):
        line = exercise_content[i]
        
        if "选择题" in line:
            current_section = 'choice'
            i += 1
            continue
        elif "编程题" in line or "实战题" in line:
            current_section = 'code'
            i += 1
            continue
        elif f"day{day_num}" in line.lower() or f"day_{day_str}" in line.lower():
            i += 1
            continue
        
        if current_section == 'choice':
            if not line or line[0] in 'ABCD':
                i += 1
                continue
            if not is_question(line):
                i += 1
                continue
            
            q_text = line
            options = []
            j = i + 1
            while j < len(exercise_content):
                opt_line = exercise_content[j]
                if "选择题" in opt_line or "编程题" in opt_line or "实战题" in opt_line:
                    break
                if opt_line.startswith('A') or opt_line.startswith('B') or opt_line.startswith('C') or opt_line.startswith('D'):
                    options.append(opt_line)
                    j += 1
                elif is_question(opt_line):
                    break
                elif opt_line:
                    options.append(opt_line)
                    j += 1
                else:
                    j += 1
            
            questions.append({
                'type': 'choice', 
                'day': day_num, 
                'number': len(questions)+1, 
                'question': q_text, 
                'options': options, 
                'answer': None
            })
            i = j
        
        elif current_section == 'code':
            if not line or line[0] in 'ABCD':
                i += 1
                continue
            if not is_question(line):
                i += 1
                continue
            
            q_text = line
            code_lines = []
            j = i + 1
            while j < len(exercise_content):
                next_line = exercise_content[j]
                if next_line.startswith('A') or next_line.startswith('B') or next_line.startswith('C') or next_line.startswith('D'):
                    break
                if "选择题" in next_line or "编程题" in next_line or "实战题" in next_line:
                    break
                if is_question(next_line):
                    break
                if next_line.strip():
                    code_lines.append(next_line)
                j += 1
            
            questions.append({
                'type': 'code', 
                'day': day_num, 
                'number': len(questions)+1, 
                'question': q_text, 
                'options': [], 
                'answer': None, 
                'code_hint': '\n'.join(code_lines)
            })
            i = j
        
        else:
            if is_question(line):
                j = i + 1
                has_options = False
                while j < len(exercise_content):
                    next_line = exercise_content[j]
                    if next_line.startswith('A') or next_line.startswith('B') or next_line.startswith('C') or next_line.startswith('D'):
                        has_options = True
                        break
                    if is_question(next_line):
                        break
                    j += 1
                
                if has_options:
                    current_section = 'choice'
                else:
                    current_section = 'code'
                continue
            
            i += 1

    if answer_content:
        answer_index = 0
        for q in questions:
            if answer_index >= len(answer_content):
                break
            
            if q['type'] == 'choice':
                while answer_index < len(answer_content):
                    answer_line = answer_content[answer_index]
                    if answer_line.startswith('A') or answer_line.startswith('B') or \
                       answer_line.startswith('C') or answer_line.startswith('D') or \
                       answer_line.startswith('答案'):
                        break
                    answer_index += 1
                
                if answer_index < len(answer_content):
                    answer_line = answer_content[answer_index]
                    if answer_line.startswith('答案'):
                        match = re.search(r'答案[：:]?\s*([ABCD])', answer_line)
                        if match:
                            q['answer'] = match.group(1)
                    elif answer_line[0] in 'ABCD':
                        q['answer'] = answer_line[0]
                    answer_index += 1
            
            else:
                code_answer = []
                while answer_index < len(answer_content):
                    answer_line = answer_content[answer_index]
                    if answer_line.startswith('A') or answer_line.startswith('B') or \
                       answer_line.startswith('C') or answer_line.startswith('D') or \
                       (is_question(answer_line) and len(code_answer) > 0):
                        break
                    code_answer.append(answer_line)
                    answer_index += 1
                
                if code_answer:
                    q['answer'] = '\n'.join(code_answer)

    return questions

all_questions = []
for day in range(1, 22):
    questions = parse_day(day)
    all_questions.extend(questions)
    print(f'Day {day}: {len(questions)}题')

for i, q in enumerate(all_questions, 1):
    q['total_order'] = i

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f'\n总题目数: {len(all_questions)}')
choice_count = sum(1 for q in all_questions if q['type'] == 'choice')
code_count = sum(1 for q in all_questions if q['type'] == 'code')
print(f'选择题: {choice_count}')
print(f'编程题: {code_count}')