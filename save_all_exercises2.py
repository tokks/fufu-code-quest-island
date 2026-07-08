import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

all_questions = []

for day in range(1, 22):
    q = parse_single_day(day)
    all_questions.extend(q)

for i, q in enumerate(all_questions, 1):
    q['total_order'] = i

import json
with open('exercises_full.json', 'w', encoding='utf-8') as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=2)

print(f'总题目数: {len(all_questions)}')