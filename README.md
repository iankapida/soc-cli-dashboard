# 🛡️ SOC CLI Real-Time Dashboard & Threat Intel Engine

An automated, terminal-based Security Operations Center (SOC) dashboard built in Python for mobile Termux and Linux environments. Features real-time log monitoring, live UI rendering with `rich`, threat intelligence IP scoring, persistent SQLite database logging, and automated test suites.

## 🚀 Key Features
- **Real-Time Terminal UI**: Displays active security telemetry powered by `rich`.
- **Threat Intelligence Integration**: Automatic IP reputation checks with simulated fallbacks and REST API readiness (AbuseIPDB).
- **SQLite Data Persistence**: Automatically logs incident telemetry to a persistent SQLite relational database (`soc_incidents.db`).
- **Automated Testing**: Unit test suite implemented with `pytest` covering API logic and database interactions.
- **Mobile-First SOC Engineering**: Engineered and optimized for execution within Termux on Android devices.

## 📦 Installation & Setup

1. **Clone the Repository**:
   ```bash
   git clone [https://github.com/iankapida/soc-cli-dashboard.git](https://github.com/iankapida/soc-cli-dashboard.git)
   cd soc-cli-dashboard
pip install rich requests pytest
python soc_database.py
python dashboard.py
pytest test_soc.py
