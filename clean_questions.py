import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for item in data:
    question = item.get('question', '')
    idx = question.find('题目要求：')
    if idx != -1:
        item['question'] = question[idx + 5:]

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("清理完成！")