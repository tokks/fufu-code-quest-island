import os
import re
from docx import Document

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

day_str = "01"
exercise_path = None

for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx") and "习题答案" not in filename:
        if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
            exercise_path = os.path.join(DOWNLOADS_DIR, filename)

print(f"文件路径: {exercise_path}")

doc = Document(exercise_path)
exercise_content = []

for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        exercise_content.append(text)

print("\n=== exercise_content ===")
for i, line in enumerate(exercise_content):
    print(f"{i}: '{line}'")
    print(f"   '选择题' in line: {'选择题' in line}")
    print(f"   line[0]: '{line[0]}'")

print("\n=== 解析过程 ===")
questions = []
i = 0

while i < len(exercise_content):
    line = exercise_content[i]
    print(f"\ni={i}, line='{line}'")
    
    if "选择题" in line:
        print("  -> 进入选择题分支")
        i += 1
        while i < len(exercise_content):
            current_line = exercise_content[i]
            print(f"    i={i}, current_line='{current_line}'")
            
            if "编程题" in current_line or "实战题" in current_line or "练习题" in current_line:
                print("    -> 遇到编程题，跳出")
                break
            
            if not current_line:
                i += 1
                continue
            
            if current_line[0] in 'ABCD' or re.match(r'^[ABCD][.．、]\s', current_line):
                print("    -> 是选项，跳过")
                i += 1
                continue
            
            q_text = current_line
            print(f"    -> 是题目: '{q_text}'")
            
            options = []
            j = i + 1
            
            while j < len(exercise_content):
                opt_line = exercise_content[j]
                print(f"      j={j}, opt_line='{opt_line}'")
                
                if opt_line.startswith('A') or opt_line.startswith('B') or opt_line.startswith('C') or opt_line.startswith('D'):
                    options.append(opt_line)
                    print(f"      -> 添加选项: {opt_line[:20]}...")
                    j += 1
                elif opt_line and not "编程题" in opt_line and not "实战题" in opt_line and not "练习题" in opt_line:
                    options.append(opt_line)
                    j += 1
                else:
                    break
            
            if options:
                questions.append({
                    'type': 'choice',
                    'question': q_text,
                    'options': options,
                    'answer': None
                })
                print(f"    -> 添加选择题: {q_text[:20]}...")
            else:
                print(f"    -> 没有选项，跳过")
            
            i = j
    
    elif "编程题" in line or "实战题" in line or "练习题" in line:
        print("  -> 进入编程题分支")
        i += 1
        while i < len(exercise_content):
            current_line = exercise_content[i]
            
            if not current_line:
                i += 1
                continue
            
            if current_line[0] in 'ABCD' or re.match(r'^[ABCD][.．、]\s', current_line):
                i += 1
                continue
            
            q_text = current_line
            
            code_lines = []
            j = i + 1
            
            while j < len(exercise_content):
                next_line = exercise_content[j]
                
                if next_line[0] in 'ABCD' or re.match(r'^[ABCD][.．、]\s', next_line):
                    break
                if "选择题" in next_line or "编程题" in next_line or "实战题" in next_line:
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
            print(f"    -> 添加编程题: {q_text[:20]}...")
            i = j
    
    else:
        print("  -> else分支")
        i += 1

print(f"\n=== 最终结果 ===")
for q in questions:
    print(f"  [{q['type']}] {q['question'][:30]}...")