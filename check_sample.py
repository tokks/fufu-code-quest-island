import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for i, q in enumerate(questions):
    if i < 5:
        print(f'\n=== 第{i+1}题 ===')
        print(f"Day: {q['day']}, Q: {q['number']}")
        print(f"Type: {q['type']}")
        print(f"Question: {q['question'][:100]}...")
        if q['type'] == 'choice':
            print(f"Options: {q['options']}")
        print(f"Answer: {repr(q.get('answer'))}")
        print(f"Code hint: {repr(q.get('code_hint', '')[:50])}")

print(f'\n=== 编程题示例 ===')
for i, q in enumerate(questions):
    if q['type'] == 'code':
        print(f'\nDay{q["day"]} Q{q["number"]}')
        print(f"Question: {q['question'][:100]}")
        print(f"Code hint: {repr(q.get('code_hint', '')[:100])}")
        print(f"Answer: {repr(q.get('answer'))}")
        break