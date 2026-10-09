import time
import random
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from threat_intel import check_ip_reputation

def generate_log_entry():
    ips = ["192.168.1.105", "185.220.101.5", "10.0.0.15", "172.16.0.4"]
    actions = ["LOGIN_SUCCESS", "LOGIN_FAILED", "FILE_DOWNLOAD", "PORT_SCAN"]
    ip = random.choice(ips)
    action = random.choice(actions)
    
    # Enrich with threat intelligence
    intel = check_ip_reputation(ip)
    
    return {
        "timestamp": time.strftime("%H:%M:%S"),
        "ip": ip,
        "action": action,
        "abuse_score": intel["abuse_score"],
        "status": intel["status"]
    }

def generate_table(log_history):
    table = Table(title="Live SOC Incident Telemetry", expand=True)
    table.add_column("Timestamp", justify="center", style="cyan")
    table.add_column("Source IP", justify="center", style="magenta")
    table.add_column("Action", justify="left", style="yellow")
    table.add_column("Abuse Score", justify="center", style="bold red")
    table.add_column("Status", justify="center")

    for log in log_history[-10:]:
        status_style = "[bold red]SUSPICIOUS[/bold red]" if log["status"] == "SUSPICIOUS" else "[bold green]CLEAN[/bold green]"
        table.add_row(
            log["timestamp"],
            log["ip"],
            log["action"],
            str(log["abuse_score"]),
            status_style
        )
    return table

if __name__ == "__main__":
    log_history = []
    print("Starting enriched SOC Dashboard (Press CTRL+C to exit)...")
    try:
        with Live(generate_table(log_history), refresh_per_second=2) as live:
            while True:
                log_history.append(generate_log_entry())
                live.update(generate_table(log_history))
                time.sleep(1)
    except KeyboardInterrupt:
        print("\nDashboard stopped.")
