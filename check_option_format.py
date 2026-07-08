import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

choice_questions = [q for q in questions if q['type'] == 'choice']

has_letter_prefix = []
no_letter_prefix = []

for q in choice_questions:
    options = q['options']
    has_prefix = all(opt.startswith(('A.', 'B.', 'C.', 'D.', 'E.')) for opt in options)
    if has_prefix:
        has_letter_prefix.append(q)
    else:
        no_letter_prefix.append(q)

print(f"有字母前缀的选择题: {len(has_letter_prefix)}")
print(f"没有字母前缀的选择题: {len(no_letter_prefix)}")

if no_letter_prefix:
    print("\n没有字母前缀的题目示例:")
    for q in no_letter_prefix[:3]:
        print(f"Day {q['day']} 第{q['number']}题:")
        print(f"  选项: {q['options']}")
        print()