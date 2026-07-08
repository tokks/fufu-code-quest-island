import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

try:
    q = parse_single_day(11)
    print(f'Day 11: {len(q)}题')
    if q:
        for i, question in enumerate(q[:3], 1):
            print(f'  {i}. [{question["type"]}] {question["question"][:50]}...')
    else:
        print('  无题目')
except Exception as e:
    print(f'Day 11: ERROR - {str(e)}')