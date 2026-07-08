import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

days_to_fix = [12, 14, 15, 18]

for day in days_to_fix:
    day_qs = sorted([q for q in questions if q['day'] == day], key=lambda x: x['number'])
    empty = [q for q in day_qs if not q.get('answer')]
    
    print(f"\n=== Day {day} ===")
    print(f"总题数: {len(day_qs)}, 缺失答案: {len(empty)}")
    print("有答案的题目:")
    for q in day_qs:
        if q.get('answer'):
            print(f"  第{q['number']}题 [{q['type']}]: {q['question'][:60]}...")
    
    print("\n缺失答案的题目:")
    for q in empty:
        print(f"  第{q['number']}题 [{q['type']}]: {q['question'][:60]}...")