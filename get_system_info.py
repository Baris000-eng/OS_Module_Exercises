import platform
import psutil
import socket
from datetime import datetime, timedelta  # Import timedelta from datetime
import time

def get_system_info():
    # Basic System Info
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"Processor: {platform.processor()}")
    print(f"CPU Cores: {psutil.cpu_count(logical=False)} (Physical), {psutil.cpu_count(logical=True)} (Logical)")

    # CPU Usage (Current Load)
    print(f"Current CPU Usage: {psutil.cpu_percent(interval=1)}%")

    # CPU Temperature (if supported by system)
    try:
        cpu_temp = psutil.sensors_temperatures()
        if 'coretemp' in cpu_temp:
            for temp in cpu_temp['coretemp']:
                print(f"CPU Temperature: {temp.current}°C")
        else:
            print("CPU Temperature: Not available")
    except Exception as e:
        print(f"Error fetching CPU temperature: {e}")

    # Memory Info
    total_memory = psutil.virtual_memory().total / (1024 ** 3)
    used_memory = psutil.virtual_memory().used / (1024 ** 3)
    memory_percent = psutil.virtual_memory().percent
    print(f"Total Memory: {total_memory:.2f} GB")
    print(f"Used Memory: {used_memory:.2f} GB")
    print(f"Memory Usage: {memory_percent}%")

    # Swap Memory Info
    total_swap = psutil.swap_memory().total / (1024 ** 3)
    used_swap = psutil.swap_memory().used / (1024 ** 3)
    swap_percent = psutil.swap_memory().percent
    print(f"Total Swap: {total_swap:.2f} GB")
    print(f"Used Swap: {used_swap:.2f} GB")
    print(f"Swap Usage: {swap_percent}%")

    # Disk Usage
    disk_usage = psutil.disk_usage('/')
    print(f"Disk Usage: {disk_usage.percent}%")
    print(f"Total Disk Space: {disk_usage.total / (1024 ** 3):.2f} GB")
    print(f"Used Disk Space: {disk_usage.used / (1024 ** 3):.2f} GB")
    print(f"Free Disk Space: {disk_usage.free / (1024 ** 3):.2f} GB")

    # Disk I/O statistics
    disk_io = psutil.disk_io_counters()
    print(f"Disk Read: {disk_io.read_bytes / (1024 ** 2):.2f} MB")
    print(f"Disk Write: {disk_io.write_bytes / (1024 ** 2):.2f} MB")

    # Network Info
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Host Name: {hostname}")
    print(f"IP Address: {ip_address}")

    # Network Sent and Received data
    net_io = psutil.net_io_counters()
    print(f"Network Sent: {net_io.bytes_sent / (1024 ** 2):.2f} MB")
    print(f"Network Recv: {net_io.bytes_recv / (1024 ** 2):.2f} MB")

    # Network Interfaces Info (for more detailed network interface data)
    net_if_addrs = psutil.net_if_addrs()
    for interface, addrs in net_if_addrs.items():
        print(f"Network Interface: {interface}")
        for addr in addrs:
            if addr.family == socket.AF_INET:
                print(f"  IPv4 Address: {addr.address}")
            elif addr.family == socket.AF_INET6:
                print(f"  IPv6 Address: {addr.address}")
            elif addr.family == socket.AF_LINK:
                print(f"  MAC Address: {addr.address}")

    # Battery Info (if on a laptop)
    battery = psutil.sensors_battery()
    if battery:
        print(f"Battery: {battery.percent}% - {'Charging' if battery.power_plugged else 'Discharging'}")
        # Use timedelta correctly
        time_left = timedelta(seconds=battery.secsleft) if battery.secsleft != -1 else 'N/A'
        print(f"Time Left: {time_left}")
    else:
        print("Battery: Not available (Not on a laptop?)")

    # Process Info
    process_count = len(psutil.pids())
    print(f"Total Processes Running: {process_count}")

    # Uptime Info
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.now() - boot_time
    print(f"System Uptime: {str(uptime).split('.')[0]}")

    # Current Time
    print(f"Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Call the function to print all info
get_system_info()

