import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day2_q9 = next(q for q in questions if q['day'] == 2 and q['number'] == 9)
print("Day 2 第9题:")
print(f"题目: {day2_q9['question']}")
print(f"答案:\n{day2_q9['answer']}")