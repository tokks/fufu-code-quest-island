import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from parse_exercises import parse_all_days

questions = parse_all_days()

with open('parse_output.txt', 'w', encoding='utf-8') as f:
    f.write(f"总题目数: {len(questions)}\n\n")
    
    days = {}
    for q in questions:
        day = q.get('day', 'unknown')
        days[day] = days.get(day, 0) + 1
    
    f.write("各Day题目数:\n")
    for day in sorted(days.keys()):
        f.write(f"  Day {day}: {days[day]}题\n")
    
    f.write("\n题目预览:\n")
    for q in questions[:5]:
        f.write(f"  [{q['type']}] Day {q['day']} Q{q['number']}: {q['question'][:50]}... 答案: {q.get('answer', '无')}\n")

print("输出已保存到 parse_output.txt")