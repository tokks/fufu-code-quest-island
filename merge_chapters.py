import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

day11_items = [i for i in data if i['day'] == 11]
day12_items = [i for i in data if i['day'] == 12]

for idx, item in enumerate(day12_items, 3):
    item['day'] = 11
    item['number'] = idx

merged_items = day11_items + day12_items

other_items = [i for i in data if i['day'] not in [11, 12]]

for item in other_items:
    if item['day'] > 12:
        item['day'] -= 1

result = other_items + merged_items
result.sort(key=lambda x: x['total_order'])

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("exercises.json 合并完成！")
for day in range(1, 21):
    day_items = [i for i in result if i.get('day') == day]
    if day_items:
        code_items = [i for i in day_items if i.get('type') == 'code']
        choice_items = [i for i in day_items if i.get('type') == 'choice']
        print(f"Day {day}: {len(day_items)} 题 ({len(choice_items)} choice, {len(code_items)} code)")