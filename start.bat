@echo off
echo 🚀 Starting Water Supply Dashboard...
cd /d C:\Users\kaviy\water-supply-dashboard

echo 📡 Starting Backend Server...
start "Backend Server" cmd /k "python backend\app.py"

timeout /t 3 /nobreak >nul

echo 📊 Starting Simulator...
start "Simulator" cmd /k "python simulator\simulate.py"

timeout /t 2 /nobreak >nul

echo 🌐 Opening Dashboard in Browser...
start frontend\index.html

echo ✅ All services started!
exit