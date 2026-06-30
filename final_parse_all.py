import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

questions = []
for day in range(1, 22):
    q = parse_single_day(day)
    questions.extend(q)
    print(f'Day {day}: {len(q)}题')

print(f'\n总题目数: {len(questions)}')

import json
with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)