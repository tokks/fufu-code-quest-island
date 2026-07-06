import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

enhanced = {
    9: {
        1: "定义一个函数greet(name)，接收一个姓名参数，打印'Hello, '加上姓名并加感叹号。然后调用greet('World')测试。",
        2: "定义一个函数add(a, b)，接收两个参数，返回它们的和。调用add(3, 5)并打印结果。",
        3: "定义一个函数calculate_area(radius)，接收半径参数，返回圆的面积（π取3.14159）。调用函数计算半径为5的圆面积。",
        4: "定义一个函数is_even(num)，接收一个整数参数，返回该数是否为偶数的布尔值。分别传入4和5测试并打印结果。"
    },
    10: {
        1: "创建一个字典student，包含name（张三）、age（18）、score（95）三个键值对。分别打印name和score的值。",
        2: "创建一个字典student，包含name（张三）、age（18）。添加score为95、gender为'男'，然后打印完整字典。",
        3: "创建字典student，包含name、age、score三个键值对。分别使用keys()、values()、items()方法获取并打印所有键、值、键值对。",
        4: "创建字典student，包含name和age。使用in关键字检查'score'是否存在于字典中，如果存在则打印对应值，否则打印提示信息。"
    },
    11: {
        1: "定义一个函数greet(name, message='Hello')，name为必传参数，message有默认值'Hello'。函数打印message加逗号加name加感叹号。调用greet('Alice')和greet('Bob', 'Hi')。",
        2: "定义一个函数add(*args)，使用可变参数接收任意数量的数字，返回它们的总和。调用add(1, 2, 3, 4)并打印结果。",
        3: "使用递归实现一个函数factorial(n)，计算n的阶乘。当n为0或1时返回1，否则返回n乘以factorial(n-1)。调用factorial(5)测试。",
        4: "使用递归实现斐波那契数列函数fibonacci(n)，当n<=1时返回n，否则返回fibonacci(n-1)+fibonacci(n-2)。调用fibonacci(10)测试。",
        5: "创建一个闭包函数make_counter()，内部定义count变量初始为0，返回一个counter函数，每次调用counter()时count加1并返回当前值。",
        6: "使用lambda表达式创建一个匿名函数add，接收两个参数x和y，返回x+y。调用add(3, 5)并打印结果。",
        7: "创建列表numbers = [1, 2, 3, 4, 5]。使用map将每个元素平方，使用filter过滤出偶数，分别打印结果。"
    },
    12: {
        1: "定义一个类Person，包含__init__方法接收name和age参数并赋值给实例属性。创建一个Person实例并打印其属性。",
        2: "定义类Student，包含类属性school='第一中学'，以及__init__方法接收name和grade参数。创建两个实例，修改其中一个的school属性，观察类属性和实例属性的区别。",
        3: "定义类Circle，使用私有属性__radius存储半径。提供get_radius和set_radius方法来访问和修改半径。创建实例并测试方法。",
        4: "定义类Calculator，包含add、subtract、multiply、divide四个方法，分别实现加减乘除运算。创建实例并测试这些方法。"
    },
    13: {
        1: "定义父类Animal，包含speak方法。定义子类Dog继承Animal，重写speak方法使其打印'汪汪汪'。创建Dog实例并调用speak方法。",
        2: "定义父类Person，包含__init__方法接收name参数。定义子类Student继承Person，使用super()调用父类构造方法，并添加grade属性。",
        3: "定义父类Shape，包含area方法返回0。定义子类Rectangle继承Shape，重写area方法计算矩形面积（长×宽）。创建Rectangle实例并调用area。",
        4: "定义类A和类B，都包含show方法。定义类C同时继承A和B，调用C实例的show方法观察MRO（方法解析顺序）。"
    },
    14: {
        1: "定义抽象父类Animal，包含speak方法。定义Dog和Cat子类分别实现speak方法。编写函数make_speak(animal)调用传入对象的speak方法，体现多态性。",
        2: "定义Bird类和Airplane类，都包含fly方法。定义函数let_it_fly(obj)调用fly方法。传入Bird和Airplane实例，演示鸭子类型。",
        3: "定义类A包含method方法打印'A'，类B继承A并重写method打印'B'，类C继承B并重写method打印'C'。创建C实例调用method方法。",
        4: "定义Animal类和Dog类（继承Animal）。创建Dog实例，使用isinstance判断该实例是否为Animal类型和Dog类型。"
    },
    15: {
        1: "定义Person类，实现__str__方法返回'Person: '加上name属性。创建实例并打印，观察输出效果。",
        2: "定义Vector类，包含x和y属性。实现__add__方法，使得两个Vector实例可以使用+运算符相加，返回新的Vector对象。",
        3: "定义Counter类，实现__call__方法，每次调用实例时count加1并返回当前计数。创建实例并多次调用测试。",
        4: "定义MyList类包装一个列表。实现__len__方法返回列表长度，实现__getitem__方法支持索引访问。创建实例测试这些特殊方法。"
    },
    16: {
        1: "使用__new__方法实现单例模式。定义Singleton类，确保无论创建多少次实例，都返回同一个对象。测试创建多个实例并比较它们的id。",
        2: "导入math模块，使用math.pi打印圆周率，使用math.sqrt(16)计算并打印16的平方根。",
        3: "使用from math import pi, sqrt导入特定函数，直接使用pi和sqrt(16)进行计算并打印结果。",
        4: "创建一个模块文件，使用__all__列表控制导出的函数。定义public_function和_private_function，__all__只包含public_function。"
    },
    17: {
        1: "使用with语句打开文件'test.txt'，以写入模式写入'Hello, World!'。确保文件正确关闭。",
        2: "使用with语句打开文件'test.txt'，以读取模式读取全部内容并打印。",
        3: "使用with语句打开文件'test.txt'，以追加模式写入换行符和'Appended content'。",
        4: "使用with语句打开文件'test.txt'，使用readlines()方法逐行读取内容并打印每一行。"
    },
    18: {
        1: "使用正则表达式匹配字符串中的所有数字。定义pattern为匹配一个或多个数字，在文本'abc123def456'中查找所有匹配并打印。",
        2: "使用正则表达式判断字符串是否为纯字母组成。定义pattern匹配以字母开头和结尾的字符串，测试'Hello'和'Hello123'。",
        3: "使用正则表达式替换字符串中的内容。将文本中所有'cat'替换为'dog'，包括'Cats'中的'cat'。",
        4: "使用正则分组提取日期信息。定义pattern匹配YYYY-MM-DD格式的日期，从文本中提取年、月、日并分别打印。"
    },
    19: {
        1: "创建一个装饰器decorator，在函数执行前打印'Before'，执行后打印'After'。使用该装饰器装饰一个简单函数并调用测试。",
        2: "创建一个带参数的装饰器repeat(times)，可以指定函数重复执行的次数。使用@repeat(3)装饰函数，调用时函数将执行3次。",
        3: "创建一个生成器函数generator()，依次yield 1、2、3。获取生成器对象并使用for循环遍历打印每个值。",
        4: "使用生成器表达式创建一个生成器，生成0到9的平方数。使用for循环遍历并打印每个元素。",
        5: "创建一个无限生成器fibonacci()，无限生成斐波那契数列。使用for循环获取前10个值并打印。"
    },
    20: {
        1: "创建一个调试装饰器debug，在函数调用前打印函数名和参数，调用后打印返回值。装饰一个加法函数并测试。",
        2: "创建一个上下文管理器类ErrorHandler，在__enter__方法中返回自身，在__exit__方法中捕获并处理异常。使用with语句测试。",
        3: "编写一个函数process_file(filename)，使用try-except语句处理文件打开异常。当文件不存在时打印友好的错误提示。",
        4: "使用logging模块配置日志输出，设置级别为DEBUG，格式包含时间、级别和消息。分别输出DEBUG、INFO、WARNING级别的日志。",
        5: "完成最终挑战！编写一个综合程序，包含函数、类、异常处理等知识点，实现一个简单的学生成绩管理系统。"
    }
}

for item in data:
    day = item.get('day')
    num = item.get('number')
    if day in enhanced and num in enhanced[day]:
        item['question'] = enhanced[day][num]

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("题目优化完成！")