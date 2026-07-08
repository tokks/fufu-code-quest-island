import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"总题目数: {len(data)}\n")

days = {}
for q in data:
    day = q.get('day', 0)
    if day not in days:
        days[day] = []
    days[day].append(q)

for day in sorted(days.keys()):
    print(f"=== Day{day} ({len(days[day])}题) ===")
    for q in days[day]:
        answer = q.get('answer', 'NULL')
        status = 'OK' if answer and answer != 'NULL' else 'ERROR'
        print(f"  第{q['number']}题 [{q['type']}]: {status}")
    print()