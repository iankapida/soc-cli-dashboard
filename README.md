# 🛡️ SOC CLI Dashboard

A lightweight, terminal-based Security Operations Center (SOC) dashboard and log parsing tool written in Python. Built to help security analysts quickly parse Linux authentication logs, detect brute-force attempts, and perform initial threat triage directly from the command line.

## ✨ Features

- **Authentication Log Parser:** Filters SSH logs for `Failed password` and `Accepted password` events.
- **Brute-Force Detection:** Automatically flags IP addresses exceeding failure thresholds.
- **Interactive CLI Menu:** Fast navigation without requiring complex command-line arguments.
- **Zero Heavy Dependencies:** Runs entirely on native Python 3 modules for maximum portability.

## 🚀 Quick Start

### Prerequisites
- Python 3.x installed
- Git

### Installation

Clone the repository and enter the directory:

```bash
git clone [https://github.com/iankapida/soc-cli-dashboard.git](https://github.com/iankapida/soc-cli-dashboard.git)
cd soc-cli-dashboard
