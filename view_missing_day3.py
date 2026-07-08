import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day3 = [q for q in questions if q['day'] == 3]

print("Day 3缺失答案的题目：")
for q in day3:
    if not q.get('answer'):
        print(f"\n第{q['number']}题 [{q['type']}]:")
        print(f"  题目: {q['question'][:100]}...")