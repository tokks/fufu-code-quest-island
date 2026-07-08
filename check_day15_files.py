import os

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

day_str = "15"

for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx"):
        if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
            print(f'找到: {filename}')