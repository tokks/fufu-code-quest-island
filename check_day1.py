import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day1 = [x for x in questions if x['day'] == 1]
print(f'day1题目数: {len(day1)}')
for x in day1:
    print(f'  {x["number"]}. {x["question"][:30]}')

print('\n所有天数统计:')
for day in range(1, 22):
    count = len([x for x in questions if x['day'] == day])
    print(f'  day{day}: {count}题')
