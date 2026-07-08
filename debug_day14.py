import sys
sys.path.insert(0, '.')
import traceback

try:
    from parse_exercises import parse_single_day
    print('导入成功')
    
    q = parse_single_day(14)
    print(f'Day 14: {len(q)}题')
except Exception as e:
    print(f'ERROR: {str(e)}')
    traceback.print_exc()