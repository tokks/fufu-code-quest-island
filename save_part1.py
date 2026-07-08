import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

questions = []
for day in range(1, 6):
    q = parse_single_day(day)
    questions.extend(q)

import json
with open('exercises_part1.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f'Part1: {len(questions)}题')