import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day14_new = [
    {
        "type": "choice",
        "day": 14,
        "number": 1,
        "question": "模拟手洗衣物的过程，按照线性步骤逐一完成每个任务：浸泡衣物、擦洗污渍、漂洗泡沫、拧干水分。根据这一描述，这个程序最符合下列哪种编程范式？",
        "options": ["面向对象编程", "面向过程编程", "声明式编程", "以上都是"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 2,
        "question": "关于Python对面向对象编程，在打车的情景中，下面哪一个选项最能说明乘客和司机之间的\"对象间交流\"？",
        "options": ["乘客自己找到目的地", "司机决定乘客的目的地", "乘客告诉司机要去的目的地", "乘客不与司机交流"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 3,
        "question": "在 Car 类中，make 和 model 是什么类型的属性？",
        "options": ["类属性", "实例属性", "静态属性", "全局属性"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 4,
        "question": "在 Car 类中，display_info属于什么方法？",
        "options": ["类方法", "静态方法", "实例方法", "魔法方法"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 5,
        "question": "在 MathUtils 类中，add() 方法是什么类型的方法？",
        "options": ["类方法", "静态方法", "实例方法", "魔法方法"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 6,
        "question": "静态方法适合用于哪种情况？",
        "options": ["当方法需要访问或修改实例属性时", "当方法仅依赖于参数而不涉及实例或类的状态时", "当方法需要访问或修改类属性时", "当方法必须由类的每个实例独立实现时"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 7,
        "question": "如果在定义类时没有显式地定义 __init__ 方法，会发生什么？",
        "options": ["类将无法创建对象", "创建对象时会抛出异常", "Python提供一个默认的__init__方法，不接收参数（除了self）", "在python中，类方法必须使用@staticmethod装饰器定义，否则无法在类中调用"],
        "answer": "C",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 8,
        "question": "示例代码中，哪个选项正确指出了代码中存在的问题？",
        "options": ["__init__方法不需要参数pet和name", "make_sound方法尝试访问未初始化的实例变量self.pet", "make_sound方法应该被声明为静态方法", "没有错误，代码可以正常工作"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 9,
        "question": "为了使代码能够正常运行，以下哪些修改是有效的？（多选）",
        "options": ["在make_sound方法中移除self.pet", "在__init__方法中添加self.pet = pet", "将make_sound改为类方法，并用@classmethod装饰", "将make_sound改为静态方法，并用@staticmethod装饰"],
        "answer": "AB",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 10,
        "question": "以下哪项是错误的创建 Animal 类实例的方式？（多选）",
        "options": ["dog = Animal(\"小狗\", \"旺财\")", "cat = Animal(pet=\"小猫\", name=\"招财\")", "bird = Animal(pet=\"小鸟\")", "fish = Animal(\"小鱼\", sound=\"泡泡\")"],
        "answer": "CD",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 11,
        "question": "关于类的初始化方法 __init__，以下哪些描述是正确的？（多选）",
        "options": ["__init__方法在创建类的新实例时自动调用", "__init__方法必须接收一个参数，通常命名为self，用于引用被创建的实例", "__init__方法可以用来初始化实例属性", "__init__方法不应返回任何值，因为它的主要职责是初始化新对象"],
        "answer": "ABCD",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 12,
        "question": "关于使用 对象 = 类名(参数) 创建对象的动作，以下哪些描述是正确的？（多选）",
        "options": ["类名(参数)代表的是一个类的实例化过程，而不是类本身", "当执行对象=类名(参数)时，对象是一个引用变量，它将指向新创建的对象", "类名(参数)的调用会触发类中定义的__init__方法来初始化新对象", "在对象=类名(参数)中传递的参数用于初始化新对象的属性"],
        "answer": "ABCD",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 13,
        "question": "定义一个Bicycle类，需要使用什么关键字？",
        "options": ["def", "class", "struct", "type"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 14,
        "question": "在类的构造器中，self参数代表什么？",
        "options": ["类本身", "实例（对象本身）", "父类", "类属性"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 15,
        "question": "如果要在类的方法中访问类的实例属性，可以使用什么方式？",
        "options": ["直接使用属性名", "使用self加上属性名", "使用类名加上属性名", "使用global关键字"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 14,
        "number": 16,
        "question": "定义静态方法使用什么装饰器？",
        "options": ["@classmethod", "@staticmethod", "@property", "@decorator"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 14,
        "number": 17,
        "question": "完善Bicycle类：定义类属性color（红色）和total_cars（初始为0），定义实例属性brand和size，每创建一个实例时total_cars加1，定义静态方法count_cars（返回车的数量）和print_color（打印颜色），完成类的实例化并调用静态方法。",
        "options": [],
        "answer": "class Bicycle:\n    color = \"red\"\n    total_cars = 0\n    \n    def __init__(self, brand, size):\n        self.brand = brand\n        self.size = size\n        Bicycle.total_cars += 1\n    \n    @staticmethod\n    def count_cars():\n        return Bicycle.total_cars\n    \n    @staticmethod\n    def print_color():\n        print(\"Bicycle color:\", Bicycle.color)\n\nbike1 = Bicycle(\"Giant\", \"Medium\")\nbike2 = Bicycle(\"Trek\", \"Large\")\nprint(f\"自行车总数: {Bicycle.count_cars()}\")\nBicycle.print_color()",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 14,
        "number": 18,
        "question": "拓展Person类：增加实例属性gender、height、weight，增加类属性total_persons（记录Person对象总数），添加calculate_bmi()方法计算BMI，添加静态方法get_total_persons()返回总人数，更新show_info()方法显示新增属性，创建多个对象并调用方法。",
        "options": [],
        "answer": "class Person:\n    total_persons = 0\n    \n    def __init__(self, name, age, gender, height, weight):\n        self.name = name\n        self.age = age\n        self.gender = gender\n        self.height = height\n        self.weight = weight\n        self.address = None\n        Person.total_persons += 1\n    \n    def set_address(self, address):\n        self.address = address\n        print(f\"{self.name} 在 {address}.\")\n    \n    def greet(self):\n        print(f\"你好, 我叫{self.name}, 我今年 {self.age} 岁。\")\n    \n    def show_info(self):\n        print(f\"名字: {self.name}\")\n        print(f\"年龄: {self.age}\")\n        print(f\"性别: {self.gender}\")\n        print(f\"身高: {self.height} cm\")\n        print(f\"体重: {self.weight} kg\")\n        if self.address:\n            print(f\"地址: {self.address}\")\n        else:\n            print(\"没有设置地址。\")\n    \n    def calculate_bmi(self):\n        height_m = self.height / 100\n        bmi = self.weight / (height_m ** 2)\n        print(f\"{self.name} 的 BMI 是 {bmi:.2f}\")\n    \n    @staticmethod\n    def get_total_persons():\n        return Person.total_persons\n\nperson1 = Person(\"六一\", 27, \"女\", 165, 55)\nperson2 = Person(\"XiaoXiao\", 30, \"男\", 175, 80)\nperson1.greet()\nperson2.set_address(\"新长海科技园\")\nperson1.show_info()\nperson2.show_info()\nperson1.calculate_bmi()\nperson2.calculate_bmi()\nprint(f\"总共创建了 {Person.get_total_persons()} 个人。\")",
        "total_order": 0
    }
]

questions = [q for q in questions if q['day'] != 14]
questions.extend(day14_new)

for i, q in enumerate(sorted(questions, key=lambda x: (x['day'], x['number'])), 1):
    q['total_order'] = i

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Day 14 已修复，共18题")