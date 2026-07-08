import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

day5_fixed = [
    {
        "type": "code",
        "day": 5,
        "number": 1,
        "question": "第 01 题：用户登陆\n题目要求：编写一个Python程序，需要用户输入用户名（admin）和密码（password）后重复三次后登录成功。\n密码用户名每正确1次提示1次，记录3次输入中正确的次数。\n3次均符合要求：提示登录成功，反之提示失败，并给出失败次数。",
        "options": [],
        "answer": "success_count = 0\nfor i in range(3):\n    username = input('请输入用户名：')\n    password = input('请输入密码：')\n    if username == 'admin' and password == 'password':\n        success_count += 1\n        print('第{}次输入正确'.format(i+1))\n    else:\n        print('第{}次输入错误'.format(i+1))\nif success_count == 3:\n    print('登录成功')\nelse:\n    print('登录失败，失败次数：', 3 - success_count)",
        "code_hint": "使用for循环控制3次输入，记录正确次数，最后判断是否登录成功。",
        "total_order": 99
    },
    {
        "type": "code",
        "day": 5,
        "number": 2,
        "question": "第 02 题：用符号*打印正方形图案\n题目要求：打印一个5行5列的正方形图案。\n图形规律：5行5列，每行打印5个*。",
        "options": [],
        "answer": "for i in range(5):\n    for j in range(5):\n        print(\"*\", end=\"  \")\n    print()",
        "code_hint": "使用嵌套for循环，外层循环控制行数，内层循环控制列数。",
        "total_order": 100
    },
    {
        "type": "code",
        "day": 5,
        "number": 3,
        "question": "第 03 题：用符号*打印一个正直角三角形\n题目要求：打印一个正直角三角形图案。\n图形规律：观察图形，图形有5行，每一行的*是逐行增加的，直到第五行有5个星号。",
        "options": [],
        "answer": "for i in range(5):\n    for j in range(i + 1):\n        print(\"*\", end=\"  \")\n    print()",
        "code_hint": "外层循环控制行数，内层循环根据行数决定每行打印的星号数量。",
        "total_order": 101
    },
    {
        "type": "code",
        "day": 5,
        "number": 4,
        "question": "第 04 题：用符号*打印一个倒直角三角形\n题目要求：打印一个倒直角三角形图案。\n图形规律：总共有5行。第1行有5个星号，第2行有4个星号，依此类推，直到第5行只有1个星号。",
        "options": [],
        "answer": "for i in range(5, 0, -1):\n    for j in range(i):\n        print(\"*\", end=\"  \")\n    print()",
        "code_hint": "外层循环从5递减到1，内层循环根据当前行数决定打印的星号数量。",
        "total_order": 102
    },
    {
        "type": "code",
        "day": 5,
        "number": 5,
        "question": "第 05 题：for循环实现99乘法表\n题目要求：使用for循环实现99乘法表。\n规律说明：99乘法表是对称的，是一个9x9的表格。每一行和每一列的数字从1递增到9。\n假设行数是i、列数是j，行由外层循环变量i控制，表示当前是第几行，也决定了该行的第一个乘数。\n列由内层循环变量j控制，表示当前行中的第几个乘法表达式。",
        "options": [],
        "answer": "for i in range(1, 10):\n    for j in range(1, i + 1):\n        print('{}x{}={}'.format(j, i, i * j), end='\\t')\n    print()",
        "code_hint": "使用嵌套for循环，外层循环控制行数，内层循环控制列数，每行的列数等于行数。",
        "total_order": 103
    },
    {
        "type": "code",
        "day": 5,
        "number": 6,
        "question": "第 06 题：存钱罐\n题目要求：你有一个存钱罐，每天存入相同数量的硬币。\n编写一个Python程序，通过用户输入每天存入的硬币数量和总天数，使用for循环计算并输出从第1天到指定天数，你总共存入了多少硬币。",
        "options": [],
        "answer": "coins_per_day = int(input('请输入每天存入的硬币数量：'))\ntotal_days = int(input('请输入总天数：'))\ntotal_coins = 0\nfor day in range(1, total_days + 1):\n    total_coins += coins_per_day\n    print('第{}天：累计存入{}枚硬币'.format(day, total_coins))\nprint('总共存入{}枚硬币'.format(total_coins))",
        "code_hint": "使用for循环累加每天存入的硬币数量，计算总存款。",
        "total_order": 104
    }
]

data = [item for item in data if item.get('day') != 5]
data.extend(day5_fixed)
data.sort(key=lambda x: x['total_order'])

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("第5天数据修复完成！")
print(f"修复后第5天题目数量: {len([item for item in data if item.get('day') == 5])}")