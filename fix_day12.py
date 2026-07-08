import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day12_new = [
    {
        "type": "code",
        "day": 12,
        "number": 1,
        "question": "创建问候语：编写一个名为create_greeting的函数，接受name（字符串）、event（字符串，默认为'Hello'）、is_upper（布尔值，默认为False），返回问候语，当is_upper为True时返回大写形式。",
        "options": [],
        "answer": "def create_greeting(name, event=\"Hello\", is_upper=False):\n    greeting = f\"{event}, {name}!\"\n    if is_upper:\n        return greeting.upper()\n    else:\n        return greeting\n\nprint(create_greeting(\"Alice\"))\nprint(create_greeting(\"Bob\", \"Goodbye\"))\nprint(create_greeting(\"Charlie\", is_upper=True))\nprint(create_greeting(\"Dave\", \"Welcome\", True))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 2,
        "question": "模拟航班预定：编写一个名为book_flight的函数，接受destination（字符串）、date（字符串）、flight_class（默认为'Economy(经济舱)'）、meal（默认为'No preference(无特殊要求)'）、insurance（默认为False），返回包含所有预订信息的字典。",
        "options": [],
        "answer": "def book_flight(destination, date, flight_class=\"Economy(经济舱)\", meal=\"No preference(无特殊要求)\", insurance=False):\n    flight_info = {\n        \"目的地\": destination,\n        \"时间\": date,\n        \"舱位等级\": flight_class,\n        \"餐食偏好\": meal,\n        \"是否购买旅行保险\": insurance\n    }\n    return flight_info\n\nflight_details = book_flight(\"上海\", \"2024-12-25\")\nprint(flight_details)\nflight_details = book_flight(\"北京\", \"2024-12-26\", flight_class=\"Business(商务舱)\", meal=\"Vegetarian(素食)\", insurance=True)\nprint(flight_details)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 3,
        "question": "计算任意数量参数的总和：编写一个名为calculate_sum的函数，使用可变位置参数*args，计算所有传入参数的总和并返回。",
        "options": [],
        "answer": "def calculate_sum(*args):\n    total = 0\n    for num in args:\n        total += num\n    return total\n\nprint(calculate_sum(1, 2, 3))\nprint(calculate_sum(10, 20, 30, 40))\nprint(calculate_sum(5))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 4,
        "question": "创建活动信息：编写一个名为create_event的函数，接受必需参数name和date，以及可变关键字参数**kwargs，返回包含所有活动信息的字典。",
        "options": [],
        "answer": "def create_event(name, date, **kwargs):\n    event_info = {\n        \"活动名称\": name,\n        \"活动日期\": date\n    }\n    event_info.update(kwargs)\n    return event_info\n\nevent = create_event(\"技术分享会\", \"2024-12-30\", location=\"会议室A\", participants=50, organizer=\"技术部\")\nprint(event)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 5,
        "question": "计算购物车折扣后的总价：编写一个名为calculate_discounted_price的函数，接受可变位置参数*prices和关键字参数discount（默认为0），计算所有价格的总和并应用折扣。",
        "options": [],
        "answer": "def calculate_discounted_price(*prices, discount=0):\n    total = sum(prices)\n    if discount > 0:\n        total = total * (1 - discount / 100)\n    return total\n\nprint(calculate_discounted_price(100, 200, 300))\nprint(calculate_discounted_price(100, 200, 300, discount=10))\nprint(calculate_discounted_price(50, 50, discount=20))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 6,
        "question": "使用回调函数进行用户问候：定义greet_user函数，接受name和callback参数，调用callback(name)；定义say_hello回调函数，打印问候语；调用greet_user函数。",
        "options": [],
        "answer": "def greet_user(name, callback):\n    callback(name)\n\ndef say_hello(name):\n    print(f\"Hello, {name}!\")\n\ndef say_goodbye(name):\n    print(f\"Goodbye, {name}!\")\n\ngreet_user(\"Alice\", say_hello)\ngreet_user(\"Bob\", say_goodbye)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 7,
        "question": "使用回调函数实现基本算术运算：定义calculate函数，接受a、b和operation回调函数，返回operation(a, b)的结果；定义add、subtract、multiply回调函数；调用calculate函数。",
        "options": [],
        "answer": "def calculate(a, b, operation):\n    return operation(a, b)\n\ndef add(a, b):\n    return a + b\n\ndef subtract(a, b):\n    return a - b\n\ndef multiply(a, b):\n    return a * b\n\ndef divide(a, b):\n    if b == 0:\n        raise ValueError('除数不能为0')\n    return a / b\n\nprint(calculate(10, 5, add))\nprint(calculate(10, 5, subtract))\nprint(calculate(10, 5, multiply))\nprint(calculate(10, 5, divide))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 8,
        "question": "使用回调函数获取天气预报：定义get_weather_forecast函数，接受location和callback参数，模拟获取天气数据并调用callback；定义display_weather回调函数，打印天气信息。",
        "options": [],
        "answer": "def get_weather_forecast(location, callback):\n    weather_data = {\n        \"location\": location,\n        \"temperature\": 25,\n        \"condition\": \"晴\",\n        \"humidity\": 60\n    }\n    callback(weather_data)\n\ndef display_weather(data):\n    print(f\"{data['location']}的天气：\")\n    print(f\"温度：{data['temperature']}°C\")\n    print(f\"状况：{data['condition']}\")\n    print(f\"湿度：{data['humidity']}%\")\n\nget_weather_forecast(\"北京\", display_weather)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 9,
        "question": "编写文本加密器：包含三种加密方式——简单文本加密（替换字符）、数字位移加密（每个字符ASCII码加n）、反向文本加密（反转字符串），编写主函数调用这些加密方式。",
        "options": [],
        "answer": "def simple_encrypt(text):\n    mapping = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e', 'e': 'f', 'f': 'g', 'g': 'h', 'h': 'i', 'i': 'j', 'j': 'k', 'k': 'l', 'l': 'm', 'm': 'n', 'n': 'o', 'o': 'p', 'p': 'q', 'q': 'r', 'r': 's', 's': 't', 't': 'u', 'u': 'v', 'v': 'w', 'w': 'x', 'x': 'y', 'y': 'z', 'z': 'a'}\n    result = ''\n    for char in text.lower():\n        result += mapping.get(char, char)\n    return result\n\ndef shift_encrypt(text, shift=3):\n    result = ''\n    for char in text:\n        if char.isalpha():\n            base = ord('A') if char.isupper() else ord('a')\n            result += chr((ord(char) - base + shift) % 26 + base)\n        else:\n            result += char\n    return result\n\ndef reverse_encrypt(text):\n    return text[::-1]\n\ndef main():\n    text = \"Hello World!\"\n    print(f\"原始文本: {text}\")\n    print(f\"简单加密: {simple_encrypt(text)}\")\n    print(f\"位移加密: {shift_encrypt(text, 3)}\")\n    print(f\"反向加密: {reverse_encrypt(text)}\")\n\nmain()",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 10,
        "question": "创建带默认参数的函数：编写一个名为create_profile的函数，接受name、age、gender（默认为'未知'）、city（默认为'未指定'），返回个人资料字典。",
        "options": [],
        "answer": "def create_profile(name, age, gender=\"未知\", city=\"未指定\"):\n    return {\n        \"姓名\": name,\n        \"年龄\": age,\n        \"性别\": gender,\n        \"城市\": city\n    }\n\nprint(create_profile(\"张三\", 25))\nprint(create_profile(\"李四\", 30, \"男\"))\nprint(create_profile(\"王五\", 28, \"女\", \"北京\"))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 11,
        "question": "使用关键字参数：编写一个名为print_student_info的函数，接受name、age、grade、major参数，使用关键字参数调用该函数。",
        "options": [],
        "answer": "def print_student_info(name, age, grade, major):\n    print(f\"学生信息：\")\n    print(f\"姓名：{name}\")\n    print(f\"年龄：{age}\")\n    print(f\"年级：{grade}\")\n    print(f\"专业：{major}\")\n\nprint_student_info(name=\"张三\", age=20, grade=\"大三\", major=\"计算机科学\")\nprint_student_info(age=19, name=\"李四\", major=\"软件工程\", grade=\"大二\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 12,
        "question": "混合参数练习：编写一个名为process_data的函数，接受必需参数data、可变位置参数*args、可变关键字参数**kwargs，打印所有参数。",
        "options": [],
        "answer": "def process_data(data, *args, **kwargs):\n    print(f\"必需参数: {data}\")\n    print(f\"可变位置参数: {args}\")\n    print(f\"可变关键字参数: {kwargs}\")\n\nprocess_data(\"基础数据\", 1, 2, 3, name=\"张三\", age=25, city=\"北京\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 13,
        "question": "匿名函数练习：使用lambda表达式创建一个加法函数，一个平方函数，一个判断是否为偶数的函数。",
        "options": [],
        "answer": "add = lambda a, b: a + b\nsquare = lambda x: x ** 2\nis_even = lambda x: x % 2 == 0\n\nprint(f\"3 + 5 = {add(3, 5)}\")\nprint(f\"4的平方 = {square(4)}\")\nprint(f\"6是偶数吗？{is_even(6)}\")\nprint(f\"7是偶数吗？{is_even(7)}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 14,
        "question": "使用map和lambda：使用map函数和lambda表达式将列表中的每个数字乘以2。",
        "options": [],
        "answer": "numbers = [1, 2, 3, 4, 5]\nresult = list(map(lambda x: x * 2, numbers))\nprint(result)\n\nstrings = [\"apple\", \"banana\", \"cherry\"]\nlengths = list(map(lambda s: len(s), strings))\nprint(lengths)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 15,
        "question": "使用filter和lambda：使用filter函数和lambda表达式过滤出列表中的偶数。",
        "options": [],
        "answer": "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(evens)\n\nwords = [\"hello\", \"world\", \"python\", \"code\"]\nlong_words = list(filter(lambda w: len(w) > 5, words))\nprint(long_words)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 16,
        "question": "使用reduce和lambda：使用reduce函数和lambda表达式计算列表中所有数字的乘积。",
        "options": [],
        "answer": "from functools import reduce\n\nnumbers = [1, 2, 3, 4, 5]\nproduct = reduce(lambda a, b: a * b, numbers)\nprint(f\"乘积: {product}\")\n\nwords = [\"Hello\", \"World\", \"Python\"]\nconcatenated = reduce(lambda a, b: a + \" \" + b, words)\nprint(f\"连接后的字符串: {concatenated}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 17,
        "question": "闭包练习：创建一个计数器闭包，每次调用返回递增的数字。",
        "options": [],
        "answer": "def make_counter():\n    count = 0\n    \n    def counter():\n        nonlocal count\n        count += 1\n        return count\n    \n    return counter\n\nc1 = make_counter()\nprint(c1())\nprint(c1())\nprint(c1())\n\nc2 = make_counter()\nprint(c2())\nprint(c2())",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 18,
        "question": "闭包练习：创建一个乘法器闭包，接受一个因子，返回一个函数，该函数将输入值乘以这个因子。",
        "options": [],
        "answer": "def make_multiplier(factor):\n    def multiplier(x):\n        return x * factor\n    return multiplier\n\ndouble = make_multiplier(2)\ntriple = make_multiplier(3)\n\nprint(f\"5 * 2 = {double(5)}\")\nprint(f\"5 * 3 = {triple(5)}\")\nprint(f\"10 * 2 = {double(10)}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 19,
        "question": "递归函数：编写一个递归函数计算阶乘。",
        "options": [],
        "answer": "def factorial(n):\n    if n == 0 or n == 1:\n        return 1\n    else:\n        return n * factorial(n - 1)\n\nprint(f\"5! = {factorial(5)}\")\nprint(f\"10! = {factorial(10)}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 20,
        "question": "递归函数：编写一个递归函数计算斐波那契数列的第n项。",
        "options": [],
        "answer": "def fibonacci(n):\n    if n <= 0:\n        return 0\n    elif n == 1:\n        return 1\n    else:\n        return fibonacci(n - 1) + fibonacci(n - 2)\n\nprint(f\"斐波那契第10项: {fibonacci(10)}\")\nprint(f\"斐波那契第15项: {fibonacci(15)}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 21,
        "question": "递归函数：编写一个递归函数计算列表中所有数字的总和。",
        "options": [],
        "answer": "def recursive_sum(numbers):\n    if not numbers:\n        return 0\n    else:\n        return numbers[0] + recursive_sum(numbers[1:])\n\nprint(f\"[1,2,3,4,5]的和: {recursive_sum([1, 2, 3, 4, 5])}\")\nprint(f\"[10,20,30]的和: {recursive_sum([10, 20, 30])}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 22,
        "question": "递归函数：编写一个递归函数反转字符串。",
        "options": [],
        "answer": "def reverse_string(s):\n    if len(s) <= 1:\n        return s\n    else:\n        return reverse_string(s[1:]) + s[0]\n\nprint(f\"'hello'反转: {reverse_string('hello')}\")\nprint(f\"'python'反转: {reverse_string('python')}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 23,
        "question": "装饰器：创建一个装饰器，记录函数的调用次数。",
        "options": [],
        "answer": "def count_calls(func):\n    def wrapper(*args, **kwargs):\n        wrapper.calls += 1\n        print(f\"{func.__name__}已调用{wrapper.calls}次\")\n        return func(*args, **kwargs)\n    wrapper.calls = 0\n    return wrapper\n\n@count_calls\ndef say_hello():\n    print(\"Hello!\")\n\n@count_calls\ndef add(a, b):\n    return a + b\n\nsay_hello()\nsay_hello()\nadd(2, 3)\nadd(5, 6)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 24,
        "question": "装饰器：创建一个装饰器，计算函数的执行时间。",
        "options": [],
        "answer": "import time\n\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f\"{func.__name__}执行时间: {end - start:.4f}秒\")\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    time.sleep(0.5)\n    print(\"函数执行完毕\")\n\n@timer\ndef calculate_sum(n):\n    return sum(range(n))\n\nslow_function()\ncalculate_sum(1000000)",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 25,
        "question": "装饰器：创建一个装饰器，验证函数参数是否为正数。",
        "options": [],
        "answer": "def validate_positive(func):\n    def wrapper(*args):\n        for arg in args:\n            if not isinstance(arg, (int, float)) or arg <= 0:\n                raise ValueError(f\"参数{arg}必须为正数\")\n        return func(*args)\n    return wrapper\n\n@validate_positive\ndef calculate_area(width, height):\n    return width * height\n\n@validate_positive\ndef calculate_volume(length, width, height):\n    return length * width * height\n\nprint(f\"面积: {calculate_area(5, 10)}\")\nprint(f\"体积: {calculate_volume(2, 3, 4)}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 26,
        "question": "偏函数：使用functools.partial创建一个固定底数为2的幂函数。",
        "options": [],
        "answer": "from functools import partial\n\ndef power(base, exponent):\n    return base ** exponent\n\nsquare = partial(power, base=2)\ncube = partial(power, base=3)\n\nprint(f\"2^3 = {square(3)}\")\nprint(f\"2^5 = {square(5)}\")\nprint(f\"3^4 = {cube(4)}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 27,
        "question": "函数参数总结：编写一个函数，综合使用必需参数、默认参数、可变位置参数和可变关键字参数。",
        "options": [],
        "answer": "def comprehensive_function(required, default=\"默认值\", *args, **kwargs):\n    print(f\"必需参数: {required}\")\n    print(f\"默认参数: {default}\")\n    print(f\"可变位置参数: {args}\")\n    print(f\"可变关键字参数: {kwargs}\")\n\ncomprehensive_function(\"必需值\")\ncomprehensive_function(\"必需值\", \"自定义默认值\", 1, 2, 3, key1=\"value1\", key2=\"value2\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 28,
        "question": "回调函数总结：定义一个通用处理函数，接受数据和处理函数作为回调，对数据进行处理。",
        "options": [],
        "answer": "def process_data(data, processor):\n    return processor(data)\n\ndef uppercase(text):\n    return text.upper()\n\ndef reverse(text):\n    return text[::-1]\n\ndef double(numbers):\n    return [x * 2 for x in numbers]\n\nprint(process_data(\"hello\", uppercase))\nprint(process_data(\"hello\", reverse))\nprint(process_data([1, 2, 3], double))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 29,
        "question": "综合练习：创建一个计算器类，包含加法、减法、乘法、除法方法，并使用lambda表达式作为回调函数。",
        "options": [],
        "answer": "class Calculator:\n    def __init__(self):\n        self.operations = {\n            'add': lambda a, b: a + b,\n            'subtract': lambda a, b: a - b,\n            'multiply': lambda a, b: a * b,\n            'divide': lambda a, b: a / b if b != 0 else None\n        }\n    \n    def calculate(self, operation, a, b):\n        if operation in self.operations:\n            return self.operations[operation](a, b)\n        else:\n            return None\n\ncalc = Calculator()\nprint(f\"5 + 3 = {calc.calculate('add', 5, 3)}\")\nprint(f\"5 - 3 = {calc.calculate('subtract', 5, 3)}\")\nprint(f\"5 * 3 = {calc.calculate('multiply', 5, 3)}\")\nprint(f\"6 / 2 = {calc.calculate('divide', 6, 2)}\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 12,
        "number": 30,
        "question": "综合练习：使用闭包创建一个带有记忆功能的斐波那契函数。",
        "options": [],
        "answer": "def memoized_fibonacci():\n    cache = {}\n    \n    def fibonacci(n):\n        if n <= 0:\n            return 0\n        elif n == 1:\n            return 1\n        elif n in cache:\n            return cache[n]\n        else:\n            result = fibonacci(n - 1) + fibonacci(n - 2)\n            cache[n] = result\n            return result\n    \n    return fibonacci\n\nfib = memoized_fibonacci()\nprint(f\"斐波那契第10项: {fib(10)}\")\nprint(f\"斐波那契第20项: {fib(20)}\")\nprint(f\"斐波那契第30项: {fib(30)}\")",
        "total_order": 0
    }
]

questions = [q for q in questions if q['day'] != 12]
questions.extend(day12_new)

for i, q in enumerate(sorted(questions, key=lambda x: (x['day'], x['number'])), 1):
    q['total_order'] = i

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Day 12 已修复，共30题")