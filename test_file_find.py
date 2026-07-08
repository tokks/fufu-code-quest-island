import os

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

for day_num in range(1, 10):
    day_str = f"{day_num:02d}"
    exercise_path = None
    answer_path = None
    
    for filename in os.listdir(DOWNLOADS_DIR):
        if filename.endswith(".docx") and "习题答案" not in filename:
            if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
                exercise_path = filename
        elif filename.endswith(".docx") and "习题答案" in filename:
            if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
                answer_path = filename
    
    print(f"Day {day_num}: 习题={exercise_path}, 答案={answer_path}")