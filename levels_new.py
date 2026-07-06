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
                "description": "Python是一种什么类型的语言？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "Python是一种什么类型的语言？",
                "type": "choice",
                "options": [
                    "A. 编译型语言",
                    "B. 解释型语言",
                    "C. 标记语言",
                    "D. 前端语言"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day1_q2",
                "name": "第2题",
                "description": "PyCharm是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "PyCharm是什么？",
                "type": "choice",
                "options": [
                    "A. 一种编程语言",
                    "B. 一种操作系统",
                    "C. 一款Python集成开发环境（IDE）",
                    "D. 一种数据库管理系统"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day1_q3",
                "name": "第3题",
                "description": "在PyCharm中，如何创建一个新的Python项目？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在PyCharm中，如何创建一个新的Python项目？",
                "type": "choice",
                "options": [
                    "A. 通过菜单选择“文件” -> “新建项目”",
                    "B. 通过命令行创建",
                    "C. 直接打开一个Python文件",
                    "D. 无法在PyCharm中创建新项目"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day1_q4",
                "name": "第4题",
                "description": "Python的主要特点之一是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "Python的主要特点之一是什么？",
                "type": "choice",
                "options": [
                    "A. 语法复杂",
                    "B. 简单易学，适合初学者",
                    "C. 仅适用于Web开发",
                    "D. 运行速度极快"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day1_q5",
                "name": "第5题",
                "description": "下列哪个领域不是Python的典型应用？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "下列哪个领域不是Python的典型应用？",
                "type": "choice",
                "options": [
                    "A. Web开发",
                    "B. 数据分析",
                    "C. 高性能实时游戏引擎开发",
                    "D. 人工智能与机器学习"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day1_q6",
                "name": "第6题",
                "description": "以下哪个是python语法的特点:...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个是python语法的特点:",
                "type": "choice",
                "options": [
                    "A. 解释性语言",
                    "B. 面向对象",
                    "C. 跨平台",
                    "D. 以上全是"
                ],
                "answer": "D",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "D"
            },
            {
                "id": "day1_q7",
                "name": "第7题",
                "description": "在PyCharm中，如何运行一个Python脚本？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在PyCharm中，如何运行一个Python脚本？",
                "type": "choice",
                "options": [
                    "A. 右键点击文件并选择“运行”",
                    "B. 通过命令行运行",
                    "C. 直接在编辑器中输入代码",
                    "D. 无法在PyCharm中运行脚本"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day1_q8",
                "name": "第8题",
                "description": "Python文件的扩展名是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "Python文件的扩展名是什么？",
                "type": "choice",
                "options": [
                    "A. .java",
                    "B. .py",
                    "C. .cpp",
                    "D. .js"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day1_q9",
                "name": "第9题",
                "description": "在Python中，单行注释使用什么符号？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，单行注释使用什么符号？",
                "type": "choice",
                "options": [
                    "A. //",
                    "B. /* */",
                    "C. #",
                    "D. --"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day1_q10",
                "name": "第10题",
                "description": "以下哪个不是Python的关键字？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个不是Python的关键字？",
                "type": "choice",
                "options": [
                    "A. if",
                    "B. for",
                    "C. function",
                    "D. else"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day1_q11",
                "name": "第11题",
                "description": "使用print函数输出两行内容：第一行'欢迎来到Python世界'，第二行'开始你的编程之旅吧'...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用print函数输出两行内容：第一行'欢迎来到Python世界'，第二行'开始你的编程之旅吧'",
                "type": "code",
                "options": [],
                "answer": "print('欢迎来到Python世界')\nprint('开始你的编程之旅吧')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "print('欢迎来到Python世界'",
                "solution": "print('欢迎来到Python世界')\nprint('开始你的编程之旅吧')"
            },
            {
                "id": "day1_q12",
                "name": "第12题",
                "description": "编写一段代码，输出以下图案：\n*\n**\n***...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一段代码，输出以下图案：\n*\n**\n***",
                "type": "code",
                "options": [],
                "answer": "print('*')\nprint('**')\nprint('***')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "print('*'",
                "solution": "print('*')\nprint('**')\nprint('***')"
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
                    "'123'",
                    "3.14",
                    "1101",
                    "\"hello\""
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day2_q2",
                "name": "第2题",
                "description": "下面选项中，哪个是符合Python变量命名规则的正确赋值语句？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "下面选项中，哪个是符合Python变量命名规则的正确赋值语句？",
                "type": "choice",
                "options": [
                    "1num = 10",
                    "int = 10",
                    "int_01 = 10",
                    "$money = 100"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day2_q3",
                "name": "第3题",
                "description": "下面关于python变量类型的说法，正确的是？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "下面关于python变量类型的说法，正确的是？",
                "type": "choice",
                "options": [
                    "变量类型必须在定义时指定",
                    "变量类型在赋值时确定",
                    "变量类型一旦确定就不能改变",
                    "变量类型与赋值无关"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day2_q4",
                "name": "第4题",
                "description": "下面变量x的类型是什么？x = 123_456_789...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "下面变量x的类型是什么？x = 123_456_789",
                "type": "choice",
                "options": [
                    "float",
                    "int",
                    "str",
                    "bool"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day2_q5",
                "name": "第5题",
                "description": "在Python中，使用input()函数接收用户输入时，输入的值默认是什么类型？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，使用input()函数接收用户输入时，输入的值默认是什么类型？",
                "type": "choice",
                "options": [
                    "输入什么类型就是什么类型。",
                    "字符串类型。",
                    "整数类型。",
                    "浮点数类型。"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day2_q6",
                "name": "第6题",
                "description": "在Python中，print函数的主要用途是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，print函数的主要用途是什么？",
                "type": "choice",
                "options": [
                    "从用户那里接收输入",
                    "将数据写入文件",
                    "在控制台输出内容",
                    "执行数学计算"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day2_q7",
                "name": "第7题",
                "description": "以下哪个表达式的结果是True？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个表达式的结果是True？",
                "type": "choice",
                "options": [
                    "3 > 5",
                    "2 == 2",
                    "1 != 1",
                    "4 < 3"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day2_q8",
                "name": "第8题",
                "description": "以下哪个是Python中的字符串？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个是Python中的字符串？",
                "type": "choice",
                "options": [
                    "123",
                    "3.14",
                    "\"hello\"",
                    "True"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day2_q9",
                "name": "第9题",
                "description": "字符串与数字类型（int、float）之间的转换：将字符串'123'转换为整数，将字符串'3.14'...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "字符串与数字类型（int、float）之间的转换：将字符串'123'转换为整数，将字符串'3.14'转换为浮点数",
                "type": "code",
                "options": [],
                "answer": "num1 = int('123')\nnum2 = float('3.14')\nprint(num1)\nprint(num2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "num1 = ",
                "solution": "num1 = int('123')\nnum2 = float('3.14')\nprint(num1)\nprint(num2)"
            },
            {
                "id": "day2_q10",
                "name": "第10题",
                "description": "从控制台接收用户输入的一个浮点数，打印输入值的类型，再将其转换为整数并打印转换后的值及其类型...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "从控制台接收用户输入的一个浮点数，打印输入值的类型，再将其转换为整数并打印转换后的值及其类型",
                "type": "code",
                "options": [],
                "answer": "num = float(input())\nprint(type(num))\nnum_int = int(num)\nprint(num_int)\nprint(type(num_int))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "num = ",
                "solution": "num = float(input())\nprint(type(num))\nnum_int = int(num)\nprint(num_int)\nprint(type(num_int))"
            },
            {
                "id": "day2_q11",
                "name": "第11题",
                "description": "转换为绝对值：计算数字-5和-3.14的绝对值...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "转换为绝对值：计算数字-5和-3.14的绝对值",
                "type": "code",
                "options": [],
                "answer": "x = -5\ny = -3.14\nprint(abs(x))\nprint(abs(y))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "x = ",
                "solution": "x = -5\ny = -3.14\nprint(abs(x))\nprint(abs(y))"
            },
            {
                "id": "day2_q12",
                "name": "第12题",
                "description": "将整数100转换为字符串，将浮点数3.14转换为字符串...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "将整数100转换为字符串，将浮点数3.14转换为字符串",
                "type": "code",
                "options": [],
                "answer": "str1 = str(100)\nstr2 = str(3.14)\nprint(str1)\nprint(str2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "str1 = ",
                "solution": "str1 = str(100)\nstr2 = str(3.14)\nprint(str1)\nprint(str2)"
            },
            {
                "id": "day2_q13",
                "name": "第13题",
                "description": "编写一个Python程序：提示用户输入一个负整数，使用abs函数计算其绝对值，输出格式为“其绝对值是...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一个Python程序：提示用户输入一个负整数，使用abs函数计算其绝对值，输出格式为“其绝对值是XXX”",
                "type": "code",
                "options": [],
                "answer": "num = int(input())\nresult = abs(num)\nprint('其绝对值是', result)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "num = ",
                "solution": "num = int(input())\nresult = abs(num)\nprint('其绝对值是', result)"
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
                "description": "变量名命名规则中，以下哪个是非法的变量名？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "变量名命名规则中，以下哪个是非法的变量名？",
                "type": "choice",
                "options": [
                    "A. lala111",
                    "B. 222baby",
                    "C. Zhou",
                    "D. _zhou"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q2",
                "name": "第2题",
                "description": "python3中，如何打印变量message的值，其中message的值为Hello, World!...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "python3中，如何打印变量message的值，其中message的值为Hello, World!？",
                "type": "choice",
                "options": [
                    "A. print 'Hello, World!'",
                    "B. print \"message\"",
                    "C. print message",
                    "D. print(message)"
                ],
                "answer": "D",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "D"
            },
            {
                "id": "day3_q3",
                "name": "第3题",
                "description": "以下哪个是Python中的布尔值？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个是Python中的布尔值？",
                "type": "choice",
                "options": [
                    "A. 只有True",
                    "B. false",
                    "C. 1",
                    "D. True 和 False"
                ],
                "answer": "D",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "D"
            },
            {
                "id": "day3_q4",
                "name": "第4题",
                "description": "如何将整数10转换为字符串？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "如何将整数10转换为字符串？",
                "type": "choice",
                "options": [
                    "A. str(10)",
                    "B. int(\"10\")",
                    "C. float(10)",
                    "D. bool(10)"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day3_q5",
                "name": "第5题",
                "description": "下列哪个不是Python的内置数据类型？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "下列哪个不是Python的内置数据类型？",
                "type": "choice",
                "options": [
                    "A. int",
                    "B. str",
                    "C. boolean",
                    "D. float"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day3_q6",
                "name": "第6题",
                "description": "在Python中，以下哪个表达式的值是False？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，以下哪个表达式的值是False？",
                "type": "choice",
                "options": [
                    "A. True and True",
                    "B. True or False",
                    "C. not True",
                    "D. True and not False"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day3_q7",
                "name": "第7题",
                "description": "以下哪个表达式的结果是True？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个表达式的结果是True？",
                "type": "choice",
                "options": [
                    "A. \"abc\" == \"ABC\"",
                    "B. 10 > 5 and 3 < 2",
                    "C. 5 != 6",
                    "D. not (2 == 2)"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day3_q8",
                "name": "第8题",
                "description": "在Python中，使用哪个关键字来定义条件判断？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，使用哪个关键字来定义条件判断？",
                "type": "choice",
                "options": [
                    "A. for",
                    "B. while",
                    "C. if",
                    "D. def"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day3_q9",
                "name": "第9题",
                "description": "以下哪个表达式的值是True？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个表达式的值是True？",
                "type": "choice",
                "options": [
                    "A. 3 >= 5",
                    "B. 4 <= 4",
                    "C. 2 > 2",
                    "D. 1 != 1"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q10",
                "name": "第10题",
                "description": "如何判断两个变量是否相等？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "如何判断两个变量是否相等？",
                "type": "choice",
                "options": [
                    "A. =",
                    "B. ==",
                    "C. ===",
                    "D. equals()"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q11",
                "name": "第11题",
                "description": "以下哪个是Python中的转义字符？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个是Python中的转义字符？",
                "type": "choice",
                "options": [
                    "A. \\\\n",
                    "B. \\n",
                    "C. /n",
                    "D. \\\\N"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day3_q12",
                "name": "第12题",
                "description": "在字符串中，如何表示换行？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在字符串中，如何表示换行？",
                "type": "choice",
                "options": [
                    "A. \\r",
                    "B. \\n",
                    "C. \\t",
                    "D. \\b"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q13",
                "name": "第13题",
                "description": "以下哪个转义字符表示制表符？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个转义字符表示制表符？",
                "type": "choice",
                "options": [
                    "A. \\n",
                    "B. \\t",
                    "C. \\r",
                    "D. \\f"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q14",
                "name": "第14题",
                "description": "布尔类型有几个值？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "布尔类型有几个值？",
                "type": "choice",
                "options": [
                    "A. 一个",
                    "B. 两个",
                    "C. 三个",
                    "D. 无数个"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q15",
                "name": "第15题",
                "description": "not True 的结果是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "not True 的结果是什么？",
                "type": "choice",
                "options": [
                    "A. True",
                    "B. False",
                    "C. None",
                    "D. Error"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q16",
                "name": "第16题",
                "description": "True and False 的结果是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "True and False 的结果是什么？",
                "type": "choice",
                "options": [
                    "A. True",
                    "B. False",
                    "C. None",
                    "D. Error"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q17",
                "name": "第17题",
                "description": "True or False 的结果是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "True or False 的结果是什么？",
                "type": "choice",
                "options": [
                    "A. True",
                    "B. False",
                    "C. None",
                    "D. Error"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day3_q18",
                "name": "第18题",
                "description": "在Python中，0的布尔值是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，0的布尔值是什么？",
                "type": "choice",
                "options": [
                    "A. True",
                    "B. False",
                    "C. None",
                    "D. Error"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q19",
                "name": "第19题",
                "description": "空字符串的布尔值是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "空字符串的布尔值是什么？",
                "type": "choice",
                "options": [
                    "A. True",
                    "B. False",
                    "C. None",
                    "D. Error"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day3_q20",
                "name": "第20题",
                "description": "以下哪个表达式的值是True？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "以下哪个表达式的值是True？",
                "type": "choice",
                "options": [
                    "A. bool(0)",
                    "B. bool(\"\")",
                    "C. bool([1])",
                    "D. bool(None)"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day3_q21",
                "name": "第21题",
                "description": "在Python中，如何将字符串转换为布尔值？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "在Python中，如何将字符串转换为布尔值？",
                "type": "choice",
                "options": [
                    "A. bool()",
                    "B. boolean()",
                    "C. to_bool()",
                    "D. convert_bool()"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
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
                "description": "从键盘上输入一个浮点数，使用if-else语句来判断这个数是正数、负数还是零，并输出相应的结果。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "从键盘上输入一个浮点数，使用if-else语句来判断这个数是正数、负数还是零，并输出相应的结果。",
                "type": "code",
                "options": [],
                "answer": "number = float(input('请输入一个浮点数：'))\nif number > 0:\n    print(number, '是正数。')\nelif number < 0:\n    print(number, '是负数。')\nelse:\n    print(number, '是零。')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "number = ",
                "solution": "number = float(input('请输入一个浮点数：'))\nif number > 0:\n    print(number, '是正数。')\nelif number < 0:\n    print(number, '是负数。')\nelse:\n    print(number, '是零。')"
            },
            {
                "id": "day4_q2",
                "name": "第2题",
                "description": "第 02 题：判断是否水仙花数\n题目描述：从键盘上输入一个三位数的数，判断这个数字是否是三位数的数字...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "第 02 题：判断是否水仙花数\n题目描述：从键盘上输入一个三位数的数，判断这个数字是否是三位数的数字，再判断是否是水仙花数。\n(水仙花数：一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。本题只需要输入3位数。)",
                "type": "code",
                "options": [],
                "answer": "number = int(input('请输入一个三位数：'))\nif number < 100 or number > 999:\n    print('无效的输入')\nelse:\n    hundreds = number // 100\n    tens = (number // 10) % 10\n    ones = number % 10\n    cube_sum = hundreds ** 3 + tens ** 3 + ones ** 3\n    if cube_sum == number:\n        print(number, '是水仙花数')\n    else:\n        print(number, '不是水仙花数')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "number = ",
                "solution": "number = int(input('请输入一个三位数：'))\nif number < 100 or number > 999:\n    print('无效的输入')\nelse:\n    hundreds = number // 100\n    tens = (number // 10) % 10\n    ones = number % 10\n    cube_sum = hundreds ** 3 + tens ** 3 + ones ** 3\n    if cube_sum == number:\n        print(number, '是水仙花数')\n    else:\n        print(number, '不是水仙花数')"
            },
            {
                "id": "day4_q3",
                "name": "第3题",
                "description": "编写一个计算商品购物折扣的程序，折扣规则如下：\n如果购物金额小于100元，则不享受折扣。\n如果购物金...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一个计算商品购物折扣的程序，折扣规则如下：\n如果购物金额小于100元，则不享受折扣。\n如果购物金额在100元（含）至300元之间，则享受9折优惠。\n如果购物金额超过300元，则享受85折优惠。",
                "type": "code",
                "options": [],
                "answer": "shopping_amount = float(input('请输入购物金额：'))\nif shopping_amount < 100:\n    print('您没有享受折扣,需支付:', str(shopping_amount), '元')\nelif shopping_amount >= 100 and shopping_amount < 300:\n    discount = shopping_amount * 0.9\n    print('您可享受9折优惠,需支付:', str(discount), '元')\nelse:\n    discount = shopping_amount * 0.85\n    print('您可享受85折优惠,需支付:', str(discount), '元')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "shopping_amount = ",
                "solution": "shopping_amount = float(input('请输入购物金额：'))\nif shopping_amount < 100:\n    print('您没有享受折扣,需支付:', str(shopping_amount), '元')\nelif shopping_amount >= 100 and shopping_amount < 300:\n    discount = shopping_amount * 0.9\n    print('您可享受9折优惠,需支付:', str(discount), '元')\nelse:\n    discount = shopping_amount * 0.85\n    print('您可享受85折优惠,需支付:', str(discount), '元')"
            },
            {
                "id": "day4_q4",
                "name": "第4题",
                "description": "编写一段代码，模拟交通信号灯的工作。要求用户输入颜色（红、黄、绿），根据颜色输出相应的指示信息。\n输...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一段代码，模拟交通信号灯的工作。要求用户输入颜色（红、黄、绿），根据颜色输出相应的指示信息。\n输入红色(red),输出:请停车\n输入黄色(yellow),输出:准备停车/尽快通行\n输入绿色(green),输出:允许通行",
                "type": "code",
                "options": [],
                "answer": "color = input('请输入颜色（红、黄、绿）：')\nif color == 'red' or color == '红色':\n    print('请停车')\nelif color == 'yellow' or color == '黄色':\n    print('准备停车/尽快通行')\nelif color == 'green' or color == '绿色':\n    print('允许通行')\nelse:\n    print('无效的颜色，请输入红色(red)、黄色(yellow)或绿色(green)')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "color = ",
                "solution": "color = input('请输入颜色（红、黄、绿）：')\nif color == 'red' or color == '红色':\n    print('请停车')\nelif color == 'yellow' or color == '黄色':\n    print('准备停车/尽快通行')\nelif color == 'green' or color == '绿色':\n    print('允许通行')\nelse:\n    print('无效的颜色，请输入红色(red)、黄色(yellow)或绿色(green)')"
            },
            {
                "id": "day4_q5",
                "name": "第5题",
                "description": "编写一个程序，让用户输入三角形的三条边长，判断并输出三角形的类型：\n等边三角形：三条边相等\n等腰三角...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一个程序，让用户输入三角形的三条边长，判断并输出三角形的类型：\n等边三角形：三条边相等\n等腰三角形：至少有两条边相等\n直角三角形：满足勾股定理\n不是三角形：不符合三角形的边长关系",
                "type": "code",
                "options": [],
                "answer": "side1 = float(input('请输入第一条边：'))\nside2 = float(input('请输入第二条边：'))\nside3 = float(input('请输入第三条边：'))\n\nif side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:\n    if side1 == side2 == side3:\n        print('这是一个等边三角形')\n    elif side1 == side2 or side1 == side3 or side2 == side3:\n        print('这是一个等腰三角形')\n    elif side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:\n        print('这是一个直角三角形')\n    else:\n        print('这是一个普通三角形')\nelse:\n    print('不是三角形')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "side1 = ",
                "solution": "side1 = float(input('请输入第一条边：'))\nside2 = float(input('请输入第二条边：'))\nside3 = float(input('请输入第三条边：'))\n\nif side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:\n    if side1 == side2 == side3:\n        print('这是一个等边三角形')\n    elif side1 == side2 or side1 == side3 or side2 == side3:\n        print('这是一个等腰三角形')\n    elif side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:\n        print('这是一个直角三角形')\n    else:\n        print('这是一个普通三角形')\nelse:\n    print('不是三角形')"
            }
        ]
    },
    {
        "id": "region_5",
        "name": "循环山脉",
        "description": "for循环与while循环",
        "icon": "fa-mountain",
        "levels": [
            {
                "id": "day5_q1",
                "name": "第1题",
                "description": "编写一个Python程序，需要用户输入用户名（admin）和密码（password）后重复三次后登录...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一个Python程序，需要用户输入用户名（admin）和密码（password）后重复三次后登录成功。",
                "type": "code",
                "options": [],
                "answer": "success_count = 0\nfor i in range(3):\n    username = input('请输入用户名：')\n    password = input('请输入密码：')\n    if username == 'admin' and password == 'password':\n        success_count += 1\n        print('第{}次输入正确'.format(i+1))\n    else:\n        print('第{}次输入错误'.format(i+1))\nif success_count == 3:\n    print('登录成功')\nelse:\n    print('登录失败，失败次数：', 3 - success_count)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "success_count = ",
                "solution": "success_count = 0\nfor i in range(3):\n    username = input('请输入用户名：')\n    password = input('请输入密码：')\n    if username == 'admin' and password == 'password':\n        success_count += 1\n        print('第{}次输入正确'.format(i+1))\n    else:\n        print('第{}次输入错误'.format(i+1))\nif success_count == 3:\n    print('登录成功')\nelse:\n    print('登录失败，失败次数：', 3 - success_count)"
            },
            {
                "id": "day5_q2",
                "name": "第2题",
                "description": "打印一个5行5列的正方形图案。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "打印一个5行5列的正方形图案。",
                "type": "code",
                "options": [],
                "answer": "for i in range(5):\n    for j in range(5):\n        print('*', end='  ')\n    print()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "for i in range(5):\n    for j in range(5):\n        print('*', end='  ')\n    print()"
            },
            {
                "id": "day5_q3",
                "name": "第3题",
                "description": "打印一个正直角三角形图案，5行，每行星号递增。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "打印一个正直角三角形图案，5行，每行星号递增。",
                "type": "code",
                "options": [],
                "answer": "for i in range(5):\n    for j in range(i + 1):\n        print('*', end='  ')\n    print()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "for i in range(5):\n    for j in range(i + 1):\n        print('*', end='  ')\n    print()"
            },
            {
                "id": "day5_q4",
                "name": "第4题",
                "description": "打印一个倒直角三角形图案，5行，每行星号递减。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "打印一个倒直角三角形图案，5行，每行星号递减。",
                "type": "code",
                "options": [],
                "answer": "for i in range(5, 0, -1):\n    for j in range(i):\n        print('*', end='  ')\n    print()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "for i in range(5, 0, -1):\n    for j in range(i):\n        print('*', end='  ')\n    print()"
            },
            {
                "id": "day5_q5",
                "name": "第5题",
                "description": "使用for循环实现99乘法表。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用for循环实现99乘法表。",
                "type": "code",
                "options": [],
                "answer": "for i in range(1, 10):\n    for j in range(1, i + 1):\n        print('{}x{}={}'.format(j, i, i * j), end='\\t')\n    print()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "for i in range(1, 10):\n    for j in range(1, i + 1):\n        print('{}x{}={}'.format(j, i, i * j), end='\\t')\n    print()"
            },
            {
                "id": "day5_q6",
                "name": "第6题",
                "description": "你有一个存钱罐，每天存入相同数量的硬币。编写一个Python程序，通过用户输入每天存入的硬币数量和总...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "你有一个存钱罐，每天存入相同数量的硬币。编写一个Python程序，通过用户输入每天存入的硬币数量和总天数，使用for循环计算并输出从第1天到指定天数，你总共存入了多少硬币。",
                "type": "code",
                "options": [],
                "answer": "coins_per_day = int(input('请输入每天存入的硬币数量：'))\ntotal_days = int(input('请输入总天数：'))\ntotal_coins = 0\nfor day in range(1, total_days + 1):\n    total_coins += coins_per_day\n    print('第{}天：累计存入{}枚硬币'.format(day, total_coins))\nprint('总共存入{}枚硬币'.format(total_coins))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "coins_per_day = ",
                "solution": "coins_per_day = int(input('请输入每天存入的硬币数量：'))\ntotal_days = int(input('请输入总天数：'))\ntotal_coins = 0\nfor day in range(1, total_days + 1):\n    total_coins += coins_per_day\n    print('第{}天：累计存入{}枚硬币'.format(day, total_coins))\nprint('总共存入{}枚硬币'.format(total_coins))"
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
                "description": "1. 在 Python 中，列表的索引是从哪个数字开始的？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "1. 在 Python 中，列表的索引是从哪个数字开始的？",
                "type": "choice",
                "options": [
                    "0",
                    "1",
                    "2",
                    "随机数"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day6_q2",
                "name": "第2题",
                "description": "2. 以下哪项是 Python 列表的一个特性？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "2. 以下哪项是 Python 列表的一个特性？",
                "type": "choice",
                "options": [
                    "所有元素必须唯一",
                    "可以修改其中的元素",
                    "元素不能排序",
                    "不能通过索引访问元素"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day6_q3",
                "name": "第3题",
                "description": "3. 以下哪个方法用于向列表末尾添加一个元素？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "3. 以下哪个方法用于向列表末尾添加一个元素？",
                "type": "choice",
                "options": [
                    "append()",
                    "extend()",
                    "insert()",
                    "pop()"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day6_q4",
                "name": "第4题",
                "description": "4.以下哪个方法用于从列表中移除指定位置的元素？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "4.以下哪个方法用于从列表中移除指定位置的元素？",
                "type": "choice",
                "options": [
                    "remove()",
                    "pop()",
                    "delete()",
                    "erase()"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day6_q5",
                "name": "第5题",
                "description": "5. 以下哪个方法用于对列表进行排序？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "5. 以下哪个方法用于对列表进行排序？",
                "type": "choice",
                "options": [
                    "sort()",
                    "order()",
                    "arrange()",
                    "sort_list()"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day6_q6",
                "name": "第6题",
                "description": "6. 以下哪个表达式可以获取列表的长度？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "6. 以下哪个表达式可以获取列表的长度？",
                "type": "choice",
                "options": [
                    "length(list)",
                    "len(list)",
                    "list.length",
                    "list.size()"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day6_q7",
                "name": "第7题",
                "description": "7. 以下哪个是列表的切片操作？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "7. 以下哪个是列表的切片操作？",
                "type": "choice",
                "options": [
                    "list[1]",
                    "list[1:3]",
                    "list(1,3)",
                    "get_slice(list,1,3)"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day6_q8",
                "name": "第8题",
                "description": "8. 以下哪个方法用于在列表指定位置插入元素？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "8. 以下哪个方法用于在列表指定位置插入元素？",
                "type": "choice",
                "options": [
                    "append()",
                    "extend()",
                    "insert()",
                    "add()"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
            },
            {
                "id": "day6_q9",
                "name": "第9题",
                "description": "9. 以下哪个方法用于反转列表？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "9. 以下哪个方法用于反转列表？",
                "type": "choice",
                "options": [
                    "reverse()",
                    "invert()",
                    "flip()",
                    "backwards()"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day6_q10",
                "name": "第10题",
                "description": "10. 以下哪个表达式可以检查元素是否在列表中？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "10. 以下哪个表达式可以检查元素是否在列表中？",
                "type": "choice",
                "options": [
                    "element in list",
                    "list.contains(element)",
                    "check(list, element)",
                    "has_element(list, element)"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
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
                "description": "1. Python 集合中的元素是有序的吗？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "1. Python 集合中的元素是有序的吗？",
                "type": "choice",
                "options": [
                    "是的，它们是有序的",
                    "不是的，它们是无序的",
                    "只有在特定情况下才是无序的",
                    "取决于集合的大小"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day7_q2",
                "name": "第2题",
                "description": "2.以下哪种定义方式，不是元组：...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "2.以下哪种定义方式，不是元组：",
                "type": "choice",
                "options": [
                    "tuple_01 = (1, 2, 3)",
                    "tuple_02 = ()",
                    "tuple_03 = (4,)",
                    "tuple_04 = tuple([5, 6, 7])",
                    "tuple_05 = (8)"
                ],
                "answer": "E",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "E"
            },
            {
                "id": "day7_q3",
                "name": "第3题",
                "description": "3. 元组和列表的主要区别是什么？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "3. 元组和列表的主要区别是什么？",
                "type": "choice",
                "options": [
                    "元组可以被修改，列表不可以",
                    "列表可以被修改，元组不可以",
                    "元组和列表都可以被修改",
                    "元组和列表都不可以被修改"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day7_q4",
                "name": "第4题",
                "description": "4. 假设有一个元组 t = (5, 'a', 3, 'b', 1)，那么 t[2:4] 的结果是什...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "4. 假设有一个元组 t = (5, 'a', 3, 'b', 1)，那么 t[2:4] 的结果是什么？",
                "type": "choice",
                "options": [
                    "(3, 'b')",
                    "('a', 3)",
                    "(5, 'a', 3)",
                    "(3, 'b', 1)"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day7_q5",
                "name": "第5题",
                "description": "5. 以下哪个方法可以向集合中添加元素？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "5. 以下哪个方法可以向集合中添加元素？",
                "type": "choice",
                "options": [
                    "append()",
                    "add()",
                    "insert()",
                    "extend()"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day7_q6",
                "name": "第6题",
                "description": "6. 以下哪个方法可以求两个集合的交集？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "6. 以下哪个方法可以求两个集合的交集？",
                "type": "choice",
                "options": [
                    "union()",
                    "intersection()",
                    "difference()",
                    "symmetric_difference()"
                ],
                "answer": "B",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "B"
            },
            {
                "id": "day7_q7",
                "name": "第7题",
                "description": "7. 以下哪个方法可以求两个集合的并集？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "7. 以下哪个方法可以求两个集合的并集？",
                "type": "choice",
                "options": [
                    "union()",
                    "intersection()",
                    "difference()",
                    "symmetric_difference()"
                ],
                "answer": "A",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "A"
            },
            {
                "id": "day7_q8",
                "name": "第8题",
                "description": "8. 以下哪个是集合的特性？...",
                "difficulty": "简单",
                "exp_reward": 20,
                "gold_reward": 10,
                "question": "8. 以下哪个是集合的特性？",
                "type": "choice",
                "options": [
                    "元素可以重复",
                    "元素是有序的",
                    "元素是唯一的",
                    "可以通过索引访问"
                ],
                "answer": "C",
                "hints": [
                    "选择正确的选项"
                ],
                "code_template": "",
                "solution": "C"
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
                "description": "使用format方法格式化字符串。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用format方法格式化字符串。",
                "type": "code",
                "options": [],
                "answer": "city = '哈尔滨'\ntemperature = -15.5\nreport = '当前城市 {} 温度为 {} 摄氏度。'\nformatted_report = report.format(city, temperature)\nprint(formatted_report)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "city = ",
                "solution": "city = '哈尔滨'\ntemperature = -15.5\nreport = '当前城市 {} 温度为 {} 摄氏度。'\nformatted_report = report.format(city, temperature)\nprint(formatted_report)"
            },
            {
                "id": "day8_q2",
                "name": "第2题",
                "description": "使用f-string格式化字符串。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用f-string格式化字符串。",
                "type": "code",
                "options": [],
                "answer": "city = '哈尔滨'\ntemperature = -15.5\nreport = f'当前城市 {city} 温度为 {temperature} 摄氏度。'\nprint(report)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "city = ",
                "solution": "city = '哈尔滨'\ntemperature = -15.5\nreport = f'当前城市 {city} 温度为 {temperature} 摄氏度。'\nprint(report)"
            },
            {
                "id": "day8_q3",
                "name": "第3题",
                "description": "使用round函数进行四舍五入。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用round函数进行四舍五入。",
                "type": "code",
                "options": [],
                "answer": "print(round(3.7))\nprint(round(3.2))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "print(round(3.7)",
                "solution": "print(round(3.7))\nprint(round(3.2))"
            },
            {
                "id": "day8_q4",
                "name": "第4题",
                "description": "使用math模块的ceil和floor函数。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用math模块的ceil和floor函数。",
                "type": "code",
                "options": [],
                "answer": "import math\nprint(math.ceil(3.2))\nprint(math.floor(3.7))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "import math\nprint(math.ceil(3.2))\nprint(math.floor(3.7))"
            },
            {
                "id": "day8_q5",
                "name": "第5题",
                "description": "计算绝对值。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "计算绝对值。",
                "type": "code",
                "options": [],
                "answer": "print(abs(-5))\nprint(abs(-3.14))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "print(abs(-5)",
                "solution": "print(abs(-5))\nprint(abs(-3.14))"
            },
            {
                "id": "day8_q6",
                "name": "第6题",
                "description": "找出最大值和最小值。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "找出最大值和最小值。",
                "type": "code",
                "options": [],
                "answer": "print(max(1, 2, 3))\nprint(min(1, 2, 3))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "print(max(1, 2, 3)",
                "solution": "print(max(1, 2, 3))\nprint(min(1, 2, 3))"
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
                "description": "定义一个函数greet(name)，接收一个姓名参数，打印'Hello, '加上姓名并加感叹号。然后...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个函数greet(name)，接收一个姓名参数，打印'Hello, '加上姓名并加感叹号。然后调用greet('World')测试。",
                "type": "code",
                "options": [],
                "answer": "def greet(name):\n    print('Hello, ' + name + '!')\ngreet('World')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def greet(name):\n    ",
                "solution": "def greet(name):\n    print('Hello, ' + name + '!')\ngreet('World')"
            },
            {
                "id": "day9_q2",
                "name": "第2题",
                "description": "定义一个函数add(a, b)，接收两个参数，返回它们的和。调用add(3, 5)并打印结果。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个函数add(a, b)，接收两个参数，返回它们的和。调用add(3, 5)并打印结果。",
                "type": "code",
                "options": [],
                "answer": "def add(a, b):\n    return a + b\nresult = add(3, 5)\nprint(result)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def add(a, b):\n    ",
                "solution": "def add(a, b):\n    return a + b\nresult = add(3, 5)\nprint(result)"
            },
            {
                "id": "day9_q3",
                "name": "第3题",
                "description": "定义一个函数calculate_area(radius)，接收半径参数，返回圆的面积（π取3.141...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个函数calculate_area(radius)，接收半径参数，返回圆的面积（π取3.14159）。调用函数计算半径为5的圆面积。",
                "type": "code",
                "options": [],
                "answer": "def calculate_area(radius):\n    return 3.14159 * radius ** 2\narea = calculate_area(5)\nprint(area)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def calculate_area(radius):\n    ",
                "solution": "def calculate_area(radius):\n    return 3.14159 * radius ** 2\narea = calculate_area(5)\nprint(area)"
            },
            {
                "id": "day9_q4",
                "name": "第4题",
                "description": "定义一个函数is_even(num)，接收一个整数参数，返回该数是否为偶数的布尔值。分别传入4和5测...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个函数is_even(num)，接收一个整数参数，返回该数是否为偶数的布尔值。分别传入4和5测试并打印结果。",
                "type": "code",
                "options": [],
                "answer": "def is_even(num):\n    return num % 2 == 0\nprint(is_even(4))\nprint(is_even(5))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def is_even(num):\n    ",
                "solution": "def is_even(num):\n    return num % 2 == 0\nprint(is_even(4))\nprint(is_even(5))"
            }
        ]
    },
    {
        "id": "region_10",
        "name": "字典王国",
        "description": "字典、深拷贝与浅拷贝",
        "icon": "fa-book-open",
        "levels": [
            {
                "id": "day10_q1",
                "name": "第1题",
                "description": "创建一个字典student，包含name（张三）、age（18）、score（95）三个键值对。分别...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个字典student，包含name（张三）、age（18）、score（95）三个键值对。分别打印name和score的值。",
                "type": "code",
                "options": [],
                "answer": "student = {'name': '张三', 'age': 18, 'score': 95}\nprint(student['name'])\nprint(student['age'])\nprint(student['score'])",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "student = ",
                "solution": "student = {'name': '张三', 'age': 18, 'score': 95}\nprint(student['name'])\nprint(student['age'])\nprint(student['score'])"
            },
            {
                "id": "day10_q2",
                "name": "第2题",
                "description": "创建一个字典student，包含name（张三）、age（18）。添加score为95、gender...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个字典student，包含name（张三）、age（18）。添加score为95、gender为'男'，然后打印完整字典。",
                "type": "code",
                "options": [],
                "answer": "student = {'name': '张三', 'age': 18}\nstudent['score'] = 95\nstudent['gender'] = '男'\nprint(student)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "student = ",
                "solution": "student = {'name': '张三', 'age': 18}\nstudent['score'] = 95\nstudent['gender'] = '男'\nprint(student)"
            },
            {
                "id": "day10_q3",
                "name": "第3题",
                "description": "创建字典student，包含name、age、score三个键值对。分别使用keys()、value...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建字典student，包含name、age、score三个键值对。分别使用keys()、values()、items()方法获取并打印所有键、值、键值对。",
                "type": "code",
                "options": [],
                "answer": "student = {'name': '张三', 'age': 18, 'score': 95}\nkeys = list(student.keys())\nvalues = list(student.values())\nitems = list(student.items())\nprint(keys)\nprint(values)\nprint(items)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "student = ",
                "solution": "student = {'name': '张三', 'age': 18, 'score': 95}\nkeys = list(student.keys())\nvalues = list(student.values())\nitems = list(student.items())\nprint(keys)\nprint(values)\nprint(items)"
            },
            {
                "id": "day10_q4",
                "name": "第4题",
                "description": "创建字典student，包含name和age。使用in关键字检查'score'是否存在于字典中，如果...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建字典student，包含name和age。使用in关键字检查'score'是否存在于字典中，如果存在则打印对应值，否则打印提示信息。",
                "type": "code",
                "options": [],
                "answer": "student = {'name': '张三', 'age': 18}\nif 'score' in student:\n    print(student['score'])\nelse:\n    print('成绩不存在')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "student = ",
                "solution": "student = {'name': '张三', 'age': 18}\nif 'score' in student:\n    print(student['score'])\nelse:\n    print('成绩不存在')"
            }
        ]
    },
    {
        "id": "region_11",
        "name": "函数进阶",
        "description": "函数参数、返回值、递归、闭包与匿名函数",
        "icon": "fa-code",
        "levels": [
            {
                "id": "day11_q1",
                "name": "第1题",
                "description": "定义一个函数greet(name, message='Hello')，name为必传参数，messa...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个函数greet(name, message='Hello')，name为必传参数，message有默认值'Hello'。函数打印message加逗号加name加感叹号。调用greet('Alice')和greet('Bob', 'Hi')。",
                "type": "code",
                "options": [],
                "answer": "def greet(name, message='Hello'):\n    print(message + ', ' + name + '!')\ngreet('World')\ngreet('World', 'Hi')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def greet(name, message = ",
                "solution": "def greet(name, message='Hello'):\n    print(message + ', ' + name + '!')\ngreet('World')\ngreet('World', 'Hi')"
            },
            {
                "id": "day11_q2",
                "name": "第2题",
                "description": "定义一个函数add(*args)，使用可变参数接收任意数量的数字，返回它们的总和。调用add(1, ...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个函数add(*args)，使用可变参数接收任意数量的数字，返回它们的总和。调用add(1, 2, 3, 4)并打印结果。",
                "type": "code",
                "options": [],
                "answer": "def add(*args):\n    total = 0\n    for num in args:\n        total += num\n    return total\nprint(add(1, 2, 3))\nprint(add(1, 2, 3, 4, 5))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def add(*args):\n    ",
                "solution": "def add(*args):\n    total = 0\n    for num in args:\n        total += num\n    return total\nprint(add(1, 2, 3))\nprint(add(1, 2, 3, 4, 5))"
            },
            {
                "id": "day11_q3",
                "name": "第3题",
                "description": "使用递归实现一个函数factorial(n)，计算n的阶乘。当n为0或1时返回1，否则返回n乘以fa...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用递归实现一个函数factorial(n)，计算n的阶乘。当n为0或1时返回1，否则返回n乘以factorial(n-1)。调用factorial(5)测试。",
                "type": "code",
                "options": [],
                "answer": "def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial(n - 1)\nprint(factorial(5))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def factorial(n):\n    ",
                "solution": "def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial(n - 1)\nprint(factorial(5))"
            },
            {
                "id": "day11_q4",
                "name": "第4题",
                "description": "使用递归实现斐波那契数列函数fibonacci(n)，当n<=1时返回n，否则返回fibonacci...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用递归实现斐波那契数列函数fibonacci(n)，当n<=1时返回n，否则返回fibonacci(n-1)+fibonacci(n-2)。调用fibonacci(10)测试。",
                "type": "code",
                "options": [],
                "answer": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)\nfor i in range(10):\n    print(fibonacci(i))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def fibonacci(n):\n    ",
                "solution": "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)\nfor i in range(10):\n    print(fibonacci(i))"
            },
            {
                "id": "day11_q5",
                "name": "第5题",
                "description": "创建一个闭包函数make_counter()，内部定义count变量初始为0，返回一个counter...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个闭包函数make_counter()，内部定义count变量初始为0，返回一个counter函数，每次调用counter()时count加1并返回当前值。",
                "type": "code",
                "options": [],
                "answer": "def make_counter():\n    count = 0\n    def counter():\n        nonlocal count\n        count += 1\n        return count\n    return counter\nc = make_counter()\nprint(c())\nprint(c())\nprint(c())",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def make_counter():\n    ",
                "solution": "def make_counter():\n    count = 0\n    def counter():\n        nonlocal count\n        count += 1\n        return count\n    return counter\nc = make_counter()\nprint(c())\nprint(c())\nprint(c())"
            },
            {
                "id": "day11_q6",
                "name": "第6题",
                "description": "使用lambda表达式创建一个匿名函数add，接收两个参数x和y，返回x+y。调用add(3, 5)...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用lambda表达式创建一个匿名函数add，接收两个参数x和y，返回x+y。调用add(3, 5)并打印结果。",
                "type": "code",
                "options": [],
                "answer": "add = lambda x, y: x + y\nprint(add(3, 5))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "add = ",
                "solution": "add = lambda x, y: x + y\nprint(add(3, 5))"
            },
            {
                "id": "day11_q7",
                "name": "第7题",
                "description": "创建列表numbers = [1, 2, 3, 4, 5]。使用map将每个元素平方，使用filte...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建列表numbers = [1, 2, 3, 4, 5]。使用map将每个元素平方，使用filter过滤出偶数，分别打印结果。",
                "type": "code",
                "options": [],
                "answer": "numbers = [1, 2, 3, 4, 5]\nsquared = list(map(lambda x: x ** 2, numbers))\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(squared)\nprint(evens)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "numbers = ",
                "solution": "numbers = [1, 2, 3, 4, 5]\nsquared = list(map(lambda x: x ** 2, numbers))\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(squared)\nprint(evens)"
            }
        ]
    },
    {
        "id": "region_12",
        "name": "面向对象",
        "description": "类与对象",
        "icon": "fa-object-group",
        "levels": [
            {
                "id": "day12_q1",
                "name": "第1题",
                "description": "定义一个类Person，包含__init__方法接收name和age参数并赋值给实例属性。创建一个P...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义一个类Person，包含__init__方法接收name和age参数并赋值给实例属性。创建一个Person实例并打印其属性。",
                "type": "code",
                "options": [],
                "answer": "class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    def introduce(self):\n        print('我叫', self.name, '今年', self.age, '岁')\np = Person('张三', 18)\np.introduce()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    def introduce(self):\n        print('我叫', self.name, '今年', self.age, '岁')\np = Person('张三', 18)\np.introduce()"
            },
            {
                "id": "day12_q2",
                "name": "第2题",
                "description": "定义类Student，包含类属性school='第一中学'，以及__init__方法接收name和g...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义类Student，包含类属性school='第一中学'，以及__init__方法接收name和grade参数。创建两个实例，修改其中一个的school属性，观察类属性和实例属性的区别。",
                "type": "code",
                "options": [],
                "answer": "class Student:\n    school = '第一中学'\n    def __init__(self, name, grade):\n        self.name = name\n        self.grade = grade\ns = Student('张三', '高三')\nprint(Student.school)\nprint(s.name, s.grade)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Student:\n    school = '第一中学'\n    def __init__(self, name, grade):\n        self.name = name\n        self.grade = grade\ns = Student('张三', '高三')\nprint(Student.school)\nprint(s.name, s.grade)"
            },
            {
                "id": "day12_q3",
                "name": "第3题",
                "description": "定义类Circle，使用私有属性__radius存储半径。提供get_radius和set_radi...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义类Circle，使用私有属性__radius存储半径。提供get_radius和set_radius方法来访问和修改半径。创建实例并测试方法。",
                "type": "code",
                "options": [],
                "answer": "class Circle:\n    def __init__(self, radius):\n        self.__radius = radius\n    def get_radius(self):\n        return self.__radius\n    def set_radius(self, radius):\n        if radius > 0:\n            self.__radius = radius\n    def area(self):\n        return 3.14159 * self.__radius ** 2\nc = Circle(5)\nprint(c.area())",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Circle:\n    def __init__(self, radius):\n        self.__radius = radius\n    def get_radius(self):\n        return self.__radius\n    def set_radius(self, radius):\n        if radius > 0:\n            self.__radius = radius\n    def area(self):\n        return 3.14159 * self.__radius ** 2\nc = Circle(5)\nprint(c.area())"
            },
            {
                "id": "day12_q4",
                "name": "第4题",
                "description": "定义类Calculator，包含add、subtract、multiply、divide四个方法，分...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义类Calculator，包含add、subtract、multiply、divide四个方法，分别实现加减乘除运算。创建实例并测试这些方法。",
                "type": "code",
                "options": [],
                "answer": "class Calculator:\n    def add(self, a, b):\n        return a + b\n    def subtract(self, a, b):\n        return a - b\n    def multiply(self, a, b):\n        return a * b\n    def divide(self, a, b):\n        if b != 0:\n            return a / b\n        return None\ncalc = Calculator()\nprint(calc.add(10, 5))\nprint(calc.divide(10, 5))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Calculator:\n    def add(self, a, b):\n        return a + b\n    def subtract(self, a, b):\n        return a - b\n    def multiply(self, a, b):\n        return a * b\n    def divide(self, a, b):\n        if b != 0:\n            return a / b\n        return None\ncalc = Calculator()\nprint(calc.add(10, 5))\nprint(calc.divide(10, 5))"
            }
        ]
    },
    {
        "id": "region_13",
        "name": "继承之城",
        "description": "类的继承与重写",
        "icon": "fa-sitemap",
        "levels": [
            {
                "id": "day13_q1",
                "name": "第1题",
                "description": "定义父类Animal，包含speak方法。定义子类Dog继承Animal，重写speak方法使其打印...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义父类Animal，包含speak方法。定义子类Dog继承Animal，重写speak方法使其打印'汪汪汪'。创建Dog实例并调用speak方法。",
                "type": "code",
                "options": [],
                "answer": "class Animal:\n    def speak(self):\n        pass\nclass Dog(Animal):\n    def speak(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def speak(self):\n        print('喵喵喵')\nd = Dog()\nd.speak()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Animal:\n    def speak(self):\n        pass\nclass Dog(Animal):\n    def speak(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def speak(self):\n        print('喵喵喵')\nd = Dog()\nd.speak()"
            },
            {
                "id": "day13_q2",
                "name": "第2题",
                "description": "定义父类Person，包含__init__方法接收name参数。定义子类Student继承Perso...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义父类Person，包含__init__方法接收name参数。定义子类Student继承Person，使用super()调用父类构造方法，并添加grade属性。",
                "type": "code",
                "options": [],
                "answer": "class Person:\n    def __init__(self, name):\n        self.name = name\n    def introduce(self):\n        print('我是', self.name)\nclass Student(Person):\n    def __init__(self, name, grade):\n        super().__init__(name)\n        self.grade = grade\n    def introduce(self):\n        super().introduce()\n        print('我在读', self.grade)\ns = Student('张三', '高三')\ns.introduce()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Person:\n    def __init__(self, name):\n        self.name = name\n    def introduce(self):\n        print('我是', self.name)\nclass Student(Person):\n    def __init__(self, name, grade):\n        super().__init__(name)\n        self.grade = grade\n    def introduce(self):\n        super().introduce()\n        print('我在读', self.grade)\ns = Student('张三', '高三')\ns.introduce()"
            },
            {
                "id": "day13_q3",
                "name": "第3题",
                "description": "定义父类Shape，包含area方法返回0。定义子类Rectangle继承Shape，重写area方...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义父类Shape，包含area方法返回0。定义子类Rectangle继承Shape，重写area方法计算矩形面积（长×宽）。创建Rectangle实例并调用area。",
                "type": "code",
                "options": [],
                "answer": "class Shape:\n    def area(self):\n        pass\nclass Rectangle(Shape):\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return 3.14159 * self.radius ** 2\nshapes = [Rectangle(4, 5), Circle(3)]\nfor shape in shapes:\n    print(shape.area())",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Shape:\n    def area(self):\n        pass\nclass Rectangle(Shape):\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return 3.14159 * self.radius ** 2\nshapes = [Rectangle(4, 5), Circle(3)]\nfor shape in shapes:\n    print(shape.area())"
            },
            {
                "id": "day13_q4",
                "name": "第4题",
                "description": "定义类A和类B，都包含show方法。定义类C同时继承A和B，调用C实例的show方法观察MRO（方法...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义类A和类B，都包含show方法。定义类C同时继承A和B，调用C实例的show方法观察MRO（方法解析顺序）。",
                "type": "code",
                "options": [],
                "answer": "class A:\n    def show(self):\n        print('A')\nclass B:\n    def show(self):\n        print('B')\nclass C(A, B):\n    pass\nc = C()\nc.show()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class A:\n    def show(self):\n        print('A')\nclass B:\n    def show(self):\n        print('B')\nclass C(A, B):\n    pass\nc = C()\nc.show()"
            }
        ]
    },
    {
        "id": "region_14",
        "name": "多态之塔",
        "description": "多继承、多态和鸭子类型",
        "icon": "fa-layer-group",
        "levels": [
            {
                "id": "day14_q1",
                "name": "第1题",
                "description": "定义抽象父类Animal，包含speak方法。定义Dog和Cat子类分别实现speak方法。编写函数...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义抽象父类Animal，包含speak方法。定义Dog和Cat子类分别实现speak方法。编写函数make_speak(animal)调用传入对象的speak方法，体现多态性。",
                "type": "code",
                "options": [],
                "answer": "class Animal:\n    def speak(self):\n        pass\nclass Dog(Animal):\n    def speak(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def speak(self):\n        print('喵喵喵')\ndef make_speak(animal):\n    animal.speak()\nmake_speak(Dog())\nmake_speak(Cat())",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Animal:\n    def speak(self):\n        pass\nclass Dog(Animal):\n    def speak(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def speak(self):\n        print('喵喵喵')\ndef make_speak(animal):\n    animal.speak()\nmake_speak(Dog())\nmake_speak(Cat())"
            },
            {
                "id": "day14_q2",
                "name": "第2题",
                "description": "定义Bird类和Airplane类，都包含fly方法。定义函数let_it_fly(obj)调用fl...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义Bird类和Airplane类，都包含fly方法。定义函数let_it_fly(obj)调用fly方法。传入Bird和Airplane实例，演示鸭子类型。",
                "type": "code",
                "options": [],
                "answer": "class Bird:\n    def fly(self):\n        print('鸟在飞')\nclass Airplane:\n    def fly(self):\n        print('飞机在飞')\ndef let_fly(obj):\n    obj.fly()\nlet_fly(Bird())\nlet_fly(Airplane())",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Bird:\n    def fly(self):\n        print('鸟在飞')\nclass Airplane:\n    def fly(self):\n        print('飞机在飞')\ndef let_fly(obj):\n    obj.fly()\nlet_fly(Bird())\nlet_fly(Airplane())"
            },
            {
                "id": "day14_q3",
                "name": "第3题",
                "description": "定义类A包含method方法打印'A'，类B继承A并重写method打印'B'，类C继承B并重写me...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义类A包含method方法打印'A'，类B继承A并重写method打印'B'，类C继承B并重写method打印'C'。创建C实例调用method方法。",
                "type": "code",
                "options": [],
                "answer": "class A:\n    def method(self):\n        print('A')\nclass B(A):\n    def method(self):\n        print('B')\nclass C(B):\n    def method(self):\n        print('C')\nc = C()\nc.method()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class A:\n    def method(self):\n        print('A')\nclass B(A):\n    def method(self):\n        print('B')\nclass C(B):\n    def method(self):\n        print('C')\nc = C()\nc.method()"
            },
            {
                "id": "day14_q4",
                "name": "第4题",
                "description": "定义Animal类和Dog类（继承Animal）。创建Dog实例，使用isinstance判断该实例...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义Animal类和Dog类（继承Animal）。创建Dog实例，使用isinstance判断该实例是否为Animal类型和Dog类型。",
                "type": "code",
                "options": [],
                "answer": "class Animal:\n    pass\nclass Dog(Animal):\n    def bark(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def meow(self):\n        print('喵喵喵')\nanimals = [Dog(), Cat()]\nfor animal in animals:\n    if isinstance(animal, Dog):\n        animal.bark()\n    elif isinstance(animal, Cat):\n        animal.meow()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Animal:\n    pass\nclass Dog(Animal):\n    def bark(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def meow(self):\n        print('喵喵喵')\nanimals = [Dog(), Cat()]\nfor animal in animals:\n    if isinstance(animal, Dog):\n        animal.bark()\n    elif isinstance(animal, Cat):\n        animal.meow()"
            }
        ]
    },
    {
        "id": "region_15",
        "name": "魔法之屋",
        "description": "魔法方法",
        "icon": "fa-sparkles",
        "levels": [
            {
                "id": "day15_q1",
                "name": "第1题",
                "description": "定义Person类，实现__str__方法返回'Person: '加上name属性。创建实例并打印，...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义Person类，实现__str__方法返回'Person: '加上name属性。创建实例并打印，观察输出效果。",
                "type": "code",
                "options": [],
                "answer": "class Person:\n    def __init__(self, name):\n        self.name = name\n    def __str__(self):\n        return 'Person: ' + self.name\np = Person('张三')\nprint(p)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Person:\n    def __init__(self, name):\n        self.name = name\n    def __str__(self):\n        return 'Person: ' + self.name\np = Person('张三')\nprint(p)"
            },
            {
                "id": "day15_q2",
                "name": "第2题",
                "description": "定义Vector类，包含x和y属性。实现__add__方法，使得两个Vector实例可以使用+运算符...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义Vector类，包含x和y属性。实现__add__方法，使得两个Vector实例可以使用+运算符相加，返回新的Vector对象。",
                "type": "code",
                "options": [],
                "answer": "class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    def __str__(self):\n        return f'({self.x}, {self.y})'\nv1 = Vector(1, 2)\nv2 = Vector(3, 4)\nprint(v1 + v2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    def __str__(self):\n        return f'({self.x}, {self.y})'\nv1 = Vector(1, 2)\nv2 = Vector(3, 4)\nprint(v1 + v2)"
            },
            {
                "id": "day15_q3",
                "name": "第3题",
                "description": "定义Counter类，实现__call__方法，每次调用实例时count加1并返回当前计数。创建实例...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义Counter类，实现__call__方法，每次调用实例时count加1并返回当前计数。创建实例并多次调用测试。",
                "type": "code",
                "options": [],
                "answer": "class Counter:\n    def __init__(self):\n        self.count = 0\n    def __call__(self):\n        self.count += 1\n        return self.count\nc = Counter()\nprint(c())\nprint(c())\nprint(c())",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Counter:\n    def __init__(self):\n        self.count = 0\n    def __call__(self):\n        self.count += 1\n        return self.count\nc = Counter()\nprint(c())\nprint(c())\nprint(c())"
            },
            {
                "id": "day15_q4",
                "name": "第4题",
                "description": "定义MyList类包装一个列表。实现__len__方法返回列表长度，实现__getitem__方法支...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "定义MyList类包装一个列表。实现__len__方法返回列表长度，实现__getitem__方法支持索引访问。创建实例测试这些特殊方法。",
                "type": "code",
                "options": [],
                "answer": "class MyList:\n    def __init__(self, items):\n        self.items = items\n    def __len__(self):\n        return len(self.items)\n    def __getitem__(self, index):\n        return self.items[index]\nml = MyList([1, 2, 3, 4, 5])\nprint(len(ml))\nprint(ml[2])",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class MyList:\n    def __init__(self, items):\n        self.items = items\n    def __len__(self):\n        return len(self.items)\n    def __getitem__(self, index):\n        return self.items[index]\nml = MyList([1, 2, 3, 4, 5])\nprint(len(ml))\nprint(ml[2])"
            }
        ]
    },
    {
        "id": "region_16",
        "name": "单例秘境",
        "description": "单例模式与模块",
        "icon": "fa-key",
        "levels": [
            {
                "id": "day16_q1",
                "name": "第1题",
                "description": "使用__new__方法实现单例模式。定义Singleton类，确保无论创建多少次实例，都返回同一个对...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用__new__方法实现单例模式。定义Singleton类，确保无论创建多少次实例，都返回同一个对象。测试创建多个实例并比较它们的id。",
                "type": "code",
                "options": [],
                "answer": "class Singleton:\n    _instance = None\n    def __new__(cls, *args, **kwargs):\n        if not cls._instance:\n            cls._instance = super().__new__(cls)\n        return cls._instance\ns1 = Singleton()\ns2 = Singleton()\nprint(s1 is s2)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class Singleton:\n    _instance = None\n    def __new__(cls, *args, **kwargs):\n        if not cls._instance:\n            cls._instance = super().__new__(cls)\n        return cls._instance\ns1 = Singleton()\ns2 = Singleton()\nprint(s1 is s2)"
            },
            {
                "id": "day16_q2",
                "name": "第2题",
                "description": "导入math模块，使用math.pi打印圆周率，使用math.sqrt(16)计算并打印16的平方根...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "导入math模块，使用math.pi打印圆周率，使用math.sqrt(16)计算并打印16的平方根。",
                "type": "code",
                "options": [],
                "answer": "import math\nprint(math.pi)\nprint(math.sqrt(16))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "import math\nprint(math.pi)\nprint(math.sqrt(16))"
            },
            {
                "id": "day16_q3",
                "name": "第3题",
                "description": "使用from math import pi, sqrt导入特定函数，直接使用pi和sqrt(16)进...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用from math import pi, sqrt导入特定函数，直接使用pi和sqrt(16)进行计算并打印结果。",
                "type": "code",
                "options": [],
                "answer": "from math import pi, sqrt\nprint(pi)\nprint(sqrt(16))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "from math import pi, sqrt\nprint(pi)\nprint(sqrt(16))"
            },
            {
                "id": "day16_q4",
                "name": "第4题",
                "description": "创建一个模块文件，使用__all__列表控制导出的函数。定义public_function和_pri...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个模块文件，使用__all__列表控制导出的函数。定义public_function和_private_function，__all__只包含public_function。",
                "type": "code",
                "options": [],
                "answer": "__all__ = ['public_function']\ndef public_function():\n    return 'public'\ndef _private_function():\n    return 'private'",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "__all__ = ",
                "solution": "__all__ = ['public_function']\ndef public_function():\n    return 'public'\ndef _private_function():\n    return 'private'"
            }
        ]
    },
    {
        "id": "region_17",
        "name": "文件港湾",
        "description": "文件操作",
        "icon": "fa-file",
        "levels": [
            {
                "id": "day17_q1",
                "name": "第1题",
                "description": "使用with语句打开文件'test.txt'，以写入模式写入'Hello, World!'。确保文件...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用with语句打开文件'test.txt'，以写入模式写入'Hello, World!'。确保文件正确关闭。",
                "type": "code",
                "options": [],
                "answer": "with open('test.txt', 'w') as f:\n    f.write('Hello, World!')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "with open('test.txt', 'w') as f:\n    f.write('Hello, World!')"
            },
            {
                "id": "day17_q2",
                "name": "第2题",
                "description": "使用with语句打开文件'test.txt'，以读取模式读取全部内容并打印。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用with语句打开文件'test.txt'，以读取模式读取全部内容并打印。",
                "type": "code",
                "options": [],
                "answer": "with open('test.txt', 'r') as f:\n    content = f.read()\n    print(content)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "with open('test.txt', 'r') as f:\n    content = f.read()\n    print(content)"
            },
            {
                "id": "day17_q3",
                "name": "第3题",
                "description": "使用with语句打开文件'test.txt'，以追加模式写入换行符和'Appended conten...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用with语句打开文件'test.txt'，以追加模式写入换行符和'Appended content'。",
                "type": "code",
                "options": [],
                "answer": "with open('test.txt', 'a') as f:\n    f.write('\\nAppended content')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "with open('test.txt', 'a') as f:\n    f.write('\\nAppended content')"
            },
            {
                "id": "day17_q4",
                "name": "第4题",
                "description": "使用with语句打开文件'test.txt'，使用readlines()方法逐行读取内容并打印每一行...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用with语句打开文件'test.txt'，使用readlines()方法逐行读取内容并打印每一行。",
                "type": "code",
                "options": [],
                "answer": "with open('test.txt', 'r') as f:\n    lines = f.readlines()\n    for line in lines:\n        print(line.strip())",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "with open('test.txt', 'r') as f:\n    lines = f.readlines()\n    for line in lines:\n        print(line.strip())"
            }
        ]
    },
    {
        "id": "region_18",
        "name": "正则海域",
        "description": "正则表达式",
        "icon": "fa-search",
        "levels": [
            {
                "id": "day18_q1",
                "name": "第1题",
                "description": "使用正则表达式匹配字符串中的所有数字。定义pattern为匹配一个或多个数字，在文本'abc123d...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用正则表达式匹配字符串中的所有数字。定义pattern为匹配一个或多个数字，在文本'abc123def456'中查找所有匹配并打印。",
                "type": "code",
                "options": [],
                "answer": "import re\npattern = r'\\d+'\ntext = 'abc123def456'\nresult = re.findall(pattern, text)\nprint(result)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "import re\npattern = r'\\d+'\ntext = 'abc123def456'\nresult = re.findall(pattern, text)\nprint(result)"
            },
            {
                "id": "day18_q2",
                "name": "第2题",
                "description": "使用正则表达式判断字符串是否为纯字母组成。定义pattern匹配以字母开头和结尾的字符串，测试'He...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用正则表达式判断字符串是否为纯字母组成。定义pattern匹配以字母开头和结尾的字符串，测试'Hello'和'Hello123'。",
                "type": "code",
                "options": [],
                "answer": "import re\npattern = r'^[a-zA-Z]+$'\ntext = 'Hello'\nresult = re.match(pattern, text)\nprint(bool(result))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "import re\npattern = r'^[a-zA-Z]+$'\ntext = 'Hello'\nresult = re.match(pattern, text)\nprint(bool(result))"
            },
            {
                "id": "day18_q3",
                "name": "第3题",
                "description": "使用正则表达式替换字符串中的内容。将文本中所有'cat'替换为'dog'，包括'Cats'中的'ca...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用正则表达式替换字符串中的内容。将文本中所有'cat'替换为'dog'，包括'Cats'中的'cat'。",
                "type": "code",
                "options": [],
                "answer": "import re\npattern = r'cat'\ntext = 'The cat is cute. Cats are nice.'\nresult = re.sub(pattern, 'dog', text)\nprint(result)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "import re\npattern = r'cat'\ntext = 'The cat is cute. Cats are nice.'\nresult = re.sub(pattern, 'dog', text)\nprint(result)"
            },
            {
                "id": "day18_q4",
                "name": "第4题",
                "description": "使用正则分组提取日期信息。定义pattern匹配YYYY-MM-DD格式的日期，从文本中提取年、月、...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用正则分组提取日期信息。定义pattern匹配YYYY-MM-DD格式的日期，从文本中提取年、月、日并分别打印。",
                "type": "code",
                "options": [],
                "answer": "import re\npattern = r'(\\d{4})-(\\d{2})-(\\d{2})'\ntext = 'Date: 2024-01-15'\nresult = re.search(pattern, text)\nif result:\n    print('Year:', result.group(1))\n    print('Month:', result.group(2))\n    print('Day:', result.group(3))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "import re\npattern = r'(\\d{4})-(\\d{2})-(\\d{2})'\ntext = 'Date: 2024-01-15'\nresult = re.search(pattern, text)\nif result:\n    print('Year:', result.group(1))\n    print('Month:', result.group(2))\n    print('Day:', result.group(3))"
            }
        ]
    },
    {
        "id": "region_19",
        "name": "装饰器峰",
        "description": "装饰器与生成器",
        "icon": "fa-gem",
        "levels": [
            {
                "id": "day19_q1",
                "name": "第1题",
                "description": "创建一个装饰器decorator，在函数执行前打印'Before'，执行后打印'After'。使用该...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个装饰器decorator，在函数执行前打印'Before'，执行后打印'After'。使用该装饰器装饰一个简单函数并调用测试。",
                "type": "code",
                "options": [],
                "answer": "def decorator(func):\n    def wrapper(*args, **kwargs):\n        print('Before')\n        result = func(*args, **kwargs)\n        print('After')\n        return result\n    return wrapper\n@decorator\ndef greet():\n    print('Hello')\ngreet()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def decorator(func):\n    ",
                "solution": "def decorator(func):\n    def wrapper(*args, **kwargs):\n        print('Before')\n        result = func(*args, **kwargs)\n        print('After')\n        return result\n    return wrapper\n@decorator\ndef greet():\n    print('Hello')\ngreet()"
            },
            {
                "id": "day19_q2",
                "name": "第2题",
                "description": "创建一个带参数的装饰器repeat(times)，可以指定函数重复执行的次数。使用@repeat(3...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个带参数的装饰器repeat(times)，可以指定函数重复执行的次数。使用@repeat(3)装饰函数，调用时函数将执行3次。",
                "type": "code",
                "options": [],
                "answer": "def repeat(times):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            results = []\n            for _ in range(times):\n                results.append(func(*args, **kwargs))\n            return results\n        return wrapper\n    return decorator\n@repeat(3)\ndef greet():\n    return 'Hello'\nprint(greet())",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def repeat(times):\n    ",
                "solution": "def repeat(times):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            results = []\n            for _ in range(times):\n                results.append(func(*args, **kwargs))\n            return results\n        return wrapper\n    return decorator\n@repeat(3)\ndef greet():\n    return 'Hello'\nprint(greet())"
            },
            {
                "id": "day19_q3",
                "name": "第3题",
                "description": "创建一个生成器函数generator()，依次yield 1、2、3。获取生成器对象并使用for循环...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个生成器函数generator()，依次yield 1、2、3。获取生成器对象并使用for循环遍历打印每个值。",
                "type": "code",
                "options": [],
                "answer": "def generator():\n    yield 1\n    yield 2\n    yield 3\ng = generator()\nfor num in g:\n    print(num)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def generator():\n    ",
                "solution": "def generator():\n    yield 1\n    yield 2\n    yield 3\ng = generator()\nfor num in g:\n    print(num)"
            },
            {
                "id": "day19_q4",
                "name": "第4题",
                "description": "使用生成器表达式创建一个生成器，生成0到9的平方数。使用for循环遍历并打印每个元素。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用生成器表达式创建一个生成器，生成0到9的平方数。使用for循环遍历并打印每个元素。",
                "type": "code",
                "options": [],
                "answer": "numbers = (x ** 2 for x in range(10))\nfor num in numbers:\n    print(num)",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "numbers = ",
                "solution": "numbers = (x ** 2 for x in range(10))\nfor num in numbers:\n    print(num)"
            },
            {
                "id": "day19_q5",
                "name": "第5题",
                "description": "创建一个无限生成器fibonacci()，无限生成斐波那契数列。使用for循环获取前10个值并打印。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个无限生成器fibonacci()，无限生成斐波那契数列。使用for循环获取前10个值并打印。",
                "type": "code",
                "options": [],
                "answer": "def fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\nfib = fibonacci()\nfor _ in range(10):\n    print(next(fib))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def fibonacci():\n    ",
                "solution": "def fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\nfib = fibonacci()\nfor _ in range(10):\n    print(next(fib))"
            }
        ]
    },
    {
        "id": "region_20",
        "name": "Bug巢穴",
        "description": "最终挑战！击败Bug之王",
        "icon": "fa-skull",
        "levels": [
            {
                "id": "day20_q1",
                "name": "第1题",
                "description": "创建一个调试装饰器debug，在函数调用前打印函数名和参数，调用后打印返回值。装饰一个加法函数并测试...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个调试装饰器debug，在函数调用前打印函数名和参数，调用后打印返回值。装饰一个加法函数并测试。",
                "type": "code",
                "options": [],
                "answer": "def debug(func):\n    def wrapper(*args, **kwargs):\n        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')\n        result = func(*args, **kwargs)\n        print(f'{func.__name__} returned {result}')\n        return result\n    return wrapper\n@debug\ndef add(a, b):\n    return a + b\nprint(add(3, 5))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def debug(func):\n    ",
                "solution": "def debug(func):\n    def wrapper(*args, **kwargs):\n        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')\n        result = func(*args, **kwargs)\n        print(f'{func.__name__} returned {result}')\n        return result\n    return wrapper\n@debug\ndef add(a, b):\n    return a + b\nprint(add(3, 5))"
            },
            {
                "id": "day20_q2",
                "name": "第2题",
                "description": "创建一个上下文管理器类ErrorHandler，在__enter__方法中返回自身，在__exit_...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "创建一个上下文管理器类ErrorHandler，在__enter__方法中返回自身，在__exit__方法中捕获并处理异常。使用with语句测试。",
                "type": "code",
                "options": [],
                "answer": "class ErrorHandler:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if exc_type:\n            print(f'Error: {exc_val}')\n            return True\n        return False\nwith ErrorHandler():\n    raise ValueError('Test error')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "class ErrorHandler:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if exc_type:\n            print(f'Error: {exc_val}')\n            return True\n        return False\nwith ErrorHandler():\n    raise ValueError('Test error')"
            },
            {
                "id": "day20_q3",
                "name": "第3题",
                "description": "编写一个函数process_file(filename)，使用try-except语句处理文件打开异...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "编写一个函数process_file(filename)，使用try-except语句处理文件打开异常。当文件不存在时打印友好的错误提示。",
                "type": "code",
                "options": [],
                "answer": "def process_file(filename):\n    try:\n        with open(filename, 'r') as f:\n            content = f.read()\n            return content\n    except FileNotFoundError:\n        print(f'File {filename} not found')\n        return None\n    except Exception as e:\n        print(f'Error: {e}')\n        return None\nprint(process_file('test.txt'))",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def process_file(filename):\n    ",
                "solution": "def process_file(filename):\n    try:\n        with open(filename, 'r') as f:\n            content = f.read()\n            return content\n    except FileNotFoundError:\n        print(f'File {filename} not found')\n        return None\n    except Exception as e:\n        print(f'Error: {e}')\n        return None\nprint(process_file('test.txt'))"
            },
            {
                "id": "day20_q4",
                "name": "第4题",
                "description": "使用logging模块配置日志输出，设置级别为DEBUG，格式包含时间、级别和消息。分别输出DEBU...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "使用logging模块配置日志输出，设置级别为DEBUG，格式包含时间、级别和消息。分别输出DEBUG、INFO、WARNING级别的日志。",
                "type": "code",
                "options": [],
                "answer": "import logging\nlogging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')\nlogging.debug('Debug message')\nlogging.info('Info message')\nlogging.warning('Warning message')\nlogging.error('Error message')",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "",
                "solution": "import logging\nlogging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')\nlogging.debug('Debug message')\nlogging.info('Info message')\nlogging.warning('Warning message')\nlogging.error('Error message')"
            },
            {
                "id": "day20_q5",
                "name": "第5题",
                "description": "完成最终挑战！编写一个综合程序，包含函数、类、异常处理等知识点，实现一个简单的学生成绩管理系统。...",
                "difficulty": "中等",
                "exp_reward": 50,
                "gold_reward": 25,
                "question": "完成最终挑战！编写一个综合程序，包含函数、类、异常处理等知识点，实现一个简单的学生成绩管理系统。",
                "type": "code",
                "options": [],
                "answer": "def challenge():\n    print('Congratulations!')\n    print('You have completed all challenges!')\n    print('Welcome to the world of Python!')\nchallenge()",
                "hints": [
                    "编写正确的Python代码"
                ],
                "code_template": "def challenge():\n    ",
                "solution": "def challenge():\n    print('Congratulations!')\n    print('You have completed all challenges!')\n    print('Welcome to the world of Python!')\nchallenge()"
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