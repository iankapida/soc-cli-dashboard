# SOC CLI Dashboard

A lightweight, command-line security operations center (SOC) utility written in Python for parsing authentication logs, detecting brute-force attack patterns, and generating automated incident reports. Built for efficiency, automation, and portability (fully tested and executed in mobile Linux/Termux environments).

## Features
- **Robust Log Parsing:** Safely processes Linux authentication logs (`auth.log`) while handling file-not-found exceptions and malformed data lines.
- **Brute-Force Detection:** Flags IP addresses exceeding configurable failure thresholds and sorts them by attack frequency.
- **Automated Test Suite:** Includes an integrated verification script (`verify.py`) to validate core logic and error handling.
- **Flexible CLI & Export:** Supports custom log paths, adjustable thresholds via `argparse`, and JSON incident report exporting.

## Installation & Setup

Clone the repository and navigate into the directory:
```bash
git clone [https://github.com/iankapida/soc-cli-dashboard.git](https://github.com/iankapida/soc-cli-dashboard.git)
cd soc-cli-dashboard
