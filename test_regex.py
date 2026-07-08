import re

test_lines = [
    '解答：A',
    '解答：A、B',
    '答案：C',
    '解答：D、E',
    '答案：A',
    '参考答案：',
]

for line in test_lines:
    match = re.search(r'[答解]案[：:]?\s*([ABCDE][、，,]*)*([ABCDE])', line)
    if match:
        print(f'"{line}" -> 匹配成功: {match.group(1)}, {match.group(2)}')
    else:
        print(f'"{line}" -> 匹配失败')