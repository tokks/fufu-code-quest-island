import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

fixed_data = []
current_code_item = None

for item in data:
    if item['type'] == 'choice':
        if current_code_item:
            fixed_data.append(current_code_item)
            current_code_item = None
        fixed_data.append(item)
        continue
    
    if item['type'] == 'code':
        q = item.get('question', '').strip()
        
        if q.startswith('第') and '题' in q and (':' in q or '：' in q):
            if current_code_item:
                fixed_data.append(current_code_item)
            
            current_code_item = {
                'type': 'code',
                'day': item['day'],
                'number': item['number'],
                'question': q,
                'options': [],
                'answer': '',
                'code_hint': '',
                'total_order': item['total_order']
            }
            
            if item.get('code_hint'):
                current_code_item['code_hint'] = item['code_hint']
        
        elif current_code_item:
            if q.startswith('题目要求') or q.startswith('具体要求') or q.startswith('题目描述'):
                current_code_item['question'] += '\n' + q
            elif q.startswith('解题思路'):
                if item.get('code_hint'):
                    if current_code_item['code_hint']:
                        current_code_item['code_hint'] += '\n' + item['code_hint']
                    else:
                        current_code_item['code_hint'] = item['code_hint']
            elif q.startswith('#'):
                if item.get('code_hint'):
                    if current_code_item['code_hint']:
                        current_code_item['code_hint'] += '\n' + item['code_hint']
                    else:
                        current_code_item['code_hint'] = item['code_hint']
            elif q.startswith('【') and q.endswith('】'):
                if item.get('code_hint'):
                    if current_code_item['code_hint']:
                        current_code_item['code_hint'] += '\n' + item['code_hint']
                    else:
                        current_code_item['code_hint'] = item['code_hint']
            else:
                current_code_item['question'] += '\n' + q
                if item.get('code_hint'):
                    if current_code_item['code_hint']:
                        current_code_item['code_hint'] += '\n' + item['code_hint']
                    else:
                        current_code_item['code_hint'] = item['code_hint']
        else:
            fixed_data.append(item)

if current_code_item:
    fixed_data.append(current_code_item)

answers = {
    4: {
        1: "number = float(input('请输入一个浮点数：'))\nif number > 0:\n    print(number, '是正数。')\nelif number < 0:\n    print(number, '是负数。')\nelse:\n    print(number, '是零。')",
        2: "number = int(input('请输入一个三位数：'))\nif number < 100 or number > 999:\n    print('无效的输入')\nelse:\n    hundreds = number // 100\n    tens = (number // 10) % 10\n    ones = number % 10\n    cube_sum = hundreds ** 3 + tens ** 3 + ones ** 3\n    if cube_sum == number:\n        print(number, '是水仙花数')\n    else:\n        print(number, '不是水仙花数')",
        3: "shopping_amount = float(input('请输入购物金额：'))\nif shopping_amount < 100:\n    print('您没有享受折扣,需支付:', str(shopping_amount), '元')\nelif shopping_amount >= 100 and shopping_amount < 300:\n    discount = shopping_amount * 0.9\n    print('您可享受9折优惠,需支付:', str(discount), '元')\nelse:\n    discount = shopping_amount * 0.85\n    print('您可享受85折优惠,需支付:', str(discount), '元')",
        4: "color = input('请输入颜色（红、黄、绿）：')\nif color == 'red' or color == '红色':\n    print('请停车')\nelif color == 'yellow' or color == '黄色':\n    print('准备停车/尽快通行')\nelif color == 'green' or color == '绿色':\n    print('允许通行')\nelse:\n    print('无效的颜色，请输入红色(red)、黄色(yellow)或绿色(green)')",
        5: "side1 = float(input('请输入第一条边：'))\nside2 = float(input('请输入第二条边：'))\nside3 = float(input('请输入第三条边：'))\n\nif side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:\n    if side1 == side2 == side3:\n        print('这是一个等边三角形')\n    elif side1 == side2 or side1 == side3 or side2 == side3:\n        print('这是一个等腰三角形')\n    elif side1**2 + side2**2 == side3**2 or side1**2 + side3**2 == side2**2 or side2**2 + side3**2 == side1**2:\n        print('这是一个直角三角形')\n    else:\n        print('这是一个普通三角形')\nelse:\n    print('不是三角形')"
    },
    5: {
        1: "success_count = 0\nfor i in range(3):\n    username = input('请输入用户名：')\n    password = input('请输入密码：')\n    if username == 'admin' and password == 'password':\n        success_count += 1\n        print('第{}次输入正确'.format(i+1))\n    else:\n        print('第{}次输入错误'.format(i+1))\nif success_count == 3:\n    print('登录成功')\nelse:\n    print('登录失败，失败次数：', 3 - success_count)",
        2: "for i in range(5):\n    for j in range(5):\n        print('*', end='  ')\n    print()",
        3: "for i in range(5):\n    for j in range(i + 1):\n        print('*', end='  ')\n    print()",
        4: "for i in range(5, 0, -1):\n    for j in range(i):\n        print('*', end='  ')\n    print()",
        5: "for i in range(1, 10):\n    for j in range(1, i + 1):\n        print('{}x{}={}'.format(j, i, i * j), end='\\t')\n    print()",
        6: "coins_per_day = int(input('请输入每天存入的硬币数量：'))\ntotal_days = int(input('请输入总天数：'))\ntotal_coins = 0\nfor day in range(1, total_days + 1):\n    total_coins += coins_per_day\n    print('第{}天：累计存入{}枚硬币'.format(day, total_coins))\nprint('总共存入{}枚硬币'.format(total_coins))"
    },
    8: {
        1: "city = '哈尔滨'\ntemperature = -15.5\nreport = '当前城市 {} 温度为 {} 摄氏度。'\nformatted_report = report.format(city, temperature)\nprint(formatted_report)",
        2: "city = '哈尔滨'\ntemperature = -15.5\nreport = f'当前城市 {city} 温度为 {temperature} 摄氏度。'\nprint(report)",
        3: "print(round(3.7))\nprint(round(3.2))",
        4: "import math\nprint(math.ceil(3.2))\nprint(math.floor(3.7))",
        5: "print(abs(-5))\nprint(abs(-3.14))",
        6: "print(max(1, 2, 3))\nprint(min(1, 2, 3))"
    },
    9: {
        1: "def greet(name):\n    print('Hello, ' + name + '!')\ngreet('World')",
        2: "def add(a, b):\n    return a + b\nresult = add(3, 5)\nprint(result)",
        3: "def calculate_area(radius):\n    return 3.14159 * radius ** 2\narea = calculate_area(5)\nprint(area)",
        4: "def is_even(num):\n    return num % 2 == 0\nprint(is_even(4))\nprint(is_even(5))"
    },
    10: {
        1: "student = {'name': '张三', 'age': 18, 'score': 95}\nprint(student['name'])\nprint(student['age'])\nprint(student['score'])",
        2: "student = {'name': '张三', 'age': 18}\nstudent['score'] = 95\nstudent['gender'] = '男'\nprint(student)",
        3: "student = {'name': '张三', 'age': 18, 'score': 95}\nkeys = list(student.keys())\nvalues = list(student.values())\nitems = list(student.items())\nprint(keys)\nprint(values)\nprint(items)",
        4: "student = {'name': '张三', 'age': 18}\nif 'score' in student:\n    print(student['score'])\nelse:\n    print('成绩不存在')"
    },
    11: {
        1: "def greet(name, message='Hello'):\n    print(message + ', ' + name + '!')\ngreet('World')\ngreet('World', 'Hi')",
        2: "def add(*args):\n    total = 0\n    for num in args:\n        total += num\n    return total\nprint(add(1, 2, 3))\nprint(add(1, 2, 3, 4, 5))"
    },
    12: {
        1: "def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    return n * factorial(n - 1)\nprint(factorial(5))",
        2: "def fibonacci(n):\n    if n <= 1:\n        return n\n    return fibonacci(n - 1) + fibonacci(n - 2)\nfor i in range(10):\n    print(fibonacci(i))",
        3: "def make_counter():\n    count = 0\n    def counter():\n        nonlocal count\n        count += 1\n        return count\n    return counter\nc = make_counter()\nprint(c())\nprint(c())\nprint(c())",
        4: "add = lambda x, y: x + y\nprint(add(3, 5))",
        5: "numbers = [1, 2, 3, 4, 5]\nsquared = list(map(lambda x: x ** 2, numbers))\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(squared)\nprint(evens)"
    },
    13: {
        1: "class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n    def introduce(self):\n        print('我叫', self.name, '今年', self.age, '岁')\np = Person('张三', 18)\np.introduce()",
        2: "class Student:\n    school = '第一中学'\n    def __init__(self, name, grade):\n        self.name = name\n        self.grade = grade\ns = Student('张三', '高三')\nprint(Student.school)\nprint(s.name, s.grade)",
        3: "class Circle:\n    def __init__(self, radius):\n        self.__radius = radius\n    def get_radius(self):\n        return self.__radius\n    def set_radius(self, radius):\n        if radius > 0:\n            self.__radius = radius\n    def area(self):\n        return 3.14159 * self.__radius ** 2\nc = Circle(5)\nprint(c.area())",
        4: "class Calculator:\n    def add(self, a, b):\n        return a + b\n    def subtract(self, a, b):\n        return a - b\n    def multiply(self, a, b):\n        return a * b\n    def divide(self, a, b):\n        if b != 0:\n            return a / b\n        return None\ncalc = Calculator()\nprint(calc.add(10, 5))\nprint(calc.divide(10, 5))"
    },
    14: {
        1: "class Animal:\n    def speak(self):\n        pass\nclass Dog(Animal):\n    def speak(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def speak(self):\n        print('喵喵喵')\nd = Dog()\nd.speak()",
        2: "class Person:\n    def __init__(self, name):\n        self.name = name\n    def introduce(self):\n        print('我是', self.name)\nclass Student(Person):\n    def __init__(self, name, grade):\n        super().__init__(name)\n        self.grade = grade\n    def introduce(self):\n        super().introduce()\n        print('我在读', self.grade)\ns = Student('张三', '高三')\ns.introduce()",
        3: "class Shape:\n    def area(self):\n        pass\nclass Rectangle(Shape):\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n    def area(self):\n        return self.width * self.height\nclass Circle(Shape):\n    def __init__(self, radius):\n        self.radius = radius\n    def area(self):\n        return 3.14159 * self.radius ** 2\nshapes = [Rectangle(4, 5), Circle(3)]\nfor shape in shapes:\n    print(shape.area())",
        4: "class A:\n    def show(self):\n        print('A')\nclass B:\n    def show(self):\n        print('B')\nclass C(A, B):\n    pass\nc = C()\nc.show()"
    },
    15: {
        1: "class Animal:\n    def speak(self):\n        pass\nclass Dog(Animal):\n    def speak(self):\n        print('汪汪汪')\nclass Cat(Animal):\n    def speak(self):\n        print('喵喵喵')\ndef make_speak(animal):\n    animal.speak()\nmake_speak(Dog())\nmake_speak(Cat())",
        2: "class Bird:\n    def fly(self):\n        print('鸟在飞')\nclass Airplane:\n    def fly(self):\n        print('飞机在飞')\ndef let_fly(obj):\n    obj.fly()\nlet_fly(Bird())\nlet_fly(Airplane())",
        3: "class A:\n    def method(self):\n        print('A')\nclass B(A):\n    def method(self):\n        print('B')\nclass C(B):\n    def method(self):\n        print('C')\nc = C()\nc.method()",
        4: "class Duck:\n    def quack(self):\n        print('嘎嘎嘎')\n    def swim(self):\n        print('鸭子在游泳')\nclass Person:\n    def quack(self):\n        print('人模仿鸭子叫')\n    def swim(self):\n        print('人在游泳')\ndef duck_test(obj):\n    obj.quack()\n    obj.swim()\nduck_test(Duck())\nduck_test(Person())"
    },
    16: {
        1: "class Person:\n    def __init__(self, name):\n        self.name = name\n    def __str__(self):\n        return 'Person: ' + self.name\np = Person('张三')\nprint(p)",
        2: "class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __add__(self, other):\n        return Vector(self.x + other.x, self.y + other.y)\n    def __str__(self):\n        return f'({self.x}, {self.y})'\nv1 = Vector(1, 2)\nv2 = Vector(3, 4)\nprint(v1 + v2)",
        3: "class Counter:\n    def __init__(self):\n        self.count = 0\n    def __call__(self):\n        self.count += 1\n        return self.count\nc = Counter()\nprint(c())\nprint(c())\nprint(c())",
        4: "class MyList:\n    def __init__(self, items):\n        self.items = items\n    def __len__(self):\n        return len(self.items)\n    def __getitem__(self, index):\n        return self.items[index]\nml = MyList([1, 2, 3, 4, 5])\nprint(len(ml))\nprint(ml[2])"
    },
    17: {
        1: "class Singleton:\n    _instance = None\n    def __new__(cls, *args, **kwargs):\n        if not cls._instance:\n            cls._instance = super().__new__(cls)\n        return cls._instance\ns1 = Singleton()\ns2 = Singleton()\nprint(s1 is s2)",
        2: "class Singleton:\n    def __init__(self):\n        pass\n    @classmethod\n    def get_instance(cls):\n        if not hasattr(cls, '_instance'):\n            cls._instance = cls()\n        return cls._instance\ns1 = Singleton.get_instance()\ns2 = Singleton.get_instance()\nprint(s1 is s2)",
        3: "import module_name\nprint(module_name.variable)\nmodule_name.function()",
        4: "from module_name import variable, function\nprint(variable)\nfunction()"
    },
    18: {
        1: "with open('test.txt', 'w') as f:\n    f.write('Hello, World!')",
        2: "with open('test.txt', 'r') as f:\n    content = f.read()\n    print(content)",
        3: "with open('test.txt', 'a') as f:\n    f.write('\\nAppended content')",
        4: "with open('test.txt', 'r') as f:\n    lines = f.readlines()\n    for line in lines:\n        print(line.strip())"
    },
    19: {
        1: "import re\npattern = r'\\d+'\ntext = 'abc123def456'\nresult = re.findall(pattern, text)\nprint(result)",
        2: "import re\npattern = r'^[a-zA-Z]+$'\ntext = 'Hello'\nresult = re.match(pattern, text)\nprint(bool(result))",
        3: "import re\npattern = r'\\b\\w+\\b'\ntext = 'Hello, world!'\nresult = re.findall(pattern, text)\nprint(result)",
        4: "import re\npattern = r'(\\d{4})-(\\d{2})-(\\d{2})'\ntext = 'Date: 2024-01-15'\nresult = re.search(pattern, text)\nif result:\n    print('Year:', result.group(1))\n    print('Month:', result.group(2))\n    print('Day:', result.group(3))"
    },
    20: {
        1: "def decorator(func):\n    def wrapper(*args, **kwargs):\n        print('Before')\n        result = func(*args, **kwargs)\n        print('After')\n        return result\n    return wrapper\n@decorator\ndef greet():\n    print('Hello')\ngreet()",
        2: "def timer(func):\n    import time\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f'{func.__name__} took {end-start:.2f} seconds')\n        return result\n    return wrapper\n@timer\ndef slow_function():\n    import time\n    time.sleep(1)\nslow_function()",
        3: "def repeat(times):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            results = []\n            for _ in range(times):\n                results.append(func(*args, **kwargs))\n            return results\n        return wrapper\n    return decorator\n@repeat(3)\ndef greet():\n    return 'Hello'\nprint(greet())",
        4: "def generator():\n    yield 1\n    yield 2\n    yield 3\ng = generator()\nfor num in g:\n    print(num)",
        5: "def fibonacci():\n    a, b = 0, 1\n    while True:\n        yield a\n        a, b = b, a + b\nfib = fibonacci()\nfor _ in range(10):\n    print(next(fib))"
    },
    21: {
        1: "def debug(func):\n    def wrapper(*args, **kwargs):\n        print(f'Calling {func.__name__} with args={args}, kwargs={kwargs}')\n        result = func(*args, **kwargs)\n        print(f'{func.__name__} returned {result}')\n        return result\n    return wrapper\n@debug\ndef add(a, b):\n    return a + b\nprint(add(3, 5))",
        2: "class ErrorHandler:\n    def __enter__(self):\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if exc_type:\n            print(f'Error: {exc_val}')\n            return True\n        return False\nwith ErrorHandler():\n    raise ValueError('Test error')",
        3: "def process_file(filename):\n    try:\n        with open(filename, 'r') as f:\n            content = f.read()\n            return content\n    except FileNotFoundError:\n        print(f'File {filename} not found')\n        return None\n    except Exception as e:\n        print(f'Error: {e}')\n        return None\nprint(process_file('test.txt'))",
        4: "import logging\nlogging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')\nlogging.debug('Debug message')\nlogging.info('Info message')\nlogging.warning('Warning message')\nlogging.error('Error message')",
        5: "def challenge():\n    print('Congratulations!')\n    print('You have completed all challenges!')\n    print('Welcome to the world of Python!')\nchallenge()"
    }
}

for item in fixed_data:
    if item['type'] == 'code' and item.get('day') in answers:
        day_answers = answers[item['day']]
        if item['number'] in day_answers:
            item['answer'] = day_answers[item['number']]

fixed_data.sort(key=lambda x: x['total_order'])

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_data, f, ensure_ascii=False, indent=2)

print("修复完成！")
print(f"总题目数: {len(fixed_data)}")

for day in range(1, 22):
    day_items = [i for i in fixed_data if i.get('day') == day]
    if day_items:
        code_items = [i for i in day_items if i.get('type') == 'code']
        choice_items = [i for i in day_items if i.get('type') == 'choice']
        print(f"Day {day}: {len(day_items)} 题 ({len(choice_items)} choice, {len(code_items)} code)")