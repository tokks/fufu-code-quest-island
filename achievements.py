from config import ACHIEVEMENTS, COLORS

class AchievementManager:
    def __init__(self):
        self.achievements = ACHIEVEMENTS

    def get_all_achievements(self):
        return self.achievements

    def get_achievement_by_id(self, achievement_id):
        for achievement in self.achievements:
            if achievement['id'] == achievement_id:
                return achievement
        return None

    def get_unlocked_achievements(self, game_state):
        return [a for a in self.achievements if a['id'] in game_state.unlocked_achievements]

    def get_locked_achievements(self, game_state):
        return [a for a in self.achievements if a['id'] not in game_state.unlocked_achievements]

    def check_achievements(self, game_state, player):
        newly_unlocked = []
        
        for achievement in self.achievements:
            if achievement['id'] in game_state.unlocked_achievements:
                continue
            
            unlocked = False
            
            if achievement['id'] == 'first_blood':
                if 'day1_q11' in game_state.completed_quests:
                    unlocked = True
            
            elif achievement['id'] == 'level_10':
                if player.level >= 10:
                    unlocked = True
            
            elif achievement['id'] == 'collector':
                equipment_count = len(player.equipment) + len([i for i in player.inventory if i.get('type') == 'equipment'])
                if equipment_count >= 5:
                    unlocked = True
            
            elif achievement['id'] == 'gold_hunter':
                if game_state.total_gold_earned >= 1000:
                    unlocked = True
            
            elif achievement['id'] == 'achievement_master':
                if len(game_state.unlocked_achievements) >= len(self.achievements) - 1:
                    unlocked = True
            
            elif achievement['id'] == 'bug_slayer':
                if 'bug_1' in game_state.completed_quests:
                    unlocked = True
            
            if unlocked:
                game_state.unlock_achievement(achievement['id'])
                player.add_gold(achievement['reward'])
                newly_unlocked.append(achievement)
        
        return newly_unlocked

    def display_achievements(self, game_state):
        print(f"\n{COLORS['bold']}{COLORS['purple']}=== 成就系统 ==={COLORS['reset']}")
        
        unlocked = self.get_unlocked_achievements(game_state)
        locked = self.get_locked_achievements(game_state)
        
        print(f"\n{COLORS['bold']}{COLORS['green']}【已解锁成就】{COLORS['reset']}")
        if unlocked:
            for achievement in unlocked:
                print(f"{COLORS['green']}✓{COLORS['reset']} {achievement['name']}")
                print(f"   {achievement['description']}")
                print(f"   奖励: {achievement['reward']} 金币")
        else:
            print("   暂无已解锁成就")
        
        print(f"\n{COLORS['bold']}{COLORS['gray']}【未解锁成就】{COLORS['reset']}")
        if locked:
            for achievement in locked:
                print(f"{COLORS['red']}✗{COLORS['reset']} {achievement['name']}")
                print(f"   {achievement['description']}")
                print(f"   奖励: {achievement['reward']} 金币")
        else:
            print("   所有成就已解锁！")
        
        print(f"\n已解锁: {len(unlocked)}/{len(self.achievements)}")

    def get_achievement_progress(self, achievement_id, game_state, player):
        achievement = self.get_achievement_by_id(achievement_id)
        if not achievement:
            return None
        
        if achievement['id'] == 'first_blood':
            return {'current': 'day1_q11' in game_state.completed_quests, 'total': 1}
        
        elif achievement['id'] == 'level_10':
            return {'current': player.level, 'total': 10}
        
        elif achievement['id'] == 'collector':
            equipment_count = len(player.equipment) + len([i for i in player.inventory if i.get('type') == 'equipment'])
            return {'current': equipment_count, 'total': 5}
        
        elif achievement['id'] == 'gold_hunter':
            return {'current': game_state.total_gold_earned, 'total': 1000}
        
        elif achievement['id'] == 'achievement_master':
            return {'current': len(game_state.unlocked_achievements), 'total': len(self.achievements)}
        
        elif achievement['id'] == 'bug_slayer':
            return {'current': 'bug_1' in game_state.completed_quests, 'total': 1}
        
        return {'current': 0, 'total': 1}