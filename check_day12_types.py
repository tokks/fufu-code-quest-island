import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day12 = [q for q in questions if q['day'] == 12]

print("Day 12题目类型分布：")
for q in day12:
    status = "有答案" if q.get('answer') else "无答案"
    print(f"  第{q['number']}题 [{q['type']}]: {status}")

choice_count = sum(1 for q in day12 if q['type'] == 'choice')
code_count = sum(1 for q in day12 if q['type'] == 'code')
empty_choice = sum(1 for q in day12 if q['type'] == 'choice' and not q.get('answer'))
empty_code = sum(1 for q in day12 if q['type'] == 'code' and not q.get('answer'))

print(f"\n选择题: {choice_count}题, 缺失{empty_choice}题")
print(f"编程题: {code_count}题, 缺失{empty_code}题")