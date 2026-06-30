import json

parts = [
    'part1.json',
    'part2.json',
    'part3a.json',
    'day13.json',
    'day14.json',
    'day15.json',
    'part4.json'
]

all_questions = []

for part in parts:
    try:
        with open(part, 'r', encoding='utf-8') as f:
            questions = json.load(f)
            all_questions.extend(questions)
            print(f'{part}: {len(questions)}题')
    except Exception as e:
        print(f'{part}: ERROR - {str(e)}')

for i, q in enumerate(all_questions, 1):
    q['total_order'] = i

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f'\n总题目数: {len(all_questions)}')

choice_count = sum(1 for q in all_questions if q['type'] == 'choice')
code_count = sum(1 for q in all_questions if q['type'] == 'code')
print(f'选择题: {choice_count}')
print(f'编程题: {code_count}')

days = {}
for q in all_questions:
    day = q.get('day', 'unknown')
    days[day] = days.get(day, 0) + 1

print('\n各天数题目数:')
for day in sorted(days.keys()):
    print(f'Day {day}: {days[day]}题')