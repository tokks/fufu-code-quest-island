from config import MAX_LEVEL, BASE_EXP_PER_LEVEL, EXP_MULTIPLIER, INITIAL_HP, INITIAL_ATTACK, INITIAL_DEFENSE

class Player:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.level = 1
        self.exp = 0
        self.gold = 0
        self.hp = INITIAL_HP
        self.max_hp = INITIAL_HP
        self.attack = INITIAL_ATTACK
        self.defense = INITIAL_DEFENSE
        self.speed = 5
        self.equipment = {}
        self.inventory = []
        self.active_effects = []
        self.is_admin = is_admin

    def get_exp_needed(self):
        return int(BASE_EXP_PER_LEVEL * (EXP_MULTIPLIER ** (self.level - 1)))

    def add_exp(self, amount):
        self.exp += amount
        levels_gained = 0
        
        while self.level < MAX_LEVEL and self.exp >= self.get_exp_needed():
            self.exp -= self.get_exp_needed()
            self.level_up()
            levels_gained += 1
        
        return levels_gained

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.attack += 5
        self.defense += 3
        self.speed += 1
        return True

    def add_gold(self, amount):
        self.gold += amount
        return self.gold

    def spend_gold(self, amount):
        if self.gold >= amount:
            self.gold -= amount
            return True
        return False

    def equip_item(self, item):
        if 'slot' in item:
            slot = item['slot']
            
            if slot in self.equipment:
                self.unequip_item(slot)
            
            self.equipment[slot] = item
            
            if 'stats' in item:
                for stat, value in item['stats'].items():
                    if hasattr(self, stat):
                        setattr(self, stat, getattr(self, stat) + value)
            
            return True
        return False

    def unequip_item(self, slot):
        if slot in self.equipment:
            item = self.equipment[slot]
            
            if 'stats' in item:
                for stat, value in item['stats'].items():
                    if hasattr(self, stat):
                        setattr(self, stat, getattr(self, stat) - value)
            
            self.inventory.append(item)
            del self.equipment[slot]
            return item
        return None

    def add_to_inventory(self, item):
        self.inventory.append(item)
        return len(self.inventory)

    def remove_from_inventory(self, item_id):
        for i, item in enumerate(self.inventory):
            if item.get('id') == item_id:
                return self.inventory.pop(i)
        return None

    def use_consumable(self, item_id):
        item = self.remove_from_inventory(item_id)
        
        if item and item.get('type') == 'consumable' and 'effect' in item:
            for stat, value in item['effect'].items():
                if stat == 'hp':
                    self.hp = min(self.hp + value, self.max_hp)
                elif hasattr(self, stat):
                    setattr(self, stat, getattr(self, stat) + value)
                    self.active_effects.append({
                        'stat': stat,
                        'value': value,
                        'duration': 3
                    })
            
            return True
        return False

    def update_effects(self):
        self.active_effects = [
            effect for effect in self.active_effects 
            if effect['duration'] > 1
        ]
        
        for effect in self.active_effects:
            effect['duration'] -= 1
        
        return len(self.active_effects)

    def take_damage(self, damage):
        actual_damage = max(1, damage - self.defense)
        self.hp = max(0, self.hp - actual_damage)
        return actual_damage

    def take_answer_damage(self, difficulty):
        """
        答错题时受到的伤害，考虑难度、防御和装备效果
        """
        # 根据难度计算基础伤害（支持中文和英文）
        difficulty_damage = {
            'easy': 5,
            'medium': 10,
            'hard': 15,
            'extreme': 20,
            '简单': 5,
            '中等': 10,
            '困难': 15,
            '极难': 20
        }
        base_damage = difficulty_damage.get(difficulty, 10)
        
        # 计算防御减免（防御越高，减免越多）
        defense_reduction = min(self.defense * 0.5, base_damage * 0.8)  # 最高减免80%
        
        # 计算装备减伤效果
        equipment_reduction = 0
        for slot, item in self.equipment.items():
            if 'damage_reduction' in item:
                equipment_reduction += item['damage_reduction']
        
        # 最终伤害
        final_damage = max(1, int(base_damage - defense_reduction - equipment_reduction))
        self.hp = max(0, self.hp - final_damage)
        
        return {
            'base_damage': base_damage,
            'defense_reduction': int(defense_reduction),
            'equipment_reduction': equipment_reduction,
            'final_damage': final_damage,
            'remaining_hp': self.hp
        }

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        old_hp = self.hp
        self.hp = min(self.hp + amount, self.max_hp)
        actual_heal = self.hp - old_hp
        return actual_heal

    def get_equipment_bonus(self, bonus_type):
        """
        获取装备提供的加成
        bonus_type: 'exp_bonus', 'gold_bonus', 'hint_count', 'damage_reduction'
        """
        total_bonus = 0
        for slot, item in self.equipment.items():
            if bonus_type in item:
                total_bonus += item[bonus_type]
        return total_bonus

    def get_total_attack(self):
        return self.attack

    def get_total_defense(self):
        return self.defense

    def to_dict(self):
        return {
            'name': self.name,
            'level': self.level,
            'exp': self.exp,
            'gold': self.gold,
            'hp': self.hp,
            'max_hp': self.max_hp,
            'attack': self.attack,
            'defense': self.defense,
            'speed': self.speed,
            'equipment': self.equipment,
            'inventory': self.inventory,
            'active_effects': self.active_effects,
            'is_admin': self.is_admin
        }

    @classmethod
    def from_dict(cls, data):
        player = cls(data['name'], data.get('is_admin', False))
        player.level = data.get('level', 1)
        player.exp = data.get('exp', 0)
        player.gold = data.get('gold', 0)
        player.hp = data.get('hp', INITIAL_HP)
        player.max_hp = data.get('max_hp', INITIAL_HP)
        player.attack = data.get('attack', INITIAL_ATTACK)
        player.defense = data.get('defense', INITIAL_DEFENSE)
        player.speed = data.get('speed', 5)
        player.equipment = data.get('equipment', {})
        player.inventory = data.get('inventory', [])
        player.active_effects = data.get('active_effects', [])
        return player