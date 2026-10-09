import time
import random
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel
from rich.layout import Layout

console = Console()

# Simulated IP reputation / threshold logic
FAILED_THRESHOLD = 3
ip_fail_counts = {}

def generate_mock_log():
    sample_ips = ["192.168.1.50", "10.0.0.12", "185.220.101.5", "192.168.1.105"]
    actions = ["LOGIN_SUCCESS", "FAILED_LOGIN", "FILE_DOWNLOAD", "SUDO_EXEC"]
    
    ip = random.choice(sample_ips)
    action = random.choice(actions)
    timestamp = time.strftime("%H:%M:%S")
    
    # Anomaly detection check
    status = "NORMAL"
    if action == "FAILED_LOGIN":
        ip_fail_counts[ip] = ip_fail_counts.get(ip, 0) + 1
        if ip_fail_counts[ip] >= FAILED_THRESHOLD:
            status = "ANOMALY (Brute Force Detected)"
    
    return {"time": timestamp, "ip": ip, "action": action, "status": status}

def generate_table(logs):
    table = Table(title="SOC Real-Time Log Monitor", expand=True)
    table.add_column("Timestamp", style="cyan", no_wrap=True)
    table.add_column("Source IP", style="magenta")
    table.add_column("Action", style="green")
    table.add_column("Threat Status", style="bold yellow")

    for log in logs[-10:]:  # Display last 10 entries
        status_style = "bold red" if "ANOMALY" in log["status"] else "dim green"
        table.add_row(
            log["time"],
            log["ip"],
            log["action"],
            f"[{status_style}]{log['status']}[/{status_style}]"
        )
    return table

def main():
    logs = []
    console.print("[bold green]Starting SOC CLI Dashboard...[/bold green]")
    time.sleep(1)
    
    with Live(generate_table(logs), refresh_per_second=2, console=console) as live:
        for _ in range(20):  # Runs for 20 simulation steps
            time.sleep(1)
            logs.append(generate_mock_log())
            live.update(generate_table(logs))

if __name__ == "__main__":
    main()
