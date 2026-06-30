import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

problem_days = [7, 12, 14, 15, 18]

for day_num in problem_days:
    day_questions = [q for q in data if q.get('day') == day_num]
    empty_count = sum(1 for q in day_questions if not q.get('answer'))
    print(f"\n=== Day{day_num} (共{len(day_questions)}题, {empty_count}题答案为空) ===")
    
    for q in day_questions:
        if not q.get('answer'):
            print(f"  第{q['number']}题 [{q['type']}]: {q['question'][:50]}...")