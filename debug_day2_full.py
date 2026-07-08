import os
import re
from docx import Document

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

def is_section_title(line, day_num):
    day_str = f"day{day_num}"
    has_day = day_str in line.lower() or f"day_{day_num}" in line.lower() or f"day {day_num}" in line.lower()
    has_type = "选择题" in line or "编程题" in line or "实战题" in line
    return has_day and has_type

def is_pure_section_title(line):
    return "选择题" in line or "编程题" in line or "实战题" in line

day_num = 2
day_str = "02"

for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx") and "习题答案" not in filename:
        if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
            print(f"文件路径: {filename}")
            
            doc = Document(os.path.join(DOWNLOADS_DIR, filename))
            exercise_content = []
            
            for para in doc.paragraphs:
                text = para.text.strip()
                if text:
                    exercise_content.append(text)
            
            print("\n=== 解析过程 ===")
            questions = []
            i = 0
            current_section = None
            
            while i < len(exercise_content):
                line = exercise_content[i]
                print(f"\ni={i}, line='{line}', current_section={current_section}")
                
                if is_section_title(line, day_num):
                    print(f"  -> is_section_title=True")
                    if "选择题" in line:
                        current_section = 'choice'
                        print(f"  -> 设置为选择题")
                    elif "编程题" in line or "实战题" in line:
                        current_section = 'code'
                        print(f"  -> 设置为编程题")
                    i += 1
                    continue
                
                if is_pure_section_title(line):
                    print(f"  -> is_pure_section_title=True")
                    if "选择题" in line:
                        current_section = 'choice'
                        print(f"  -> 设置为选择题")
                    elif "编程题" in line or "实战题" in line:
                        current_section = 'code'
                        print(f"  -> 设置为编程题")
                    i += 1
                    continue
                
                if current_section == 'choice':
                    print(f"  -> 在选择题区域")
                    if not line:
                        i += 1
                        continue
                    
                    if line[0] in 'ABCD':
                        print(f"  -> 是选项，跳过")
                        i += 1
                        continue
                    
                    q_text = line
                    print(f"  -> 是题目: '{q_text}'")
                    
                    options = []
                    j = i + 1
                    while j < len(exercise_content):
                        opt_line = exercise_content[j]
                        print(f"      j={j}, opt_line='{opt_line}'")
                        
                        if is_section_title(opt_line, day_num) or is_pure_section_title(opt_line):
                            print(f"      -> 遇到新章节，跳出")
                            break
                        
                        if opt_line.startswith('A') or opt_line.startswith('B') or opt_line.startswith('C') or opt_line.startswith('D'):
                            options.append(opt_line)
                            print(f"      -> 添加选项")
                            j += 1
                        elif opt_line and len(options) < 4:
                            options.append(opt_line)
                            j += 1
                        elif len(options) >= 4:
                            break
                        else:
                            j += 1
                    
                    if options:
                        questions.append({
                            'type': 'choice',
                            'question': q_text,
                            'options': options,
                            'answer': None
                        })
                        print(f"    -> 添加选择题")
                    i = j
                
                elif current_section == 'code':
                    print(f"  -> 在编程题区域")
                    if not line:
                        i += 1
                        continue
                    
                    if line[0] in 'ABCD':
                        i += 1
                        continue
                    
                    q_text = line
                    print(f"  -> 是题目: '{q_text}'")
                    
                    code_lines = []
                    j = i + 1
                    while j < len(exercise_content):
                        next_line = exercise_content[j]
                        if next_line.startswith('A') or next_line.startswith('B') or next_line.startswith('C') or next_line.startswith('D'):
                            break
                        if is_section_title(next_line, day_num) or is_pure_section_title(next_line):
                            break
                        if next_line.strip():
                            code_lines.append(next_line)
                        j += 1
                    
                    questions.append({
                        'type': 'code',
                        'question': q_text,
                        'options': [],
                        'answer': None,
                        'code_hint': '\n'.join(code_lines)
                    })
                    print(f"    -> 添加编程题")
                    i = j
                
                else:
                    print(f"  -> 未知区域，跳过")
                    i += 1
            
            print(f"\n=== 最终结果 ===")
            for q in questions:
                print(f"  [{q['type']}] {q['question'][:50]}")
            print(f"总题目数: {len(questions)}")
            break