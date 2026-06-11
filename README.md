#  **SIEM-Lite: Security Information and Event Management System**

A lightweight **Security Information and Event Management (SIEM)** system built using **Python, Flask, SQLite, Docker, and AWS EC2**.

SIEM-Lite simulates real-world cyber attacks by generating logs, detecting suspicious activities through multiple detection rules, storing alerts in a database, and visualizing them through a real-time Security Operations Center (SOC) dashboard.

---

# 🚀 Features

*  Log Generator Simulation
*  Incremental Log Collection
*  Brute Force Detection
*  Password Spray Detection
*  Suspicious File Access Detection
*  Unauthorized Access Flood Detection
*  Privilege Escalation Detection
*  SQLite Alert Storage
*  Flask SOC Dashboard
*  Alert Statistics
*  Severity Counters
*  Alert Distribution Pie Chart
*  Engine Status Monitoring
*  Auto Refresh Dashboard
*  Docker Containerization
*  AWS EC2 Deployment

---

# 🏗️ Architecture

```
                 +----------------------+
                 |   Log Generator      |
                 +----------+-----------+
                            |
                            v
                    +---------------+
                    |   logs.txt    |
                    +-------+-------+
                            |
                            v
                  +-------------------+
                  |  Log Collector    |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  |    SIEM Engine    |
                  +---------+---------+
                            |
   ---------------------------------------------------------
   |            |              |            |               |
   v            v              v            v               v

Brute      Password      File Access   Unauthorized   Privilege
Force       Spray         Detector        Access      Escalation
Detector    Detector                      Detector      Detector

                            |
                            v

                  +-------------------+
                  |  Alert Manager    |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  |  SQLite Database  |
                  +---------+---------+
                            |
                            v
                  +-------------------+
                  | Flask Dashboard   |
                  +-------------------+
```

---

# ⚙️ Technologies Used

* Python
* Flask
* SQLite
* HTML
* CSS
* JavaScript
* Chart.js
* Docker
* AWS EC2
* Git
* GitHub

---

# 📂 Project Structure

```
SIEM-LITE/

├── agents/
│   ├── log_generator.py
│   └── logs.txt
│
├── backend/
│   ├── alert_manager.py
│   ├── log_collector.py
│   ├── threat_detector.py
│   ├── password_spray_detector.py
│   ├── file_access_detector.py
│   ├── unauthorized_access.py
│   ├── privilege_escalation.py
│   ├── siem_engine.py
│   └── log_state.txt
│
├── database/
│   ├── alerts.db
│   ├── database.py
│   └── view_alerts.py
│
├── frontend/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# ** Running the Project Locally**

## 1. Clone the Repository

```bash
git clone https://github.com/Roshanshaik78609/SIEM-LITE.git
cd SIEM-LITE
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Initialize the Database (Run Once)

```bash
cd database
python database.py
```

---

## 5. Start the Log Generator

Open **Terminal 1**

```bash
cd agents
python log_generator.py
```

---

## 6. Start the SIEM Engine

Open **Terminal 2**

```bash
cd backend
python siem_engine.py
```

---

## 7. Start the Flask Dashboard

Open **Terminal 3**

```bash
cd frontend
python app.py
```

Visit:

```
http://127.0.0.1:5000
```

The dashboard refreshes automatically every 5 seconds and displays newly detected alerts.

---

# 🐳 Docker

Build the image:

```bash
docker build -t siem-lite .
```

Run the container:

```bash
docker run -p 5000:5000 siem-lite
```

List running containers:

```bash
docker ps
```

View logs:

```bash
docker logs <container_id>
```

Stop container:

```bash
docker stop <container_id>
```

Remove container:

```bash
docker rm <container_id>
```

---

# ☁️ Deploying on AWS EC2

Clone the repository:

```bash
git clone https://github.com/Roshanshaik78609/SIEM-LITE.git
cd SIEM-LITE
```

Build the Docker image:

```bash
docker build -t siem-lite .
```

Run the Docker container:

```bash
docker run -d -p 5000:5000 --name siem-lite-app siem-lite
```

Verify the running container:

```bash
docker ps
```

View container logs:

```bash
docker logs siem-lite-app
```

Ensure **TCP Port 5000** is open in the EC2 Security Group.

Access the dashboard:

```
http://<EC2-PUBLIC-IP>:5000
```

---

# 🎯 Future Improvements

* Email Alert Notifications
* Slack Integration
* ELK Stack Integration
* Machine Learning Based Anomaly Detection
* Threat Intelligence Feed Integration
* Multi-Agent Log Collection
* Role-Based User Authentication

---

# 👨‍💻 Author

**Roshan Shaik**

**MCA Student | Cybersecurity Enthusiast | Cloud & Security Learner**

GitHub:
https://github.com/Roshanshaik78609

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
