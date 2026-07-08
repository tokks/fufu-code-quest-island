from levels import LevelManager

lm = LevelManager()
regions = lm.get_all_regions()
print('Regions:', [r['id'] for r in regions])

next_region = lm.get_next_region('day1')
print('Next region after day1:', next_region)

levels = lm.get_levels_for_region('day1')
print('day1 levels:', [l['id'] for l in levels])

from game_state import GameState
from player import Player

player = Player('test')
state = GameState()
state.player = player

print('\nInitial unlocked regions:', state.unlocked_regions)

state.unlock_region('day2')
print('After unlocking day2:', state.unlocked_regions)

completed = ['day1_q1', 'day1_q2', 'day1_q3', 'day1_q4', 'day1_q5', 
             'day1_q6', 'day1_q7', 'day1_q8', 'day1_q9', 'day1_q10',
             'day1_q11', 'day1_q12', 'day1_q13']
state.completed_quests = completed

all_levels = lm.get_levels_for_region('day1')
all_done = all(l['id'] in completed for l in all_levels)
print('All day1 levels completed:', all_done)

if all_done:
    next_reg = lm.get_next_region('day1')
    print('Next region to unlock:', next_reg)
    state.unlock_region(next_reg)
    print('Final unlocked regions:', state.unlocked_regions)
