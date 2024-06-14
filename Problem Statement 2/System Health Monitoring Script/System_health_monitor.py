import psutil
import logging
import time

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define thresholds
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 80.0  # in percentage
INTERVAL = 10  # in seconds

def check_cpu_usage():
    """Check CPU usage and log if it exceeds the threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    return cpu_usage

def check_memory_usage():
    """Check memory usage and log if it exceeds the threshold."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f"High Memory usage detected: {memory_usage}%")
    return memory_usage

def check_disk_usage():
    """Check disk usage and log if it exceeds the threshold."""
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f"High Disk usage detected: {disk_usage}%")
    return disk_usage

def log_running_processes():
    """Log running processes."""
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'username'])]
    logging.info(f"Running processes: {processes}")

def monitor_system():
    """Monitor the system health and log if thresholds are exceeded."""
    while True:
        cpu = check_cpu_usage()
        memory = check_memory_usage()
        disk = check_disk_usage()
        log_running_processes()

        print(f"CPU Usage: {cpu}%, Memory Usage: {memory}%, Disk Usage: {disk}%")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    monitor_system()

