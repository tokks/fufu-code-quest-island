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
        except Exception as e:
            pass
    
    return content

def is_section_title(line, day_num):
    day_str = f"day{day_num}"
    has_day = day_str in line.lower() or f"day_{day_num}" in line.lower() or f"day {day_num}" in line.lower()
    has_type = "选择题" in line or "编程题" in line or "实战题" in line
    return has_day and has_type

def is_pure_section_title(line):
    return "选择题" in line or "编程题" in line or "实战题" in line

def is_question(line):
    if line.endswith('？') or line.endswith('?') or line.endswith('：') or line.endswith(':'):
        return True
    if re.match(r'第\s*\d+\s*题[：:]', line):
        return True
    return False

def is_day_title(line, day_num):
    day_str = f"day{day_num}"
    return day_str in line.lower() or f"day_{day_num}" in line.lower() or f"day {day_num}" in line.lower()

def parse_single_day(day_num):
    day_str = f"{day_num:02d}"
    
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
    
    if not exercise_path or not answer_path:
        print(f"Day {day_num}: 缺少文件")
        return []
    
    print(f"处理 Day {day_num}...")
    
    exercise_content = parse_docx(exercise_path)
    answer_content = parse_docx(answer_path)
    
    questions = []
    i = 0
    current_section = None
    
    while i < len(exercise_content):
        line = exercise_content[i]
        
        if is_section_title(line, day_num) or is_pure_section_title(line):
            if "选择题" in line:
                current_section = 'choice'
            elif "编程题" in line or "实战题" in line:
                current_section = 'code'
            i += 1
            continue
        
        if is_day_title(line, day_num):
            i += 1
            continue
        
        if current_section == 'choice':
            if not line:
                i += 1
                continue
            
            if line[0] in 'ABCD':
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
                
                if is_section_title(opt_line, day_num) or is_pure_section_title(opt_line) or is_day_title(opt_line, day_num):
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
            
            if options:
                questions.append({
                    'type': 'choice',
                    'day': day_num,
                    'number': len(questions) + 1,
                    'question': q_text,
                    'options': options,
                    'answer': None
                })
            i = j
        
        elif current_section == 'code':
            if not line:
                i += 1
                continue
            
            if line[0] in 'ABCD':
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
                if is_section_title(next_line, day_num) or is_pure_section_title(next_line) or is_day_title(next_line, day_num):
                    break
                if is_question(next_line):
                    break
                if next_line.strip():
                    code_lines.append(next_line)
                j += 1
            
            questions.append({
                'type': 'code',
                'day': day_num,
                'number': len(questions) + 1,
                'question': q_text,
                'options': [],
                'answer': None,
                'code_hint': '\n'.join(code_lines)
            })
            i = j
        
        else:
            if is_question(line):
                q_text = line
                
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
                    continue
                else:
                    current_section = 'code'
                    continue
            
            i += 1
    
    answer_questions = []
    ai = 0
    current_section = None
    
    while ai < len(answer_content):
        line = answer_content[ai]
        
        if is_section_title(line, day_num) or is_pure_section_title(line):
            if "选择题" in line:
                current_section = 'choice'
            elif "编程题" in line or "实战题" in line:
                current_section = 'code'
            ai += 1
            continue
        
        if current_section == 'choice':
            if not line:
                ai += 1
                continue
            
            if line[0] in 'ABCD':
                ai += 1
                continue
            
            if not is_question(line):
                ai += 1
                continue
            
            match = re.search(r'[（(]([ABCD])[）)]', line)
            answer_char = match.group(1) if match else None
            
            answer_questions.append({
                'question': line.split('(')[0].split('（')[0].strip(),
                'answer': answer_char
            })
            ai += 1
        
        elif current_section == 'code':
            code_answer = []
            while ai < len(answer_content):
                al = answer_content[ai]
                if al.startswith('A') or al.startswith('B') or al.startswith('C') or al.startswith('D'):
                    break
                if is_section_title(al, day_num) or is_pure_section_title(al):
                    break
                if al.strip():
                    code_answer.append(al)
                ai += 1
            if code_answer:
                answer_questions.append({
                    'question': '编程题',
                    'answer': '\n'.join(code_answer)
                })
        
        else:
            ai += 1
    
    for i, q in enumerate(questions):
        if i < len(answer_questions):
            q['answer'] = answer_questions[i]['answer']
    
    return questions

def parse_all_days():
    all_questions = []
    
    for day in range(1, 22):
        try:
            day_questions = parse_single_day(day)
            print(f"  Day {day}: {len(day_questions)}题")
            all_questions.extend(day_questions)
        except Exception as e:
            print(f"  Day {day}: 错误 - {str(e)}")
    
    for i, q in enumerate(all_questions, 1):
        q['total_order'] = i
    
    return all_questions

if __name__ == "__main__":
    questions = []
    for day in range(1, 22):
        day_questions = parse_single_day(day)
        questions.extend(day_questions)
    
    for i, q in enumerate(questions, 1):
        q['total_order'] = i
    
    output_file = "exercises.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    choice_count = sum(1 for q in questions if q['type'] == 'choice')
    code_count = sum(1 for q in questions if q['type'] == 'code')
    
    print(f"\n解析完成！")
    print(f"总题目数: {len(questions)}")
    print(f"选择题: {choice_count}")
    print(f"编程题: {code_count}")
    print(f"结果已保存到 {output_file}")