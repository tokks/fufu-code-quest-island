import json
import os
from datetime import datetime
from config import SAVE_DIR

class GameState:
    def __init__(self):
        self.player = None
        self.current_region = 'day1'
        self.unlocked_regions = ['day1']
        self.completed_quests = []
        self.unlocked_achievements = []
        self.total_gold_earned = 0
        self.game_start_time = datetime.now().isoformat()
        self.last_save_time = None

    def save_game(self, filename="save.json"):
        save_data = {
            'player': self.player.to_dict() if self.player else None,
            'current_region': self.current_region,
            'unlocked_regions': self.unlocked_regions,
            'completed_quests': self.completed_quests,
            'unlocked_achievements': self.unlocked_achievements,
            'total_gold_earned': self.total_gold_earned,
            'game_start_time': self.game_start_time,
            'last_save_time': datetime.now().isoformat()
        }
        
        save_path = os.path.join(SAVE_DIR, filename)
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
        
        self.last_save_time = save_data['last_save_time']
        return save_path

    @classmethod
    def load_game(cls, filename="save.json"):
        save_path = os.path.join(SAVE_DIR, filename)
        
        if not os.path.exists(save_path):
            return None
        
        with open(save_path, 'r', encoding='utf-8') as f:
            save_data = json.load(f)
        
        state = cls()
        state.current_region = save_data['current_region']
        state.unlocked_regions = save_data['unlocked_regions']
        state.completed_quests = save_data['completed_quests']
        state.unlocked_achievements = save_data['unlocked_achievements']
        state.total_gold_earned = save_data['total_gold_earned']
        state.game_start_time = save_data['game_start_time']
        state.last_save_time = save_data.get('last_save_time')
        
        return state

    def unlock_region(self, region_id):
        if region_id not in self.unlocked_regions:
            self.unlocked_regions.append(region_id)
            return True
        return False

    def complete_quest(self, quest_id):
        if quest_id not in self.completed_quests:
            self.completed_quests.append(quest_id)
            return True
        return False

    def unlock_achievement(self, achievement_id):
        if achievement_id not in self.unlocked_achievements:
            self.unlocked_achievements.append(achievement_id)
            return True
        return False

    def add_gold_earned(self, amount):
        self.total_gold_earned += amount

    def to_dict(self):
        return {
            'current_region': self.current_region,
            'unlocked_regions': self.unlocked_regions,
            'completed_quests': self.completed_quests,
            'unlocked_achievements': self.unlocked_achievements,
            'total_gold_earned': self.total_gold_earned,
            'game_start_time': self.game_start_time,
            'last_save_time': self.last_save_time
        }

    @classmethod
    def from_dict(cls, data):
        state = cls()
        state.current_region = data.get('current_region', 'region_1')
        unlocked = data.get('unlocked_regions', ['region_1'])
        if 'tutorial' in unlocked and 'region_1' not in unlocked:
            unlocked = ['region_1']
        state.unlocked_regions = unlocked
        state.completed_quests = data.get('completed_quests', [])
        state.unlocked_achievements = data.get('unlocked_achievements', [])
        state.total_gold_earned = data.get('total_gold_earned', 0)
        state.game_start_time = data.get('game_start_time', datetime.now().isoformat())
        state.last_save_time = data.get('last_save_time')
        return state