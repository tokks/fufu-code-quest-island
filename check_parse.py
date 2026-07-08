import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'总题目数: {len(data)}')
print()
print('前5题:')
for i, d in enumerate(data[:5], 1):
    print(f'{i}. Day{d["day"]} Q{d["number"]}')
    print(f'   问题: {d["question"][:100]}...')
    if d['answer']:
        print(f'   答案: {d["answer"][:80]}...')
    print()