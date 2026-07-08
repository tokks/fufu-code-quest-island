import json
from docx import Document

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day7 = [q for q in questions if q['day'] == 7]

print("=== Day 7 当前题目 ===")
for q in day7:
    status = "有答案" if q.get('answer') else "无答案"
    print(f"第{q['number']}题 [{q['type']}]: {status}")
    if q.get('answer'):
        print(f"  题目: {q['question'][:60]}")
        print(f"  答案: {q['answer'][:60]}")
    print()

print("\n=== Day 7 答案文件 ===")
file_path = r"C:\Users\97541\Downloads\day_07+数据结构之集合与元组[习题答案].docx"
doc = Document(file_path)
for i, para in enumerate(doc.paragraphs[:50], 1):
    text = para.text.strip()
    if text:
        print(f"{i:3d}: [{text[:60]}]")