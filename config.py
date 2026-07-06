import os

GAME_VERSION = "1.0.0"
GAME_TITLE = "编程闯关岛"

SAVE_DIR = os.path.join(os.path.dirname(__file__), "saves")
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")

os.makedirs(SAVE_DIR, exist_ok=True)
os.makedirs(ASSETS_DIR, exist_ok=True)

MAX_LEVEL = 50
BASE_EXP_PER_LEVEL = 100
EXP_MULTIPLIER = 1.5

BASE_GOLD_REWARD = 10
GOLD_MULTIPLIER = 1.2

INITIAL_HP = 100
INITIAL_ATTACK = 0
INITIAL_DEFENSE = 0

COLORS = {
    'reset': '\033[0m',
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'underline': '\033[4m'
}

MAP_REGIONS = [
    {'id': 'tutorial', 'name': '新手村', 'description': 'Python大陆的起点，学习基础语法', 'unlocked': True},
    {'id': 'variable_forest', 'name': '变量森林', 'description': '探索变量的奥秘，收集变量戒指', 'unlocked': False},
    {'id': 'function_cave', 'name': '函数洞穴', 'description': '掌握函数的力量，获取函数宝典', 'unlocked': False},
    {'id': 'condition_castle', 'name': '条件城堡', 'description': '运用条件判断，获得条件之盾', 'unlocked': False},
    {'id': 'loop_mountain', 'name': '循环山脉', 'description': '攀登循环的高峰', 'unlocked': False},
    {'id': 'data_ocean', 'name': '数据海洋', 'description': '探索数据结构的深海', 'unlocked': False},
    {'id': 'class_palace', 'name': '类之宫殿', 'description': '面向对象的终极殿堂', 'unlocked': False},
    {'id': 'bug_lair', 'name': 'Bug巢穴', 'description': '最终挑战！击败Bug之王', 'unlocked': False}
]

ACHIEVEMENTS = [
    {'id': 'first_blood', 'name': '初战告捷', 'description': '完成第一个编程任务', 'reward': 50},
    {'id': 'level_10', 'name': '初露锋芒', 'description': '达到10级', 'reward': 100},
    {'id': 'collector', 'name': '装备收藏家', 'description': '收集5件装备', 'reward': 150},
    {'id': 'gold_hunter', 'name': '金币猎人', 'description': '累计获得1000金币', 'reward': 200},
    {'id': 'achievement_master', 'name': '成就大师', 'description': '解锁所有成就', 'reward': 500},
    {'id': 'bug_slayer', 'name': 'Bug杀手', 'description': '击败Bug之王', 'reward': 1000}
]

SHOP_ITEMS = [
    {'id': 'wisdom_hat', 'name': '智慧之帽', 'description': '答对时额外获得10%经验值', 'price': 150, 'type': 'equipment', 'slot': 'hat', 'exp_bonus': 0.1},
    {'id': 'gold_ring', 'name': '财富戒指', 'description': '答对时额外获得5金币', 'price': 100, 'type': 'equipment', 'slot': 'ring', 'gold_bonus': 5},
    {'id': 'iron_armor', 'name': '铁甲护身', 'description': '答错时减少3点伤害', 'price': 200, 'type': 'equipment', 'slot': 'armor', 'damage_reduction': 3, 'stats': {'defense': 10}},
    {'id': 'hint_scroll', 'name': '提示卷轴', 'description': '查看答案时消耗一个', 'price': 50, 'type': 'consumable', 'effect': {'hint': 1}}
]

EQUIPMENT_SLOTS = ['hat', 'ring', 'armor']