import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day3_new = [
    {
        "type": "choice",
        "day": 3,
        "number": 1,
        "question": "变量名命名规则中，以下哪个是非法的变量名？",
        "options": ["A. lala111", "B. 222baby", "C. Zhou", "D. _zhou"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 2,
        "question": "python3中，如何打印变量message的值，其中message的值为Hello, World!？",
        "options": ["A. print 'Hello, World!'", "B. print \"message\"", "C. print message", "D. print(message)"],
        "answer": "D",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 3,
        "question": "以下哪个是Python中的布尔值？",
        "options": ["A. 只有True", "B. false", "C. 1", "D. True 和 False"],
        "answer": "D",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 4,
        "question": "如何将整数10转换为字符串？",
        "options": ["A. str(10)", "B. int(\"10\")", "C. float(10)", "D. bool(10)"],
        "answer": "A",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 5,
        "question": "以下哪个函数用于获取对象的内存地址？",
        "options": ["A. type()", "B. id()", "C. len()", "D. bool()"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 6,
        "question": "在Python中，如何注释掉一行代码？",
        "options": ["A. 使用//在行首", "B. 使用#在行首", "C. 使用/* */包围代码", "D. 使用<!-- -->包围代码"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 7,
        "question": "注释在Python中有什么作用？",
        "options": ["A. 修改代码的执行逻辑。", "B. 使代码运行更快。", "C. 对代码进行解释说明，且不被执行。", "D. 存储临时不用的代码。"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 8,
        "question": "Python中用来输出内容的函数是什么？",
        "options": ["A. output()", "B. print()", "C. echo()", "D. display()"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 9,
        "question": "以下哪个选项正确描述了变量名的大小写敏感性？",
        "options": ["A. Zhou和zhou是同一个变量名。", "B. Zhou和zhou是两个不同的变量名。", "C. Python不区分大小写。", "D. 大小写敏感性取决于操作系统。"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 10,
        "question": "字面量的定义是什么？",
        "options": ["A. 代码中直接写出的固定值，如数字和文本。", "B. 代码中可变的值，如变量。", "C. 代码中的注释。", "D. 代码中的函数。"],
        "answer": "A",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 11,
        "question": "如何打印字面量？",
        "options": ["A. 使用input()函数。", "B. 使用print()函数。", "C. 直接在代码中显示。", "D. 无法打印字面量。"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 12,
        "question": "在python中，字符串类型使用哪种引号包围？",
        "options": ["A. 只能使用单引号。", "B. 只能使用双引号。", "C. 可以使用单引号、双引号或三引号，但必须配对。", "D. 不需要引号。"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 13,
        "question": "input()函数的作用是什么？",
        "options": ["A. 打印输出结果。", "B. 接收用户输入的数据。", "C. 计算输入数据的绝对值。", "D. 获取数据的内存地址。"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 14,
        "question": "如何将整数转换为字符串？",
        "options": ["A. 使用int()函数。", "B. 使用str()函数。", "C. 使用float()函数。", "D. 使用bool()函数。"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 15,
        "question": "以下哪个是Python中的转义字符？",
        "options": ["A. /n", "B. \\n", "C. //n", "D. |n"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 16,
        "question": "在Python中，\\t表示什么？",
        "options": ["A. 换行符", "B. 制表符", "C. 回车符", "D. 退格符"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 17,
        "question": "以下哪个表达式的结果是True？",
        "options": ["A. 3 > 5", "B. 10 == 10", "C. 5 != 5", "D. 2 < 1"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 18,
        "question": "以下哪个表达式的结果是False？",
        "options": ["A. True and True", "B. True or False", "C. not True", "D. False or True"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 19,
        "question": "None在Python中表示什么？",
        "options": ["A. 0", "B. 空字符串", "C. 空值", "D. 错误"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 20,
        "question": "以下哪个是Python中的正确编码格式？",
        "options": ["A. ASCII", "B. UTF-8", "C. GBK", "D. Unicode"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 3,
        "number": 21,
        "question": "以下哪个操作符用于比较两个对象的身份？",
        "options": ["A. ==", "B. is", "C. >", "D. <"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 22,
        "question": "编写一个程序，将字符串'123'转换为整数，将字符串'3.14'转换为浮点数。",
        "options": [],
        "answer": "num1 = int('123')\nnum2 = float('3.14')\nprint(num1)\nprint(num2)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 23,
        "question": "从控制台接收用户输入的一个浮点数，打印输入值的类型，再将其转换为整数并打印转换后的值及其类型。",
        "options": [],
        "answer": "num = float(input())\nprint(type(num))\nnum_int = int(num)\nprint(num_int)\nprint(type(num_int))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 24,
        "question": "编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串，包含单引号、双引号、反斜杠、换行符和制表符。",
        "options": [],
        "answer": "print('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 25,
        "question": "编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。",
        "options": [],
        "answer": "num1 = float(input(\"请输入第一个数字：\"))\nnum2 = float(input(\"请输入第二个数字：\"))\nprint(num1 + num2)\nprint(num1 - num2)\nprint(num1 * num2)\nprint(num1 / num2)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 26,
        "question": "编写一个程序，让用户输入文件名和扩展名，然后构造并打印出带有正确转义字符的完整文件路径，假定文件位于D:\\Documents\\Projects目录下。",
        "options": [],
        "answer": "filename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名：\")\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\nprint(path)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 27,
        "question": "编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。",
        "options": [],
        "answer": "value = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\nvalue = user_input\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 28,
        "question": "编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。",
        "options": [],
        "answer": "bool_true = True\nbool_false = False\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 29,
        "question": "编写代码，比较列表a=[1,2,3]和b=[1,2,3]以及c=a的内存地址，使用==和is进行比较。",
        "options": [],
        "answer": "a = [1, 2, 3]\nb = [1, 2, 3]\nc = a\nprint('a的内存地址：', id(a))\nprint('b的内存地址：', id(b))\nprint('c的内存地址：', id(c))\nprint('a == b', a == b)\nprint('a is b', a is b)\nprint('a == c', a == c)\nprint('a is c', a is c)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 3,
        "number": 30,
        "question": "编写逻辑表达式来判断变量x是否不等于y并且x小于15；判断age是否在18到65岁之间；判断name是否既不是Alice也不是Bob；判断score是否大于90并且小于100或者等于80。",
        "options": [],
        "answer": "x = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：', r)\nage = 10\nprint('18 <= age <= 65判断结果', 18 <= age <= 65)\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\", rel)",
        "total_order": 0
    }
]

questions = [q for q in questions if q['day'] != 3]
questions.extend(day3_new)

for i, q in enumerate(sorted(questions, key=lambda x: (x['day'], x['number'])), 1):
    q['total_order'] = i

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Day 3 已修复，共30题")