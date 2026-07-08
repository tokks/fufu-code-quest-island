import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['day'] == 1 and q['number'] == 13:
        print("修复前:", repr(q['answer']))
        q['answer'] = "print('欢迎来到Python世界')\nprint('开始你的编程之旅吧')"
        print("修复后:", repr(q['answer']))

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("已修复")