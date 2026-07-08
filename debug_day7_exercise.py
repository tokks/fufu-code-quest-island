import re
from docx import Document

file_path = r"C:\Users\97541\Downloads\day_07+数据结构之集合与元组[习题].docx"
doc = Document(file_path)

content = []
for para in doc.paragraphs:
    text = para.text.strip()
    if text:
        content.append(text)

def is_question(line):
    if line.endswith('？') or line.endswith('?') or line.endswith('：') or line.endswith(':'):
        return True
    if re.match(r'第\s*\d+\s*题[：:]', line):
        return True
    if re.match(r'\d+\.\s*', line):
        return True
    return False

questions = []
i = 0
section_type = None

while i < len(content):
    line = content[i]
    
    if "选择题" in line:
        section_type = 'choice'
        print(f"=== 进入选择题部分 ===")
        i += 1
        continue
    elif "编程题" in line or "实战题" in line:
        section_type = 'code'
        print(f"=== 进入编程题部分 ===")
        i += 1
        continue
    elif line.startswith('day') or line.startswith('Day') or line.startswith('DAY'):
        i += 1
        continue
    
    if is_question(line):
        q_text = line
        options = []
        code_hint = []
        j = i + 1
        
        while j < len(content):
            next_line = content[j]
            
            if next_line.startswith('A') or next_line.startswith('B') or \
               next_line.startswith('C') or next_line.startswith('D') or \
               next_line.startswith('E'):
                if section_type == 'choice' or not section_type:
                    options.append(next_line)
                    j += 1
                    continue
                else:
                    break
            
            if "选择题" in next_line or "编程题" in next_line or "实战题" in next_line:
                break
            
            if is_question(next_line):
                break
            
            if next_line.strip():
                if section_type == 'choice' or not section_type:
                    options.append(next_line)
                else:
                    code_hint.append(next_line)
            j += 1
        
        if len(options) >= 2:
            q_type = 'choice'
        else:
            q_type = 'code'
        
        questions.append({
            'type': q_type,
            'number': len(questions) + 1,
            'question': q_text,
            'options': options[:4],
        })
        
        print(f"第{len(questions)}题 [{q_type}]: {q_text[:50]}...")
        if options:
            print(f"   选项: {[o[:30] for o in options]}")
        
        i = j
    else:
        i += 1

print(f"\n共解析出 {len(questions)} 题")