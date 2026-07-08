import os
import re
from docx import Document

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

day_num = 2
day_str = "02"

def is_section_title(line, day_num):
    day_str = f"day{day_num}"
    has_day = day_str in line.lower() or f"day_{day_num}" in line.lower() or f"day {day_num}" in line.lower()
    has_type = "选择题" in line or "编程题" in line or "实战题" in line
    return has_day and has_type

def is_pure_section_title(line):
    return "选择题" in line or "编程题" in line or "实战题" in line

def is_question(line):
    return line.endswith('？') or line.endswith('?') or line.endswith('：') or line.endswith(':')

print(f"=== Day {day_num} 文件查找 ===")
exercise_path = None
answer_path = None

for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx") and "习题答案" not in filename:
        if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
            exercise_path = os.path.join(DOWNLOADS_DIR, filename)
            print(f"找到习题文件: {filename}")
    elif filename.endswith(".docx") and "习题答案" in filename:
        if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
            answer_path = os.path.join(DOWNLOADS_DIR, filename)
            print(f"找到答案文件: {filename}")

if not exercise_path or not answer_path:
    print("缺少文件！")
    exit()

print(f"\n=== Day {day_num} 文件内容 ===")
doc = Document(exercise_path)
content = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        content.append(text)

for i, line in enumerate(content):
    print(f"{i}: '{line}'")

print(f"\n=== Day {day_num} 解析 ===")
questions = []
i = 0
current_section = None

while i < len(content):
    line = content[i]
    print(f"\ni={i}, line='{line[:30]}...', current_section={current_section}")
    
    if is_section_title(line, day_num):
        print("  -> is_section_title=True")
        if "选择题" in line:
            current_section = 'choice'
        elif "编程题" in line or "实战题" in line:
            current_section = 'code'
        i += 1
        continue
    
    if is_pure_section_title(line):
        print("  -> is_pure_section_title=True")
        if "选择题" in line:
            current_section = 'choice'
        elif "编程题" in line or "实战题" in line:
            current_section = 'code'
        i += 1
        continue
    
    if current_section == 'choice':
        print("  -> 在选择题区域")
        if not line:
            i += 1
            continue
        
        if line[0] in 'ABCD':
            i += 1
            continue
        
        if not is_question(line):
            print(f"    -> 不是问题格式 '{line}', 跳过")
            i += 1
            continue
        
        q_text = line
        print(f"    -> 是题目: '{q_text}'")
        
        options = []
        j = i + 1
        while j < len(content):
            opt_line = content[j]
            print(f"      j={j}, opt_line='{opt_line[:30]}...'")
            
            if is_section_title(opt_line, day_num) or is_pure_section_title(opt_line):
                print("      -> 遇到新章节，跳出")
                break
            
            if opt_line.startswith('A') or opt_line.startswith('B') or opt_line.startswith('C') or opt_line.startswith('D'):
                options.append(opt_line)
                j += 1
            elif is_question(opt_line):
                print("      -> 遇到新问题，跳出")
                break
            elif opt_line:
                options.append(opt_line)
                j += 1
            else:
                j += 1
        
        if options:
            questions.append({
                'type': 'choice',
                'question': q_text,
                'options': options,
                'answer': None
            })
            print(f"    -> 添加选择题，共{len(options)}个选项")
        i = j
    
    elif current_section == 'code':
        print("  -> 在编程题区域")
        if not line:
            i += 1
            continue
        
        if line[0] in 'ABCD':
            i += 1
            continue
        
        q_text = line
        print(f"    -> 是题目: '{q_text}'")
        
        code_lines = []
        j = i + 1
        while j < len(content):
            next_line = content[j]
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
        print("  -> 未知区域，跳过")
        i += 1

print(f"\n=== 结果 ===")
print(f"总题目数: {len(questions)}")
for q in questions:
    print(f"  [{q['type']}] {q['question'][:50]}")