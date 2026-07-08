import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

questions = parse_single_day(2)
print(f'Day 2 题目数: {len(questions)}')
for q in questions:
    print(f'  [{q["type"]}] {q["question"][:50]}...')