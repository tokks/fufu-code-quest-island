import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

all_questions = []
results = []

for day in range(1, 22):
    questions = parse_single_day(day)
    all_questions.extend(questions)
    results.append(f'Day {day}: {len(questions)}题')

results.append(f'\n总题目数: {len(all_questions)}')

days = {}
for q in all_questions:
    day = q.get('day', 'unknown')
    days[day] = days.get(day, 0) + 1

results.append('\n各Day题目数:')
for day in sorted(days.keys()):
    results.append(f'  Day {day}: {days[day]}题')

with open('all_days_results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print('Done')