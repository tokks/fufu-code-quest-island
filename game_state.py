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
        self.revealed_quests = []
        self.completed_quests_count = {}

    def save_game(self, player_name=None):
        if player_name:
            filename = f"save_{player_name}.json"
        else:
            filename = f"save_{self.player.name}.json" if self.player else "save.json"
        
        save_data = {
            'player': self.player.to_dict() if self.player else None,
            'current_region': self.current_region,
            'unlocked_regions': self.unlocked_regions,
            'completed_quests': self.completed_quests,
            'unlocked_achievements': self.unlocked_achievements,
            'total_gold_earned': self.total_gold_earned,
            'game_start_time': self.game_start_time,
            'last_save_time': datetime.now().isoformat(),
            'revealed_quests': self.revealed_quests,
            'completed_quests_count': self.completed_quests_count
        }
        
        save_path = os.path.join(SAVE_DIR, filename)
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(save_data, f, ensure_ascii=False, indent=2)
        
        self.last_save_time = save_data['last_save_time']
        return save_path

    @classmethod
    def load_game(cls, player_name=None):
        if player_name:
            filename = f"save_{player_name}.json"
        else:
            filename = "save.json"
        
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
        state.revealed_quests = save_data.get('revealed_quests', [])
        state.completed_quests_count = save_data.get('completed_quests_count', {})
        
        if save_data.get('player'):
            from player import Player
            state.player = Player.from_dict(save_data['player'])
        
        return state
    
    @classmethod
    def player_exists(cls, player_name):
        filename = f"save_{player_name}.json"
        save_path = os.path.join(SAVE_DIR, filename)
        return os.path.exists(save_path)
    
    @classmethod
    def get_all_players(cls):
        players = []
        if not os.path.exists(SAVE_DIR):
            return players
        
        for filename in os.listdir(SAVE_DIR):
            if filename.startswith('save_') and filename.endswith('.json'):
                player_name = filename[5:-5]
                players.append(player_name)
        
        return players
    
    @classmethod
    def delete_player(cls, player_name):
        filename = f"save_{player_name}.json"
        save_path = os.path.join(SAVE_DIR, filename)
        
        if os.path.exists(save_path):
            os.remove(save_path)
            return True
        return False

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

    def reveal_quest(self, quest_id):
        if quest_id not in self.revealed_quests:
            self.revealed_quests.append(quest_id)
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
            'last_save_time': self.last_save_time,
            'revealed_quests': self.revealed_quests
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