from config import BASE_GOLD_REWARD, GOLD_MULTIPLIER

class QuestManager:
    def __init__(self):
        self.quests = {
            'main': [
                {
                    'id': 'q_main_1',
                    'name': '踏上旅程',
                    'description': '完成新手村的所有任务',
                    'type': 'main',
                    'objective': '完成tut_1, tut_2, tut_3',
                    'required_quests': [],
                    'exp_reward': 100,
                    'gold_reward': 50,
                    'item_reward': None,
                    'region': 'tutorial'
                },
                {
                    'id': 'q_main_2',
                    'name': '变量大师',
                    'description': '完成变量森林的所有任务',
                    'type': 'main',
                    'objective': '完成var_1, var_2, var_3',
                    'required_quests': ['q_main_1'],
                    'exp_reward': 200,
                    'gold_reward': 100,
                    'item_reward': {'id': 'variable_ring', 'name': '变量戒指', 'type': 'equipment', 'slot': 'ring', 'stats': {'attack': 10}},
                    'region': 'variable_forest'
                },
                {
                    'id': 'q_main_3',
                    'name': '函数专家',
                    'description': '完成函数洞穴的所有任务',
                    'type': 'main',
                    'objective': '完成func_1, func_2, func_3',
                    'required_quests': ['q_main_2'],
                    'exp_reward': 250,
                    'gold_reward': 125,
                    'item_reward': {'id': 'function_book', 'name': '函数宝典', 'type': 'equipment', 'slot': 'book', 'stats': {'attack': 15}},
                    'region': 'function_cave'
                },
                {
                    'id': 'q_main_4',
                    'name': '条件守护者',
                    'description': '完成条件城堡的所有任务',
                    'type': 'main',
                    'objective': '完成cond_1, cond_2, cond_3',
                    'required_quests': ['q_main_3'],
                    'exp_reward': 250,
                    'gold_reward': 125,
                    'item_reward': {'id': 'condition_shield', 'name': '条件之盾', 'type': 'equipment', 'slot': 'shield', 'stats': {'defense': 20}},
                    'region': 'condition_castle'
                },
                {
                    'id': 'q_main_5',
                    'name': '循环征服者',
                    'description': '完成循环山脉的所有任务',
                    'type': 'main',
                    'objective': '完成loop_1, loop_2, loop_3',
                    'required_quests': ['q_main_4'],
                    'exp_reward': 300,
                    'gold_reward': 150,
                    'item_reward': {'id': 'loop_boots', 'name': '循环之靴', 'type': 'equipment', 'slot': 'boots', 'stats': {'speed': 10}},
                    'region': 'loop_mountain'
                },
                {
                    'id': 'q_main_6',
                    'name': '数据探索者',
                    'description': '完成数据海洋的所有任务',
                    'type': 'main',
                    'objective': '完成data_1, data_2, data_3',
                    'required_quests': ['q_main_5'],
                    'exp_reward': 350,
                    'gold_reward': 175,
                    'item_reward': {'id': 'data_amulet', 'name': '数据护符', 'type': 'equipment', 'slot': 'amulet', 'stats': {'defense': 15}},
                    'region': 'data_ocean'
                },
                {
                    'id': 'q_main_7',
                    'name': '面向对象大师',
                    'description': '完成类之宫殿的所有任务',
                    'type': 'main',
                    'objective': '完成class_1, class_2, class_3',
                    'required_quests': ['q_main_6'],
                    'exp_reward': 400,
                    'gold_reward': 200,
                    'item_reward': None,
                    'region': 'class_palace'
                },
                {
                    'id': 'q_main_8',
                    'name': '终极挑战',
                    'description': '击败Bug之王',
                    'type': 'main',
                    'objective': '完成bug_1',
                    'required_quests': ['q_main_7'],
                    'exp_reward': 1000,
                    'gold_reward': 500,
                    'item_reward': None,
                    'region': 'bug_lair'
                }
            ],
            'side': [
                {
                    'id': 'q_side_1',
                    'name': '装备收集者',
                    'description': '收集3件装备',
                    'type': 'side',
                    'objective': '拥有3件装备',
                    'required_quests': [],
                    'exp_reward': 150,
                    'gold_reward': 75,
                    'item_reward': None,
                    'region': None
                },
                {
                    'id': 'q_side_2',
                    'name': '金币猎人',
                    'description': '累计获得500金币',
                    'type': 'side',
                    'objective': '累计获得500金币',
                    'required_quests': [],
                    'exp_reward': 200,
                    'gold_reward': 100,
                    'item_reward': None,
                    'region': None
                },
                {
                    'id': 'q_side_3',
                    'name': '快速升级',
                    'description': '达到10级',
                    'type': 'side',
                    'objective': '达到10级',
                    'required_quests': [],
                    'exp_reward': 300,
                    'gold_reward': 150,
                    'item_reward': None,
                    'region': None
                }
            ]
        }

    def get_all_quests(self):
        all_quests = []
        for quest_type in self.quests.values():
            all_quests.extend(quest_type)
        return all_quests

    def get_main_quests(self):
        return self.quests['main']

    def get_side_quests(self):
        return self.quests['side']

    def get_quest_by_id(self, quest_id):
        for quest_type in self.quests.values():
            for quest in quest_type:
                if quest['id'] == quest_id:
                    return quest
        return None

    def get_active_quests(self, game_state, player):
        active_quests = []
        
        for quest in self.get_all_quests():
            if quest['id'] in game_state.completed_quests:
                continue
            
            can_accept = True
            for required in quest['required_quests']:
                if required not in game_state.completed_quests:
                    can_accept = False
                    break
            
            if can_accept:
                progress = self.get_quest_progress(quest, game_state, player)
                active_quests.append({
                    'quest': quest,
                    'progress': progress
                })
        
        return active_quests

    def get_quest_progress(self, quest, game_state, player):
        if quest['type'] == 'main':
            objectives = quest['objective'].split(', ')
            completed = sum(1 for obj in objectives if obj.strip() in game_state.completed_quests)
            return {'current': completed, 'total': len(objectives)}
        
        elif quest['id'] == 'q_side_1':
            equipment_count = len(player.equipment) + len([i for i in player.inventory if i.get('type') == 'equipment'])
            return {'current': equipment_count, 'total': 3}
        
        elif quest['id'] == 'q_side_2':
            return {'current': game_state.total_gold_earned, 'total': 500}
        
        elif quest['id'] == 'q_side_3':
            return {'current': player.level, 'total': 10}
        
        return {'current': 0, 'total': 1}

    def check_quest_completion(self, quest, game_state, player):
        progress = self.get_quest_progress(quest, game_state, player)
        return progress['current'] >= progress['total']

    def complete_quest(self, player, quest, game_state):
        if not self.check_quest_completion(quest, game_state, player):
            return False, "任务未完成"
        
        if quest['id'] in game_state.completed_quests:
            return False, "任务已完成"
        
        player.add_exp(quest['exp_reward'])
        player.add_gold(quest['gold_reward'])
        game_state.complete_quest(quest['id'])
        game_state.add_gold_earned(quest['gold_reward'])
        
        if quest['item_reward']:
            player.add_to_inventory(quest['item_reward'])
            return True, f"任务完成！获得 {quest['exp_reward']} 经验，{quest['gold_reward']} 金币，以及 {quest['item_reward']['name']}"
        
        return True, f"任务完成！获得 {quest['exp_reward']} 经验，{quest['gold_reward']} 金币"

    def calculate_gold_reward(self, level_difficulty):
        multipliers = {'简单': 1.0, '中等': 1.5, '困难': 2.0, '极难': 3.0}
        multiplier = multipliers.get(level_difficulty, 1.0)
        return int(BASE_GOLD_REWARD * multiplier * GOLD_MULTIPLIER)