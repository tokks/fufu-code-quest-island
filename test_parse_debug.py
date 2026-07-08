import sys
import json
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

all_questions = []
errors = []

for day in range(1, 22):
    try:
        q = parse_single_day(day)
        all_questions.extend(q)
        print(f'Day {day}: {len(q)}题')
    except Exception as e:
        errors.append(f'Day {day}: {str(e)}')
        print(f'Day {day}: ERROR - {str(e)}')

print(f'\n总题目数: {len(all_questions)}')

if errors:
    print('\n错误列表:')
    for e in errors:
        print(e)

with open('exercises_full.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print('\n已保存到 exercises_full.json')