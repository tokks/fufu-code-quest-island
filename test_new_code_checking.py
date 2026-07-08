import sys
sys.path.insert(0, '.')

from levels import LevelManager

manager = LevelManager()

level = {
    'question': "字符串与数字类型（int、float）之间的转换：将字符串'123'转换为整数，将字符串'3.14'转换为浮点数",
    'answer': """num1 = int('123')
num2 = float('3.14')
print(num1)
print(num2)""",
    'type': 'code'
}

test_cases = [
    ("num1 = float(int('123'))", "用户代码1: 链式转换"),
    ("x = int('123')\ny = float('3.14')\nprint(x)\nprint(y)", "用户代码2: 不同变量名"),
    ("a = 123\nb = 3.14\nprint(a)\nprint(b)", "用户代码3: 直接赋值"),
    ("print(int('123'))\nprint(float('3.14'))", "用户代码4: 直接输出"),
    ("num1 = int('123')", "用户代码5: 只转换整数"),
    ("num1 = int('abc')", "用户代码6: 错误转换"),
]

print("测试结果:")
for code, desc in test_cases:
    result = manager.check_answer(level, code)
    status = "通过" if result else "失败"
    print("{}: {}".format(desc, status))