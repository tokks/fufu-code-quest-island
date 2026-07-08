import sys
import json
import os
sys.path.insert(0, '.')
from parse_exercises import parse_all_days

questions = parse_all_days()

output_file = "exercises.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

choice_count = sum(1 for q in questions if q['type'] == 'choice')
code_count = sum(1 for q in questions if q['type'] == 'code')

results = []
results.append(f"解析完成！")
results.append(f"总题目数: {len(questions)}")
results.append(f"选择题: {choice_count}")
results.append(f"编程题: {code_count}")
results.append(f"结果已保存到 {output_file}")

days = {}
for q in questions:
    day = q.get('day', 'unknown')
    days[day] = days.get(day, 0) + 1

results.append("\n各Day题目数:")
for day in sorted(days.keys()):
    results.append(f"  Day {day}: {days[day]}题")

with open('parse_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

with open('parse_result.txt', 'r', encoding='utf-8') as f:
    print(f.read())