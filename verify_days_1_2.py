import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print("=== Day 1 ===")
day1 = sorted([q for q in questions if q['day'] == 1], key=lambda x: x['number'])
for q in day1:
    print(f"第{q['number']}题: {q['question'][:50]}... -> {q['answer']}")

print("\n=== Day 2 ===")
day2 = sorted([q for q in questions if q['day'] == 2], key=lambda x: x['number'])
for q in day2:
    print(f"第{q['number']}题: {q['question'][:50]}... -> {q['answer']}")