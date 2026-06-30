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
INITIAL_ATTACK = 10
INITIAL_DEFENSE = 5

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
    # 消耗品
    {'id': 'hp_potion_small', 'name': '小型生命药水', 'description': '恢复30点生命值', 'price': 20, 'type': 'consumable', 'effect': {'hp': 30}},
    {'id': 'hp_potion', 'name': '生命药水', 'description': '恢复50点生命值', 'price': 30, 'type': 'consumable', 'effect': {'hp': 50}},
    {'id': 'hp_potion_large', 'name': '大型生命药水', 'description': '恢复100点生命值', 'price': 50, 'type': 'consumable', 'effect': {'hp': 100}},
    {'id': 'attack_boost', 'name': '攻击药剂', 'description': '临时提升20点攻击力（答题减伤）', 'price': 50, 'type': 'consumable', 'effect': {'defense': 10}},
    {'id': 'defense_boost', 'name': '防御药剂', 'description': '临时提升20点防御力（答题减伤）', 'price': 50, 'type': 'consumable', 'effect': {'defense': 20}},
    
    # 装备 - 基础属性
    {'id': 'variable_ring', 'name': '变量戒指', 'description': '永久提升10点攻击力', 'price': 200, 'type': 'equipment', 'slot': 'ring', 'stats': {'attack': 10}},
    {'id': 'function_book', 'name': '函数宝典', 'description': '永久提升15点攻击力', 'price': 300, 'type': 'equipment', 'slot': 'book', 'stats': {'attack': 15}},
    {'id': 'condition_shield', 'name': '条件之盾', 'description': '永久提升20点防御力，答错减伤2点', 'price': 250, 'type': 'equipment', 'slot': 'shield', 'stats': {'defense': 20}, 'damage_reduction': 2},
    {'id': 'loop_boots', 'name': '循环之靴', 'description': '永久提升10点速度', 'price': 150, 'type': 'equipment', 'slot': 'boots', 'stats': {'speed': 10}},
    {'id': 'data_amulet', 'name': '数据护符', 'description': '永久提升15点防御力', 'price': 280, 'type': 'equipment', 'slot': 'amulet', 'stats': {'defense': 15}},
    
    # 装备 - 答题战斗专属
    {'id': 'wisdom_hat', 'name': '智慧之帽', 'description': '答对时额外获得10%经验值', 'price': 350, 'type': 'equipment', 'slot': 'hat', 'exp_bonus': 0.1},
    {'id': 'gold_ring', 'name': '财富戒指', 'description': '答对时额外获得5金币', 'price': 400, 'type': 'equipment', 'slot': 'ring2', 'gold_bonus': 5},
    {'id': 'iron_armor', 'name': '铁甲护身', 'description': '答错时减少3点伤害', 'price': 500, 'type': 'equipment', 'slot': 'armor', 'damage_reduction': 3, 'stats': {'defense': 10}},
    {'id': 'master_cloak', 'name': '大师斗篷', 'description': '答错时减少5点伤害，答对额外10%经验', 'price': 800, 'type': 'equipment', 'slot': 'cloak', 'damage_reduction': 5, 'exp_bonus': 0.1, 'stats': {'defense': 25}},
    {'id': 'hint_scroll', 'name': '提示卷轴', 'description': '每关可查看一次免费提示', 'price': 600, 'type': 'equipment', 'slot': 'scroll', 'hint_count': 1}
]

EQUIPMENT_SLOTS = ['weapon', 'armor', 'shield', 'ring', 'ring2', 'amulet', 'boots', 'book', 'hat', 'cloak', 'scroll']