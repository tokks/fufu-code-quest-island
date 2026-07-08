import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

try:
    q = parse_single_day(14)
    print(f'Day 14: {len(q)}题')
except Exception as e:
    import traceback
    print(f'Day 14: ERROR - {str(e)}')
    traceback.print_exc()