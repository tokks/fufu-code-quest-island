import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

all_questions = []
errors = []

for day in range(1, 22):
    try:
        q = parse_single_day(day)
        all_questions.extend(q)
    except Exception as e:
        errors.append(f'Day {day}: {str(e)}')

import json
with open('exercises_full.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

with open('parse_result.txt', 'w', encoding='utf-8') as f:
    f.write(f'总题目数: {len(all_questions)}\n')
    if errors:
        f.write('\n错误:\n')
        for e in errors:
            f.write(e + '\n')