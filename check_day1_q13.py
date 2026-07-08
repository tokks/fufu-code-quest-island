import json
import ast

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day1 = [q for q in questions if q['day'] == 1]

q13 = [q for q in day1 if q['number'] == 13][0]
print(f"第13题 [{q13['type']}]:")
print(f"  题目: {q13['question']}")
print(f"  答案: {repr(q13['answer'])}")

try:
    compile(q13['answer'], '<string>', 'exec')
    print("  ✓ 语法正确")
except SyntaxError as e:
    print(f"  ✗ 语法错误: {e}")