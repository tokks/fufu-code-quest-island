import sys
from io import StringIO

def capture_output(code):
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        exec(code, {})
    except Exception:
        pass
    sys.stdout = old_stdout
    return captured_output.getvalue()

correct_code = """num1 = int('123')
num2 = float('3.14')
print(num1)
print(num2)"""

user_code1 = "num1 = float(int('123'))"
user_code2 = "x = int('123')\ny = float('3.14')\nprint(x)\nprint(y)"
user_code3 = "a = 123\nb = 3.14\nprint(a)\nprint(b)"
user_code4 = "print(int('123'))\nprint(float('3.14'))"

print("正确代码输出:")
print(repr(capture_output(correct_code)))

print("\n用户代码1输出:")
print(repr(capture_output(user_code1)))

print("\n用户代码2输出:")
print(repr(capture_output(user_code2)))

print("\n用户代码3输出:")
print(repr(capture_output(user_code3)))

print("\n用户代码4输出:")
print(repr(capture_output(user_code4)))