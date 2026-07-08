import sys
sys.path.insert(0, '.')
from parse_exercises import parse_single_day

all_questions = []

for day in range(1, 6):
    questions = parse_single_day(day)
    if questions:
        all_questions.extend(questions)
        print(f'Day {day}: {len(questions)}题')
    else:
        print(f'Day {day}: 0题')

print(f'\n总题目数: {len(all_questions)}')