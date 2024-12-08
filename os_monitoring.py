import psutil
import time
import logging
from datetime import datetime

# Thresholds for alerting

# in percentages
CPU_THRESHOLD = 80  
MEMORY_THRESHOLD = 80  
DISK_THRESHOLD = 85  


ALERT_LOG_FILE = "system_alerts.log"  

# Initialize logging
logging.basicConfig(filename=ALERT_LOG_FILE, level=logging.INFO, 
                    format="%(asctime)s - %(message)s")

def log_alert(message):
    """Logs alerts to a log file."""
    print(message)  # Print to console as well
    logging.info(message)

def check_cpu_usage():
    """Check if CPU usage exceeds the defined threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    print('Cpu usage is: '+str(cpu_usage)+'')
    if cpu_usage > CPU_THRESHOLD:
        log_alert(f"ALERT: CPU Usage is at {cpu_usage}% - Exceeds {CPU_THRESHOLD}% threshold.")

def check_memory_usage():
    """Check if memory usage exceeds the defined threshold."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    print('Memory usage is: '+str(memory_usage)+'')
    if memory_usage > MEMORY_THRESHOLD:
        log_alert(f"ALERT: Memory Usage is at {memory_usage}% - Exceeds {MEMORY_THRESHOLD}% threshold.")

def check_disk_usage():
    """Check if disk usage exceeds the defined threshold."""
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    print('Disk usage is: '+str(disk_usage)+'')
    if disk_usage > DISK_THRESHOLD:
        log_alert(f"ALERT: Disk Usage is at {disk_usage}% - Exceeds {DISK_THRESHOLD}% threshold.")

def check_network_usage():
    """Check the network usage (bytes sent and received)."""
    net_io = psutil.net_io_counters()
    sent = net_io.bytes_sent / (1024 ** 2)  # MB
    recv = net_io.bytes_recv / (1024 ** 2)  # MB
    log_alert(f"Network Usage: {sent:.2f} MB Sent | {recv:.2f} MB Received")

def monitor_processes():
    """Monitor processes and alert if any process uses too much CPU or memory."""

    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            cpu_usage = proc.info['cpu_percent']
            memory_usage = proc.info['memory_percent']
            if cpu_usage is not None and cpu_usage > 50:
                log_alert(f"ALERT: Process '{proc.info['name']}' (PID: {proc.info['pid']}) using {cpu_usage}% CPU")
            if memory_usage is not None and memory_usage > 50:
                log_alert(f"ALERT: Process '{proc.info['name']}' (PID: {proc.info['pid']}) using {memory_usage}% Memory")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            # Ignore processes that no longer exist or can't be accessed
            pass

def get_system_info():
    """Gathers basic system information."""
    uname = psutil.users()
    print(f"System Users: {uname}")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")
    print(f"Disk Usage: {psutil.disk_usage('/').percent}%")
    print(f"Network Sent/Received: {psutil.net_io_counters().bytes_sent / (1024 ** 2):.2f} MB / {psutil.net_io_counters().bytes_recv / (1024 ** 2):.2f} MB")

def monitor_system():
    """Monitor the system at regular intervals."""
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_network_usage()
        monitor_processes()
        print()
        print()
        print('-------------------------------------------------------------------------')

        time.sleep(3)  # Sleep for 3 seconds before checking again

if __name__ == "__main__":
    log_alert("System Monitoring Started")
    print()
    try:
        monitor_system()  # Start monitoring system
    except KeyboardInterrupt:
        print()
        log_alert("System Monitoring Stopped by User")
