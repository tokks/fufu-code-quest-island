import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['day'] == 1 and q['number'] == 13:
        code = q['answer']
        print("答案内容:")
        print(code)
        print()
        try:
            compile(code, '<string>', 'exec')
            print("Syntax OK")
        except SyntaxError as e:
            print("Syntax Error:", e)
        break