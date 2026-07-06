import json

exercises = []

total_order = 1

def add_choice(day, number, question, options, answer):
    global total_order
    exercises.append({
        "type": "choice",
        "day": day,
        "number": number,
        "question": question,
        "options": options,
        "answer": answer,
        "total_order": total_order
    })
    total_order += 1

def add_code(day, number, question, answer, code_hint=""):
    global total_order
    exercises.append({
        "type": "code",
        "day": day,
        "number": number,
        "question": question,
        "options": [],
        "answer": answer,
        "code_hint": code_hint,
        "total_order": total_order
    })
    total_order += 1

add_choice(1, 1, "Python是一种什么类型的语言？", 
           ["A. 编译型语言", "B. 解释型语言", "C. 标记语言", "D. 前端语言"], "B")
add_choice(1, 2, "PyCharm是什么？", 
           ["A. 一种编程语言", "B. 一种操作系统", "C. 一款Python集成开发环境（IDE）", "D. 一种数据库管理系统"], "C")
add_choice(1, 3, "在PyCharm中，如何创建一个新的Python项目？", 
           ["A. 通过菜单选择“文件” -> “新建项目”", "B. 通过命令行创建", "C. 直接打开一个Python文件", "D. 无法在PyCharm中创建新项目"], "A")
add_choice(1, 4, "Python的主要特点之一是什么？", 
           ["A. 语法复杂", "B. 简单易学，适合初学者", "C. 仅适用于Web开发", "D. 运行速度极快"], "B")
add_choice(1, 5, "下列哪个领域不是Python的典型应用？", 
           ["A. Web开发", "B. 数据分析", "C. 高性能实时游戏引擎开发", "D. 人工智能与机器学习"], "C")
add_choice(1, 6, "以下哪个是python语法的特点:", 
           ["A. 解释性语言", "B. 面向对象", "C. 跨平台", "D. 以上全是"], "D")
add_choice(1, 7, "在PyCharm中，如何运行一个Python脚本？", 
           ["A. 右键点击文件并选择“运行”", "B. 通过命令行运行", "C. 直接在编辑器中输入代码", "D. 无法在PyCharm中运行脚本"], "A")
add_choice(1, 8, "Python文件的扩展名是什么？", 
           ["A. .java", "B. .py", "C. .cpp", "D. .js"], "B")
add_choice(1, 9, "在Python中，单行注释使用什么符号？", 
           ["A. //", "B. /* */", "C. #", "D. --"], "C")
add_choice(1, 10, "以下哪个不是Python的关键字？", 
           ["A. if", "B. for", "C. function", "D. else"], "C")

add_code(1, 11, "使用print函数输出两行内容：第一行'欢迎来到Python世界'，第二行'开始你的编程之旅吧'",
         "print('欢迎来到Python世界')\nprint('开始你的编程之旅吧')",
         "提示：可以使用两个print()函数")
add_code(1, 12, "编写一段代码，输出以下图案：\n*\n**\n***",
         "print('*')\nprint('**')\nprint('***')",
         "提示：使用三个print()函数")

add_choice(2, 1, "下面选项中，哪个是Python中的整数字面量？", 
           ["'123'", "3.14", "1101", "\"hello\""], "C")
add_choice(2, 2, "下面选项中，哪个是符合Python变量命名规则的正确赋值语句？", 
           ["1num = 10", "int = 10", "int_01 = 10", "$money = 100"], "C")
add_choice(2, 3, "下面关于python变量类型的说法，正确的是？", 
           ["变量类型必须在定义时指定", "变量类型在赋值时确定", "变量类型一旦确定就不能改变", "变量类型与赋值无关"], "B")
add_choice(2, 4, "下面变量x的类型是什么？x = 123_456_789", 
           ["float", "int", "str", "bool"], "B")
add_choice(2, 5, "在Python中，使用input()函数接收用户输入时，输入的值默认是什么类型？", 
           ["输入什么类型就是什么类型。", "字符串类型。", "整数类型。", "浮点数类型。"], "B")
add_choice(2, 6, "在Python中，print函数的主要用途是什么？", 
           ["从用户那里接收输入", "将数据写入文件", "在控制台输出内容", "执行数学计算"], "C")
add_choice(2, 7, "以下哪个表达式的结果是True？", 
           ["3 > 5", "2 == 2", "1 != 1", "4 < 3"], "B")
add_choice(2, 8, "以下哪个是Python中的字符串？", 
           ["123", "3.14", "\"hello\"", "True"], "C")

add_code(2, 9, "字符串与数字类型（int、float）之间的转换：将字符串'123'转换为整数，将字符串'3.14'转换为浮点数",
         "num1 = int('123')\nnum2 = float('3.14')\nprint(num1)\nprint(num2)",
         "提示：使用int()和float()函数")
add_code(2, 10, "从控制台接收用户输入的一个浮点数，打印输入值的类型，再将其转换为整数并打印转换后的值及其类型",
         "num = float(input())\nprint(type(num))\nnum_int = int(num)\nprint(num_int)\nprint(type(num_int))",
         "提示：使用input()接收输入，type()查看类型")
add_code(2, 11, "转换为绝对值：计算数字-5和-3.14的绝对值",
         "x = -5\ny = -3.14\nprint(abs(x))\nprint(abs(y))",
         "提示：使用abs()函数")
add_code(2, 12, "将整数100转换为字符串，将浮点数3.14转换为字符串",
         "str1 = str(100)\nstr2 = str(3.14)\nprint(str1)\nprint(str2)",
         "提示：使用str()函数")
add_code(2, 13, "编写一个Python程序：提示用户输入一个负整数，使用abs函数计算其绝对值，输出格式为“其绝对值是XXX”",
         "num = int(input())\nresult = abs(num)\nprint('其绝对值是', result)",
         "提示：使用input()接收输入，abs()计算绝对值")

for i in range(1, 22):
    if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
        continue

questions_by_day = {
    3: [
        ("变量名命名规则中，以下哪个是非法的变量名？", ["A. lala111", "B. 222baby", "C. Zhou", "D. _zhou"], "B"),
        ("python3中，如何打印变量message的值，其中message的值为Hello, World!？", 
         ["A. print 'Hello, World!'", "B. print \"message\"", "C. print message", "D. print(message)"], "D"),
        ("以下哪个是Python中的布尔值？", ["A. 只有True", "B. false", "C. 1", "D. True 和 False"], "D"),
        ("如何将整数10转换为字符串？", ["A. str(10)", "B. int(\"10\")", "C. float(10)", "D. bool(10)"], "A"),
        ("下列哪个不是Python的内置数据类型？", ["A. int", "B. str", "C. boolean", "D. float"], "C"),
        ("在Python中，以下哪个表达式的值是False？", ["A. True and True", "B. True or False", "C. not True", "D. True and not False"], "C"),
        ("以下哪个表达式的结果是True？", ["A. \"abc\" == \"ABC\"", "B. 10 > 5 and 3 < 2", "C. 5 != 6", "D. not (2 == 2)"], "C"),
        ("在Python中，使用哪个关键字来定义条件判断？", ["A. for", "B. while", "C. if", "D. def"], "C"),
        ("以下哪个表达式的值是True？", ["A. 3 >= 5", "B. 4 <= 4", "C. 2 > 2", "D. 1 != 1"], "B"),
        ("如何判断两个变量是否相等？", ["A. =", "B. ==", "C. ===", "D. equals()"], "B"),
        ("以下哪个是Python中的转义字符？", ["A. \\\\n", "B. \\n", "C. /n", "D. \\\\N"], "A"),
        ("在字符串中，如何表示换行？", ["A. \\r", "B. \\n", "C. \\t", "D. \\b"], "B"),
        ("以下哪个转义字符表示制表符？", ["A. \\n", "B. \\t", "C. \\r", "D. \\f"], "B"),
        ("布尔类型有几个值？", ["A. 一个", "B. 两个", "C. 三个", "D. 无数个"], "B"),
        ("not True 的结果是什么？", ["A. True", "B. False", "C. None", "D. Error"], "B"),
        ("True and False 的结果是什么？", ["A. True", "B. False", "C. None", "D. Error"], "B"),
        ("True or False 的结果是什么？", ["A. True", "B. False", "C. None", "D. Error"], "A"),
        ("在Python中，0的布尔值是什么？", ["A. True", "B. False", "C. None", "D. Error"], "B"),
        ("空字符串的布尔值是什么？", ["A. True", "B. False", "C. None", "D. Error"], "B"),
        ("以下哪个表达式的值是True？", ["A. bool(0)", "B. bool(\"\")", "C. bool([1])", "D. bool(None)"], "C"),
        ("在Python中，如何将字符串转换为布尔值？", ["A. bool()", "B. boolean()", "C. to_bool()", "D. convert_bool()"], "A"),
    ],
    4: [],
    5: [],
    6: [
        ("1. 在 Python 中，列表的索引是从哪个数字开始的？", ["0", "1", "2", "随机数"], "A"),
        ("2. 以下哪项是 Python 列表的一个特性？", ["所有元素必须唯一", "可以修改其中的元素", "元素不能排序", "不能通过索引访问元素"], "B"),
        ("3. 以下哪个方法用于向列表末尾添加一个元素？", ["append()", "extend()", "insert()", "pop()"], "A"),
        ("4.以下哪个方法用于从列表中移除指定位置的元素？", ["remove()", "pop()", "delete()", "erase()"], "B"),
        ("5. 以下哪个方法用于对列表进行排序？", ["sort()", "order()", "arrange()", "sort_list()"], "A"),
        ("6. 以下哪个表达式可以获取列表的长度？", ["length(list)", "len(list)", "list.length", "list.size()"], "B"),
        ("7. 以下哪个是列表的切片操作？", ["list[1]", "list[1:3]", "list(1,3)", "get_slice(list,1,3)"], "B"),
        ("8. 以下哪个方法用于在列表指定位置插入元素？", ["append()", "extend()", "insert()", "add()"], "C"),
        ("9. 以下哪个方法用于反转列表？", ["reverse()", "invert()", "flip()", "backwards()"], "A"),
        ("10. 以下哪个表达式可以检查元素是否在列表中？", ["element in list", "list.contains(element)", "check(list, element)", "has_element(list, element)"], "A"),
    ],
    7: [
        ("1. Python 集合中的元素是有序的吗？", ["是的，它们是有序的", "不是的，它们是无序的", "只有在特定情况下才是无序的", "取决于集合的大小"], "B"),
        ("2.以下哪种定义方式，不是元组：", 
         ["tuple_01 = (1, 2, 3)", "tuple_02 = ()", "tuple_03 = (4,)", "tuple_04 = tuple([5, 6, 7])", "tuple_05 = (8)"], "E"),
        ("3. 元组和列表的主要区别是什么？", ["元组可以被修改，列表不可以", "列表可以被修改，元组不可以", "元组和列表都可以被修改", "元组和列表都不可以被修改"], "B"),
        ("4. 假设有一个元组 t = (5, 'a', 3, 'b', 1)，那么 t[2:4] 的结果是什么？", 
         ["(3, 'b')", "('a', 3)", "(5, 'a', 3)", "(3, 'b', 1)"], "A"),
        ("5. 以下哪个方法可以向集合中添加元素？", ["append()", "add()", "insert()", "extend()"], "B"),
        ("6. 以下哪个方法可以求两个集合的交集？", ["union()", "intersection()", "difference()", "symmetric_difference()"], "B"),
        ("7. 以下哪个方法可以求两个集合的并集？", ["union()", "intersection()", "difference()", "symmetric_difference()"], "A"),
        ("8. 以下哪个是集合的特性？", ["元素可以重复", "元素是有序的", "元素是唯一的", "可以通过索引访问"], "C"),
    ],
    8: [],
    9: [],
    10: [],
    11: [],
    12: [],
    13: [],
    14: [],
    15: [],
    16: [],
    17: [],
    18: [],
    19: [],
    20: [],
    21: [],
}

for day, questions in questions_by_day.items():
    for idx, (question, options, answer) in enumerate(questions, 1):
        add_choice(day, idx, question, options, answer)

add_code(4, 1, "第 01 题：判断一个数的正负\n题目要求：从键盘上输入一个浮点数，使用if-else语句来判断这个数是正数、负数还是零，并输出相应的结果。",
         "number = float(input('请输入一个浮点数：'))\nif number > 0:\n    print(number, '是正数。')\nelif number < 0:\n    print(number, '是负数。')\nelse:\n    print(number, '是零。')",
         "提示：使用if-elif-else语句")
add_code(4, 2, "第 02 题：判断是否水仙花数\n题目描述：从键盘上输入一个三位数的数，判断这个数字是否是三位数的数字，再判断是否是水仙花数。\n(水仙花数：一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。本题只需要输入3位数。)",
         "number = int(input('请输入一个三位数：'))\nif number < 100 or number > 999:\n    print('无效的输入')\nelse:\n    hundreds = number // 100\n    tens = (number // 10) % 10\n    ones = number % 10\n    cube_sum = hundreds ** 3 + tens ** 3 + ones ** 3\n    if cube_sum == number:\n        print(number, '是水仙花数')\n    else:\n        print(number, '不是水仙花数')",
         "提示：分解数字，计算立方和")
add_code(4, 3, "第 03 题：计算商品购物折扣\n题目要求：编写一个计算商品购物折扣的程序，折扣规则如下：\n如果购物金额小于100元，则不享受折扣。\n如果购物金额在100元（含）至300元之间，则享受9折优惠。\n如果购物金额超过300元，则享受85折优惠。",
         "shopping_amount = float(input('请输入购物金额：'))\nif shopping_amount < 100:\n    print('您没有享受折扣,需支付:', str(shopping_amount), '元')\nelif shopping_amount >= 100 and shopping_amount < 300:\n    discount = shopping_amount * 0.9\n    print('您可享受9折优惠,需支付:', str(discount), '元')\nelse:\n    discount = shopping_amount * 0.85\n    print('您可享受85折优惠,需支付:', str(discount), '元')",
         "提示：使用if-elif-else语句判断折扣")
add_code(4, 4, "第 04 题：简单的交通信号灯判断\n题目要求：编写一段代码，模拟交通信号灯的工作。要求用户输入颜色（红、黄、绿），根据颜色输出相应的指示信息。\n输入红色(red),输出:请停车\n输入黄色(yellow),输出:准备停车/尽快通行\n输入绿色(green),输出:允许通行",
         "color = input('请输入颜色（红、黄、绿）：')\nif color == 'red' or color == '红色':\n    print('请停车')\nelif color == 'yellow' or color == '黄色':\n    print('准备停车/尽快通行')\nelif color == 'green' or color == '绿色':\n    print('允许通行')\nelse:\n    print('无效的颜色，请输入红色(red)、黄色(yellow)或绿色(green)')",
         "提示：使用if-elif-else语句")
add_code(4, 5, "第 05 题：判断三角形类型\n题目要求：编写一个程序，让用户输入三角形的三条边长，判断并输出三角形的类型：\n等边三角形：三条边相等\n等腰三角形：至少有两条边相等\n直角三角形：满足勾股定理\n不是三角形：不符合三角形的边长关系",
         "side1 = float(input('请输入第一条边：'))\nside2 = float(input('请输入第二条边：'))\nside3 = float(input('请输入第三条边：'))\n\nif side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:\n    if side1 == side2 == side3:\n        print('这是一个等边三角形')\n    elif side1 == side2 or side1 == side3 or side2 == side3:\n        print('这是一个等腰三角形')\n    elif side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:\n        print('这是一个直角三角形')\n    else:\n        print('这是一个普通三角形')\nelse:\n    print('不是三角形')",
         "提示：先判断是否构成三角形，再判断类型")

add_code(5, 1, "第 01 题：用户登陆\n题目要求：编写一个Python程序，需要用户输入用户名（admin）和密码（password）后重复三次后登录成功。",
         "success_count = 0\nfor i in range(3):\n    username = input('请输入用户名：')\n    password = input('请输入密码：')\n    if username == 'admin' and password == 'password':\n        success_count += 1\n        print('第{}次输入正确'.format(i+1))\n    else:\n        print('第{}次输入错误'.format(i+1))\nif success_count == 3:\n    print('登录成功')\nelse:\n    print('登录失败，失败次数：', 3 - success_count)",
         "提示：使用for循环")
add_code(5, 2, "第 02 题：用符号*打印正方形图案\n题目要求：打印一个5行5列的正方形图案。",
         "for i in range(5):\n    for j in range(5):\n        print('*', end='  ')\n    print()",
         "提示：使用嵌套for循环")
add_code(5, 3, "第 03 题：用符号*打印一个正直角三角形\n题目要求：打印一个正直角三角形图案，5行，每行星号递增。",
         "for i in range(5):\n    for j in range(i + 1):\n        print('*', end='  ')\n    print()",
         "提示：内层循环次数等于行数")
add_code(5, 4, "第 04 题：用符号*打印一个倒直角三角形\n题目要求：打印一个倒直角三角形图案，5行，每行星号递减。",
         "for i in range(5, 0, -1):\n    for j in range(i):\n        print('*', end='  ')\n    print()",
         "提示：使用递减的range")
add_code(5, 5, "第 05 题：for循环实现99乘法表\n题目要求：使用for循环实现99乘法表。",
         "for i in range(1, 10):\n    for j in range(1, i + 1):\n        print('{}x{}={}'.format(j, i, i * j), end='\\t')\n    print()",
         "提示：使用嵌套for循环")
add_code(5, 6, "第 06 题：存钱罐\n题目要求：你有一个存钱罐，每天存入相同数量的硬币。编写一个Python程序，通过用户输入每天存入的硬币数量和总天数，使用for循环计算并输出从第1天到指定天数，你总共存入了多少硬币。",
         "coins_per_day = int(input('请输入每天存入的硬币数量：'))\ntotal_days = int(input('请输入总天数：'))\ntotal_coins = 0\nfor day in range(1, total_days + 1):\n    total_coins += coins_per_day\n    print('第{}天：累计存入{}枚硬币'.format(day, total_coins))\nprint('总共存入{}枚硬币'.format(total_coins))",
         "提示：使用for循环累加")

add_code(8, 1, "第 01 题：字符串格式化\n题目要求：使用format方法格式化字符串。",
         "city = '哈尔滨'\ntemperature = -15.5\nreport = '当前城市 {} 温度为 {} 摄氏度。'\nformatted_report = report.format(city, temperature)\nprint(formatted_report)",
         "提示：使用str.format()方法")
add_code(8, 2, "第 02 题：f-string格式化\n题目要求：使用f-string格式化字符串。",
         "city = '哈尔滨'\ntemperature = -15.5\nreport = f'当前城市 {city} 温度为 {temperature} 摄氏度。'\nprint(report)",
         "提示：使用f-string")
add_code(8, 3, "第 03 题：round函数\n题目要求：使用round函数进行四舍五入。",
         "print(round(3.7))\nprint(round(3.2))",
         "提示：使用round()函数")
add_code(8, 4, "第 04 题：math模块\n题目要求：使用math模块的ceil和floor函数。",
         "import math\nprint(math.ceil(3.2))\nprint(math.floor(3.7))",
         "提示：导入math模块")
add_code(8, 5, "第 05 题：abs函数\n题目要求：计算绝对值。",
         "print(abs(-5))\nprint(abs(-3.14))",
         "提示：使用abs()函数")
add_code(8, 6, "第 06 题：max和min函数\n题目要求：找出最大值和最小值。",
         "print(max(1, 2, 3))\nprint(min(1, 2, 3))",
         "提示：使用max()和min()函数")

add_code(9, 1, "第 01 题：函数定义\n题目要求：定义一个简单的函数。",
         "def greet(name):\n    print('Hello, ' + name + '!')\ngreet('World')",
         "提示：使用def关键字")
add_code(9, 2, "第 02 题：函数返回值\n题目要求：定义一个带有返回值的函数。",
         "def add(a, b):\n    return a + b\nresult = add(3, 5)\nprint(result)",
         "提示：使用return语句")
add_code(9, 3, "第 03 题：函数计算面积\n题目要求：定义一个计算圆面积的函数。",
         "def calculate_area(radius):\n    return 3.14159 * radius ** 2\narea = calculate_area(5)\nprint(area)",
         "提示：圆面积公式")
add_code(9, 4, "第 04 题：函数判断偶数\n题目要求：定义一个判断偶数的函数。",
         "def is_even(num):\n    return num % 2 == 0\nprint(is_even(4))\nprint(is_even(5))",
         "提示：使用取模运算")

add_code(10, 1, "第 01 题：字典基础\n题目要求：创建并访问字典。",
         "student = {'name': '张三', 'age': 18, 'score': 95}\nprint(student['name'])\nprint(student['age'])\nprint(student['score'])",
         "提示：使用键访问值")
add_code(10, 2, "第 02 题：字典修改\n题目要求：修改和添加字典元素。",
         "student = {'name': '张三', 'age': 18}\nstudent['score'] = 95\nstudent['gender'] = '男'\nprint(student)",
         "提示：通过键赋值")
add_code(10, 3, "第 03 题：字典方法\n题目要求：使用字典的keys、values、items方法。",
         "student = {'name': '张三', 'age': 18, 'score': 95}\nkeys = list(student.keys())\nvalues = list(student.values())\nitems = list(student.items())\nprint(keys)\nprint(values)\nprint(items)",
         "提示：使用字典方法")
add_code(10, 4, "第 04 题：字典查找\n题目要求：检查键是否存在于字典中。",
         "student = {'name': '张三', 'age': 18}\nif 'score' in student:\n    print(student['score'])\nelse:\n    print('成绩不存在')",
         "提示：使用in关键字")

add_code(11, 1, "第 01 题：函数默认参数\n题目要求：定义带有默认参数的函数。",
         "def greet(name, message='Hello'):\n    print(message + ', ' + name + '!')\ngreet('World')\ngreet('World', 'Hi')",
         "提示：设置默认参数")
add_code(11, 2, "第 02 题：可变参数\n题目要求：定义带有可变参数的函数。",
         "def add(*args):\n    total = 0\n    for num in args:\n        total += num\n    return total\nprint(add(1, 2, 3))\nprint(add(1, 2, 3, 4, 5))",
         "提示：使用*args")

add_code(12, 1, "第 01 题：递归函数\n题目要求：使用递归计算阶乘。",
         "def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial(n - 1)\nprint(factorial(5))",
         "提示：递归终止条件")
add_code(12, 2, "第 02 题：斐波那契数列\n题目要求：使用递归计算斐波那契数列。",
         "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)\nfor i in range(10):\n    print(fibonacci(i))",
         "提示：递归计算")
add_code(12, 3, "第 03 题：闭包\n题目要求：创建一个闭包函数。",
         "def make_counter():\n    count = 0\n    def counter():\n        nonlocal count\n        count += 1\n        return count\n    return counter\nc = make_counter()\nprint(c())\nprint(c())\nprint(c())",
         "提示：使用nonlocal")
add_code(12, 4, "第 04 题：匿名函数\n题目要求：使用lambda表达式创建匿名函数。",
         "add = lambda x, y: x + y\nprint(add(3, 5))",
         "提示：使用lambda")
add_code(12, 5, "第 05 题：map和filter\n题目要求：使用map和filter函数。",
         "numbers = [1, 2, 3, 4, 5]\nsquared = list(map(lambda x: x ** 2, numbers))\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(squared)\nprint(evens)",
         "提示：使用map和filter")

add_code(13, 1, "第 01 题：类的定义\n题目要求：定义一个类并创建实例。",
         "class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    def introduce(self):\n        print('我叫', self.name, '今年', self.age, '岁')\np = Person('张三', 18)\np.introduce()",
         "提示：使用class关键字")
add_code(13, 2, "第 02 题：类属性\n题目要求：使用类属性和实例属性。",
         "class Student:\n    school = '第一中学'\n    def __init__(self, name, grade):\n        self.name = name\n        self.grade = grade\ns = Student('张三', '高三')\nprint(Student.school)\nprint(s.name, s.grade)",
         "提示：类属性和实例属性")
add_code(13, 3, "第 03 题：私有属性\n题目要求：使用私有属性。",
         "class Circle:\n    def __init__(self, radius):\n        self.__radius = radius\n    def get_radius(self):\n        return self.__radius\n    def set_radius(self, radius):\n        if radius > 0:\n            self.__radius = radius\n    def area(self):\n        return 3.14159 * self.__radius ** 2\nc = Circle(5)\nprint(c.area())",
         "提示：使用__前缀")
add_code(13, 4, "第 04 题：类方法\n题目要求：定义类的多个方法。",
         "class Calculator:\n    def add(self, a, b):\n        return a + b\n    def subtract(self, a, b):\n        return a - b\n    def multiply(self, a, b):\n        return a * b\n    def divide(self, a, b):\n        if b != 0:\n            return a / b\n        return None\ncalc = Calculator()\nprint(calc.add(10, 5))\nprint(calc.divide(10, 5))",
         "提示：定义多个方法")

add_code(14, 1, "第 01 题：类的继承\n题目要求：创建子类继承父类。",
         "class Animal:\n    def speak(self):\n        pass\nclass Dog(Animal):\n    def speak(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def speak(self):\n        print('喵喵喵')\nd = Dog()\nd.speak()",
         "提示：使用class Dog(Animal)")
add_code(14, 2, "第 02 题：super函数\n题目要求：使用super函数调用父类方法。",
         "class Person:\n    def __init__(self, name):\n        self.name = name\n    def introduce(self):\n        print('我是', self.name)\nclass Student(Person):\n    def __init__(self, name, grade):\n        super().__init__(name)\n        self.grade = grade\n    def introduce(self):\n        super().introduce()\n        print('我在读', self.grade)\ns = Student('张三', '高三')\ns.introduce()",
         "提示：使用super()")
add_code(14, 3, "第 03 题：方法重写\n题目要求：重写父类方法。",
         "class Shape:\n    def area(self):\n        pass\nclass Rectangle(Shape):\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return 3.14159 * self.radius ** 2\nshapes = [Rectangle(4, 5), Circle(3)]\nfor shape in shapes:\n    print(shape.area())",
         "提示：重写area方法")
add_code(14, 4, "第 04 题：多继承\n题目要求：使用多继承。",
         "class A:\n    def show(self):\n        print('A')\nclass B:\n    def show(self):\n        print('B')\nclass C(A, B):\n    pass\nc = C()\nc.show()",
         "提示：class C(A, B)")

add_code(15, 1, "第 01 题：多态\n题目要求：实现多态。",
         "class Animal:\n    def speak(self):\n        pass\nclass Dog(Animal):\n    def speak(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def speak(self):\n        print('喵喵喵')\ndef make_speak(animal):\n    animal.speak()\nmake_speak(Dog())\nmake_speak(Cat())",
         "提示：不同对象调用相同方法")
add_code(15, 2, "第 02 题：鸭子类型\n题目要求：实现鸭子类型。",
         "class Bird:\n    def fly(self):\n        print('鸟在飞')\nclass Airplane:\n    def fly(self):\n        print('飞机在飞')\ndef let_fly(obj):\n    obj.fly()\nlet_fly(Bird())\nlet_fly(Airplane())",
         "提示：关注方法而非类型")
add_code(15, 3, "第 03 题：方法覆盖\n题目要求：多层继承中的方法覆盖。",
         "class A:\n    def method(self):\n        print('A')\nclass B(A):\n    def method(self):\n        print('B')\nclass C(B):\n    def method(self):\n        print('C')\nc = C()\nc.method()",
         "提示：调用最子类的方法")
add_code(15, 4, "第 04 题：isinstance\n题目要求：使用isinstance判断类型。",
         "class Animal:\n    pass\nclass Dog(Animal):\n    def bark(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def meow(self):\n        print('喵喵喵')\nanimals = [Dog(), Cat()]\nfor animal in animals:\n    if isinstance(animal, Dog):\n        animal.bark()\n    elif isinstance(animal, Cat):\n        animal.meow()",
         "提示：使用isinstance")

add_code(16, 1, "第 01 题：__str__方法\n题目要求：实现__str__方法。",
         "class Person:\n    def __init__(self, name):\n        self.name = name\n    def __str__(self):\n        return 'Person: ' + self.name\np = Person('张三')\nprint(p)",
         "提示：重写__str__方法")
add_code(16, 2, "第 02 题：__add__方法\n题目要求：实现__add__方法。",
         "class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    def __str__(self):\n        return f'({self.x}, {self.y})'\nv1 = Vector(1, 2)\nv2 = Vector(3, 4)\nprint(v1 + v2)",
         "提示：重写__add__方法")
add_code(16, 3, "第 03 题：__call__方法\n题目要求：实现__call__方法。",
         "class Counter:\n    def __init__(self):\n        self.count = 0\n    def __call__(self):\n        self.count += 1\n        return self.count\nc = Counter()\nprint(c())\nprint(c())\nprint(c())",
         "提示：重写__call__方法")
add_code(16, 4, "第 04 题：容器协议\n题目要求：实现__len__和__getitem__方法。",
         "class MyList:\n    def __init__(self, items):\n        self.items = items\n    def __len__(self):\n        return len(self.items)\n    def __getitem__(self, index):\n        return self.items[index]\nml = MyList([1, 2, 3, 4, 5])\nprint(len(ml))\nprint(ml[2])",
         "提示：重写__len__和__getitem__")

add_code(17, 1, "第 01 题：单例模式\n题目要求：使用__new__实现单例模式。",
         "class Singleton:\n    _instance = None\n    def __new__(cls, *args, **kwargs):\n        if not cls._instance:\n            cls._instance = super().__new__(cls)\n        return cls._instance\ns1 = Singleton()\ns2 = Singleton()\nprint(s1 is s2)",
         "提示：重写__new__方法")
add_code(17, 2, "第 02 题：模块导入\n题目要求：导入模块并使用。",
         "import math\nprint(math.pi)\nprint(math.sqrt(16))",
         "提示：使用import")
add_code(17, 3, "第 03 题：from导入\n题目要求：使用from导入。",
         "from math import pi, sqrt\nprint(pi)\nprint(sqrt(16))",
         "提示：使用from...import")
add_code(17, 4, "第 04 题：__all__\n题目要求：使用__all__控制导出。",
         "__all__ = ['public_function']\ndef public_function():\n    return 'public'\ndef _private_function():\n    return 'private'",
         "提示：定义__all__")

add_code(18, 1, "第 01 题：文件写入\n题目要求：向文件写入内容。",
         "with open('test.txt', 'w') as f:\n    f.write('Hello, World!')",
         "提示：使用with语句")
add_code(18, 2, "第 02 题：文件读取\n题目要求：从文件读取内容。",
         "with open('test.txt', 'r') as f:\n    content = f.read()\n    print(content)",
         "提示：使用with语句")
add_code(18, 3, "第 03 题：文件追加\n题目要求：向文件追加内容。",
         "with open('test.txt', 'a') as f:\n    f.write('\\nAppended content')",
         "提示：使用'a'模式")
add_code(18, 4, "第 04 题：逐行读取\n题目要求：逐行读取文件内容。",
         "with open('test.txt', 'r') as f:\n    lines = f.readlines()\n    for line in lines:\n        print(line.strip())",
         "提示：使用readlines()")

add_code(19, 1, "第 01 题：正则匹配\n题目要求：使用正则表达式匹配数字。",
         "import re\npattern = r'\\d+'\ntext = 'abc123def456'\nresult = re.findall(pattern, text)\nprint(result)",
         "提示：使用re.findall")
add_code(19, 2, "第 02 题：正则匹配字符串\n题目要求：匹配纯字母字符串。",
         "import re\npattern = r'^[a-zA-Z]+$'\ntext = 'Hello'\nresult = re.match(pattern, text)\nprint(bool(result))",
         "提示：使用re.match")
add_code(19, 3, "第 03 题：正则替换\n题目要求：使用正则替换字符串。",
         "import re\npattern = r'cat'\ntext = 'The cat is cute. Cats are nice.'\nresult = re.sub(pattern, 'dog', text)\nprint(result)",
         "提示：使用re.sub")
add_code(19, 4, "第 04 题：正则分组\n题目要求：使用正则分组提取信息。",
         "import re\npattern = r'(\\d{4})-(\\d{2})-(\\d{2})'\ntext = 'Date: 2024-01-15'\nresult = re.search(pattern, text)\nif result:\n    print('Year:', result.group(1))\n    print('Month:', result.group(2))\n    print('Day:', result.group(3))",
         "提示：使用分组")

add_code(20, 1, "第 01 题：装饰器\n题目要求：创建一个装饰器。",
         "def decorator(func):\n    def wrapper(*args, **kwargs):\n        print('Before')\n        result = func(*args, **kwargs)\n        print('After')\n        return result\n    return wrapper\n@decorator\ndef greet():\n    print('Hello')\ngreet()",
         "提示：使用@语法")
add_code(20, 2, "第 02 题：带参数装饰器\n题目要求：创建带参数的装饰器。",
         "def repeat(times):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            results = []\n            for _ in range(times):\n                results.append(func(*args, **kwargs))\n            return results\n        return wrapper\n    return decorator\n@repeat(3)\ndef greet():\n    return 'Hello'\nprint(greet())",
         "提示：三层嵌套")
add_code(20, 3, "第 03 题：生成器\n题目要求：创建一个生成器。",
         "def generator():\n    yield 1\n    yield 2\n    yield 3\ng = generator()\nfor num in g:\n    print(num)",
         "提示：使用yield")
add_code(20, 4, "第 04 题：生成器表达式\n题目要求：使用生成器表达式。",
         "numbers = (x ** 2 for x in range(10))\nfor num in numbers:\n    print(num)",
         "提示：使用()")
add_code(20, 5, "第 05 题：无限生成器\n题目要求：创建一个无限生成器。",
         "def fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\nfib = fibonacci()\nfor _ in range(10):\n    print(next(fib))",
         "提示：无限循环")

add_code(21, 1, "第 01 题：调试装饰器\n题目要求：创建一个调试装饰器。",
         "def debug(func):\n    def wrapper(*args, **kwargs):\n        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')\n        result = func(*args, **kwargs)\n        print(f'{func.__name__} returned {result}')\n        return result\n    return wrapper\n@debug\ndef add(a, b):\n    return a + b\nprint(add(3, 5))",
         "提示：打印调用信息")
add_code(21, 2, "第 02 题：上下文管理器\n题目要求：创建一个上下文管理器。",
         "class ErrorHandler:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if exc_type:\n            print(f'Error: {exc_val}')\n            return True\n        return False\nwith ErrorHandler():\n    raise ValueError('Test error')",
         "提示：实现__enter__和__exit__")
add_code(21, 3, "第 03 题：异常处理\n题目要求：处理文件异常。",
         "def process_file(filename):\n    try:\n        with open(filename, 'r') as f:\n            content = f.read()\n            return content\n    except FileNotFoundError:\n        print(f'File {filename} not found')\n        return None\n    except Exception as e:\n        print(f'Error: {e}')\n        return None\nprint(process_file('test.txt'))",
         "提示：使用try-except")
add_code(21, 4, "第 04 题：日志\n题目要求：使用logging模块。",
         "import logging\nlogging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')\nlogging.debug('Debug message')\nlogging.info('Info message')\nlogging.warning('Warning message')\nlogging.error('Error message')",
         "提示：配置logging")
add_code(21, 5, "第 05 题：最终挑战\n题目要求：完成最终挑战！",
         "def challenge():\n    print('Congratulations!')\n    print('You have completed all challenges!')\n    print('Welcome to the world of Python!')\nchallenge()",
         "提示：完成所有挑战！")

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(exercises, f, ensure_ascii=False, indent=2)

print(f"生成完成！总题目数: {len(exercises)}")
for day in range(1, 22):
    day_items = [i for i in exercises if i.get('day') == day]
    if day_items:
        code_items = [i for i in day_items if i.get('type') == 'code']
        choice_items = [i for i in day_items if i.get('type') == 'choice']
        print(f"Day {day}: {len(day_items)} 题 ({len(choice_items)} choice, {len(code_items)} code)")