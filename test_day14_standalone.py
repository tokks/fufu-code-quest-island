import os
import re
from docx import Document

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

def parse_docx(file_path):
    print(f'读取文件: {file_path}')
    doc = Document(file_path)
    content = []
    for para in doc.paragraphs:
        try:
            text = para.text.strip()
            if text:
                content.append(text)
        except Exception as e:
            print(f'  段落解析错误: {str(e)}')
    print(f'  读取到 {len(content)} 行')
    return content

day_num = 14
day_str = "14"

exercise_path = None
answer_path = None

for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx"):
        has_day = f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower()
        is_exercise = "习题答案" not in filename and "参考答案" not in filename
        is_answer = "习题答案" in filename or "参考答案" in filename
        
        if has_day and is_exercise:
            exercise_path = os.path.join(DOWNLOADS_DIR, filename)
            print(f'找到习题文件: {exercise_path}')
        elif has_day and is_answer:
            answer_path = os.path.join(DOWNLOADS_DIR, filename)
            print(f'找到答案文件: {answer_path}')

if exercise_path and answer_path:
    exercise_content = parse_docx(exercise_path)
    answer_content = parse_docx(answer_path)
    print(f'解析完成')
else:
    print('文件未找到')