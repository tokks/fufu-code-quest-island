import os
from docx import Document

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

days_with_missing = [3, 7, 12, 14, 15, 18]

for day in days_with_missing:
    day_str2 = str(day).zfill(2)
    found = False
    
    for filename in os.listdir(DOWNLOADS_DIR):
        if filename.endswith(".docx"):
            lower_name = filename.lower()
            has_day = f"day_{day_str2}" in lower_name or f"day{day_str2}" in lower_name
            
            if has_day and ("习题答案" in filename or "参考答案" in filename):
                file_path = os.path.join(DOWNLOADS_DIR, filename)
                doc = Document(file_path)
                
                print(f"\n{'='*60}")
                print(f"Day {day}: {filename}")
                print(f"{'='*60}")
                
                for i, para in enumerate(doc.paragraphs[:40], 1):
                    text = para.text.strip()
                    if text:
                        print(f"{i:3d}: [{text[:80]}]")
                
                found = True
                break
    
    if not found:
        print(f"\nDay {day}: 未找到答案文件")