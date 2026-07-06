import json
import copy

REGIONS = [
    {
        "id": "region_1",
        "name": "新手村",
        "description": "Python基础概念与PyCharm使用",
        "icon": "fa-house",
        "levels": []
    },
    {
        "id": "region_2",
        "name": "变量森林",
        "description": "字面量、变量、字符串和数字",
        "icon": "fa-tree",
        "levels": []
    },
    {
        "id": "region_3",
        "name": "数据洞穴",
        "description": "转义字符、布尔类型、逻辑判断",
        "icon": "fa-cave",
        "levels": []
    },
    {
        "id": "region_4",
        "name": "条件城堡",
        "description": "条件判断、运算与优先级",
        "icon": "fa-castle",
        "levels": []
    },
    {
        "id": "region_5",
        "name": "循环山脉",
        "description": "for循环与while循环",
        "icon": "fa-mountain",
        "levels": []
    },
    {
        "id": "region_6",
        "name": "列表森林",
        "description": "数据结构之列表",
        "icon": "fa-list",
        "levels": []
    },
    {
        "id": "region_7",
        "name": "集合岛屿",
        "description": "数据结构之集合与元组",
        "icon": "fa-circle",
        "levels": []
    },
    {
        "id": "region_8",
        "name": "函数殿堂",
        "description": "函数定义与使用",
        "icon": "fa-book",
        "levels": []
    },
    {
        "id": "region_9",
        "name": "迭代器谷",
        "description": "迭代器和常用函数",
        "icon": "fa-repeat",
        "levels": []
    },
    {
        "id": "region_10",
        "name": "字典王国",
        "description": "字典、深拷贝与浅拷贝",
        "icon": "fa-book-open",
        "levels": []
    },
    {
        "id": "region_11",
        "name": "函数进阶",
        "description": "函数参数、返回值、递归、闭包与匿名函数",
        "icon": "fa-code",
        "levels": []
    },
    {
        "id": "region_12",
        "name": "面向对象",
        "description": "类与对象",
        "icon": "fa-object-group",
        "levels": []
    },
    {
        "id": "region_13",
        "name": "继承之城",
        "description": "类的继承与重写",
        "icon": "fa-sitemap",
        "levels": []
    },
    {
        "id": "region_14",
        "name": "多态之塔",
        "description": "多继承、多态和鸭子类型",
        "icon": "fa-layer-group",
        "levels": []
    },
    {
        "id": "region_15",
        "name": "魔法之屋",
        "description": "魔法方法",
        "icon": "fa-sparkles",
        "levels": []
    },
    {
        "id": "region_16",
        "name": "单例秘境",
        "description": "单例模式与模块",
        "icon": "fa-key",
        "levels": []
    },
    {
        "id": "region_17",
        "name": "文件港湾",
        "description": "文件操作",
        "icon": "fa-file",
        "levels": []
    },
    {
        "id": "region_18",
        "name": "正则海域",
        "description": "正则表达式",
        "icon": "fa-search",
        "levels": []
    },
    {
        "id": "region_19",
        "name": "装饰器峰",
        "description": "装饰器与生成器",
        "icon": "fa-gem",
        "levels": []
    },
    {
        "id": "region_20",
        "name": "Bug巢穴",
        "description": "最终挑战！击败Bug之王",
        "icon": "fa-skull",
        "levels": []
    }
]

with open('exercises.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for region in REGIONS:
    day = int(region['id'].split('_')[1])
    day_questions = [q for q in questions if q['day'] == day]
    
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
            template = q.get('code_template', '')
            
            if not template:
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
        
        region['levels'].append(level)

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
    return REGIONS

def load_all_levels():
    regions = copy.deepcopy(REGIONS)
    for i, region in enumerate(regions):
        region['levels'] = []
        region['id'] = f"day{i + 1}"
    
    with open('exercises.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)
    
    for region in regions:
        day = int(region['id'].replace('day', ''))
        day_questions = [q for q in questions if q['day'] == day]
        
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
                template = q.get('code_template', '')
                
                if not template:
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
            
            region['levels'].append(level)
    
    return regions

class LevelManager:
    def __init__(self):
        self.regions = load_all_levels()
    
    def reload(self):
        self.regions = load_all_levels()
    
    def get_region_by_id(self, region_id):
        for region in self.regions:
            if region['id'] == region_id:
                return region
        return None
    
    def get_level_by_id(self, region_id, level_id):
        region = self.get_region_by_id(region_id)
        if region:
            for level in region['levels']:
                if level['id'] == level_id:
                    return level
        return None
    
    def get_all_regions(self):
        return self.regions
    
    def get_levels_for_region(self, region_id):
        region = self.get_region_by_id(region_id)
        return region['levels'] if region else []
    
    def get_next_region(self, region_id):
        current_index = None
        for i, region in enumerate(self.regions):
            if region['id'] == region_id:
                current_index = i
                break
        
        if current_index is not None and current_index < len(self.regions) - 1:
            return self.regions[current_index + 1]['id']
        return None
    
    def get_level(self, region_id, level_id):
        return self.get_level_by_id(region_id, level_id)
    
    def get_progress(self, game_state):
        progress = []
        is_admin = game_state.player.is_admin if game_state.player else False
        
        for region in self.regions:
            total_levels = len(region['levels'])
            completed_levels = sum(1 for level in region['levels'] 
                                   if level['id'] in game_state.completed_quests)
            
            is_unlocked = is_admin or (region['id'] in game_state.unlocked_regions)
            
            progress.append({
                'region': region,
                'is_unlocked': is_unlocked,
                'total_levels': total_levels,
                'completed_levels': completed_levels,
                'is_admin': is_admin
            })
        return progress
    
    def normalize_code(self, code):
        lines = code.strip().split('\n')
        normalized_lines = []
        
        for line in lines:
            line = line.strip()
            
            if '=' in line and '==' not in line:
                parts = line.split('=', 1)
                left = parts[0].strip()
                right = parts[1].strip()
                
                if right:
                    if right[0] in '"\'' and right[-1] in '"\'' and len(right) > 1:
                        normalized_lines.append(f"{left}={right}")
                    else:
                        try:
                            if '.' in right:
                                normalized_lines.append(f"{left}={float(right)}")
                            else:
                                normalized_lines.append(f"{left}={int(right)}")
                        except ValueError:
                            normalized_lines.append(f"{left}={right}")
                else:
                    normalized_lines.append(line)
            else:
                normalized_lines.append(line)
        
        return '\n'.join(normalized_lines)
    
    def remove_all_spaces(self, code):
        result = []
        i = 0
        while i < len(code):
            if code[i] in '"\'':
                quote = code[i]
                result.append(quote)
                i += 1
                while i < len(code) and code[i] != quote:
                    result.append(code[i])
                    i += 1
                if i < len(code):
                    result.append(quote)
                    i += 1
            else:
                if code[i] != ' ':
                    result.append(code[i])
                i += 1
        return ''.join(result)
    
    def check_answer(self, level, user_answer):
        if not user_answer or not user_answer.strip():
            return False
        
        user_answer = user_answer.strip()
        
        if level.get('type') == 'choice':
            correct_answer = level.get('answer', '')
            user_answer_clean = user_answer.strip().upper()
            
            if user_answer_clean == correct_answer.upper():
                return True
            
            options = level.get('options', [])
            for opt in options:
                opt_upper = opt.upper()
                if opt_upper.startswith(correct_answer.upper() + '.') or opt_upper.startswith(correct_answer.upper() + ')'):
                    if opt_upper.startswith(user_answer_clean + '.') or opt_upper.startswith(user_answer_clean + ')'):
                        return True
            
            return False
        
        correct_answer = level.get('answer', '')
        
        normalized_correct = self.normalize_code(correct_answer)
        normalized_user = self.normalize_code(user_answer)
        
        if normalized_correct == normalized_user:
            return True
        
        correct_no_space = self.remove_all_spaces(correct_answer)
        user_no_space = self.remove_all_spaces(user_answer)
        
        if correct_no_space == user_no_space:
            return True
        
        try:
            compile(user_answer, '<string>', 'exec')
        except SyntaxError:
            return False
        
        try:
            correct_vars = {}
            user_vars = {}
            
            correct_code = correct_answer
            user_code = user_answer
            
            if 'input()' in correct_code or 'input()' in user_code:
                test_input = '123.45'
                correct_code = correct_code.replace('input()', repr(test_input))
                user_code = user_code.replace('input()', repr(test_input))
            
            exec(correct_code, {}, correct_vars)
            exec(user_code, {}, user_vars)
            
            if level.get('type_check'):
                for var_name in correct_vars:
                    if var_name not in user_vars:
                        return False
                    if type(correct_vars[var_name]) != type(user_vars[var_name]):
                        return False
                return True
            
            if correct_vars == user_vars:
                return True
            
            for func_name in correct_vars:
                if func_name not in user_vars:
                    continue
                
                correct_func = correct_vars[func_name]
                user_func = user_vars[func_name]
                
                if callable(correct_func) and callable(user_func):
                    import inspect
                    
                    correct_sig = inspect.signature(correct_func)
                    user_sig = inspect.signature(user_func)
                    
                    if correct_sig == user_sig:
                        correct_params = correct_sig.parameters
                        user_params = user_sig.parameters
                        
                        match = True
                        for name, param in correct_params.items():
                            if name not in user_params:
                                match = False
                                break
                            if param.default != user_params[name].default:
                                match = False
                                break
                        
                        if match:
                            return True
                    
                    try:
                        test_args = []
                        for param in correct_sig.parameters.values():
                            if param.default is inspect.Parameter.empty:
                                test_args.append(10)
                            else:
                                test_args.append(param.default)
                        
                        correct_result = correct_func(*test_args)
                        user_result = user_func(*test_args)
                        
                        if correct_result == user_result:
                            return True
                    except:
                        pass
        except:
            pass
        
        lines_correct = [l.strip() for l in correct_answer.split('\n') if l.strip()]
        lines_user = [l.strip() for l in user_answer.split('\n') if l.strip()]
        
        if len(lines_correct) == len(lines_user):
            all_match = True
            for lc, lu in zip(lines_correct, lines_user):
                if self.remove_all_spaces(lc) != self.remove_all_spaces(lu):
                    all_match = False
                    break
            if all_match:
                return True
        
        try:
            correct_output = self.capture_output(correct_answer)
            user_output = self.capture_output(user_answer)
            
            if correct_output.strip() and correct_output.strip() == user_output.strip():
                return True
            
            correct_lines = [l.strip() for l in correct_output.strip().split('\n') if l.strip()]
            user_lines = [l.strip() for l in user_output.strip().split('\n') if l.strip()]
            
            if correct_lines == user_lines:
                return True
        except:
            pass
        
        try:
            correct_vars = {}
            user_vars = {}
            
            correct_code = correct_answer
            user_code = user_answer
            
            if 'input()' in correct_code or 'input()' in user_code:
                test_input = '123.45'
                correct_code = correct_code.replace('input()', repr(test_input))
                user_code = user_code.replace('input()', repr(test_input))
            
            exec(correct_code, {}, correct_vars)
            exec(user_code, {}, user_vars)
            
            correct_values = sorted([(type(v).__name__, v) for k, v in correct_vars.items() if not k.startswith('_')], key=lambda x: str(x))
            user_values = sorted([(type(v).__name__, v) for k, v in user_vars.items() if not k.startswith('_')], key=lambda x: str(x))
            
            if correct_values == user_values:
                return True
            
            if len(correct_values) > 0 and len(correct_values) == len(user_values):
                match = True
                for (correct_type, correct_val), (user_type, user_val) in zip(correct_values, user_values):
                    if correct_type != user_type:
                        match = False
                        break
                    try:
                        if correct_val != user_val:
                            match = False
                            break
                    except:
                        match = False
                        break
                if match:
                    return True
            
            correct_values_no_type = sorted([str(v) for k, v in correct_vars.items() if not k.startswith('_')])
            user_values_no_type = sorted([str(v) for k, v in user_vars.items() if not k.startswith('_')])
            
            if set(correct_values_no_type).issubset(set(user_values_no_type)) or set(user_values_no_type).issubset(set(correct_values_no_type)):
                return True
            
            correct_numeric = []
            user_numeric = []
            for k, v in correct_vars.items():
                if not k.startswith('_'):
                    try:
                        correct_numeric.append(float(v))
                    except:
                        correct_numeric.append(str(v))
            for k, v in user_vars.items():
                if not k.startswith('_'):
                    try:
                        user_numeric.append(float(v))
                    except:
                        user_numeric.append(str(v))
            
            correct_numeric_sorted = sorted(correct_numeric)
            user_numeric_sorted = sorted(user_numeric)
            
            if correct_numeric_sorted == user_numeric_sorted:
                return True
            
            if len(correct_numeric) > 0 and len(user_numeric) > 0:
                common_values = set(correct_numeric).intersection(set(user_numeric))
                if len(common_values) >= min(len(correct_numeric), len(user_numeric)):
                    return True
        except:
            pass
        
        return False
    
    def capture_output(self, code):
        import sys
        from io import StringIO
        
        old_stdout = sys.stdout
        sys.stdout = captured_output = StringIO()
        
        try:
            if 'input()' in code:
                test_inputs = ['123.45', '3.14', '100', '0.5']
                
                for test_input in test_inputs:
                    code_with_input = code.replace('input()', repr(test_input))
                    try:
                        exec(code_with_input, {})
                    except Exception:
                        pass
            else:
                exec(code, {})
        except Exception:
            pass
        
        sys.stdout = old_stdout
        return captured_output.getvalue()