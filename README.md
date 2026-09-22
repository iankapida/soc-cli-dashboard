# Enterprise Security Operations Center (SOC) - CLI Dashboard

A modular, Python-driven Security Operations Center command-line interface designed for automated threat detection, security auditing, and incident response triage.

## 🚀 Overview
The **SOC CLI Dashboard** is built to streamline security operations by integrating multiple diagnostic and defensive security phases into a single interactive tool. Designed with an 8-phase pipeline architecture, it bridges automated scanning with modular data analysis.

## 🛠️ Operational Modules (8-Phase Pipeline)

* **[1] Ultimate Master Orchestrator:** Executes a full end-to-end 8-phase security automation pipeline sequentially.
* **[2] Proactive Port Scanner:** Rapidly maps open ports to identify potential network exposure and entry vectors.
* **[3] File Integrity Monitor (FIM):** Tracks system and configuration files for unauthorized or malicious modifications.
* **[4] Cloud API & JWT Token Auditor:** Evaluates cloud configurations and checks JSON Web Tokens for security flaws.
* **[5] IAM Privilege & Access Control Auditor:** Audits user privileges and access rights to flag escalation risks.
* **[6] DFIR Forensic Artifact Parser:** Processes digital forensics artifacts to assist with threat hunting and incident triage.
* **[7] Network Flow Anomaly Analyzer:** Inspects traffic patterns to detect behavioral deviations and anomalous spikes.
* **[8] Endpoint Security Monitor:** Evaluates endpoint telemetry and host-level security indicators.

## 💻 Tech Stack
* **Language:** Python
* **Environment:** Linux / Termux
* **Architecture:** Modular CLI Design

## ⚙️ Usage
Run the dashboard script from your terminal:
```bash
python soc_dashboard.py
