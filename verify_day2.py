import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day2 = [q for q in questions if q['day'] == 2]

print("Day 2（变量森林）所有题目和答案：")
for q in day2:
    print(f"\n第{q['number']}题 [{q['type']}]:")
    print(f"  题目: {q['question']}")
    if q['options']:
        print(f"  选项: {q['options']}")
    print(f"  答案: {q['answer']}")