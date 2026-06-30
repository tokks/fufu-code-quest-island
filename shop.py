from config import SHOP_ITEMS, COLORS

class Shop:
    def __init__(self):
        self.items = SHOP_ITEMS

    def get_items_by_category(self, category):
        if category == 'consumables':
            return [item for item in self.items if item.get('type') == 'consumable']
        elif category == 'equipment':
            return [item for item in self.items if item.get('type') == 'equipment']
        return self.items

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item['id'] == item_id:
                return item
        return None

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

    def can_equip(self, player, item):
        if item.get('type') != 'equipment':
            return False
        
        slot = item.get('slot')
        if slot in player.equipment:
            return False
        
        return True

    def sell_item(self, player, item_id):
        item = player.remove_from_inventory(item_id)
        
        if not item:
            for slot, equipped_item in player.equipment.items():
                if equipped_item.get('id') == item_id:
                    player.unequip_item(slot)
                    item = equipped_item
                    break
        
        if not item:
            return False, "没有找到该物品"
        
        sell_price = item['price'] // 2
        player.add_gold(sell_price)
        
        return True, f"出售成功，获得 {sell_price} 金币"

    def display_shop(self, player):
        print(f"\n{COLORS['bold']}{COLORS['cyan']}=== 商城 ==={COLORS['reset']}")
        print(f"您的金币: {COLORS['yellow']}{player.gold}{COLORS['reset']}")
        
        print(f"\n{COLORS['bold']}【消耗品】{COLORS['reset']}")
        consumables = self.get_items_by_category('consumables')
        for i, item in enumerate(consumables, 1):
            print(f"{i}. {item['name']} - {item['price']} 金币")
            print(f"   {item['description']}")
        
        print(f"\n{COLORS['bold']}【装备】{COLORS['reset']}")
        equipment = self.get_items_by_category('equipment')
        for i, item in enumerate(equipment, 1):
            price_color = COLORS['green'] if player.gold >= item['price'] else COLORS['red']
            print(f"{i}. {item['name']} - {price_color}{item['price']}{COLORS['reset']} 金币")
            print(f"   {item['description']}")
            if 'stats' in item:
                stats_str = ", ".join([f"{k}: +{v}" for k, v in item['stats'].items()])
                print(f"   属性: {stats_str}")
        
        print(f"\n0. 返回")

    def get_item_index(self, index, category='all'):
        items = self.get_items_by_category(category)
        if 1 <= index <= len(items):
            return items[index - 1]
        return None