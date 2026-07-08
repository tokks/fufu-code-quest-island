import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

day7_new = [
    {
        "type": "choice",
        "day": 7,
        "number": 1,
        "question": "1. Python 集合中的元素是有序的吗？",
        "options": ["是的，它们是有序的", "不是的，它们是无序的", "只有在特定情况下才是无序的", "取决于集合的大小"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 7,
        "number": 2,
        "question": "2.以下哪种定义方式，不是元组：",
        "options": ["tuple_01 = (1, 2, 3)", "tuple_02 = ()", "tuple_03 = (4,)", "tuple_04 = tuple([5, 6, 7])", "tuple_05 = (8)"],
        "answer": "E",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 7,
        "number": 3,
        "question": "3. 元组和列表的主要区别是什么？",
        "options": ["元组可以被修改，列表不可以", "列表可以被修改，元组不可以", "元组和列表都可以被修改", "元组和列表都不可以被修改"],
        "answer": "B",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 7,
        "number": 4,
        "question": "4. 假设有一个元组 t = (5, 'a', 3, 'b', 1)，那么 t[2:4] 的结果是什么？",
        "options": ["(3, 'b')", "('a', 3)", "(5, 'a', 3)", "(3, 'b', 1)"],
        "answer": "A",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 7,
        "number": 5,
        "question": "5. 以下哪个操作是元组支持的？（多选）",
        "options": ["索引取值", "切片操作", "元素修改", "元素添加"],
        "answer": "AB",
        "total_order": 0
    },
    {
        "type": "choice",
        "day": 7,
        "number": 6,
        "question": "6. 以下哪个操作是集合支持的？（多选）",
        "options": ["索引取值", "切片操作", "元素修改", "元素添加", "元素删除"],
        "answer": "DE",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 7,
        "number": 7,
        "question": "将规定字符串转为列表后去重：将字符串string = \"abcabcefgg\"转成列表后，去重，并打印排序后的列表。",
        "options": [],
        "answer": "string = \"abcabcefgg\"\nstr_list = []\nfor i in string:\n    str_list.append(i)\nset_list = set(str_list)\nprint(sorted(set_list))",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 7,
        "number": 8,
        "question": "查找元组中最大值及其索引：找出元组tuple_01 = (10, 50, 30, 20, 70, 40)的最大值及其对应的第一个索引并打印。",
        "options": [],
        "answer": "tuple_01 = (10, 50, 30, 20, 70, 40)\nmax_value = tuple_01[0]\nmax_index = 0\nfor i in range(1, len(tuple_01)):\n    if tuple_01[i] > max_value:\n        max_value = tuple_01[i]\n        max_index = i\nprint(\"最大值是:\", max_value, \"，它位于索引\", max_index, \"处。\")",
        "total_order": 0
    },
    {
        "type": "code",
        "day": 7,
        "number": 9,
        "question": "管理动物园的动物特征：定义动物列表，打印每种动物的特征，使用集合找出所有动物最喜欢的不同食物，更新列表增加活力值。",
        "options": [],
        "answer": "animal_list = [(\"狮子\", '金色的', '吃肉'), (\"麻雀\", \"灰色\", \"吃谷子\"), (\"兔子\", \"白色\", \"吃胡萝卜\")]\nfor animal in animal_list:\n    print(\"动物名称：\", animal[0], \",颜色：\", animal[1], \",最喜欢：\", animal[2])\nlove_foods = set()\nfor animal in animal_list:\n    love_foods.add(animal[2])\nprint(\"所有动物最喜欢的不同食物有：\", love_foods)\nupdated_animal_list = []\nfor animal in animal_list:\n    name, color, food = animal\n    energy_level = 1\n    if food == '吃肉':\n        energy_level += 2\n    updated_animal_list.append((name, color, food, energy_level))\nfor animal in updated_animal_list:\n    print(\"动物名称：\", animal[0], \"，颜色：\", animal[1], \"，最喜欢：\", animal[2], \"，活力值:\", animal[3])",
        "total_order": 0
    }
]

questions = [q for q in questions if q['day'] != 7]
questions.extend(day7_new)

for i, q in enumerate(sorted(questions, key=lambda x: (x['day'], x['number'])), 1):
    q['total_order'] = i

with open('exercises.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Day 7 已修复，共9题")