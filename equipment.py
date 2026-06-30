from config import SHOP_ITEMS, EQUIPMENT_SLOTS

class EquipmentManager:
    def __init__(self):
        self.shop_items = SHOP_ITEMS
        self.equipment_slots = EQUIPMENT_SLOTS

    def get_all_shop_items(self):
        return self.shop_items

    def get_item_by_id(self, item_id):
        for item in self.shop_items:
            if item['id'] == item_id:
                return item
        return None

    def get_consumables(self):
        return [item for item in self.shop_items if item.get('type') == 'consumable']

    def get_equipment(self):
        return [item for item in self.shop_items if item.get('type') == 'equipment']

    def get_equipment_by_slot(self, slot):
        return [item for item in self.shop_items if item.get('type') == 'equipment' and item.get('slot') == slot]

    def can_equip(self, player, item):
        if item.get('type') != 'equipment':
            return False
        
        slot = item.get('slot')
        if slot not in self.equipment_slots:
            return False
        
        return True

    def buy_item(self, player, item_id):
        item = self.get_item_by_id(item_id)
        
        if not item:
            return False, "物品不存在"
        
        if player.gold < item['price']:
            return False, "金币不足"
        
        player.spend_gold(item['price'])
        
        if item['type'] == 'equipment':
            if self.can_equip(player, item):
                player.equip_item(item.copy())
                return True, f"成功装备 {item['name']}"
            else:
                player.add_to_inventory(item.copy())
                return True, f"已放入背包: {item['name']}"
        else:
            player.add_to_inventory(item.copy())
            return True, f"已放入背包: {item['name']}"

    def sell_item(self, player, item_id):
        item = player.remove_from_inventory(item_id)
        
        if not item:
            return False, "背包中没有该物品"
        
        sell_price = item['price'] // 2
        player.add_gold(sell_price)
        
        return True, f"出售成功，获得 {sell_price} 金币"

    def get_equipment_stats(self, player):
        stats = {}
        
        for slot, item in player.equipment.items():
            if 'stats' in item:
                for stat, value in item['stats'].items():
                    stats[stat] = stats.get(stat, 0) + value
        
        return stats

    def get_formatted_equipment(self, player):
        result = []
        
        for slot in self.equipment_slots:
            item = player.equipment.get(slot, None)
            if item:
                result.append(f"{slot}: {item['name']}")
            else:
                result.append(f"{slot}: 空")
        
        return result