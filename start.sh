#!/bin/bash

echo "======================================"
echo "  编程闯关岛 - 部署启动脚本"
echo "======================================"

if [ ! -d "saves" ]; then
    mkdir saves
    chmod 755 saves
    echo "[OK] 创建saves目录"
fi

if [ -f ".env" ]; then
    echo "[OK] 环境配置文件已存在"
else
    echo "[INFO] 创建默认环境配置文件"
    cat > .env << EOF
FLASK_ENV=production
SECRET_KEY=code_quest_island_production_key
EOF
fi

echo ""
echo "选择启动方式:"
echo "1. 开发模式 (Flask内置服务器)"
echo "2. 生产模式 (Gunicorn)"
echo "3. Docker模式 (推荐)"
read -p "请输入选择 [1/2/3]: " choice

case $choice in
    1)
        echo "[INFO] 启动开发模式..."
        python app.py
        ;;
    2)
        echo "[INFO] 启动生产模式..."
        gunicorn --bind 0.0.0.0:5000 --workers=4 --timeout=120 app:app
        ;;
    3)
        echo "[INFO] 启动Docker模式..."
        docker-compose up -d --build
        echo "[OK] 容器已启动"
        echo ""
        echo "查看日志: docker-compose logs -f"
        echo "停止服务: docker-compose down"
        echo "查看状态: docker-compose ps"
        ;;
    *)
        echo "[ERROR] 无效选择"
        exit 1
        ;;
esac
