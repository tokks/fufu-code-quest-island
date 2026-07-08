import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

day4_fixed = [
    {
        "type": "code",
        "day": 4,
        "number": 1,
        "question": "第 01 题：判断一个数的正负\n题目要求：从键盘上输入一个浮点数，使用if-else语句来判断这个数是正数、负数还是零，并输出相应的结果。",
        "options": [],
        "answer": "number = float(input('请输入一个浮点数：'))\nif number > 0:\n    print(number, '是正数。')\nelif number < 0:\n    print(number, '是负数。')\nelse:\n    print(number, '是零。')",
        "code_hint": "1.定义一个变量number，用来接收用户输入的数值。并转换为float。\n2.使用 if-elif-else 语句判断正负：\nnumber > 0 ; 输出：number, \"是正数。\"\nnumber < 0 ; 输出：number, \"是负数。\"\nnumber = 0 ; 输出：number, \"是零。\"",
        "total_order": 57
    },
    {
        "type": "code",
        "day": 4,
        "number": 2,
        "question": "第 02 题：判断是否水仙花数\n题目描述：从键盘上输入一个三位数的数，判断这个数字是否是三位数的数字，再判断是否是水仙花数。\n(什么是水仙花数：一个n位数（n≥3），它的每个位上的数字的n次幂之和等于它本身。本题只需要输入3位数，也就是：该数的每个位上的数字的立方和等于该数本身。)\n(数学示例：153>>>:1³=1 ; 5³=125 ; 3³=27 ; 他们的和等于153，所以这个数是水仙花数，不符合要求的就不是。)",
        "options": [],
        "answer": "number = int(input('请输入一个三位数：'))\nif number < 100 or number > 999:\n    print('无效的输入')\nelse:\n    hundreds = number // 100\n    tens = (number // 10) % 10\n    ones = number % 10\n    cube_sum = hundreds ** 3 + tens ** 3 + ones ** 3\n    if cube_sum == number:\n        print(number, '是水仙花数')\n    else:\n        print(number, '不是水仙花数')",
        "code_hint": "定义一个变量number，使用 input() 函数提示用户输入一个三位数。并转换为int\n初步判断：判断number是否是三位数的数字。\n是-则进行是否水仙花数的处理；\n否-输出提示：无效的输入\n分解数字：使用算术运算符，分别提取百位，十位，个位上的数字。\n将取出来的数字，计算立方和。\n立方和与原数字相等-输出：number 是水仙花数\n不等-则输出：number 不是水仙花数",
        "total_order": 58
    },
    {
        "type": "code",
        "day": 4,
        "number": 3,
        "question": "第 03 题：计算商品购物折扣\n题目要求：编写一个计算商品购物折扣的程序，折扣规则如下：\n如果购物金额小于100元，则不享受折扣。\n如果购物金额在100元（含）至300元之间，则享受9折优惠。\n如果购物金额超过300元，则享受85折优惠。",
        "options": [],
        "answer": "shopping_amount = float(input('请输入购物金额：'))\nif shopping_amount < 100:\n    print('您没有享受折扣,需支付:', str(shopping_amount), '元')\nelif shopping_amount >= 100 and shopping_amount < 300:\n    discount = shopping_amount * 0.9\n    print('您可享受9折优惠,需支付:', str(discount), '元')\nelse:\n    discount = shopping_amount * 0.85\n    print('您可享受85折优惠,需支付:', str(discount), '元')",
        "code_hint": "1.定义一个变量(shopping_amount)，用户输入购物金额。\n2.使用if_elif_else进行折扣规则判断：\n如果购物金额小于100元(不含)，则不享受折扣。\n如果购物金额在100元（含）至300元之间，则享受9折优惠。\n如果购物金额超过300元（含），则享受85折优惠。",
        "total_order": 59
    },
    {
        "type": "code",
        "day": 4,
        "number": 4,
        "question": "第 04 题：简单的交通信号灯判断\n题目要求：编写一段代码，模拟交通信号灯的工作。要求用户输入颜色（红、黄、绿），根据颜色输出相应的指示信息。\n输入红色(red),输出:请停车\n输入黄色(yellow),输出:准备停车/尽快通行\n输入绿色(green),输出:允许通行\n输入其它错误字符,输出:\"无效的颜色，请输入红色(red)、黄色(yellow)或绿色(green)\"",
        "options": [],
        "answer": "color = input('请输入颜色（红、黄、绿）：')\nif color == 'red' or color == '红色':\n    print('请停车')\nelif color == 'yellow' or color == '黄色':\n    print('准备停车/尽快通行')\nelif color == 'green' or color == '绿色':\n    print('允许通行')\nelse:\n    print('无效的颜色，请输入红色(red)、黄色(yellow)或绿色(green)')",
        "code_hint": "让用户输入颜色（红、黄、绿），根据颜色输出相应的指示信息。",
        "total_order": 60
    },
    {
        "type": "code",
        "day": 4,
        "number": 5,
        "question": "第 05 题：判断三角形类型\n题目要求：编写一个程序，让用户输入三角形的三条边长，判断并输出三角形的类型：\n等边三角形：三条边相等\n等腰三角形：至少有两条边相等\n直角三角形：满足勾股定理\n不是三角形：不符合三角形的边长关系",
        "options": [],
        "answer": "side1 = float(input('请输入第一条边：'))\nside2 = float(input('请输入第二条边：'))\nside3 = float(input('请输入第三条边：'))\n\nif side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:\n    if side1 == side2 == side3:\n        print('这是一个等边三角形')\n    elif side1 == side2 or side1 == side3 or side2 == side3:\n        print('这是一个等腰三角形')\n    elif side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:\n        print('这是一个直角三角形')\n    else:\n        print('这是一个普通三角形')\nelse:\n    print('不是三角形')",
        "code_hint": "提示用户输入三条边长，使用 input() 函数提示用户依次输入三条边的长度。将输入的字符串转换为浮点数（float）。\n使用条件语句判断是否构成三角形：任意两边之和大于第三边\n再嵌套判断是否符合三角形类型的要求。",
        "total_order": 61
    }
]

data = [item for item in data if item.get('day') != 4]
data.extend(day4_fixed)
data.sort(key=lambda x: x['total_order'])

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("第4天数据修复完成！")
print(f"修复后第4天题目数量: {len([item for item in data if item.get('day') == 4])}")