import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day15_new = [
    {
        "type": "choice",
        "day": 15,
        "number": 1,
        "question": "Vehicle类中__init__方法的作用是什么？",
        "options": ["定义类的属性", "创建类的实例", "初始化对象的属性", "定义类的方法"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 2,
        "question": "创建ElectricCar对象my_car后，调用drive方法会打印什么？",
        "options": ["父类的drive方法", "子类的drive方法", "两个都会打印", "都不会打印"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 3,
        "question": "在提供的代码示例中，Bicycle类显式地继承了哪个类？",
        "options": ["Vehicle", "Car", "Motorcycle", "没有继承任何类"],
        "answer": "A",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 4,
        "question": "什么是类的继承？",
        "options": ["一个类复制另一个类的代码", "一个类获得另一个类的属性和方法", "一个类创建另一个类的实例", "一个类调用另一个类的函数"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 5,
        "question": "关于Python类的继承正确的说法是？",
        "options": ["子类不能覆盖父类的方法", "子类只能继承一个父类", "子类可以继承父类的所有属性和方法", "子类不能添加新的属性和方法"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 6,
        "question": "在Python中，如何正确地在子类中重写父类的方法？",
        "options": ["使用super()函数", "使用@override装饰器", "直接定义同名方法", "使用parent关键字"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 7,
        "question": "在Python中，当你创建了一个从多个类继承的子类时，Python使用什么规则来决定应该首先检查哪个父类的方法或属性？",
        "options": ["深度优先搜索", "广度优先搜索", "随机选择", "按照继承顺序从左到右"],
        "answer": "D",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 8,
        "question": "什么是多继承？",
        "options": ["一个类只有一个父类", "一个类有多个父类", "多个类继承同一个父类", "一个类继承自身"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 9,
        "question": "以下哪一项描述了实例方法和实例属性之间的正确关系？",
        "options": ["实例方法不能访问实例属性", "实例方法必须通过self访问实例属性", "实例属性只能通过类名访问", "实例方法和实例属性没有关系"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 10,
        "question": "关于Python中的实例方法和实例属性，以下哪项陈述是正确的？",
        "options": ["实例方法不需要self参数", "实例属性可以在类外部直接访问", "实例方法只能访问类属性", "实例属性每个对象都有独立的副本"],
        "answer": "D",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 11,
        "question": "class AdvancedWasher(SpinDryer, SteamCleaner)表示什么？",
        "options": ["AdvancedWasher类被SpinDryer和SteamCleaner继承", "AdvancedWasher类继承自SpinDryer和SteamCleaner", "AdvancedWasher是SpinDryer和SteamCleaner的父类", "AdvancedWasher创建SpinDryer和SteamCleaner的实例"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 12,
        "question": "在子类的__init__方法中，如何调用父类的__init__方法？",
        "options": ["使用parent.__init__()", "使用super().__init__()", "直接调用父类名.__init__()", "不需要调用，会自动执行"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 13,
        "question": "当子类重写父类方法时，如何在子类方法中调用父类的同名方法？",
        "options": ["使用super().方法名()", "使用parent.方法名()", "使用self.父类名.方法名()", "无法调用"],
        "answer": "A",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 14,
        "question": "以下关于super()函数的说法，哪个是正确的？",
        "options": ["super()只能在父类中使用", "super()返回父类的实例", "super()可以调用父类的方法", "super()不能传递参数"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 15,
        "question": "什么是方法重写？",
        "options": ["在子类中定义与父类同名的方法", "在父类中修改子类的方法", "创建一个新方法替换原有方法", "复制父类方法到子类"],
        "answer": "A",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 15,
        "number": 16,
        "question": "在多继承中，当多个父类有同名方法时，Python会按照什么顺序查找方法？",
        "options": ["按照继承顺序从右到左", "按照继承顺序从左到右", "随机顺序", "按照方法定义的时间顺序"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 15,
        "number": 17,
        "question": "设计一个简单烤箱系统：创建Kaohongshu类，包含level属性（初始为0），cook方法根据时间增加level并判断烤制状态，info方法打印烤制状态。",
        "options": [],
        "answer": "class Kaohongshu:\n    def __init__(self):\n        self.level = 0\n    \n    def cook(self, time):\n        self.level += time\n        if self.level > 8:\n            print('烤焦了')\n        elif self.level > 5:\n            print('烤熟了')\n        elif self.level > 3:\n            print('半生不熟')\n        else:\n            print('还是生的')\n    \n    def info(self):\n        print(f'当前烤制程度: {self.level}')\n\ntest = Kaohongshu()\ntest.cook(2)\ntest.cook(2)\ntest.cook(3)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 15,
        "number": 18,
        "question": "创建一个Vehicle父类，包含drive方法；创建Car子类继承Vehicle并重写drive方法；创建ElectricCar子类继承Car并重写drive方法；创建实例并调用drive方法验证继承关系。",
        "options": [],
        "answer": "class Vehicle:\n    def drive(self):\n        print('交通工具正在行驶')\n\nclass Car(Vehicle):\n    def drive(self):\n        print('汽车正在行驶')\n\nclass ElectricCar(Car):\n    def drive(self):\n        print('电动汽车正在行驶')\n\nv = Vehicle()\nv.drive()\nc = Car()\nc.drive()\ne = ElectricCar()\ne.drive()",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 15,
        "number": 19,
        "question": "创建Base类，创建Derived类继承Base，在Derived的__init__中调用super().__init__()，并添加额外属性。",
        "options": [],
        "answer": "class Base:\n    def __init__(self, value):\n        self.value = value\n        print(f'Base初始化: {value}')\n\nclass Derived(Base):\n    def __init__(self, value, extra):\n        super().__init__(value)\n        self.extra = extra\n        print(f'Derived初始化: {extra}')\n\nd = Derived(10, '额外信息')\nprint(f'value: {d.value}, extra: {d.extra}')",
        "total_order": 0
    }
]

questions = [q for q in questions if q['day'] != 15]
questions.extend(day15_new)

for i, q in enumerate(sorted(questions, key=lambda x: (x['day'], x['number'])), 1):
    q['total_order'] = i

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Day 15 已修复，共19题")