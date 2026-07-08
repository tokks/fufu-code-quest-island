import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

print(f'总题目数: {len(questions)}')
print(f'第1题: Day{questions[0]["day"]} Q{questions[0]["number"]}')
print(f'最后一题: Day{questions[-1]["day"]} Q{questions[-1]["number"]}')

days = {}
for q in questions:
    day = q.get('day', 'unknown')
    days[day] = days.get(day, 0) + 1

print('\n各天数题目数:')
for day in sorted(days.keys()):
    print(f'Day {day}: {days[day]}题')