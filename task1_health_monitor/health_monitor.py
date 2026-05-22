import psutil
import logging
from datetime import datetime

# Setup log file
logging.basicConfig(
    filename='health_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

logging.info("="*40)
logging.info(f"Health Check Started: {datetime.now()}")
logging.info("="*40)

# Check CPU usage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage: {cpu_usage}%")
logging.info(f"CPU Usage: {cpu_usage}%")  #

if cpu_usage > 80:
    print("ALERT: CPU usage is too high!")
    logging.warning("ALERT: CPU usage is too high!")  # 
else:
    print("CPU usage is normal.")
    logging.info("CPU usage is normal.")  # ← add this

#check memory usages
memory = psutil.virtual_memory()
memory_usage = memory.percent
print(f"Memory Usage: {memory_usage}%")
logging.info(f"Memory Usages: {memory_usage}%")

#Alert if memory exceed threshold
if memory_usage > 90:
    print("ALERT: memory use is too high!")
    logging.warning("ALERT: memory use is too high!")
else:
    print("memory use is normal")
    logging.info("memory use is normal")

# check disk space

disk = psutil.disk_usage('/')
disk_usage = disk.percent
print(f"Disk Usage: {disk_usage}%")
logging.info(f"Disk Usage: {disk_usage}%")

# Alert if Disk exceeds threshold
if disk_usage > 90:
    print("ALERT: Disk space is too low!")
    logging.warning("ALERT: Disk space is too low!")
else:
    print("disk use is normal")
    logging.info("disk use is normal")

# Check Running Processes
process_count = len(psutil.pids())
print(f"Running Processes: {process_count}")
logging.info(f"Running Process: { process_count}")

# Alert if processes exceed threshold
if process_count > 300:
    print("ALERT: Too many processes running!")
    logging.warning("ALERT: Too many processes running!")
else:
    print("Process count is normal.")
    logging.info("Process count is normal")