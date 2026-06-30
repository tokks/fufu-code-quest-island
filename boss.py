import random
import time
from config import COLORS

class BugKing:
    def __init__(self):
        self.name = "Bug之王"
        self.max_hp = 500
        self.hp = 500
        self.attack = 30
        self.defense = 15
        self.phases = [
            {
                'name': '第一阶段 - 语法错误',
                'description': 'Bug之王释放语法错误攻击！',
                'hp_threshold': 500,
                'attack_pattern': 'normal',
                'skills': ['SyntaxError', 'IndentationError']
            },
            {
                'name': '第二阶段 - 逻辑错误',
                'description': 'Bug之王变得更强大了！',
                'hp_threshold': 300,
                'attack_pattern': 'double',
                'skills': ['LogicError', 'RuntimeError']
            },
            {
                'name': '第三阶段 - 致命错误',
                'description': 'Bug之王进入狂暴状态！',
                'hp_threshold': 100,
                'attack_pattern': 'triple',
                'skills': ['FatalError', 'SystemCrash']
            }
        ]
        self.current_phase = 0
        self.skill_descriptions = {
            'SyntaxError': '让你的代码无法运行！',
            'IndentationError': '打乱你的代码缩进！',
            'LogicError': '让你的逻辑出现漏洞！',
            'RuntimeError': '在运行时发生错误！',
            'FatalError': '致命错误！',
            'SystemCrash': '系统崩溃！'
        }

    def get_current_phase(self):
        for i, phase in enumerate(self.phases):
            if self.hp <= phase['hp_threshold']:
                self.current_phase = i
                return phase
        return self.phases[0]

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        
        new_phase = self.get_current_phase()
        if new_phase != self.phases[self.current_phase]:
            self.current_phase = self.phases.index(new_phase)
            return actual_damage, True, new_phase
        
        return actual_damage, False, None

    def attack_player(self, player):
        phase = self.get_current_phase()
        damage = self.attack
        skill = random.choice(phase['skills'])
        
        if phase['attack_pattern'] == 'double':
            damage *= 1.5
        elif phase['attack_pattern'] == 'triple':
            damage *= 2
        
        damage = int(damage + random.randint(-5, 10))
        actual_damage = player.take_damage(damage)
        
        return {
            'skill': skill,
            'description': self.skill_descriptions[skill],
            'damage': actual_damage,
            'phase': phase['name']
        }

    def is_alive(self):
        return self.hp > 0

    def get_hp_percentage(self):
        return (self.hp / self.max_hp) * 100

    def display_hp_bar(self):
        bar_length = 30
        percentage = self.get_hp_percentage()
        filled = int(bar_length * percentage / 100)
        
        bar = f"{'█' * filled}{'░' * (bar_length - filled)}"
        print(f"\n{COLORS['red']}{self.name}{COLORS['reset']} HP: {bar} {self.hp}/{self.max_hp}")

class BossBattle:
    def __init__(self, player, game_state, level_manager):
        self.player = player
        self.game_state = game_state
        self.level_manager = level_manager
        self.boss = BugKing()
        self.battle_log = []

    def start_battle(self):
        print(f"\n{COLORS['bold']}{COLORS['red']}=== BOSS战开始 ==={COLORS['reset']}")
        print(f"你面对的是 {COLORS['bold']}{COLORS['red']}{self.boss.name}{COLORS['reset']}！")
        print("只有修复所有Bug才能击败它！")
        
        time.sleep(2)
        
        while self.player.is_alive() and self.boss.is_alive():
            self.boss.display_hp_bar()
            self.display_player_status()
            
            action = self.get_player_action()
            
            if action == 'attack':
                self.player_attack()
            elif action == 'skill':
                self.use_skill()
            elif action == 'item':
                self.use_item()
            elif action == 'retreat':
                print("你选择了撤退...")
                return False
            
            if self.boss.is_alive():
                self.boss_turn()
            
            time.sleep(1)
        
        if self.player.is_alive() and not self.boss.is_alive():
            self.victory()
            return True
        else:
            self.defeat()
            return False

    def get_player_action(self):
        print(f"\n{COLORS['bold']}选择行动:{COLORS['reset']}")
        print("1. 攻击")
        print("2. 使用技能")
        print("3. 使用物品")
        print("4. 撤退")
        
        while True:
            choice = input("请输入选择 (1-4): ")
            if choice in ['1', '2', '3', '4']:
                return ['attack', 'skill', 'item', 'retreat'][int(choice) - 1]
            print("无效选择，请重新输入")

    def player_attack(self):
        damage = self.player.get_total_attack() + random.randint(-3, 8)
        actual_damage, phase_changed, new_phase = self.boss.take_damage(damage)
        
        print(f"\n{COLORS['green']}你对 {self.boss.name} 造成了 {actual_damage} 点伤害！{COLORS['reset']}")
        
        if phase_changed and new_phase:
            print(f"\n{COLORS['red']}{new_phase['description']}{COLORS['reset']}")
            print(f"进入 {new_phase['name']}！")

    def use_skill(self):
        print(f"\n{COLORS['bold']}可用技能:{COLORS['reset']}")
        print("1. 代码修复 - 造成大量伤害")
        print("2. 防御模式 - 提升防御力")
        
        choice = input("请输入选择 (1-2): ")
        
        if choice == '1':
            damage = self.player.get_total_attack() * 2 + random.randint(0, 20)
            actual_damage, _, _ = self.boss.take_damage(damage)
            print(f"\n{COLORS['cyan']}你使用了【代码修复】！{COLORS['reset']}")
            print(f"对 {self.boss.name} 造成了 {actual_damage} 点伤害！")
        
        elif choice == '2':
            temp_defense = 20
            self.player.defense += temp_defense
            print(f"\n{COLORS['blue']}你使用了【防御模式】！{COLORS['reset']}")
            print(f"防御力提升 {temp_defense} 点！")
            time.sleep(1)
            self.player.defense -= temp_defense
            print(f"防御模式结束，防御力恢复正常")

    def use_item(self):
        if not self.player.inventory:
            print("背包是空的！")
            return
        
        print(f"\n{COLORS['bold']}背包物品:{COLORS['reset']}")
        for i, item in enumerate(self.player.inventory, 1):
            print(f"{i}. {item['name']}")
        
        choice = input("请选择物品 (输入序号): ")
        
        try:
            index = int(choice) - 1
            if 0 <= index < len(self.player.inventory):
                item = self.player.inventory[index]
                if self.player.use_consumable(item['id']):
                    print(f"使用了 {item['name']}！")
                else:
                    print("无法使用该物品")
            else:
                print("无效选择")
        except ValueError:
            print("无效输入")

    def boss_turn(self):
        result = self.boss.attack_player(self.player)
        
        print(f"\n{COLORS['red']}{self.boss.name} 使用了【{result['skill']}】！{COLORS['reset']}")
        print(f"{result['description']}")
        print(f"对你造成了 {result['damage']} 点伤害！")

    def display_player_status(self):
        hp_percentage = (self.player.hp / self.player.max_hp) * 100
        bar_length = 20
        filled = int(bar_length * hp_percentage / 100)
        
        bar = f"{'█' * filled}{'░' * (bar_length - filled)}"
        print(f"\n{COLORS['green']}{self.player.name}{COLORS['reset']} HP: {bar} {self.player.hp}/{self.player.max_hp}")
        print(f"攻击力: {self.player.attack} | 防御力: {self.player.defense}")

    def victory(self):
        print(f"\n{COLORS['bold']}{COLORS['yellow']}=== 胜利！ ==={COLORS['reset']}")
        print(f"你成功击败了 {COLORS['bold']}{COLORS['red']}{self.boss.name}{COLORS['reset']}！")
        print("恭喜你成为了真正的编程大师！")
        
        exp_reward = 500
        gold_reward = 200
        
        print(f"\n获得奖励:")
        print(f"经验值: {exp_reward}")
        print(f"金币: {gold_reward}")
        
        self.player.add_exp(exp_reward)
        self.player.add_gold(gold_reward)
        self.game_state.complete_quest('bug_1')
        self.game_state.add_gold_earned(gold_reward)
        
        self.game_state.unlock_region('bug_lair')

    def defeat(self):
        print(f"\n{COLORS['bold']}{COLORS['red']}=== 失败 ==={COLORS['reset']}")
        print("你被Bug之王击败了...")
        print("不要灰心，提升等级和装备后再来挑战！")
        
        self.player.hp = max(1, self.player.hp)

def start_boss_battle(player, game_state, level_manager):
    battle = BossBattle(player, game_state, level_manager)
    return battle.start_battle()