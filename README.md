# Code Quest Island

一个基于 Flask 的编程学习游戏，通过闯关答题的方式学习 Python 编程。

## 功能特点

- 🎮 **游戏化学习**: 将编程学习转化为有趣的闯关游戏
- 🗺️ **世界地图**: 探索多个区域，每个区域包含多个关卡
- 🏆 **成就系统**: 完成特定任务解锁成就
- 🛒 **商店系统**: 使用金币购买装备和提示卷轴
- 📊 **排行榜**: 查看所有玩家的闯关进度
- 🤖 **NPC 交互**: 与 NPC 对话获取任务和奖励
- 📷 **头像自定义**: 支持上传自定义头像
- 💾 **自动保存**: 游戏进度自动保存，支持跨设备继续游戏

## 技术栈

- **后端**: Flask 2.0+
- **数据库**: PostgreSQL / SQLite
- **前端**: HTML5, CSS3, JavaScript
- **部署**: Render

## 项目结构

```
code-quest-island/
├── app.py                 # Flask 应用主入口
├── config.py              # 配置文件
├── database.py            # 数据库操作模块
├── game_state.py          # 游戏状态管理
├── player.py              # 玩家类
├── levels.py              # 关卡管理
├── quests.py              # 任务管理
├── shop.py                # 商店系统
├── achievements.py        # 成就系统
├── equipment.py           # 装备系统
├── boss.py                # Boss 系统
├── static/
│   ├── css/style.css      # 样式文件
│   ├── js/game.js         # 游戏逻辑
│   └── images/            # 图片资源
├── templates/
│   ├── base.html          # 基础模板
│   ├── index.html         # 登录页面
│   └── game.html          # 游戏页面
├── exercises.json         # 题目数据库
├── npc_config.json        # NPC 配置
├── admin_config.json      # 管理员配置
├── requirements.txt       # Python 依赖
├── render.yaml            # Render 部署配置
├── Dockerfile             # Docker 配置
├── docker-compose.yml     # Docker Compose 配置
├── start.bat              # Windows 启动脚本
└── start.sh               # Linux/Mac 启动脚本
```

## 快速开始

### 本地开发

```bash
# 克隆项目
git clone https://github.com/tokks/fufu-code-quest-island.git
cd fufu-code-quest-island

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt

# 设置环境变量
set DATABASE_URL=postgresql://user:password@host:5432/dbname
set SECRET_KEY=your_secret_key

# 启动开发服务器
python app.py
```

### 部署到 Render

1. Fork 本项目到你的 GitHub 账户
2. 在 [Render](https://render.com/) 创建新的 Web 服务
3. 连接你的 GitHub 仓库
4. 配置环境变量：
   - `DATABASE_URL`: PostgreSQL 数据库连接字符串
   - `SECRET_KEY`: 任意长字符串用于 session 加密
5. 部署完成后访问你的服务地址

### 使用 Render PostgreSQL

1. 在 Render Dashboard 中创建 PostgreSQL 数据库（Free 版本可用）
2. 复制 Internal Database URL
3. 在你的 Web 服务环境变量中添加 `DATABASE_URL`

## 游戏玩法

1. **创建角色**: 在登录页面输入唯一昵称创建角色
2. **探索世界**: 在世界地图上选择区域进行探索
3. **完成关卡**: 每个关卡包含选择题或编程题
4. **获取奖励**: 答对题目获得金币和经验
5. **提升等级**: 积累经验提升等级，解锁更多区域
6. **购买装备**: 在商店购买装备提升属性
7. **使用提示**: 消耗提示卷轴查看答案

## 管理员功能

- 管理玩家账户（发放金币、删除账户）
- 配置 NPC 名称和头像
- 查看所有玩家数据

## 许可证

MIT License