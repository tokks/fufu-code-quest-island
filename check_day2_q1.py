import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day2_q1 = next(q for q in questions if q['day'] == 2 and q['number'] == 1)
print("Day 2 第1题:")
print(f"题目: {day2_q1['question']}")
print(f"选项: {day2_q1['options']}")
print(f"答案: {day2_q1['answer']}")