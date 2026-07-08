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

def find_files(day_num):
    day_str = str(day_num)
    day_str2 = day_str.zfill(2)
    
    exercise_path = None
    answer_path = None

    for filename in os.listdir(DOWNLOADS_DIR):
        if filename.endswith(".docx"):
            lower_name = filename.lower()
            has_day = f"day_{day_str2}" in lower_name or f"day_{day_str}" in lower_name or \
                      f"day{day_str2}" in lower_name or f"day{day_str}" in lower_name
            
            if has_day:
                is_exercise = "习题答案" not in filename and "参考答案" not in filename
                is_answer = "习题答案" in filename or "参考答案" in filename
                
                if is_exercise:
                    exercise_path = os.path.join(DOWNLOADS_DIR, filename)
                elif is_answer:
                    answer_path = os.path.join(DOWNLOADS_DIR, filename)

    return exercise_path, answer_path

def parse_exercise_file(content):
    questions = []
    i = 0
    in_choice_section = False
    in_code_section = False
    in_fill_section = False
    q_number = 0
    
    while i < len(content):
        line = content[i]
        
        if "选择题" in line:
            in_choice_section = True
            in_code_section = False
            in_fill_section = False
            i += 1
            continue
        
        if "编程题" in line or "实战题" in line:
            in_code_section = True
            in_choice_section = False
            in_fill_section = False
            i += 1
            continue
        
        if "填空题" in line:
            in_fill_section = True
            in_choice_section = False
            in_code_section = False
            i += 1
            continue
        
        if line.startswith('day') or line.startswith('Day') or line.startswith('DAY'):
            i += 1
            continue
        
        if re.match(r'\d+\.\s*', line):
            q_number += 1
            q_text = line
            options = []
            j = i + 1
            
            while j < len(content):
                next_line = content[j]
                
                if next_line.startswith('A') or next_line.startswith('B') or \
                   next_line.startswith('C') or next_line.startswith('D') or \
                   next_line.startswith('E'):
                    options.append(next_line)
                    j += 1
                    continue
                
                if re.match(r'\d+\.\s*', next_line):
                    break
                
                if "选择题" in next_line or "编程题" in next_line or "实战题" in next_line or "填空题" in next_line:
                    break
                
                if in_choice_section and next_line.strip():
                    options.append(next_line)
                    j += 1
                    continue
                
                if in_code_section and next_line.strip():
                    q_text += '\n' + next_line
                    j += 1
                    continue
                
                if not in_choice_section and not in_code_section:
                    q_text += '\n' + next_line
                    j += 1
                    continue
                
                j += 1
            
            if len(options) >= 2:
                q_type = 'choice'
            elif in_code_section:
                q_type = 'code'
            else:
                q_type = 'choice'
            
            questions.append({
                'type': q_type,
                'day': 0,
                'number': q_number,
                'question': q_text,
                'options': options[:5],
                'answer': None,
            })
            i = j
            continue
        
        if in_fill_section and line.endswith('？'):
            q_number += 1
            questions.append({
                'type': 'choice',
                'day': 0,
                'number': q_number,
                'question': line,
                'options': [],
                'answer': None,
            })
            i += 1
            continue
        
        i += 1
    
    return questions

def extract_answers(content):
    answers = []
    i = 0
    
    while i < len(content):
        line = content[i]
        
        choice_match = re.search(r'(答案|解答)[：:]?\s*([ABCDE])', line)
        if choice_match:
            answer = choice_match.group(2)
            answers.append({'type': 'choice', 'answer': answer})
            i += 1
            continue
        
        if "参考答案" in line or "参考代码" in line:
            i += 1
            code_lines = []
            while i < len(content):
                code_line = content[i]
                
                if re.match(r'\d+\.\s*', code_line) and len(code_lines) > 0:
                    break
                
                if "选择题" in code_line or "编程题" in code_line or "实战题" in code_line or "填空题" in code_line:
                    break
                
                if re.search(r'(答案|解答)[：:]?\s*[ABCDE]', code_line):
                    break
                
                if code_line.strip():
                    code_lines.append(code_line)
                i += 1
            if code_lines:
                answers.append({'type': 'code', 'answer': '\n'.join(code_lines)})
            continue
        
        i += 1
    
    return answers

def parse_day(day_num):
    exercise_path, answer_path = find_files(day_num)

    if not exercise_path:
        print(f'Day {day_num}: 未找到习题文件')
        return []

    exercise_content = parse_docx(exercise_path)
    questions = parse_exercise_file(exercise_content)
    
    for q in questions:
        q['day'] = day_num
    
    if answer_path:
        answer_content = parse_docx(answer_path)
        answers = extract_answers(answer_content)
        
        choice_idx = 0
        code_idx = 0
        
        for q in questions:
            if q['type'] == 'choice':
                if choice_idx < len(answers) and answers[choice_idx]['type'] == 'choice':
                    q['answer'] = answers[choice_idx]['answer']
                    choice_idx += 1
            else:
                if code_idx < len(answers) and answers[code_idx]['type'] == 'code':
                    q['answer'] = answers[code_idx]['answer']
                    code_idx += 1

    return questions

all_questions = []
for day in range(1, 22):
    questions = parse_day(day)
    all_questions.extend(questions)
    print(f'Day {day}: {len(questions)}题')

for i, q in enumerate(all_questions, 1):
    q['total_order'] = i

with open('exercises_new.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f'\n总题目数: {len(all_questions)}')
choice_count = sum(1 for q in all_questions if q['type'] == 'choice')
code_count = sum(1 for q in all_questions if q['type'] == 'code')
empty_answers = sum(1 for q in all_questions if not q.get('answer'))
print(f'选择题: {choice_count}')
print(f'编程题: {code_count}')
print(f'答案为空: {empty_answers}')