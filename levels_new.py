import json

REGIONS = [
    {
        "id": "region_1",
        "name": "新手村",
        "description": "Python基础概念与PyCharm使用",
        "icon": "fa-house",
        "levels": [
            {
                "id": "day1_q1",
                "name": "第1题",
                "description": "day1选择题...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "day1选择题",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day1_q2",
                "name": "第2题",
                "description": "day1编程题...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "day1编程题",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_2",
        "name": "变量森林",
        "description": "字面量、变量、字符串和数字",
        "icon": "fa-tree",
        "levels": [
            {
                "id": "day2_q1",
                "name": "第1题",
                "description": "下面选项中，哪个是Python中的整数字面量？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "下面选项中，哪个是Python中的整数字面量？",
                "type": "choice",
                "options": [
                    "'123'"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q2",
                "name": "第2题",
                "description": "14...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "14",
                "type": "choice",
                "options": [
                    "1101",
                    "下面选项中，哪个是符合Python变量命名规则的正确赋值语句？",
                    "1num = 10",
                    "int = 10"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q3",
                "name": "第3题",
                "description": "int_01 = 10...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "int_01 = 10",
                "type": "choice",
                "options": [
                    "下面关于python变量类型的说法，正确的是？",
                    "变量类型必须在定义时指定",
                    "变量类型在赋值时确定",
                    "变量类型一旦确定就不能改变"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q4",
                "name": "第4题",
                "description": "变量类型与赋值无关...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "变量类型与赋值无关",
                "type": "choice",
                "options": [
                    "下面变量x的类型是什么？",
                    "x = 123_456_789",
                    "print(x)",
                    "print(type(x))"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q5",
                "name": "第5题",
                "description": "float...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "float",
                "type": "choice",
                "options": [
                    "int",
                    "str",
                    "bool",
                    "在Python中，使用input()函数接收用户输入时，输入的值默认是什么类型？"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q6",
                "name": "第6题",
                "description": "输入什么类型就是什么类型。...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "输入什么类型就是什么类型。",
                "type": "choice",
                "options": [
                    "字符串类型。",
                    "整数类型。",
                    "浮点数类型。",
                    "在Python中，print函数的主要用途是什么？"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q7",
                "name": "第7题",
                "description": "从用户那里接收输入...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "从用户那里接收输入",
                "type": "choice",
                "options": [
                    "将数据写入文件",
                    "在控制台输出内容",
                    "执行数学计算",
                    "在Python中，下面哪个函数用于创建浮点数？"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q8",
                "name": "第8题",
                "description": "double()...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "double()",
                "type": "choice",
                "options": [
                    "Number()",
                    "float()",
                    "float32()",
                    "在Python中，有变量x = -5和y = -3.14，以下哪个代码片段可以正确地将x和y转换为它们的绝对值？"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q9",
                "name": "第9题",
                "description": "x = abs(x) 和 y = abs(y)...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "x = abs(x) 和 y = abs(y)",
                "type": "choice",
                "options": [
                    "x = |x| 和 y = |y|",
                    "x = fabs(x) 和 y = fabs(y)",
                    "x = absolute(x) 和 y = absolute(y)",
                    "在PyCharm中，默认用来添加注释、移除注释的快捷键是：（多选）"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q10",
                "name": "第10题",
                "description": "Ctrl + /...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "Ctrl + /",
                "type": "choice",
                "options": [
                    "Ctrl + D",
                    "Shift+Alt+鼠标从光标位置按住下滑或上滑",
                    "command + /"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day2_q11",
                "name": "第11题",
                "description": "字符串与数字类型（int、float）之间的转换：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "字符串与数字类型（int、float）之间的转换：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_3",
        "name": "数据洞穴",
        "description": "转义字符、布尔类型、逻辑判断",
        "icon": "fa-cave",
        "levels": [
            {
                "id": "day3_q1",
                "name": "第1题",
                "description": "选择题：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "选择题：",
                "type": "code",
                "options": [],
                "answer": "# 编写一个程序，让用户在控制台输入他们的名字，然后打印出来。打印示例：\"你好，Alice！欢迎来到Python的世界。\"\n# 详细步骤：\n#       1.定义一个变量名name，使用input()接收用户输入。\n#       2.使用print()打印：\"你好，\" + name + \"！欢迎来到Python的世界。\"\nname = input(\"请输入您的名字：\")\nprint(\"你好，\" + name + \"！欢迎来到Python的世界。\")\n'''---------------------------第 2 题：浮点数之和--------------------------------'''\n# 编写一个程序，让用户输入两个数字，在将数字转换为浮点数（float），然后两个数字相加，显示它们的和。\n# 详细步骤：\n#       1.定义变量num1，使用input()接收用户输入的数字1.\n#       2.定义变量num2，使用input()接收用户输入的数字2.\n#       3.定义变量sums，将上面两个字符串，转成float，再相加。\n#       4.使用print()。输出第3点的sums。\nnum1 = input(\"输入第一个数字：\")\nnum2 = input(\"输入第二个数字：\")\nsums = float(num1) + float(num2)\nprint(\"两数之和：\",sums)\n'''---------------------------第 3 题：字符串与数字的类型转换--------------------------------'''\n# 编写一个程序，让用户分别输入一个字符串形式的整数和一个小数（浮点数），然后将它们转换为对应的数值类型并打印出来。\n# 详细步骤：\n#       1.定义一个变量：str_int，使其可以再控制台输入一个整数类型的字符串。\n#       2.定义一个变量：str_float，使其可以再控制台输入一个浮点类型的字符串。\n#       3.分别定义两个变量：int_value 和 float_value，分别转换为int和float类型。\n#       4.分别打印int_value 和 float_value 以及 type(int_value) 和 type(float_value)\n# 获取用户输入的字符串形式的整数，并转换为整型\nstr_int = input(\"请输入一个字符串形式的整数：\")\nint_value = int(str_int)\nprint(int_value)\nprint(type(int_value))\n# 获取用户输入的字符串形式的小数，并转换为浮点型\nstr_float = input(\"请输入一个字符串形式的小数：\")\nfloat_value = float(str_float)\nprint(float_value)\nprint(type(float_value))\n'''---------------------------第 4 题：使用转义字符打印特殊文本--------------------------------'''\n# 描述: 编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串。\n# 字符串中应包含不同类型的引号（单引号和双引号）、反斜杠（作为转义字符）、换行符和制表符。\n# 要求程序能够正确处理这些特殊字符，并按照预期格式输出。\n# 示例语句：\"她说了：'Python是'最'棒的语言！'\"\n# 详细步骤：\n#       1.打印包含单引号和双引号的字符串\n#       2.打印包含换行符和制表符的字符串\n#       3.使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别\nprint('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")\nprint(\"并且原始字符串表示为：\")\nprint(r\"她说了：'Python是'最'棒的语言！'\")  # 原始字符串，不需要转义反斜杠\n'''---------------------------第 5 题：简单的数学运算--------------------------------'''\n# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 编写一个程序，让用户在控制台输入他们的名字，然后打印出来。打印示例：\"你好，Alice！欢迎来到Python的世界。\"\n# 详细步骤：\n#       1.定义一个变量名name，使用input()接收用户输入。\n#       2.使用print()打印：\"你好，\" + name + \"！欢迎来到Python的世界。\"\nname = input(\"请输入您的名字：\")\nprint(\"你好，\" + name + \"！欢迎来到Python的世界。\")\n'''---------------------------第 2 题：浮点数之和--------------------------------'''\n# 编写一个程序，让用户输入两个数字，在将数字转换为浮点数（float），然后两个数字相加，显示它们的和。\n# 详细步骤：\n#       1.定义变量num1，使用input()接收用户输入的数字1.\n#       2.定义变量num2，使用input()接收用户输入的数字2.\n#       3.定义变量sums，将上面两个字符串，转成float，再相加。\n#       4.使用print()。输出第3点的sums。\nnum1 = input(\"输入第一个数字：\")\nnum2 = input(\"输入第二个数字：\")\nsums = float(num1) + float(num2)\nprint(\"两数之和：\",sums)\n'''---------------------------第 3 题：字符串与数字的类型转换--------------------------------'''\n# 编写一个程序，让用户分别输入一个字符串形式的整数和一个小数（浮点数），然后将它们转换为对应的数值类型并打印出来。\n# 详细步骤：\n#       1.定义一个变量：str_int，使其可以再控制台输入一个整数类型的字符串。\n#       2.定义一个变量：str_float，使其可以再控制台输入一个浮点类型的字符串。\n#       3.分别定义两个变量：int_value 和 float_value，分别转换为int和float类型。\n#       4.分别打印int_value 和 float_value 以及 type(int_value) 和 type(float_value)\n# 获取用户输入的字符串形式的整数，并转换为整型\nstr_int = input(\"请输入一个字符串形式的整数：\")\nint_value = int(str_int)\nprint(int_value)\nprint(type(int_value))\n# 获取用户输入的字符串形式的小数，并转换为浮点型\nstr_float = input(\"请输入一个字符串形式的小数：\")\nfloat_value = float(str_float)\nprint(float_value)\nprint(type(float_value))\n'''---------------------------第 4 题：使用转义字符打印特殊文本--------------------------------'''\n# 描述: 编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串。\n# 字符串中应包含不同类型的引号（单引号和双引号）、反斜杠（作为转义字符）、换行符和制表符。\n# 要求程序能够正确处理这些特殊字符，并按照预期格式输出。\n# 示例语句：\"她说了：'Python是'最'棒的语言！'\"\n# 详细步骤：\n#       1.打印包含单引号和双引号的字符串\n#       2.打印包含换行符和制表符的字符串\n#       3.使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别\nprint('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")\nprint(\"并且原始字符串表示为：\")\nprint(r\"她说了：'Python是'最'棒的语言！'\")  # 原始字符串，不需要转义反斜杠\n'''---------------------------第 5 题：简单的数学运算--------------------------------'''\n# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q2",
                "name": "第2题",
                "description": "编程题-上手操作：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编程题-上手操作：",
                "type": "code",
                "options": [],
                "answer": "# 编写一个程序，让用户输入两个数字，在将数字转换为浮点数（float），然后两个数字相加，显示它们的和。\n# 详细步骤：\n#       1.定义变量num1，使用input()接收用户输入的数字1.\n#       2.定义变量num2，使用input()接收用户输入的数字2.\n#       3.定义变量sums，将上面两个字符串，转成float，再相加。\n#       4.使用print()。输出第3点的sums。\nnum1 = input(\"输入第一个数字：\")\nnum2 = input(\"输入第二个数字：\")\nsums = float(num1) + float(num2)\nprint(\"两数之和：\",sums)\n'''---------------------------第 3 题：字符串与数字的类型转换--------------------------------'''\n# 编写一个程序，让用户分别输入一个字符串形式的整数和一个小数（浮点数），然后将它们转换为对应的数值类型并打印出来。\n# 详细步骤：\n#       1.定义一个变量：str_int，使其可以再控制台输入一个整数类型的字符串。\n#       2.定义一个变量：str_float，使其可以再控制台输入一个浮点类型的字符串。\n#       3.分别定义两个变量：int_value 和 float_value，分别转换为int和float类型。\n#       4.分别打印int_value 和 float_value 以及 type(int_value) 和 type(float_value)\n# 获取用户输入的字符串形式的整数，并转换为整型\nstr_int = input(\"请输入一个字符串形式的整数：\")\nint_value = int(str_int)\nprint(int_value)\nprint(type(int_value))\n# 获取用户输入的字符串形式的小数，并转换为浮点型\nstr_float = input(\"请输入一个字符串形式的小数：\")\nfloat_value = float(str_float)\nprint(float_value)\nprint(type(float_value))\n'''---------------------------第 4 题：使用转义字符打印特殊文本--------------------------------'''\n# 描述: 编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串。\n# 字符串中应包含不同类型的引号（单引号和双引号）、反斜杠（作为转义字符）、换行符和制表符。\n# 要求程序能够正确处理这些特殊字符，并按照预期格式输出。\n# 示例语句：\"她说了：'Python是'最'棒的语言！'\"\n# 详细步骤：\n#       1.打印包含单引号和双引号的字符串\n#       2.打印包含换行符和制表符的字符串\n#       3.使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别\nprint('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")\nprint(\"并且原始字符串表示为：\")\nprint(r\"她说了：'Python是'最'棒的语言！'\")  # 原始字符串，不需要转义反斜杠\n'''---------------------------第 5 题：简单的数学运算--------------------------------'''\n# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 编写一个程序，让用户输入两个数字，在将数字转换为浮点数（float），然后两个数字相加，显示它们的和。\n# 详细步骤：\n#       1.定义变量num1，使用input()接收用户输入的数字1.\n#       2.定义变量num2，使用input()接收用户输入的数字2.\n#       3.定义变量sums，将上面两个字符串，转成float，再相加。\n#       4.使用print()。输出第3点的sums。\nnum1 = input(\"输入第一个数字：\")\nnum2 = input(\"输入第二个数字：\")\nsums = float(num1) + float(num2)\nprint(\"两数之和：\",sums)\n'''---------------------------第 3 题：字符串与数字的类型转换--------------------------------'''\n# 编写一个程序，让用户分别输入一个字符串形式的整数和一个小数（浮点数），然后将它们转换为对应的数值类型并打印出来。\n# 详细步骤：\n#       1.定义一个变量：str_int，使其可以再控制台输入一个整数类型的字符串。\n#       2.定义一个变量：str_float，使其可以再控制台输入一个浮点类型的字符串。\n#       3.分别定义两个变量：int_value 和 float_value，分别转换为int和float类型。\n#       4.分别打印int_value 和 float_value 以及 type(int_value) 和 type(float_value)\n# 获取用户输入的字符串形式的整数，并转换为整型\nstr_int = input(\"请输入一个字符串形式的整数：\")\nint_value = int(str_int)\nprint(int_value)\nprint(type(int_value))\n# 获取用户输入的字符串形式的小数，并转换为浮点型\nstr_float = input(\"请输入一个字符串形式的小数：\")\nfloat_value = float(str_float)\nprint(float_value)\nprint(type(float_value))\n'''---------------------------第 4 题：使用转义字符打印特殊文本--------------------------------'''\n# 描述: 编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串。\n# 字符串中应包含不同类型的引号（单引号和双引号）、反斜杠（作为转义字符）、换行符和制表符。\n# 要求程序能够正确处理这些特殊字符，并按照预期格式输出。\n# 示例语句：\"她说了：'Python是'最'棒的语言！'\"\n# 详细步骤：\n#       1.打印包含单引号和双引号的字符串\n#       2.打印包含换行符和制表符的字符串\n#       3.使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别\nprint('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")\nprint(\"并且原始字符串表示为：\")\nprint(r\"她说了：'Python是'最'棒的语言！'\")  # 原始字符串，不需要转义反斜杠\n'''---------------------------第 5 题：简单的数学运算--------------------------------'''\n# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q3",
                "name": "第3题",
                "description": "输出简单的问候语'''...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "输出简单的问候语'''",
                "type": "code",
                "options": [],
                "answer": "# 编写一个程序，让用户分别输入一个字符串形式的整数和一个小数（浮点数），然后将它们转换为对应的数值类型并打印出来。\n# 详细步骤：\n#       1.定义一个变量：str_int，使其可以再控制台输入一个整数类型的字符串。\n#       2.定义一个变量：str_float，使其可以再控制台输入一个浮点类型的字符串。\n#       3.分别定义两个变量：int_value 和 float_value，分别转换为int和float类型。\n#       4.分别打印int_value 和 float_value 以及 type(int_value) 和 type(float_value)\n# 获取用户输入的字符串形式的整数，并转换为整型\nstr_int = input(\"请输入一个字符串形式的整数：\")\nint_value = int(str_int)\nprint(int_value)\nprint(type(int_value))\n# 获取用户输入的字符串形式的小数，并转换为浮点型\nstr_float = input(\"请输入一个字符串形式的小数：\")\nfloat_value = float(str_float)\nprint(float_value)\nprint(type(float_value))\n'''---------------------------第 4 题：使用转义字符打印特殊文本--------------------------------'''\n# 描述: 编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串。\n# 字符串中应包含不同类型的引号（单引号和双引号）、反斜杠（作为转义字符）、换行符和制表符。\n# 要求程序能够正确处理这些特殊字符，并按照预期格式输出。\n# 示例语句：\"她说了：'Python是'最'棒的语言！'\"\n# 详细步骤：\n#       1.打印包含单引号和双引号的字符串\n#       2.打印包含换行符和制表符的字符串\n#       3.使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别\nprint('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")\nprint(\"并且原始字符串表示为：\")\nprint(r\"她说了：'Python是'最'棒的语言！'\")  # 原始字符串，不需要转义反斜杠\n'''---------------------------第 5 题：简单的数学运算--------------------------------'''\n# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 编写一个程序，让用户分别输入一个字符串形式的整数和一个小数（浮点数），然后将它们转换为对应的数值类型并打印出来。\n# 详细步骤：\n#       1.定义一个变量：str_int，使其可以再控制台输入一个整数类型的字符串。\n#       2.定义一个变量：str_float，使其可以再控制台输入一个浮点类型的字符串。\n#       3.分别定义两个变量：int_value 和 float_value，分别转换为int和float类型。\n#       4.分别打印int_value 和 float_value 以及 type(int_value) 和 type(float_value)\n# 获取用户输入的字符串形式的整数，并转换为整型\nstr_int = input(\"请输入一个字符串形式的整数：\")\nint_value = int(str_int)\nprint(int_value)\nprint(type(int_value))\n# 获取用户输入的字符串形式的小数，并转换为浮点型\nstr_float = input(\"请输入一个字符串形式的小数：\")\nfloat_value = float(str_float)\nprint(float_value)\nprint(type(float_value))\n'''---------------------------第 4 题：使用转义字符打印特殊文本--------------------------------'''\n# 描述: 编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串。\n# 字符串中应包含不同类型的引号（单引号和双引号）、反斜杠（作为转义字符）、换行符和制表符。\n# 要求程序能够正确处理这些特殊字符，并按照预期格式输出。\n# 示例语句：\"她说了：'Python是'最'棒的语言！'\"\n# 详细步骤：\n#       1.打印包含单引号和双引号的字符串\n#       2.打印包含换行符和制表符的字符串\n#       3.使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别\nprint('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")\nprint(\"并且原始字符串表示为：\")\nprint(r\"她说了：'Python是'最'棒的语言！'\")  # 原始字符串，不需要转义反斜杠\n'''---------------------------第 5 题：简单的数学运算--------------------------------'''\n# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q4",
                "name": "第4题",
                "description": "定义一个变量名name，使用input()接收用户输入。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个变量名name，使用input()接收用户输入。",
                "type": "code",
                "options": [],
                "answer": "# 描述: 编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串。\n# 字符串中应包含不同类型的引号（单引号和双引号）、反斜杠（作为转义字符）、换行符和制表符。\n# 要求程序能够正确处理这些特殊字符，并按照预期格式输出。\n# 示例语句：\"她说了：'Python是'最'棒的语言！'\"\n# 详细步骤：\n#       1.打印包含单引号和双引号的字符串\n#       2.打印包含换行符和制表符的字符串\n#       3.使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别\nprint('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")\nprint(\"并且原始字符串表示为：\")\nprint(r\"她说了：'Python是'最'棒的语言！'\")  # 原始字符串，不需要转义反斜杠\n'''---------------------------第 5 题：简单的数学运算--------------------------------'''\n# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 描述: 编写一个Python程序，处理并打印带有多种特殊字符的复杂字符串。\n# 字符串中应包含不同类型的引号（单引号和双引号）、反斜杠（作为转义字符）、换行符和制表符。\n# 要求程序能够正确处理这些特殊字符，并按照预期格式输出。\n# 示例语句：\"她说了：'Python是'最'棒的语言！'\"\n# 详细步骤：\n#       1.打印包含单引号和双引号的字符串\n#       2.打印包含换行符和制表符的字符串\n#       3.使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别\nprint('她说了：\"Python是\\'最\\'棒的语言！\"')\nprint(\"她说了：\\n\\t'Python是\\\"最\\\"棒的语言！'\")\nprint(\"并且原始字符串表示为：\")\nprint(r\"她说了：'Python是'最'棒的语言！'\")  # 原始字符串，不需要转义反斜杠\n'''---------------------------第 5 题：简单的数学运算--------------------------------'''\n# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q5",
                "name": "第5题",
                "description": "使用print()打印：\"你好，\" + name + \"！欢迎来到Python的世界。\"...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用print()打印：\"你好，\" + name + \"！欢迎来到Python的世界。\"",
                "type": "code",
                "options": [],
                "answer": "# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 描述: 编写一个程序，让用户输入两个数字，然后分别显示这两个数字的和、差、积、商。\n# 详细步骤：\n#       1.分别定义两个变量：num1,num2，让用户输入两个数字。\n#       2.在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。\n#       3.分别使用+，-，*，/四个符号，计算n1 和 n2的结果。\nnum1 = input(\"请输入第一个数字：\")\nnum2 = input(\"请输入第二个数字：\")\n# 转换为浮点数进行数学运算\nn1 = float(num1)\nn2 = float(num2)\nprint(n1 + n2)\nprint(n1 - n2)\nprint(n1 * n2)\nprint(n1 / n2)\n'''---------------------------第 6 题：使用转义字符和字符串操作打印格式化路径--------------------------------'''\n# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q6",
                "name": "第6题",
                "description": "浮点数之和...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "浮点数之和",
                "type": "code",
                "options": [],
                "answer": "# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 【这个题和第4题类似】编写一个程序，让用户输入文件名和扩展名，\n# 然后构造并打印出带有正确转义字符的完整文件路径。为了简化，假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 详细步骤：\n#       1.定义变量filename，用来接收用户输入的文件名。\n#       2.定义变量extension，用来接收用户输入的文件扩展名。\n#       3.定义变量path，拼接字符串。\n#       4.打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。\n# 获取用户输入的文件名和扩展名\nfilename = input(\"请输入文件名（不带扩展名）：\")\nextension = input(\"请输入文件扩展名（例如txt, py等）：\")\n# 构造文件路径，注意使用双反斜杠进行转义\npath = 'D:\\\\Documents\\\\Projects\\\\' + filename + '.' + extension\n# 打印构造的文件路径\nprint(path)\n'''---------------------------第 7 题：NoneType 的实际应用场景--------------------------------'''\n# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q7",
                "name": "第7题",
                "description": "定义变量num1，使用input()接收用户输入的数字1....",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义变量num1，使用input()接收用户输入的数字1.",
                "type": "code",
                "options": [],
                "answer": "# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 编写一个程序，定义一个变量为None，然后尝试打印它的值和类型。再将该变量赋值为用户输入的一段文本，并再次打印它的值和类型。\n# 详细步骤：\n#       1.定义一个初始值value为 None 的变量.然后分别打印value和type(value).\n#       2.获取用户输入的文本.\n#       3.将变量赋值为用户输入的文本\n#       4.再次打印变量的值和类型\nvalue = None\nprint(\"初始值:\", value)\nprint(\"初始类型:\", type(value))\nuser_input = input(\"请输入一段文本：\")\n# 将变量赋值为用户输入的文本\nvalue = user_input\n# 再次打印变量的值和类型\nprint(\"更新后的值:\", value)\nprint(\"更新后的类型:\", type(value))\n'''---------------------------第 8 题：布尔值的操作和展示--------------------------------'''\n# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q8",
                "name": "第8题",
                "description": "定义变量num2，使用input()接收用户输入的数字2....",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义变量num2，使用input()接收用户输入的数字2.",
                "type": "code",
                "options": [],
                "answer": "# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 编写一个程序，定义两个布尔变量，分别设置为True和False。然后打印这两个布尔值及其类型。接下来，尝试将这两个布尔值转换为整数并打印结果。\n# 详细步骤：\n#       1.定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。\n#       2.打印两个布尔变量的值和类型。\n#       3.将两个布尔值转换为整数并打印。\n# 定义两个布尔变量\nbool_true = True\nbool_false = False\n# 打印布尔值及其类型\nprint(\"第一个布尔值:\", bool_true)\nprint(\"第一个布尔值的类型:\", type(bool_true))\nprint(\"第二个布尔值:\", bool_false)\nprint(\"第二个布尔值的类型:\", type(bool_false))\n# 将布尔值转换为整数并打印\nprint(\"True 转换为整数:\", int(bool_true))\nprint(\"False 转换为整数:\", int(bool_false))\n'''---------------------------第 9 题：is和==--------------------------------'''\n# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q9",
                "name": "第9题",
                "description": "定义变量sums，将上面两个字符串，转成float，再相加。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义变量sums，将上面两个字符串，转成float，再相加。",
                "type": "code",
                "options": [],
                "answer": "# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 请根据示例内容，完成任务：\n# 示例：\na = [1, 2, 3]\nb = [1, 2, 3]\nc = a\n# 任务：\n# 1. 编写代码，打印出a、b和c的内存地址，即它们各自的id。\n# 2. 比较a==b；a is b；a == c；a is c的结果。\n# 3. 修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。\n# 任务1：编写代码，打印出a、b和c的内存地址，即它们各自的id。\nprint('a的内存地址：',id(a))\nprint('b的内存地址：',id(b))\nprint('c的内存地址：',id(c))\n# 任务2：比较a == b；a is b；a == c；a is c的结果。\nprint('a == b',a == b)  # 输出：True\nprint('a is b',a is b)  # 输出：False\nprint('a == c',a == c)  # 输出：True\nprint('a is c',a is c)  # 输出：True\n# 任务3: 修改变量b，使其与a包含不同的元素，然后再次打印出a和b的比较结果(分别使用==和is比对)。\nb = [4, 5, 6]  # 修改b的元素\nprint(\"\\n修改b后的比较结果:\")\nprint(\"a == b:\", a == b)  # 使用==比较a和b的值     // 输出：False\nprint(\"a is b:\", a is b)  # 使用is比较a和b的身份    // 输出：False\n'''---------------------------第 10 题：逻辑表达式的综合运用--------------------------------'''\n# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q10",
                "name": "第10题",
                "description": "使用print()。输出第3点的sums。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用print()。输出第3点的sums。",
                "type": "code",
                "options": [],
                "answer": "# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "# 1.给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。\nx = 10\ny = 20\nr = x != y and x < 15\nprint('x != y and x < 15判断结果：',r)\n# 2.编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。\nage = 10\nprint('18 <= age <= 65判断结果',18 <= age <= 65)\n# 3. 给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。\nname = \"六一\"\nrel = name != \"Alice\" and name != \"Bob\"\nprint(\"name != 'Alice' and name != 'Bob'判断结果：\",rel)\n# 4. 给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80\nscore = float(input(\"请输入成绩（分数）：\"))\nrel = (90 < score < 100) or score == 80\nprint('(90 < score < 100) or score == 80判断结果：',rel)\n# 5. 编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。\n# 分别写出，不构成和构成两种的。\na = int(input(\"请输入第一条边长：\"))\nb = int(input(\"请输入第二条边长：\"))\nc = int(input(\"请输入第三条边长：\"))\n# 构成的\nyes1 = a + b > c\nyes2 = a + c > b\nyes3 = b + c > a\nrel_yes = yes1 and yes2 and yes3\nprint(\"是否构成：\",rel_yes)\n# 不构成的：\nno1 = a + b <= c\nno2 = a + c <= b\nno3 = b + c <= a\nrel_no = no1 or no2 or no3\nprint(\"是否构成：\",rel_no)\n# 6.编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。\n# 是闰年\nyear = int(input(\"请输入年份：\"))\nis_leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)\nprint(\"是否闰年：\", is_leap_year)\n# 不是闰年：\n#     年份不能被4整除；\n#     年份能被100整除但不能被400整除。\nis_not_leap_year1 = not ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))\nis_not_leap_year2 = (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)\nprint(\"是否不是闰年is_not_leap_year1：\",is_not_leap_year1,\"是否不是闰年is_not_leap_year2：\",is_not_leap_year2)"
            },
            {
                "id": "day3_q11",
                "name": "第11题",
                "description": "字符串与数字的类型转换...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "字符串与数字的类型转换",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q12",
                "name": "第12题",
                "description": "定义一个变量：str_int，使其可以再控制台输入一个整数类型的字符串。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个变量：str_int，使其可以再控制台输入一个整数类型的字符串。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q13",
                "name": "第13题",
                "description": "定义一个变量：str_float，使其可以再控制台输入一个浮点类型的字符串。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个变量：str_float，使其可以再控制台输入一个浮点类型的字符串。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q14",
                "name": "第14题",
                "description": "分别定义两个变量：int_value 和 float_value，分别转换为int和float类型。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "分别定义两个变量：int_value 和 float_value，分别转换为int和float类型。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q15",
                "name": "第15题",
                "description": "分别打印int_value 和 float_value 以及 type(int_value) 和 t...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "分别打印int_value 和 float_value 以及 type(int_value) 和 type(float_value)",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q16",
                "name": "第16题",
                "description": "使用转义字符打印特殊文本...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用转义字符打印特殊文本",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q17",
                "name": "第17题",
                "description": "打印包含单引号和双引号的字符串...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "打印包含单引号和双引号的字符串",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q18",
                "name": "第18题",
                "description": "打印包含换行符和制表符的字符串...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "打印包含换行符和制表符的字符串",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q19",
                "name": "第19题",
                "description": "使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用原始字符串打印相同的内容，展示原始字符串和非原始字符串的区别",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q20",
                "name": "第20题",
                "description": "简单的数学运算...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "简单的数学运算",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q21",
                "name": "第21题",
                "description": "分别定义两个变量：num1,num2，让用户输入两个数字。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "分别定义两个变量：num1,num2，让用户输入两个数字。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q22",
                "name": "第22题",
                "description": "在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "在定义两个变量：n1 和 n2，用来将num1,num2转换为浮点数。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q23",
                "name": "第23题",
                "description": "分别使用+，-，*，/四个符合，计算n1 和 n2的结果。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "分别使用+，-，*，/四个符合，计算n1 和 n2的结果。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q24",
                "name": "第24题",
                "description": "使用转义字符和字符串操作打印格式化路径...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用转义字符和字符串操作打印格式化路径",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q25",
                "name": "第25题",
                "description": "定义变量filename，用来接收用户输入的文件名。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义变量filename，用来接收用户输入的文件名。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q26",
                "name": "第26题",
                "description": "定义变量extension，用来接收用户输入的文件扩展名。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义变量extension，用来接收用户输入的文件扩展名。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q27",
                "name": "第27题",
                "description": "定义变量path，拼接字符串。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义变量path，拼接字符串。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q28",
                "name": "第28题",
                "description": "打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。【...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "打印拼接后的字符串path。假定文件位于 \"D:\\Documents\\Projects\" 目录下。【拼接可以参照第一题】",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q29",
                "name": "第29题",
                "description": "NoneType 的实际应用场景...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "NoneType 的实际应用场景",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q30",
                "name": "第30题",
                "description": "定义一个初始值value为 None 的变量.然后分别打印value和type(value)....",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个初始值value为 None 的变量.然后分别打印value和type(value).",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q31",
                "name": "第31题",
                "description": "获取用户输入的文本....",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "获取用户输入的文本.",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q32",
                "name": "第32题",
                "description": "将变量赋值为用户输入的文本...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "将变量赋值为用户输入的文本",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q33",
                "name": "第33题",
                "description": "再次打印变量的值和类型...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "再次打印变量的值和类型",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q34",
                "name": "第34题",
                "description": "布尔值的操作和展示...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "布尔值的操作和展示",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q35",
                "name": "第35题",
                "description": "定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义两个布尔变量：bool_true 和 bool_false，分别赋值True和False。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q36",
                "name": "第36题",
                "description": "打印两个布尔变量的值和类型。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "打印两个布尔变量的值和类型。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q37",
                "name": "第37题",
                "description": "将两个布尔值转换为整数并打印。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "将两个布尔值转换为整数并打印。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q38",
                "name": "第38题",
                "description": "is和==...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "is和==",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q39",
                "name": "第39题",
                "description": "编写代码，打印出a、b和c的内存地址，即它们各自的id。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写代码，打印出a、b和c的内存地址，即它们各自的id。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q40",
                "name": "第40题",
                "description": "比较a==b；a is b；a == c；a is c的结果。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "比较a==b；a is b；a == c；a is c的结果。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q41",
                "name": "第41题",
                "description": "修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "修改变量b，使其与a包含不同的元素，例如[4, 5, 6]，然后再次打印出a和b的比较结果（使用==和is）。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q42",
                "name": "第42题",
                "description": "逻辑表达式的综合运用...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "逻辑表达式的综合运用",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q43",
                "name": "第43题",
                "description": "【示例】给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "【示例】给定两个变量 x 和 y，其中 x 为 10，y 为 20，请编写一个表达式来判断 x 是否不等于 y，并且 x 小于 15。需要输出判断结果。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q44",
                "name": "第44题",
                "description": "编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一个Python表达式来判断一个变量 age 是否在 18 到 65 岁之间（包括18岁和65岁）。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q45",
                "name": "第45题",
                "description": "给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "给定一个字符串变量 name，请使用逻辑运算符检查 name 是否既不是 \"Alice\" 也不是 \"Bob\"。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q46",
                "name": "第46题",
                "description": "给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 10...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "给定一个数字变量 score，请编写一个逻辑表达式来判断 score 是否大于 90 并且小于 100，或者等于 80",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q47",
                "name": "第47题",
                "description": "编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一个Python程序，接受用户输入的三个数字，写出判断这三个数字是否构成一个三角形的边长（任意两边之和大于第三边）的逻辑表达式。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day3_q48",
                "name": "第48题",
                "description": "编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一个Python程序，判断一个给定的年份 year 是否为闰年的逻辑表达式。闰年的条件是：能被4整除但不能被100整除，或者能被400整除。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_4",
        "name": "条件城堡",
        "description": "条件判断、运算与优先级",
        "icon": "fa-castle",
        "levels": [
            {
                "id": "day4_q1",
                "name": "第1题",
                "description": "判断一个数的正负...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "判断一个数的正负",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q2",
                "name": "第2题",
                "description": "定义一个变量number，用来接收用户输入的数值。并转换为float。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个变量number，用来接收用户输入的数值。并转换为float。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q3",
                "name": "第3题",
                "description": "使用 if-elif-else 语句判断正负：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用 if-elif-else 语句判断正负：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q4",
                "name": "第4题",
                "description": "判断是否水仙花数...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "判断是否水仙花数",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q5",
                "name": "第5题",
                "description": "计算商品购物折扣...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "计算商品购物折扣",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q6",
                "name": "第6题",
                "description": "定义一个变量(shopping_amount)，用户输入购物金额。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个变量(shopping_amount)，用户输入购物金额。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q7",
                "name": "第7题",
                "description": "使用if_elif_else进行折扣规则判断，如下：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用if_elif_else进行折扣规则判断，如下：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q8",
                "name": "第8题",
                "description": "简单的交通信号灯判断...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "简单的交通信号灯判断",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q9",
                "name": "第9题",
                "description": "判断三角形类型(day02、03的课后练习题出现过，现在完善一下这道题)...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "判断三角形类型(day02、03的课后练习题出现过，现在完善一下这道题)",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q10",
                "name": "第10题",
                "description": "公园门票优惠政策模拟...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "公园门票优惠政策模拟",
                "type": "code",
                "options": [],
                "answer": "题目要求：编写一个 Python 程序，模拟存款利息的计算。用户可以输入存款金额和存款期限（年），程序将根据以下规则计算到期后的总金额并输出结果：\n年利率为3%。\n如果存款期限超过5年，超出部分的年利率为2%。\n利息计算使用简单利息公式：利息 = 本金 × 利率 × 时间。\n解题思路：\n定义变量principal、time，分别让用户输入存款金额（float型数据）和存款期限（int型数据）。\n初始化利息（interest = 0）和总金额（total_amount = principal）\n根据存款期限计算利息：\n如果(if)存款期限超过5年：\n计算前5年的利息（按3%的年利率）。\n计算超过5年的部分的利息（按2%的年利率）。\n如果(if)存款期限不超过5年：\n直接根据存款期限和3%的年利率计算利息。\n判断结束后：计算到期后的总金额（total_amount）\n输出到期后的总金额。",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "题目要求：编写一个 Python 程序，模拟存款利息的计算。用户可以输入存款金额和存款期限（年），程序将根据以下规则计算到期后的总金额并输出结果：\n年利率为3%。\n如果存款期限超过5年，超出部分的年利率为2%。\n利息计算使用简单利息公式：利息 = 本金 × 利率 × 时间。\n解题思路：\n定义变量principal、time，分别让用户输入存款金额（float型数据）和存款期限（int型数据）。\n初始化利息（interest = 0）和总金额（total_amount = principal）\n根据存款期限计算利息：\n如果(if)存款期限超过5年：\n计算前5年的利息（按3%的年利率）。\n计算超过5年的部分的利息（按2%的年利率）。\n如果(if)存款期限不超过5年：\n直接根据存款期限和3%的年利率计算利息。\n判断结束后：计算到期后的总金额（total_amount）\n输出到期后的总金额。"
            },
            {
                "id": "day4_q11",
                "name": "第11题",
                "description": "实现一个简易计算器...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "实现一个简易计算器",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q12",
                "name": "第12题",
                "description": "提示用户输入：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "提示用户输入：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q13",
                "name": "第13题",
                "description": "验证运算符的有效性：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "验证运算符的有效性：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q14",
                "name": "第14题",
                "description": "根据输入的运算符执行相应的计算操作：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "根据输入的运算符执行相应的计算操作：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q15",
                "name": "第15题",
                "description": "处理除以零的情况：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "处理除以零的情况：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q16",
                "name": "第16题",
                "description": "输出计算结果：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "输出计算结果：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q17",
                "name": "第17题",
                "description": "计算应缴纳的车辆购置税...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "计算应缴纳的车辆购置税",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q18",
                "name": "第18题",
                "description": "书籍借阅最大借阅量...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "书籍借阅最大借阅量",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day4_q19",
                "name": "第19题",
                "description": "存款利率计算...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "存款利率计算",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_6",
        "name": "列表森林",
        "description": "数据结构之列表",
        "icon": "fa-list",
        "levels": [
            {
                "id": "day6_q1",
                "name": "第1题",
                "description": "在 Python 中，列表的索引是从哪个数字开始的？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在 Python 中，列表的索引是从哪个数字开始的？",
                "type": "choice",
                "options": [
                    "0",
                    "1",
                    "2",
                    "随机数"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q2",
                "name": "第2题",
                "description": "以下哪项是 Python 列表的一个特性？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪项是 Python 列表的一个特性？",
                "type": "choice",
                "options": [
                    "所有元素必须唯一",
                    "可以修改其中的元素",
                    "元素不能排序",
                    "不能通过索引访问元素"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q3",
                "name": "第3题",
                "description": "以下哪个方法用于向列表末尾添加一个元素？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个方法用于向列表末尾添加一个元素？",
                "type": "choice",
                "options": [
                    "append()",
                    "extend()",
                    "insert()",
                    "pop()"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q4",
                "name": "第4题",
                "description": "以下哪个方法用于从列表中移除指定位置的元素？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个方法用于从列表中移除指定位置的元素？",
                "type": "choice",
                "options": [
                    "remove()",
                    "pop()",
                    "delete()",
                    "erase()"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q5",
                "name": "第5题",
                "description": "填空题：...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "填空题：",
                "type": "choice",
                "options": [
                    "语句：sorted([1, 2, 3], reverse=True) 输出结果为                   。",
                    "切片操作 list(range(6))[::2] 执行结果为                   。",
                    "已知 y = [4, 5, 6, 5, 7]，执行语句 y.remove(5) 和 y.pop(2) 之后，y 的值为                   。",
                    "实操题："
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q6",
                "name": "第6题",
                "description": "反转列表。...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "反转列表。",
                "type": "choice",
                "options": [
                    "题目要求：将下面列表反转并打印。",
                    "lst = list(range(1, 11))",
                    "解题思路：方法一",
                    "使用切片的方式"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q7",
                "name": "第7题",
                "description": "解题思路：方法二...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "解题思路：方法二",
                "type": "choice",
                "options": [
                    "使用方法reverse()/sort()"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q8",
                "name": "第8题",
                "description": "遍历列表找出长度大于3的字符...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "遍历列表找出长度大于3的字符",
                "type": "choice",
                "options": [
                    "题目要求：遍历下面的列表，找出长度大于3的字符。",
                    "words = [\"六一\", \"儿童节\", \"五一劳动节\", \"元旦节快乐\", 'Christmas', 'happy', \"day\" ]",
                    "解题思路：",
                    "使用for循环遍历字典。"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q9",
                "name": "第9题",
                "description": "使用len()计算取出来的字符串长度。...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "使用len()计算取出来的字符串长度。",
                "type": "choice",
                "options": [
                    "使用if判断字符串长度是否大于3。",
                    "大于--打印出来",
                    "小于等于--无需打印。"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q10",
                "name": "第10题",
                "description": "有两个列表A和B，使用列表C来获取两个列表中公共的元素...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "有两个列表A和B，使用列表C来获取两个列表中公共的元素",
                "type": "choice",
                "options": [
                    "题目要求：将下面列表的重复值取出，放入到列表C中，并打印列表C。",
                    "A = [\"吃饭\", '睡觉', \"打豆豆\"]",
                    "B = [\"上班\", \"跑步\", \"睡觉\"]",
                    "解题思路："
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day6_q11",
                "name": "第11题",
                "description": "定义一个空列表C。...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "定义一个空列表C。",
                "type": "choice",
                "options": [
                    "使用循环遍历的方式遍历列表A。",
                    "再内循环遍历列表B。",
                    "使用if判断两个列表遍历的值是否相等。",
                    "将相等的值添加进入列表C即可。"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            }
        ]
    },
    {
        "id": "region_7",
        "name": "集合岛屿",
        "description": "数据结构之集合与元组",
        "icon": "fa-circle",
        "levels": [
            {
                "id": "day7_q1",
                "name": "第1题",
                "description": "将规定字符串转为列表后去重...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "将规定字符串转为列表后去重",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day7_q2",
                "name": "第2题",
                "description": "查找元组中最大值及其索引。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "查找元组中最大值及其索引。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day7_q3",
                "name": "第3题",
                "description": "循环完毕后，输出最大值max_value和最大值索引值max_index。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "循环完毕后，输出最大值max_value和最大值索引值max_index。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_8",
        "name": "函数殿堂",
        "description": "函数定义与使用",
        "icon": "fa-book",
        "levels": [
            {
                "id": "day8_q1",
                "name": "第1题",
                "description": "填空题：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "填空题：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day8_q2",
                "name": "第2题",
                "description": "实战题：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "实战题：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day8_q3",
                "name": "第3题",
                "description": "使用while循环表述上面的内容。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用while循环表述上面的内容。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day8_q4",
                "name": "第4题",
                "description": "表述要求，必须用到break 和 continue...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "表述要求，必须用到break 和 continue",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_9",
        "name": "迭代器谷",
        "description": "迭代器和常用函数",
        "icon": "fa-repeat",
        "levels": [
            {
                "id": "day9_q1",
                "name": "第1题",
                "description": "填空题：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "填空题：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day9_q2",
                "name": "第2题",
                "description": "next()函数用于获取迭代器的下一个          。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "next()函数用于获取迭代器的下一个          。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day9_q3",
                "name": "第3题",
                "description": "如果迭代器中没有更多的元素，调用next()函数会抛出一个            异常。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "如果迭代器中没有更多的元素，调用next()函数会抛出一个            异常。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day9_q4",
                "name": "第4题",
                "description": "在Python中，使用for循环迭代一个对象时，实际上是在内部调用该对象的           方法...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "在Python中，使用for循环迭代一个对象时，实际上是在内部调用该对象的           方法。",
                "type": "code",
                "options": [],
                "answer": "具体任务：\n解题思路：\n参考答案：\n# 获取用户输入的数据\nuser_input = input(\"请输入一组数据（列表包元组），例如 [(1, 2), (3, 4), (5, 6)]: \")\ntry:\n# 使用 eval() 将输入字符串转换为 Python 数据结构\ndata_structure = eval(user_input)\n# 创建迭代器\ndata_iterator = iter(data_structure)\nprint(\"开始对每个元组内的数据进行简单运算：\")\nwhile True:\ntry:\n# 获取下一个元组\ntuple_data = next(data_iterator)\na, b = tuple_data\n# 执行简单运算\nprint(f\"元组: {tuple_data}\")\nprint(f\"加法: {a} + {b} = {a + b}\")\nprint(f\"减法: {a} - {b} = {a - b}\")\nprint(f\"乘法: {a} * {b} = {a * b}\")\nif b != 0:\nprint(f\"除法: {a} / {b} = {a / b}\")\nelse:\nprint(\"除法: 分母不能为零\")\nexcept StopIteration:\nbreak  # 当所有元素都被访问过后停止循环\nexcept Exception as e:\nprint(f\"无效输入或处理错误: {e}\")",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "具体任务：\n解题思路：\n参考答案：\n# 获取用户输入的数据\nuser_input = input(\"请输入一组数据（列表包元组），例如 [(1, 2), (3, 4), (5, 6)]: \")\ntry:\n# 使用 eval() 将输入字符串转换为 Python 数据结构\ndata_structure = eval(user_input)\n# 创建迭代器\ndata_iterator = iter(data_structure)\nprint(\"开始对每个元组内的数据进行简单运算：\")\nwhile True:\ntry:\n# 获取下一个元组\ntuple_data = next(data_iterator)\na, b = tuple_data\n# 执行简单运算\nprint(f\"元组: {tuple_data}\")\nprint(f\"加法: {a} + {b} = {a + b}\")\nprint(f\"减法: {a} - {b} = {a - b}\")\nprint(f\"乘法: {a} * {b} = {a * b}\")\nif b != 0:\nprint(f\"除法: {a} / {b} = {a / b}\")\nelse:\nprint(\"除法: 分母不能为零\")\nexcept StopIteration:\nbreak  # 当所有元素都被访问过后停止循环\nexcept Exception as e:\nprint(f\"无效输入或处理错误: {e}\")"
            },
            {
                "id": "day9_q5",
                "name": "第5题",
                "description": "实战题...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "实战题",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day9_q6",
                "name": "第6题",
                "description": "第 01 题：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "第 01 题：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day9_q7",
                "name": "第7题",
                "description": "第 02 题：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "第 02 题：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day9_q8",
                "name": "第8题",
                "description": "iter()和next()的应用...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "iter()和next()的应用",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day9_q9",
                "name": "第9题",
                "description": "使用eval()计算简单的数学表达式...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用eval()计算简单的数学表达式",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_11",
        "name": "函数进阶",
        "description": "函数参数与返回值",
        "icon": "fa-code",
        "levels": [
            {
                "id": "day11_q1",
                "name": "第1题",
                "description": "函数的参数和返回值...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "函数的参数和返回值",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day11_q2",
                "name": "第2题",
                "description": "计算三角形面积（基本参数传递与返回值理解）...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "计算三角形面积（基本参数传递与返回值理解）",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day11_q3",
                "name": "第3题",
                "description": "计算统计数据(多个位置参数与返回值)...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "计算统计数据(多个位置参数与返回值)",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_12",
        "name": "函数深化",
        "description": "递归、闭包、匿名函数",
        "icon": "fa-code-branch",
        "levels": [
            {
                "id": "day12_q1",
                "name": "第1题",
                "description": "创建问候语（默认值参数）...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建问候语（默认值参数）",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day12_q2",
                "name": "第2题",
                "description": "模拟航班预定(关键字参数)...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "模拟航班预定(关键字参数)",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day12_q3",
                "name": "第3题",
                "description": "计算任意数量参数的总和（可变位置参数）...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "计算任意数量参数的总和（可变位置参数）",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day12_q4",
                "name": "第4题",
                "description": "创建活动信息-可变关键字参数...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建活动信息-可变关键字参数",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day12_q5",
                "name": "第5题",
                "description": "计算购物车折扣后的总价-混合参数练习...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "计算购物车折扣后的总价-混合参数练习",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day12_q6",
                "name": "第6题",
                "description": "使用回调函数进行用户问候...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用回调函数进行用户问候",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day12_q7",
                "name": "第7题",
                "description": "使用回调函数实现基本算术运算...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用回调函数实现基本算术运算",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_14",
        "name": "继承之城",
        "description": "类的继承与重写",
        "icon": "fa-sitemap",
        "levels": [
            {
                "id": "day14_q1",
                "name": "第1题",
                "description": "完善Bicycle类...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "完善Bicycle类",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_15",
        "name": "多态之塔",
        "description": "多继承、多态和鸭子类型",
        "icon": "fa-layer-group",
        "levels": [
            {
                "id": "day15_q1",
                "name": "第1题",
                "description": "Vehicle类中__init__方法的作用是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "Vehicle类中__init__方法的作用是什么？",
                "type": "choice",
                "options": [
                    "启动车辆",
                    "打印车辆",
                    "初始化车辆的品牌和型号",
                    "充电"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q2",
                "name": "第2题",
                "description": "Car类继承自哪个类？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "Car类继承自哪个类？",
                "type": "choice",
                "options": [
                    "Bicycle",
                    "ElectricCar",
                    "Vehicle",
                    "不继承任何类"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q3",
                "name": "第3题",
                "description": "ElectricCar类可以访问哪些方法？（多选）...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "ElectricCar类可以访问哪些方法？（多选）",
                "type": "choice",
                "options": [
                    "start",
                    "drive",
                    "charge",
                    "只有charge"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q4",
                "name": "第4题",
                "description": "创建ElectricCar对象my_car后，调用drive方法会打印什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "创建ElectricCar对象my_car后，调用drive方法会打印什么？",
                "type": "choice",
                "options": [
                    "\"特斯拉 Model S 启动了。\"",
                    "\"特斯拉 Model S 在路上行驶。\"",
                    "\"特斯拉 Model S 正在充电。\"",
                    "\"自行车正在骑行中。\""
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q5",
                "name": "第5题",
                "description": "在提供的代码示例中，Bicycle类显式地继承了哪个类？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在提供的代码示例中，Bicycle类显式地继承了哪个类？",
                "type": "choice",
                "options": [
                    "Object类",
                    "Vehicle类",
                    "没有显示的继承任何类",
                    "它自己"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q6",
                "name": "第6题",
                "description": "什么是类的继承？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "什么是类的继承？",
                "type": "choice",
                "options": [
                    "类的继承是指一个类（称为子类）可以继承另一个类（称为父类）的属性和方法。",
                    "类的继承是指一个类可以从多个类继承属性和方法，但只能有一个主要父类。",
                    "类的继承是指一个类可以完全替换另一个类的所有属性和方法。",
                    "类的继承是指一个类可以复制另一个类的属性和方法，但不能修改它们。"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q7",
                "name": "第7题",
                "description": "关于Python类的继承正确的说法是？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "关于Python类的继承正确的说法是？",
                "type": "choice",
                "options": [
                    "Python类无法继承其他类",
                    "子类继承父类后，无法调用父类的构造函数",
                    "可以有多个父类",
                    "不能有多个父类"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q8",
                "name": "第8题",
                "description": "在Python中，如何正确地在子类中重写父类的方法？？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，如何正确地在子类中重写父类的方法？？",
                "type": "choice",
                "options": [
                    "使用override关键字定义一个与父类中相同名称的方法",
                    "在子类中定义一个与父类中相同名称的方法即可",
                    "使用super()函数直接修改父类的方法定义",
                    "在子类的方法中使用@overload装饰器来指定要重写的方法"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q9",
                "name": "第9题",
                "description": "在Python中，当你创建了一个从多个类继承的子类时，Python使用什么规则来决定应该首先检查哪个...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，当你创建了一个从多个类继承的子类时，Python使用什么规则来决定应该首先检查哪个父类的方法或属性？",
                "type": "choice",
                "options": [
                    "随机选择一个父类开始查找",
                    "总是从最后一个列出的父类开始查找",
                    "使用一种叫做方法解析顺序（MRO）的特殊规则来决定查找顺序",
                    "只查找第一个父类，忽略其他的父类"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q10",
                "name": "第10题",
                "description": "按照字母顺序排列父类名称后进行查找...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "按照字母顺序排列父类名称后进行查找",
                "type": "choice",
                "options": [
                    "什么是多继承？",
                    "多继承是指一个类可以从多个父类继承属性和方法",
                    "多继承是指一个类可以在不同程序中被多次定义",
                    "多继承是指多个子类可以共享同一个父类"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q11",
                "name": "第11题",
                "description": "多继承是指一个类可以作为多个其他类的父类...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "多继承是指一个类可以作为多个其他类的父类",
                "type": "choice",
                "options": [
                    "以下哪一项描述了实例方法和实例属性之间的正确关系？",
                    "实例方法可以在不使用self的情况下直接访问和修改实例属性。",
                    "实例方法只能修改但不能读取实例属性 。",
                    "实例方法可以通过self参数访问并修改实例属性。"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q12",
                "name": "第12题",
                "description": "关于Python中的实例方法和实例属性，以下哪项陈述是正确的？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "关于Python中的实例方法和实例属性，以下哪项陈述是正确的？",
                "type": "choice",
                "options": [
                    "A. 实例方法必须通过类名来访问实例属性。",
                    "B. 实例属性只能在__init__方法中定义。",
                    "C. 实例方法可以通过self参数读取和修改其他实例的属性。",
                    "D. 实例方法可以通过self参数读取和修改同一个实例的属性。"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q13",
                "name": "第13题",
                "description": "填空题...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "填空题",
                "type": "choice",
                "options": [
                    "洗衣机",
                    "在上述代码中，Washer类是一个                 。",
                    "它有两个实例属性（brand（品牌）和负载量（load）），以及 wash 和 dry 两个方法。",
                    "AdvancedWasher 类继承自 SpinDryer 和 SteamCleaner 类，"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q14",
                "name": "第14题",
                "description": "其中 SpinDryer 继承自 Washer 类，...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "其中 SpinDryer 继承自 Washer 类，",
                "type": "choice",
                "options": [
                    "因此 AdvancedWasher 类具有 Washer 类的             方法和 SteamCleaner 类的             方法。",
                    "已知SpinDryer继承了 Washer 类，因此在 AdvancedWasher 类的__init__函数中，可以通过调用                 方法来初始化品牌属性。",
                    "\"\"\"。。。省略。。。\"\"\"",
                    "class AdvancedWasher(SpinDryer, SteamCleaner):"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q15",
                "name": "第15题",
                "description": "def __init__(self, brand, has_steam=True):...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "def __init__(self, brand, has_steam=True):",
                "type": "choice",
                "options": [
                    "第3小题：_________________________",
                    "self.has_steam = has_steam",
                    "\"\"\"。。。省略。。。\"\"\"",
                    "AdvancedWasher 类的 wash 方法中，如果洗衣机具有蒸汽功能，则会调用             方法来启动蒸汽清洁。"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q16",
                "name": "第16题",
                "description": "\"\"\"。。。省略。。。\"\"\"...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "\"\"\"。。。省略。。。\"\"\"",
                "type": "choice",
                "options": [
                    "class AdvancedWasher(SpinDryer, SteamCleaner):",
                    "def __init__(self, brand, has_steam=True):",
                    "第3小题：_________________________",
                    "self.has_steam = has_steam"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q17",
                "name": "第17题",
                "description": "def wash(self):...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "def wash(self):",
                "type": "choice",
                "options": [
                    "print(f\"{self.brand} 高级洗衣机开始洗衣程序。\")",
                    "if self.has_steam:",
                    "第4小题：____________",
                    "Washer.wash(self)  # 直接调用Washer类的wash方法"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q18",
                "name": "第18题",
                "description": "\"\"\"。。。省略。。。\"\"\"...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "\"\"\"。。。省略。。。\"\"\"",
                "type": "choice",
                "options": [
                    "当调用 advanced_washer.dry() 时，首先执行的是              类重写的 dry方法，该方法内部调用了 super().dry()，这会执行             类的原始 dry 方法。"
                ],
                "answer": null,
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": null
            },
            {
                "id": "day15_q19",
                "name": "第19题",
                "description": "实现烤箱-烤玉米...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "实现烤箱-烤玉米",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_16",
        "name": "魔法之屋",
        "description": "魔法方法",
        "icon": "fa-sparkles",
        "levels": [
            {
                "id": "day16_q1",
                "name": "第1题",
                "description": "作业 01：车辆租赁费用计算...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "作业 01：车辆租赁费用计算",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_18",
        "name": "文件港湾",
        "description": "文件操作",
        "icon": "fa-file",
        "levels": [
            {
                "id": "day18_q1",
                "name": "第1题",
                "description": "游戏全局状态管理器 - GameManager 类设计...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "游戏全局状态管理器 - GameManager 类设计",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day18_q2",
                "name": "第2题",
                "description": "数据验证...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "数据验证",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day18_q3",
                "name": "第3题",
                "description": "测试代码和主程序保护...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "测试代码和主程序保护",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day18_q4",
                "name": "第4题",
                "description": "命名空间包...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "命名空间包",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day18_q5",
                "name": "第5题",
                "description": "模块的导入方式...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "模块的导入方式",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    },
    {
        "id": "region_19",
        "name": "正则海域",
        "description": "正则表达式",
        "icon": "fa-search",
        "levels": [
            {
                "id": "day19_q1",
                "name": "第1题",
                "description": "完成下列操作前。先创建一个day_18的文件夹。所有操作，均在这个文件夹下完成。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "完成下列操作前。先创建一个day_18的文件夹。所有操作，均在这个文件夹下完成。",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day19_q2",
                "name": "第2题",
                "description": "5...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "5",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day19_q3",
                "name": "第3题",
                "description": "8...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "8",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day19_q4",
                "name": "第4题",
                "description": "将排序后的结果依次输入到新文件中。排序结果要求如下：...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "将排序后的结果依次输入到新文件中。排序结果要求如下：",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day19_q5",
                "name": "第5题",
                "description": "0...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "0",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day19_q6",
                "name": "第6题",
                "description": "8...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "8",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day19_q7",
                "name": "第7题",
                "description": "5...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "5",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            },
            {
                "id": "day19_q8",
                "name": "第8题",
                "description": "0...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "0",
                "type": "code",
                "options": [],
                "answer": "",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": ""
            }
        ]
    }
]

def get_region_by_id(region_id):
    for region in REGIONS:
        if region['id'] == region_id:
            return region
    return None

def get_level_by_id(region_id, level_id):
    region = get_region_by_id(region_id)
    if region:
        for level in region['levels']:
            if level['id'] == level_id:
                return level
    return None

def get_all_regions():
    return REGIONS