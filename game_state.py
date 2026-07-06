import json
import os
from datetime import datetime
from database import save_player, load_player, player_exists as db_player_exists, delete_player as db_delete_player, get_all_players as db_get_all_players

class GameState:
    def __init__(self):
        self.player = None
        self.current_region = 'region_1'
        self.unlocked_regions = ['region_1']
        self.completed_quests = []
        self.unlocked_achievements = []
        self.total_gold_earned = 0
        self.game_start_time = datetime.now().isoformat()
        self.last_save_time = None
        self.revealed_quests = []
        self.completed_quests_count = {}

    def save_game(self, player_name=None):
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
        
        player_name_to_save = player_name or (self.player.name if self.player else None)
        if player_name_to_save:
            save_player(player_name_to_save, save_data)
        
        self.last_save_time = save_data['last_save_time']
        return True

    @classmethod
    def load_game(cls, player_name=None):
        if not player_name:
            return None
        
        save_data = load_player(player_name)
        
        if save_data is None:
            return None
        
        state = cls()
        state.current_region = save_data.get('current_region', 'region_1')
        state.unlocked_regions = save_data.get('unlocked_regions', ['region_1'])
        state.completed_quests = save_data.get('completed_quests', [])
        state.unlocked_achievements = save_data.get('unlocked_achievements', [])
        state.total_gold_earned = save_data.get('total_gold_earned', 0)
        state.game_start_time = save_data.get('game_start_time', datetime.now().isoformat())
        state.last_save_time = save_data.get('last_save_time')
        state.revealed_quests = save_data.get('revealed_quests', [])
        state.completed_quests_count = save_data.get('completed_quests_count', {})
        
        if save_data.get('player'):
            from player import Player
            state.player = Player.from_dict(save_data['player'])
        
        return state
    
    @classmethod
    def player_exists(cls, player_name):
        return db_player_exists(player_name)
    
    @classmethod
    def get_all_players(cls):
        return db_get_all_players()
    
    @classmethod
    def delete_player(cls, player_name):
        return db_delete_player(player_name)

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
