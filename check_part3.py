import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

for day in range(11, 16):
    try:
        q = parse_single_day(day)
        print(f'Day {day}: {len(q)}题')
    except Exception as e:
        print(f'Day {day}: ERROR - {str(e)}')