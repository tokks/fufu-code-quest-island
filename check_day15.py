import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

try:
    q = parse_single_day(15)
    print(f'Day 15: {len(q)}题')
except Exception as e:
    print(f'Day 15: ERROR - {str(e)}')