from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import json
import os

from config import SAVE_DIR
from database import save_player, load_player

app = Flask(__name__)
app.secret_key = 'code_quest_island_secret_key'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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

@app.route('/api/db_test')
def api_db_test():
    import os
    db_url = os.environ.get('DATABASE_URL', '未配置')
    
    result = {
        'success': False,
        'database_url': '已配置 (长度: ' + str(len(db_url)) + ')' if db_url else '未配置',
        'is_postgresql': 'postgresql' in db_url.lower() if db_url else False,
        'test_save_load': False,
        'total_players': 0,
        'database_type': 'SQLite',
        'errors': []
    }
    
    try:
        from database import player_exists, save_player, load_player, get_all_players, get_connection
        
        conn, is_postgresql = get_connection()
        conn.close()
        result['database_type'] = 'PostgreSQL' if is_postgresql else 'SQLite'
        
        test_data = {
            'test': 'data',
            'timestamp': str(os.urandom(8).hex())
        }
        save_player('_test_user', test_data)
        loaded = load_player('_test_user')
        
        if loaded and loaded.get('test') == 'data':
            result['test_save_load'] = True
        else:
            result['errors'].append(f'数据加载不匹配: 期望 test=data, 实际: {loaded}')
        
        players = get_all_players()
        result['total_players'] = len(players)
        result['success'] = True
        
        return jsonify(result)
    except Exception as e:
        result['errors'].append(str(e))
        return jsonify(result)

@app.route('/api/players')
def api_players():
    try:
        from database import get_all_players, load_player, get_connection
        
        conn, is_postgresql = get_connection()
        conn.close()
        
        players_summary = get_all_players()
        
        detailed_players = []
        for p in players_summary:
            if p['name'] != '_test_user':
                full_data = load_player(p['name'])
                if full_data:
                    detailed_players.append({
                        'name': p['name'],
                        'level': p['level'],
                        'region': p['region'],
                        'gold': p['gold'],
                        'full_data': full_data
                    })
        
        return jsonify({
            'success': True,
            'database_type': 'PostgreSQL' if is_postgresql else 'SQLite',
            'total_players': len(detailed_players),
            'players': detailed_players
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

quest_manager = QuestManager()
shop = Shop()
achievement_manager = AchievementManager()

def get_game_state():
    player_name = session.get('player_name')
    
    if player_name:
        saved_state = GameState.load_game(player_name)
        
        if saved_state and saved_state.player:
            state = saved_state
            
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
            
            return state
    
    if 'game_state' in session and 'player' in session:
        state = GameState.from_dict(session['game_state'])
        state.player = Player.from_dict(session['player'])
        
        if 'tutorial' in state.unlocked_regions and 'region_1' not in state.unlocked_regions:
            state.unlocked_regions = ['region_1']
        return state
    else:
        state = GameState()
        state.unlocked_regions = ['day1']
    
    return state

def save_game_state(state):
    if state.player:
        state.save_game(state.player.name)
        session['player_name'] = state.player.name
    else:
        state.save_game()
    session.permanent = True

@app.route('/')
def index():
    session.clear()
    return render_template('index.html')

@app.route('/new_game', methods=['POST'])
def new_game():
    name = request.form.get('name', '冒险者').strip()
    
    if not name:
        return jsonify({'success': False, 'message': '角色名称不能为空'})
    
    if GameState.player_exists(name):
        saved_state = GameState.load_game(name)
        if saved_state and saved_state.player:
            save_game_state(saved_state)
            return redirect(url_for('game'))
    
    player = Player(name)
    game_state = GameState()
    game_state.player = player
    
    save_game_state(game_state)
    
    return redirect(url_for('game'))

@app.route('/api/check_player', methods=['POST'])
def check_player():
    name = request.form.get('name', '').strip()
    exists = GameState.player_exists(name)
    return jsonify({'exists': exists})

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
        
        session['is_admin'] = True
        
        return redirect(url_for('game'))
    else:
        return jsonify({'success': False, 'message': '用户名或密码错误'})

@app.route('/game')
def game():
    game_state = get_game_state()
    
    if not game_state.player:
        return redirect(url_for('index'))
    
    if game_state.player.is_admin:
        session['is_admin'] = True
    
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

@app.route('/api/reset_region/<region_id>', methods=['POST'])
def api_reset_region(region_id):
    game_state = get_game_state()
    
    region = level_manager.get_region_by_id(region_id)
    if not region:
        return jsonify({'success': False, 'message': '区域不存在'}), 404
    
    levels = level_manager.get_levels_for_region(region_id)
    for level in levels:
        if level['id'] in game_state.completed_quests:
            game_state.completed_quests.remove(level['id'])
        if level['id'] in game_state.revealed_quests:
            game_state.revealed_quests.remove(level['id'])
    
    save_game_state(game_state)
    
    return jsonify({'success': True, 'message': '区域已重置'})

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
    
    print(f"DEBUG - user_answer: '{user_answer}', type: {type(user_answer)}, level_answer: '{level.get('answer')}'")
    
    is_correct = level_manager.check_answer(level, user_answer)
    
    if is_correct:
        if level_id not in game_state.completed_quests:
            game_state.complete_quest(level_id)
        
        if not is_admin:
            completion_count = game_state.completed_quests_count.get(level_id, 0)
            
            if level_id in game_state.revealed_quests:
                exp_reward = 5
                gold_reward = 5
            elif completion_count >= 1:
                exp_reward = level['exp_reward'] // 2
                gold_reward = level['gold_reward'] // 2
            else:
                exp_reward = level['exp_reward']
                gold_reward = level['gold_reward']
            
            game_state.completed_quests_count[level_id] = completion_count + 1
            
            player.add_exp(exp_reward)
            player.add_gold(gold_reward)
            game_state.add_gold_earned(gold_reward)
            
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
        
        save_game_state(game_state)
        
        reward_exp = exp_reward if not is_admin else level['exp_reward']
        reward_gold = gold_reward if not is_admin else level['gold_reward']
        
        return jsonify({
            'success': True,
            'message': '回答正确！',
            'exp_reward': reward_exp,
            'gold_reward': reward_gold,
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
        
        scroll_count = sum(1 for item in player.inventory if item.get('id') == 'hint_scroll')
        
        if scroll_count <= 0:
            return jsonify({
                'success': False,
                'message': '提示卷轴不足！请先购买提示卷轴'
            })
        
        player.remove_from_inventory('hint_scroll')
        game_state.reveal_quest(level_id)
        save_game_state(game_state)
    
    return jsonify({
        'success': True,
        'message': '消耗一个提示卷轴查看答案',
        'answer': level['answer'],
        'player': player.to_dict() if player else None
    })

@app.route('/api/player')
def api_player():
    game_state = get_game_state()
    return jsonify(game_state.player.to_dict() if game_state.player else {})

@app.route('/api/set_avatar', methods=['POST'])
def api_set_avatar():
    game_state = get_game_state()
    data = request.get_json()
    avatar = data.get('avatar', '👤')
    
    if game_state.player:
        game_state.player.avatar = avatar
        save_game_state(game_state)
        session['game_state'] = game_state.to_dict()
        session['player'] = game_state.player.to_dict()
        return jsonify({'success': True, 'avatar': avatar})
    
    return jsonify({'success': False, 'message': '玩家不存在'}), 400

@app.route('/api/npc_config')
def api_get_npc_config():
    with open('npc_config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
    return jsonify(config)

@app.route('/api/npc_config', methods=['POST'])
def api_set_npc_config():
    if not session.get('is_admin'):
        return jsonify({'success': False, 'message': '需要管理员权限'}), 403
    
    data = request.get_json()
    avatar = data.get('avatar', '👩‍🏫')
    name = data.get('name', '富富')
    
    config = {
        'avatar': avatar,
        'name': name
    }
    
    with open('npc_config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
    
    return jsonify({'success': True, 'avatar': avatar, 'name': name})

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

@app.route('/api/leaderboard')
def api_leaderboard():
    players = GameState.get_all_players()
    leaderboard = []
    
    for player_data in players:
        player_name = player_data['name']
        state = GameState.load_game(player_name)
        if state and state.player and not getattr(state.player, 'is_admin', False):
            player = state.player
            leaderboard.append({
                'name': player.name,
                'level': player.level,
                'exp': player.exp,
                'gold': player.gold,
                'completed_quests': len(state.completed_quests),
                'unlocked_regions': len(state.unlocked_regions),
                'avatar': player.avatar
            })
    
    leaderboard.sort(key=lambda x: (x['level'], x['exp'], x['completed_quests']), reverse=True)
    
    return jsonify({'success': True, 'leaderboard': leaderboard})

@app.route('/api/admin/add_gold', methods=['POST'])
def admin_add_gold():
    if not session.get('is_admin'):
        return jsonify({'success': False, 'message': '没有管理员权限'})
    
    data = request.get_json()
    player_name = data.get('player_name')
    gold_amount = data.get('gold_amount', 0)
    
    if not player_name:
        return jsonify({'success': False, 'message': '请指定玩家名称'})
    
    if player_name == '管理员':
        return jsonify({'success': False, 'message': '不能给管理员发放金币'})
    
    if gold_amount <= 0:
        return jsonify({'success': False, 'message': '金币数量必须大于0'})
    
    save_data = load_player(player_name)
    if save_data is None:
        return jsonify({'success': False, 'message': '玩家不存在'})
    
    try:
        if 'player' in save_data:
            save_data['player']['gold'] = save_data['player'].get('gold', 0) + gold_amount
        
        save_player(player_name, save_data)
        
        return jsonify({'success': True, 'message': f'成功给玩家 {player_name} 发放 {gold_amount} 金币'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'操作失败：{str(e)}'})

@app.route('/api/admin/delete_player', methods=['POST'])
def admin_delete_player():
    if not session.get('is_admin'):
        return jsonify({'success': False, 'message': '没有管理员权限'})
    
    data = request.get_json()
    player_name = data.get('player_name')
    
    if not player_name:
        return jsonify({'success': False, 'message': '请指定要删除的玩家名称'})
    
    if player_name == '管理员':
        return jsonify({'success': False, 'message': '不能删除管理员账号'})
    
    success = GameState.delete_player(player_name)
    
    if success:
        return jsonify({'success': True, 'message': f'玩家 {player_name} 已被删除'})
    else:
        return jsonify({'success': False, 'message': '删除失败，玩家不存在'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)