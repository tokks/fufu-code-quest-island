import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

try:
    q = parse_single_day(12)
    print(f'Day 12: {len(q)}题')
except Exception as e:
    print(f'Day 12: ERROR - {str(e)}')