import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

try:
    q = parse_single_day(13)
    print(f'Day 13: {len(q)}题')
except Exception as e:
    print(f'Day 13: ERROR - {str(e)}')