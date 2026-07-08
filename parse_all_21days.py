import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

all_questions = []

for day in range(1, 22):
    try:
        q = parse_single_day(day)
        all_questions.extend(q)
        print(f'Day {day}: {len(q)}题')
    except Exception as e:
        print(f'Day {day}: ERROR - {str(e)}')

print(f'\n总题目数: {len(all_questions)}')

import json
with open('exercises_all.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)