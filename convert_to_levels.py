import json

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

region_mapping = {
    1: {'id': 'region_1', 'name': '新手村', 'description': 'Python基础概念与PyCharm使用', 'icon': 'fa-house'},
    2: {'id': 'region_2', 'name': '变量森林', 'description': '字面量、变量、字符串和数字', 'icon': 'fa-tree'},
    3: {'id': 'region_3', 'name': '数据洞穴', 'description': '转义字符、布尔类型、逻辑判断', 'icon': 'fa-cave'},
    4: {'id': 'region_4', 'name': '条件城堡', 'description': '条件判断、运算与优先级', 'icon': 'fa-castle'},
    5: {'id': 'region_5', 'name': '循环山脉', 'description': 'for循环与while循环', 'icon': 'fa-mountain'},
    6: {'id': 'region_6', 'name': '列表森林', 'description': '数据结构之列表', 'icon': 'fa-list'},
    7: {'id': 'region_7', 'name': '集合岛屿', 'description': '数据结构之集合与元组', 'icon': 'fa-circle'},
    8: {'id': 'region_8', 'name': '函数殿堂', 'description': '函数定义与使用', 'icon': 'fa-book'},
    9: {'id': 'region_9', 'name': '迭代器谷', 'description': '迭代器和常用函数', 'icon': 'fa-repeat'},
    10: {'id': 'region_10', 'name': '字典王国', 'description': '字典、深拷贝与浅拷贝', 'icon': 'fa-book-open'},
    11: {'id': 'region_11', 'name': '函数进阶', 'description': '函数参数与返回值', 'icon': 'fa-code'},
    12: {'id': 'region_12', 'name': '函数深化', 'description': '递归、闭包、匿名函数', 'icon': 'fa-code-branch'},
    13: {'id': 'region_13', 'name': '面向对象', 'description': '类与对象', 'icon': 'fa-object-group'},
    14: {'id': 'region_14', 'name': '继承之城', 'description': '类的继承与重写', 'icon': 'fa-sitemap'},
    15: {'id': 'region_15', 'name': '多态之塔', 'description': '多继承、多态和鸭子类型', 'icon': 'fa-layer-group'},
    16: {'id': 'region_16', 'name': '魔法之屋', 'description': '魔法方法', 'icon': 'fa-sparkles'},
    17: {'id': 'region_17', 'name': '单例秘境', 'description': '单例模式与模块', 'icon': 'fa-key'},
    18: {'id': 'region_18', 'name': '文件港湾', 'description': '文件操作', 'icon': 'fa-file'},
    19: {'id': 'region_19', 'name': '正则海域', 'description': '正则表达式', 'icon': 'fa-search'},
    20: {'id': 'region_20', 'name': '装饰器峰', 'description': '装饰器与生成器', 'icon': 'fa-gem'},
    21: {'id': 'region_21', 'name': 'Bug巢穴', 'description': '最终挑战！击败Bug之王', 'icon': 'fa-skull'}
}

regions = []

for day in range(1, 22):
    day_questions = [q for q in questions if q['day'] == day]
    
    if not day_questions:
        print(f"Day {day}: 没有题目")
        continue
    
    if day not in region_mapping:
        region_info = {
            'id': f'region_{day}',
            'name': f'第{day}天区域',
            'description': f'第{day}天学习内容',
            'icon': 'fa-question-circle'
        }
    else:
        region_info = region_mapping[day]
    
    levels = []
    for q in day_questions:
        level_id = f"day{day}_q{q['number']}"
        
        if q['type'] == 'choice':
            level = {
                'id': level_id,
                'name': f"第{q['number']}题",
                'description': q['question'][:50] + '...',
                'difficulty': '简单',
                'exp_reward': 20,
                'gold_reward': 10,
                'question': q['question'],
                'type': 'choice',
                'options': q['options'],
                'answer': q['answer'],
                'hints': ['选择正确的选项'],
                'code_template': '',
                'solution': q['answer']
            }
        else:
            answer_code = q['answer'] if q['answer'] else ''
            
            if answer_code:
                first_line = answer_code.split('\n')[0].strip()
                if first_line.startswith('print'):
                    template = first_line[:-1] if first_line.endswith(')') else first_line
                elif '=' in first_line:
                    parts = first_line.split('=', 1)
                    template = parts[0].strip() + ' = '
                elif first_line.startswith('def'):
                    template = first_line + '\n    '
                else:
                    template = ''
            else:
                template = ''
            
            level = {
                'id': level_id,
                'name': f"第{q['number']}题",
                'description': q['question'][:50] + '...',
                'difficulty': '中等',
                'exp_reward': 50,
                'gold_reward': 25,
                'question': q['question'],
                'type': 'code',
                'options': [],
                'answer': answer_code,
                'hints': ['编写正确的Python代码'],
                'code_template': template,
                'solution': answer_code
            }
        
        levels.append(level)
    
    region = {
        'id': region_info['id'],
        'name': region_info['name'],
        'description': region_info['description'],
        'icon': region_info['icon'],
        'levels': levels
    }
    
    regions.append(region)

output_content = '''import json

REGIONS = ''' + json.dumps(regions, ensure_ascii=False, indent=4) + '''

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
    return REGIONS'''

with open('levels_new.py', 'w', encoding='utf-8') as f:
    f.write(output_content)

print(f"转换完成！")
print(f"总区域数: {len(regions)}")
total_levels = sum(len(r['levels']) for r in regions)
print(f"总关卡数: {total_levels}")