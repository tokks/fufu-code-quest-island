from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = 'code_quest_island_secret_key'

from game_state import GameState
from player import Player
from levels import LevelManager
from quests import QuestManager
from shop import Shop
from achievements import AchievementManager

level_manager = LevelManager()

@app.route('/api/reload_data')
def api_reload_data():
    level_manager.reload()
    return jsonify({'success': True, 'message': '数据已重新加载'})
quest_manager = QuestManager()
shop = Shop()
achievement_manager = AchievementManager()

def get_game_state():
    if 'game_state' in session:
        state = GameState.from_dict(session['game_state'])
        
        if 'tutorial' in state.unlocked_regions and 'region_1' not in state.unlocked_regions:
            state.unlocked_regions = ['region_1']
        
        migrated = False
        new_unlocked = []
        for region_id in state.unlocked_regions:
            if region_id.startswith('region_'):
                day_num = region_id.split('_')[1]
                new_unlocked.append(f'day{day_num}')
                migrated = True
            else:
                new_unlocked.append(region_id)
        
        if migrated:
            state.unlocked_regions = new_unlocked
            session['game_state'] = state.to_dict()
    else:
        state = GameState()
        state.unlocked_regions = ['day1']
    
    if 'player' in session:
        state.player = Player.from_dict(session['player'])
    
    return state

def save_game_state(state):
    session['game_state'] = state.to_dict()
    if state.player:
        session['player'] = state.player.to_dict()
    session.permanent = True

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    name = request.form.get('name', '冒险者')
    
    player = Player(name.strip())
    game_state = GameState()
    game_state.player = player
    
    save_game_state(game_state)
    
    return redirect(url_for('game'))

@app.route('/admin_login', methods=['POST'])
def admin_login():
    import json
    
    try:
        with open('admin_config.json', 'r', encoding='utf-8') as f:
            config = json.load(f)
    except:
        return jsonify({'success': False, 'message': '管理员配置不存在'})
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username == config.get('admin_username') and password == config.get('admin_password'):
        player = Player('管理员', is_admin=True)
        player.gold = config.get('admin_gold', 9999)
        player.level = config.get('admin_level', 99)
        
        game_state = GameState()
        game_state.player = player
        
        all_region_ids = [f'day{i}' for i in range(1, 22)]
        game_state.unlocked_regions = all_region_ids
        
        save_game_state(game_state)
        
        return redirect(url_for('game'))
    else:
        return jsonify({'success': False, 'message': '用户名或密码错误'})

@app.route('/game')
def game():
    game_state = get_game_state()
    
    if not game_state.player:
        return redirect(url_for('index'))
    
    return render_template('game.html', 
                           player=game_state.player,
                           game_state=game_state)

@app.route('/api/world_map')
def api_world_map():
    game_state = get_game_state()
    progress = level_manager.get_progress(game_state)
    
    print(f"DEBUG - unlocked_regions: {game_state.unlocked_regions}")
    print(f"DEBUG - region_1 unlocked: {'region_1' in game_state.unlocked_regions}")
    
    return jsonify(progress)

@app.route('/api/region/<region_id>')
def api_region(region_id):
    game_state = get_game_state()
    player = game_state.player
    is_admin = player.is_admin if player else False
    
    region = level_manager.get_region_by_id(region_id)
    levels = level_manager.get_levels_for_region(region_id)
    
    if not region:
        return jsonify({'error': '区域不存在'}), 404
    
    return jsonify({
        'region': region,
        'levels': levels,
        'completed_quests': game_state.completed_quests,
        'is_admin': is_admin
    })

@app.route('/api/level/<region_id>/<level_id>')
def api_level(region_id, level_id):
    game_state = get_game_state()
    player = game_state.player
    is_admin = player.is_admin if player else False
    
    level = level_manager.get_level(region_id, level_id)
    
    if not level:
        return jsonify({'error': '关卡不存在'}), 404
    
    is_completed = level_id in game_state.completed_quests
    
    level_data = level.copy()
    level_data['is_completed'] = is_completed
    level_data['is_admin'] = is_admin
    
    return jsonify(level_data)

@app.route('/api/submit_answer', methods=['POST'])
def api_submit_answer():
    data = request.get_json()
    region_id = data.get('region_id')
    level_id = data.get('level_id')
    user_answer = data.get('answer', '')
    
    game_state = get_game_state()
    player = game_state.player
    
    if not player:
        return jsonify({'success': False, 'message': '请先登录游戏'})
    
    is_admin = player.is_admin
    
    level = level_manager.get_level(region_id, level_id)
    
    if not level:
        return jsonify({'success': False, 'message': '关卡不存在'})
    
    if level_id in game_state.completed_quests and not is_admin:
        return jsonify({'success': False, 'message': '该关卡已完成'})
    
    print(f"DEBUG - user_answer: '{user_answer}', type: {type(user_answer)}, level_answer: '{level.get('answer')}'")
    
    is_correct = level_manager.check_answer(level, user_answer)
    
    if is_correct:
        if not is_admin:
            player.add_exp(level['exp_reward'])
            player.add_gold(level['gold_reward'])
            game_state.add_gold_earned(level['gold_reward'])
            
            newly_unlocked = achievement_manager.check_achievements(game_state, player)
            
            levels = level_manager.get_levels_for_region(region_id)
            all_completed = all(l['id'] in game_state.completed_quests for l in levels)
            
            next_region_id = None
            if all_completed:
                next_region_id = level_manager.get_next_region(region_id)
                if next_region_id:
                    game_state.unlock_region(next_region_id)
        else:
            newly_unlocked = []
            all_completed = False
            next_region_id = None
        
        if level_id not in game_state.completed_quests:
            game_state.complete_quest(level_id)
        
        save_game_state(game_state)
        
        return jsonify({
            'success': True,
            'message': '回答正确！',
            'exp_reward': level['exp_reward'],
            'gold_reward': level['gold_reward'],
            'newly_unlocked': newly_unlocked,
            'all_completed': all_completed,
            'next_region': next_region_id,
            'player': player.to_dict() if player else None
        })
    else:
        # 答错时扣除HP（管理员不扣）
        damage_info = None
        if player and not is_admin:
            damage_info = player.take_answer_damage(level.get('difficulty', '中等'))
            save_game_state(game_state)
        
        return jsonify({
            'success': False,
            'message': '回答错误，请重试',
            'hint': level.get('hints', [])[0] if level.get('hints') else None,
            'damage_info': damage_info,
            'player': player.to_dict() if player else None
        })

@app.route('/api/reveal_answer', methods=['POST'])
def api_reveal_answer():
    data = request.get_json()
    region_id = data.get('region_id')
    level_id = data.get('level_id')
    
    game_state = get_game_state()
    player = game_state.player
    is_admin = player.is_admin if player else False
    
    level = level_manager.get_level(region_id, level_id)
    
    if not level:
        return jsonify({'success': False, 'message': '关卡不存在'})
    
    if not is_admin:
        if not player:
            return jsonify({'success': False, 'message': '请先登录'})
        
        reveal_cost = level['gold_reward'] + 5
        
        if player.gold < reveal_cost:
            return jsonify({
                'success': False,
                'message': f'金币不足！需要 {reveal_cost} 金币，你有 {player.gold} 金币'
            })
        
        player.add_gold(-reveal_cost)
        save_game_state(game_state)
    
    reveal_cost = level['gold_reward'] + 5 if not is_admin else 0
    
    return jsonify({
        'success': True,
        'message': f'花费 {reveal_cost} 金币查看答案',
        'answer': level['answer'],
        'player': player.to_dict() if player else None
    })

@app.route('/api/player')
def api_player():
    game_state = get_game_state()
    return jsonify(game_state.player.to_dict() if game_state.player else {})

@app.route('/api/quests')
def api_quests():
    game_state = get_game_state()
    player = game_state.player
    
    active_quests = quest_manager.get_active_quests(game_state, player)
    
    return jsonify([{
        'quest': q['quest'],
        'progress': q['progress']
    } for q in active_quests])

@app.route('/api/complete_quest', methods=['POST'])
def api_complete_quest():
    data = request.get_json()
    quest_id = data.get('quest_id')
    
    game_state = get_game_state()
    player = game_state.player
    
    quest = quest_manager.get_quest_by_id(quest_id)
    
    if not quest:
        return jsonify({'success': False, 'message': '任务不存在'})
    
    success, message = quest_manager.complete_quest(player, quest, game_state)
    
    if success:
        newly_unlocked = achievement_manager.check_achievements(game_state, player)
        save_game_state(game_state)
        
        return jsonify({
            'success': True,
            'message': message,
            'newly_unlocked': newly_unlocked,
            'player': player.to_dict()
        })
    
    return jsonify({'success': False, 'message': message})

@app.route('/api/shop')
def api_shop():
    game_state = get_game_state()
    player = game_state.player
    
    items = shop.get_items_by_category('all')
    
    return jsonify({
        'items': items,
        'player_gold': player.gold if player else 0
    })

@app.route('/api/buy_item', methods=['POST'])
def api_buy_item():
    data = request.get_json()
    item_id = data.get('item_id')
    
    game_state = get_game_state()
    player = game_state.player
    
    success, message = shop.buy_item(player, item_id)
    
    if success:
        save_game_state(game_state)
        return jsonify({
            'success': True,
            'message': message,
            'player': player.to_dict()
        })
    
    return jsonify({'success': False, 'message': message})

@app.route('/api/achievements')
def api_achievements():
    game_state = get_game_state()
    
    return jsonify({
        'achievements': achievement_manager.get_all_achievements(),
        'unlocked': game_state.unlocked_achievements
    })

@app.route('/api/inventory')
def api_inventory():
    game_state = get_game_state()
    player = game_state.player
    
    return jsonify({
        'inventory': player.inventory if player else [],
        'equipment': player.equipment if player else {}
    })

@app.route('/api/equip_item', methods=['POST'])
def api_equip_item():
    data = request.get_json()
    item_id = data.get('item_id')
    
    game_state = get_game_state()
    player = game_state.player
    
    item = None
    for i, inv_item in enumerate(player.inventory):
        if inv_item.get('id') == item_id:
            item = inv_item
            break
    
    if not item:
        return jsonify({'success': False, 'message': '物品不存在'})
    
    if player.equip_item(item.copy()):
        player.remove_from_inventory(item_id)
        save_game_state(game_state)
        return jsonify({
            'success': True,
            'message': f'成功装备 {item["name"]}',
            'player': player.to_dict()
        })
    
    return jsonify({'success': False, 'message': '装备失败'})

@app.route('/api/use_item', methods=['POST'])
def api_use_item():
    data = request.get_json()
    item_id = data.get('item_id')
    
    game_state = get_game_state()
    player = game_state.player
    
    if player.use_consumable(item_id):
        save_game_state(game_state)
        return jsonify({
            'success': True,
            'message': '使用成功',
            'player': player.to_dict()
        })
    
    return jsonify({'success': False, 'message': '使用失败'})

@app.route('/api/save_game')
def api_save_game():
    game_state = get_game_state()
    save_game_state(game_state)
    return jsonify({'success': True, 'message': '游戏已保存'})

@app.route('/api/reset_game')
def api_reset_game():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)