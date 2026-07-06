@echo off
chcp 65001 >nul
echo ======================================
echo   编程闯关岛 - 部署启动脚本
echo ======================================
echo.

if not exist saves (
    mkdir saves
    echo [OK] 创建saves目录
)

echo.
echo 选择启动方式:
echo 1. 开发模式 (Flask内置服务器)
echo 2. 生产模式 (Gunicorn)
echo.
set /p choice=请输入选择 [1/2]: 

if "%choice%"=="1" (
    echo [INFO] 启动开发模式...
    echo 访问地址: http://localhost:5000
    python app.py
) else if "%choice%"=="2" (
    echo [INFO] 启动生产模式...
    echo 访问地址: http://localhost:5000
    gunicorn --bind 0.0.0.0:5000 --workers=4 --timeout=120 app:app
) else (
    echo [ERROR] 无效选择
    pause
    exit /b 1
)
