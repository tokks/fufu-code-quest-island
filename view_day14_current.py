import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day14 = sorted([q for q in questions if q['day'] == 14], key=lambda x: x['number'])

for q in day14:
    print(f"\n第{q['number']}题 [{q['type']}]:")
    print(f"  题目: {q['question'][:80]}...")
    if q['type'] == 'choice':
        print(f"  选项: {q['options']}")
    print(f"  答案: {q['answer'] if q['answer'] else '(空)'}")