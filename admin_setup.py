import json

ADMIN_CONFIG = {
    'admin_username': 'admin',
    'admin_password': 'admin123',
    'admin_gold': 9999,
    'admin_level': 99
}

with open('admin_config.json', 'w', encoding='utf-8') as f:
    json.dump(ADMIN_CONFIG, f, ensure_ascii=False, indent=2)

print("管理员配置文件已创建")