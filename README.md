# QA Assessment

This project contains two automation scripts written in Python.

## Task 1 - System Health Monitor
Monitors the health of a system by checking:
- CPU Usage (Alert if > 80%)
- Memory Usage (Alert if > 90%)
- Disk Usage (Alert if > 90%)
- Running Processes (Alert if > 300)

Results are saved to `health_monitor.log`

## Task 2 - Application Health Checker
Checks the uptime of web applications by:
- Checking HTTP status codes
- Measuring response time (Alert if > 3 seconds)
- Detecting if application is UP ✅ or DOWN ❌

Results are saved to `app_health.log`

## Requirements
Install required libraries:
pip install psutil requests

## How to Run

### Task 1:
python task1_health_monitor/health_monitor.py

### Task 2:
python task2_app_health_checker/app_health_checker.py