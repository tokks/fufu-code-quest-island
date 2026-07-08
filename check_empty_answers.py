import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

days = {}
for q in questions:
    day = q['day']
    if day not in days:
        days[day] = {'total': 0, 'empty': 0}
    days[day]['total'] += 1
    if not q.get('answer'):
        days[day]['empty'] += 1

print("各Day答案缺失情况：")
for day in sorted(days.keys()):
    total = days[day]['total']
    empty = days[day]['empty']
    percent = (empty / total * 100) if total > 0 else 0
    print(f"Day {day:2d}: 共{total}题, 缺失{empty}题 ({percent:.1f}%)")