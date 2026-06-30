import sys
import json
import os
sys.path.insert(0, '.')
from parse_exercises import parse_all_days

try:
    questions = parse_all_days()
    total = len(questions)
    
    with open('exercises.json', 'w', encoding='utf-8') as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    
    with open('final_result.txt', 'w', encoding='utf-8') as f:
        f.write(f'总题目数: {total}\n')
        
        days = {}
        for q in questions:
            day = q.get('day', 'unknown')
            days[day] = days.get(day, 0) + 1
        
        for day in sorted(days.keys()):
            f.write(f'Day {day}: {days[day]}题\n')
    
    with open('final_result.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    
    with open('final_result.txt', 'w', encoding='utf-8') as f:
        f.write(content)
        
except Exception as e:
    with open('error_log.txt', 'w', encoding='utf-8') as f:
        f.write(f'Error: {str(e)}')