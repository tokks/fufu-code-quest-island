import os
from docx import Document

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

day_str = "04"

exercise_path = None
answer_path = None

for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx"):
        has_day = f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower()
        is_exercise = "习题答案" not in filename and "参考答案" not in filename
        is_answer = "习题答案" in filename or "参考答案" in filename
        
        if has_day and is_exercise:
            exercise_path = filename
        elif has_day and is_answer:
            answer_path = filename

print(f"Day 4: 习题={exercise_path}, 答案={answer_path}")

if exercise_path:
    doc = Document(os.path.join(DOWNLOADS_DIR, exercise_path))
    content = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            content.append(text)
    
    print(f"\n内容预览（前20行）:")
    for i, line in enumerate(content[:20]):
        print(f"{i}: '{line}'")