import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parse_exercises import parse_all_days

print("开始解析所有题目...")
questions = parse_all_days()
print(f"解析完成！总题目数: {len(questions)}")

days = {}
for q in questions:
    day = q.get('day', 'unknown')
    days[day] = days.get(day, 0) + 1

print("各Day题目数:")
for day in sorted(days.keys()):
    print(f"  Day {day}: {days[day]}题")