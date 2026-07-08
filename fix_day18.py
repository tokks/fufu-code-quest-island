import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day18_new = [
    {
        "type": "code",
        "day": 18,
        "number": 1,
        "question": "创建一个商品类Product，包含name、price、quantity属性，在__init__中进行输入验证（价格和数量必须大于0），添加get_total_value方法计算商品总价值，添加discount方法计算折扣后价格。",
        "options": [],
        "answer": "class Product:\n    def __init__(self, name, price, quantity):\n        self.name = name\n        if price <= 0:\n            raise ValueError('价格必须大于0')\n        self.price = price\n        if quantity <= 0:\n            raise ValueError('数量必须大于0')\n        self.quantity = quantity\n    \n    def get_total_value(self):\n        return self.price * self.quantity\n    \n    def discount(self, percent):\n        if percent < 0 or percent > 100:\n            raise ValueError('折扣必须在0-100之间')\n        return self.price * (1 - percent / 100)\n\np = Product('笔记本', 50, 10)\nprint(f'总价值: {p.get_total_value()}')\nprint(f'折扣后价格: {p.discount(20):.2f}')",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 18,
        "number": 2,
        "question": "实现单例模式：创建一个Singleton类，确保只有一个实例存在。",
        "options": [],
        "answer": "class Singleton:\n    _instance = None\n    \n    def __new__(cls, *args, **kwargs):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance\n\ns1 = Singleton()\ns2 = Singleton()\nprint(s1 is s2)  # True",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 18,
        "number": 3,
        "question": "创建一个数学工具包math_tools，包含basic_operations模块（add, subtract, multiply, divide函数）和geometry模块（area_circle, area_rectangle函数），在主程序中导入并使用。",
        "options": [],
        "answer": "# math_tools/__init__.py\n# 空文件\n\n# math_tools/basic_operations.py\ndef add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n\ndef multiply(a, b):\n    return a * b\n\ndef divide(a, b):\n    if b == 0:\n        raise ValueError('除数不能为0')\n    return a / b\n\n# math_tools/geometry.py\nimport math\n\ndef area_circle(radius):\n    return math.pi * radius ** 2\n\ndef area_rectangle(width, height):\n    return width * height\n\n# 主程序\nfrom math_tools.basic_operations import add, multiply\nfrom math_tools.geometry import area_circle\n\nprint(f'3 + 5 = {add(3, 5)}')\nprint(f'4 * 6 = {multiply(4, 6)}')\nprint(f'半径为3的圆面积: {area_circle(3):.2f}')",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 18,
        "number": 4,
        "question": "创建一个包目录结构，包含导入整个模块、从模块导入特定函数、使用别名三种导入方式的示例。",
        "options": [],
        "answer": "# 包目录结构:\n# mypackage/\n#     __init__.py\n#     module1.py\n#     module2.py\n\n# mypackage/module1.py\ndef greet(name):\n    return f'Hello, {name}!'\n\n# mypackage/module2.py\ndef calculate_sum(a, b):\n    return a + b\n\n# 导入整个模块\nimport mypackage.module1 as m1\nprint(m1.greet('Alice'))\n\n# 从模块导入特定函数\nfrom mypackage.module2 import calculate_sum\nprint(calculate_sum(10, 20))\n\n# 使用别名\nfrom mypackage.module1 import greet as say_hello\nprint(say_hello('Bob'))",
        "total_order": 0
    }
]

questions = [q for q in questions if q['day'] != 18]
questions.extend(day18_new)

for i, q in enumerate(sorted(questions, key=lambda x: (x['day'], x['number'])), 1):
    q['total_order'] = i

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Day 18 已修复，共4题")