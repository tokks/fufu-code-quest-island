import os
import time
from config import COLORS, MAP_REGIONS, EQUIPMENT_SLOTS
from game_state import GameState
from player import Player
from levels import LevelManager
from quests import QuestManager
from shop import Shop
from achievements import AchievementManager
from boss import start_boss_battle

class Game:
    def __init__(self):
        self.game_state = None
        self.player = None
        self.level_manager = LevelManager()
        self.quest_manager = QuestManager()
        self.shop = Shop()
        self.achievement_manager = AchievementManager()
        self.is_running = True

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_title(self):
        title = """
    ██████╗██╗     ██╗███████╗███████╗██████╗     ██████╗  █████╗ ███╗   ███╗███████╗
    ██╔════╝██║     ██║██╔════╝██╔════╝██╔══██╗    ██╔══██╗██╔══██╗████╗ ████║██╔════╝
    ██║     ██║     ██║█████╗  ███████╗██████╔╝    ██████╔╝███████║██╔████╔██║█████╗  
    ██║     ██║     ██║██╔══╝  ╚════██║██╔═══╝     ██╔═══╝ ██╔══██║██║╚██╔╝██║██╔══╝  
    ╚██████╗███████╗██║███████╗███████║██║         ██║     ██║  ██║██║ ╚═╝ ██║███████╗
     ╚═════╝╚══════╝╚═╝╚══════╝╚══════╝╚═╝         ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
        """
        print(f"{COLORS['cyan']}{title}{COLORS['reset']}")
        print(f"{COLORS['yellow']}                     游戏化编程学习项目{COLORS['reset']}")
        print(f"{COLORS['yellow']}                        Version 1.0.0{COLORS['reset']}")

    def main_menu(self):
        self.clear_screen()
        self.print_title()
        
        print(f"\n{COLORS['bold']}=== 主菜单 ==={COLORS['reset']}")
        print("1. 新游戏")
        print("2. 继续游戏")
        print("3. 退出游戏")
        
        while True:
            choice = input("\n请输入选择 (1-3): ")
            
            if choice == '1':
                self.start_new_game()
                break
            elif choice == '2':
                if self.load_game():
                    self.game_loop()
                else:
                    print("没有找到存档文件")
                    time.sleep(2)
            elif choice == '3':
                self.is_running = False
                print("感谢游玩编程闯关岛！")
                break
            else:
                print("无效选择，请重新输入")

    def start_new_game(self):
        self.clear_screen()
        self.print_title()
        
        print(f"\n{COLORS['bold']}=== 创建新角色 ==={COLORS['reset']}")
        name = input("请输入你的冒险者名字: ")
        
        if not name.strip():
            name = "冒险者"
        
        self.player = Player(name.strip())
        self.game_state = GameState()
        self.game_state.player = self.player
        
        print(f"\n欢迎来到编程闯关岛，{COLORS['bold']}{COLORS['green']}{self.player.name}{COLORS['reset']}！")
        print("你的冒险即将开始...")
        time.sleep(2)
        
        self.game_loop()

    def load_game(self):
        self.game_state = GameState.load_game()
        
        if self.game_state:
            save_data = self.game_state.to_dict()
            if self.game_state.player:
                self.player = Player.from_dict(self.game_state.player)
            return True
        
        return False

    def save_game(self):
        if self.game_state and self.player:
            self.game_state.player = self.player
            save_path = self.game_state.save_game()
            print(f"游戏已保存到: {save_path}")
            return True
        return False

    def game_loop(self):
        while self.is_running:
            self.clear_screen()
            self.print_title()
            
            print(f"\n{COLORS['bold']}=== 游戏主界面 ==={COLORS['reset']}")
            print(f"角色: {COLORS['green']}{self.player.name}{COLORS['reset']} | 等级: {COLORS['yellow']}{self.player.level}{COLORS['reset']}")
            print(f"经验值: {self.player.exp}/{self.player.get_exp_needed()} | 金币: {COLORS['yellow']}{self.player.gold}{COLORS['reset']}")
            print(f"生命值: {self.player.hp}/{self.player.max_hp}")
            print(f"攻击力: {self.player.attack} | 防御力: {self.player.defense}")
            
            print(f"\n{COLORS['bold']}选择操作:{COLORS['reset']}")
            print("1. 世界地图")
            print("2. 角色信息")
            print("3. 背包")
            print("4. 任务")
            print("5. 商城")
            print("6. 成就")
            print("7. 保存游戏")
            print("8. 返回主菜单")
            
            choice = input("\n请输入选择 (1-8): ")
            
            if choice == '1':
                self.world_map()
            elif choice == '2':
                self.character_info()
            elif choice == '3':
                self.inventory()
            elif choice == '4':
                self.quests()
            elif choice == '5':
                self.shop_menu()
            elif choice == '6':
                self.achievements()
            elif choice == '7':
                self.save_game()
                time.sleep(2)
            elif choice == '8':
                break
            else:
                print("无效选择，请重新输入")
                time.sleep(1)

    def world_map(self):
        self.clear_screen()
        print(f"{COLORS['bold']}{COLORS['cyan']}=== 世界地图 ==={COLORS['reset']}")
        
        progress = self.level_manager.get_progress(self.game_state)
        
        for i, region_data in enumerate(progress, 1):
            region = region_data['region']
            
            if region_data['is_unlocked']:
                status = f"{COLORS['green']}已解锁{COLORS['reset']}"
                completed = region_data['completed_levels']
                total = region_data['total_levels']
                progress_str = f" ({completed}/{total} 任务)"
            else:
                status = f"{COLORS['red']}未解锁{COLORS['reset']}"
                progress_str = ""
            
            print(f"\n{i}. {region['name']}")
            print(f"   状态: {status}{progress_str}")
            print(f"   {region['description']}")
        
        print(f"\n0. 返回")
        
        while True:
            choice = input("\n请选择区域 (输入序号): ")
            
            if choice == '0':
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(progress):
                    region_data = progress[index]
                    if region_data['is_unlocked']:
                        self.region_menu(region_data['region'])
                        break
                    else:
                        print("该区域尚未解锁")
                        time.sleep(1)
                else:
                    print("无效选择")
            except ValueError:
                print("无效输入")

    def region_menu(self, region):
        while True:
            self.clear_screen()
            print(f"{COLORS['bold']}{COLORS['cyan']}=== {region['name']} ==={COLORS['reset']}")
            print(f"{region['description']}")
            
            levels = self.level_manager.get_levels_for_region(region['id'])
            
            print(f"\n{COLORS['bold']}关卡列表:{COLORS['reset']}")
            for i, level in enumerate(levels, 1):
                status = COLORS['green'] + "已完成" + COLORS['reset'] if level['id'] in self.game_state.completed_quests else COLORS['yellow'] + "未完成" + COLORS['reset']
                print(f"{i}. {level['name']} - {level['difficulty']}")
                print(f"   状态: {status}")
            
            print(f"\n0. 返回")
            
            choice = input("\n请选择关卡 (输入序号): ")
            
            if choice == '0':
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(levels):
                    level = levels[index]
                    if level['id'] in self.game_state.completed_quests:
                        print("该关卡已完成")
                        time.sleep(1)
                    else:
                        self.play_level(region, level)
                else:
                    print("无效选择")
                    time.sleep(1)
            except ValueError:
                print("无效输入")
                time.sleep(1)

    def play_level(self, region, level):
        self.clear_screen()
        print(f"{COLORS['bold']}{COLORS['purple']}=== {level['name']} ==={COLORS['reset']}")
        print(f"区域: {region['name']}")
        print(f"难度: {level['difficulty']}")
        print(f"\n任务描述:")
        print(f"{level['description']}")
        print(f"\n问题:")
        print(f"{level['question']}")
        
        if level.get('code_template'):
            print(f"\n代码模板:")
            print(f"{level['code_template']}")
        
        attempts = 3
        
        while attempts > 0:
            print(f"\n剩余尝试次数: {attempts}")
            user_answer = input("请输入你的答案: ")
            
            if self.level_manager.check_answer(level, user_answer):
                print(f"\n{COLORS['green']}{COLORS['bold']}✓ 回答正确！{COLORS['reset']}")
                print(f"获得 {level['exp_reward']} 经验值，{level['gold_reward']} 金币")
                
                self.player.add_exp(level['exp_reward'])
                self.player.add_gold(level['gold_reward'])
                self.game_state.complete_quest(level['id'])
                self.game_state.add_gold_earned(level['gold_reward'])
                
                newly_unlocked = self.achievement_manager.check_achievements(self.game_state, self.player)
                if newly_unlocked:
                    print(f"\n{COLORS['yellow']}{COLORS['bold']}解锁新成就！{COLORS['reset']}")
                    for achievement in newly_unlocked:
                        print(f"- {achievement['name']}: {achievement['reward']} 金币")
                
                self.check_region_completion(region)
                
                time.sleep(3)
                return
            else:
                attempts -= 1
                print(f"\n{COLORS['red']}✗ 回答错误{COLORS['reset']}")
                
                if attempts > 0 and level.get('hints'):
                    hint_index = min(2 - attempts, len(level['hints']) - 1)
                    print(f"提示: {level['hints'][hint_index]}")
        
        print(f"\n{COLORS['red']}游戏结束，正确答案是:{COLORS['reset']}")
        print(f"{level['solution']}")
        time.sleep(3)

    def check_region_completion(self, region):
        levels = self.level_manager.get_levels_for_region(region['id'])
        all_completed = all(level['id'] in self.game_state.completed_quests for level in levels)
        
        if all_completed:
            print(f"\n{COLORS['yellow']}{COLORS['bold']}恭喜！你完成了 {region['name']} 所有关卡！{COLORS['reset']}")
            
            next_region_id = self.level_manager.get_next_region(region['id'])
            if next_region_id:
                self.game_state.unlock_region(next_region_id)
                next_region = self.level_manager.get_region_by_id(next_region_id)
                print(f"\n{COLORS['green']}{COLORS['bold']}新区域解锁: {next_region['name']}{COLORS['reset']}")

    def character_info(self):
        self.clear_screen()
        print(f"{COLORS['bold']}{COLORS['green']}=== 角色信息 ==={COLORS['reset']}")
        print(f"名字: {self.player.name}")
        print(f"等级: {self.player.level}")
        
        exp_percentage = (self.player.exp / self.player.get_exp_needed()) * 100
        bar_length = 20
        filled = int(bar_length * exp_percentage / 100)
        exp_bar = f"{'█' * filled}{'░' * (bar_length - filled)}"
        print(f"经验值: {exp_bar} {self.player.exp}/{self.player.get_exp_needed()} ({exp_percentage:.1f}%)")
        
        print(f"\n{COLORS['bold']}属性:{COLORS['reset']}")
        print(f"生命值: {self.player.hp}/{self.player.max_hp}")
        print(f"攻击力: {self.player.attack}")
        print(f"防御力: {self.player.defense}")
        print(f"速度: {self.player.speed}")
        print(f"金币: {self.player.gold}")
        
        print(f"\n{COLORS['bold']}装备:{COLORS['reset']}")
        for slot in EQUIPMENT_SLOTS:
            item = self.player.equipment.get(slot)
            if item:
                print(f"{slot}: {item['name']}")
            else:
                print(f"{slot}: 空")
        
        input("\n按回车键继续...")

    def inventory(self):
        self.clear_screen()
        print(f"{COLORS['bold']}{COLORS['blue']}=== 背包 ==={COLORS['reset']}")
        
        if not self.player.inventory:
            print("背包是空的")
        else:
            for i, item in enumerate(self.player.inventory, 1):
                print(f"{i}. {item['name']}")
                print(f"   {item['description']}")
                if 'stats' in item:
                    stats_str = ", ".join([f"{k}: +{v}" for k, v in item['stats'].items()])
                    print(f"   属性: {stats_str}")
        
        print(f"\n0. 返回")
        
        while True:
            choice = input("\n请选择物品 (输入序号): ")
            
            if choice == '0':
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(self.player.inventory):
                    item = self.player.inventory[index]
                    print(f"\n{COLORS['bold']}{item['name']}{COLORS['reset']}")
                    print(f"{item['description']}")
                    
                    if item.get('type') == 'consumable':
                        use_choice = input("是否使用？(y/n): ")
                        if use_choice.lower() == 'y':
                            if self.player.use_consumable(item['id']):
                                print("使用成功！")
                            else:
                                print("使用失败")
                    elif item.get('type') == 'equipment':
                        use_choice = input("是否装备？(y/n): ")
                        if use_choice.lower() == 'y':
                            if self.player.equip_item(item.copy()):
                                self.player.remove_from_inventory(item['id'])
                                print("装备成功！")
                            else:
                                print("装备失败")
                    
                    time.sleep(1)
                    self.inventory()
                    return
                else:
                    print("无效选择")
            except ValueError:
                print("无效输入")

    def quests(self):
        self.clear_screen()
        print(f"{COLORS['bold']}{COLORS['yellow']}=== 任务 ==={COLORS['reset']}")
        
        active_quests = self.quest_manager.get_active_quests(self.game_state, self.player)
        
        if not active_quests:
            print("没有活跃任务")
        else:
            for i, quest_data in enumerate(active_quests, 1):
                quest = quest_data['quest']
                progress = quest_data['progress']
                
                print(f"\n{i}. {quest['name']}")
                print(f"   {quest['description']}")
                print(f"   类型: {quest['type']}")
                print(f"   进度: {progress['current']}/{progress['total']}")
                print(f"   奖励: {quest['exp_reward']} 经验, {quest['gold_reward']} 金币")
                
                if self.quest_manager.check_quest_completion(quest, self.game_state, self.player):
                    print(f"   {COLORS['green']}可领取奖励！{COLORS['reset']}")
        
        print(f"\n0. 返回")
        
        while True:
            choice = input("\n请选择任务 (输入序号): ")
            
            if choice == '0':
                return
            
            try:
                index = int(choice) - 1
                if 0 <= index < len(active_quests):
                    quest_data = active_quests[index]
                    quest = quest_data['quest']
                    
                    if self.quest_manager.check_quest_completion(quest, self.game_state, self.player):
                        success, message = self.quest_manager.complete_quest(self.player, quest, self.game_state)
                        print(f"\n{message}")
                        
                        newly_unlocked = self.achievement_manager.check_achievements(self.game_state, self.player)
                        if newly_unlocked:
                            print(f"\n{COLORS['yellow']}{COLORS['bold']}解锁新成就！{COLORS['reset']}")
                            for achievement in newly_unlocked:
                                print(f"- {achievement['name']}: {achievement['reward']} 金币")
                    else:
                        print("\n任务尚未完成")
                    
                    time.sleep(2)
                    self.quests()
                    return
                else:
                    print("无效选择")
            except ValueError:
                print("无效输入")

    def shop_menu(self):
        self.clear_screen()
        self.shop.display_shop(self.player)
        
        choice = input("\n请选择物品 (输入序号): ")
        
        if choice == '0':
            return
        
        try:
            index = int(choice)
            
            all_items = self.shop.get_items_by_category('all')
            if 1 <= index <= len(all_items):
                item = all_items[index - 1]
                success, message = self.shop.buy_item(self.player, item['id'])
                print(f"\n{message}")
            else:
                print("无效选择")
        except ValueError:
            print("无效输入")
        
        time.sleep(2)
        self.shop_menu()

    def achievements(self):
        self.clear_screen()
        self.achievement_manager.display_achievements(self.game_state)
        
        input("\n按回车键继续...")

    def run(self):
        while self.is_running:
            self.main_menu()

if __name__ == "__main__":
    game = Game()
    game.run()