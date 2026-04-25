import psutil

def get_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    battery = psutil.sensors_battery()

    battery_percent = battery.percent if battery else "Unknown"

    return {
        "cpu_percent": cpu,
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "battery_percent": battery_percent
    }

def get_health_verdict(health):
    cpu = health["cpu_percent"]
    memory = health["memory_percent"]
    disk = health["disk_percent"]
    battery = health["battery_percent"]

    if cpu > 85 or memory > 85 or disk > 90:
        return "Are you running a heavy workload? Consider closing some applications to improve performance."
    elif cpu < 60 and memory > 70 and disk > 80:
        return "System is currently stable, but keep an eye on memory and disk usage to prevent potential issues."
    elif battery < 20:
        return "Battery level is low. Consider plugging in your device."
    elif battery < 20 and (cpu > 70 or memory > 70):
        return "Working hard, I see! Just make sure to plug in soon, especially if you're pushing the limits of your CPU or memory."
    else:
        return "All systems stable. Ready for action!"
    
def format_system_report():
    health = get_system_health()
    verdict = get_health_verdict(health)

    return (
        f"CPU Usage: {health['cpu_percent']}%\n"
        f"Memory Usage: {health['memory_percent']}%\n"
        f"Disk Usage: {health['disk_percent']}%\n"
        f"Battery: {health['battery_percent']}%\n"
        f"Verdict: {verdict}\n"
    )