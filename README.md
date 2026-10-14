# Enterprise Security Operations Center (SOC) CLI Dashboard & Automation Suite

An enterprise-grade, modular Security Operations Center (SOC) telemetry, monitoring, and incident response platform engineered entirely in Python and Bash for terminal environments.

This repository features 58 primary scripts and modular subdirectories providing end-to-end security orchestration, threat intelligence integration, real-time log parsing, network packet inspection, and behavioral threat detection.

---

## Key Features & Functional Modules

### 1. Log Forensics & Parsing (`parser.py`, `log_forensics.py`)
* Extracts indicators of compromise (IOCs) such as malicious IP addresses, failed authentication spikes, and timestamps from system logs using optimized regular expressions (`re`).
* Normalizes multi-line unstructured syslog formats into structured JSON reports.

### 2. Behavioral Threat Detection (`brute_detector.py`)
* Dynamically monitors traffic streams for high-frequency access failures.
* Flags brute-force and credential-stuffing patterns based on configurable threshold heuristics.

### 3. Network Reconnaissance & Packet Analysis (`port_scanner.py`, `packet_analyzer.py`)
* Multi-threaded TCP/UDP port scanner designed to assess target system surface exposure.
* Scapy-inspired network packet dissector evaluating frame headers, flags (e.g., SYN scans), and payload anomalies.

### 4. Containment & Firewall Rule Management (`firewall_blocker.py`)
* Automated containment script that translates flagged attacker IPs directly into persistent rule lists (`firewall_deny.list`).

### 5. Threat Intelligence & Alerting (`threat_intel.py`, `alert_notifier.py`)
* Interfaces with threat intelligence lookup feeds to cross-reference target IPs against known bad actor databases.
* Generates structured incident alerts for SOC analyst notification pipelines.

### 6. Operations Telemetry, Archiving & SIEM Aggregation (`soc_metrics.py`, `log_archiver.py`, `siem_aggregator.py`)
* Archives processed log files securely into backup storage (`archives/`).
* Compiles workspace telemetry, active blocklists, and honeytoken statuses into a centralized master report (`siem_master_report.json`).

### 7. Deception Engineering & Canary Tripwires (`honeytoken.py`)
* Deploys strategic canary decoy files (`aws_credentials_backup.json`) to detect unauthorized internal file access attempts.

### 8. Bash Workflow Orchestration (`soc_pipeline.sh`)
* Executable Bash script chaining traffic simulation, threat detection, and SIEM aggregation into an automated sequence.

---

## Directory Structure

```text
soc-cli-dashboard/
├── dashboard.py               # Core operational interface
├── soc_pipeline.sh            # Automated Bash orchestrator
├── brute_detector.py          # Behavioral threat detection engine
├── log_forensics.py           # Regex IOC extraction and log parser
├── packet_analyzer.py         # Network frame & packet dissector
├── firewall_blocker.py        # Automated rule manager & IP blocker
├── threat_intel.py            # Threat intelligence lookup client
├── honeytoken.py              # Tripwire canary file monitor
├── siem_aggregator.py         # Centralized SIEM master reporting
├── soc_metrics.py             # Operational health metrics engine
├── log_archiver.py            # Automated log rotation and backup
├── traffic_generator.py       # Attack vector & traffic simulator
├── soc_lab/                   # Lab testing configurations & data
└── soc_toolkit/               # Modular security utility scripts
