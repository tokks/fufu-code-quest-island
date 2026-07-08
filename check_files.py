import os

DOWNLOADS_DIR = r"C:\Users\97541\Downloads"

files = []
for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx"):
        files.append(filename)

print("所有docx文件:")
for f in sorted(files):
    print(f"  {f}")

print("\n--- Day 2 文件检查 ---")
day_str = "02"
for filename in os.listdir(DOWNLOADS_DIR):
    if filename.endswith(".docx"):
        if f"day_{day_str}" in filename.lower() or f"day{day_str}" in filename.lower():
            print(f"  匹配: {filename}")