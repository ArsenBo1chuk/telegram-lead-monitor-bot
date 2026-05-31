# 🔍 Telegram Keyword Monitor

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge)
![Telethon](https://img.shields.io/badge/Telethon-Latest-success?style=for-the-badge)
![Telegram](https://img.shields.io/badge/Telegram-Monitoring-2CA5E0?style=for-the-badge)


A lightweight Telegram monitoring tool built with Python and Telethon that continuously scans selected Telegram channels and chats for predefined keywords and instantly forwards matching messages to a specified recipient.

Designed for:

- 🎯 Lead generation
- 💼 Job opportunity tracking
- 📢 Brand monitoring
- 🛒 Client acquisition
- 🔎 Market research

---

## ✨ Features

### 🔍 Keyword Monitoring

Monitor hundreds of Telegram channels simultaneously.

Whenever a message contains one of your predefined keywords, the system instantly detects it.

### ⚡ Real-Time Notifications

Receive alerts directly in:

- Saved Messages
- Personal Telegram account
- Any configured Telegram user

### 📂 Configurable Sources

Manage monitored chats through a simple text file:

```text
chats.txt
```

No code modifications required.

### 🏷️ Custom Keyword Lists

Define unlimited keywords:

```text
python
telegram bot
cpp
website
developer
```

Stored in:

```text
keywords.txt
```

### 🚫 Duplicate Protection

The system tracks processed messages and prevents duplicate notifications.

### 📝 Logging System

Every detection is automatically written to log files:

```text
2026-05-30 18:20:01 | Chat: IT Jobs UA | Keyword: python
```

### 📊 Persistent History

Processed message IDs are stored locally to survive restarts.

---

## 🏗 Architecture

```text
Telegram Channels
         │
         ▼
    Telethon Client
         │
         ▼
 Message Listener
         │
         ▼
 Keyword Matcher
         │
 ┌───────┴────────┐
 ▼                ▼
 Logger      Notification
 ▼                ▼
logs.txt      Telegram DM
```

---

## 📁 Project Structure

```text
telegram-keyword-monitor/
│
├── main.py
├── config.py
│
├── keywords.txt
├── chats.txt
│
├── logs.txt
├── sent_messages.txt
│
└── session.session
```

---

## ⚙️ Configuration

## config.py

Example:

```python
API_ID = 12345678
API_HASH = "YOUR_API_HASH"

MY_ID = 123456789

KEYWORDS_FILE = "keywords.txt"
CHATS_FILE = "chats.txt"

LOG_FILE = "logs.txt"
SENT_FILE = "sent_messages.txt"

SESSION_NAME = "session"
```

---

## 📝 Keywords

Example:

```text
python
django
telegram bot
website
backend
cpp
```

File:

```text
keywords.txt
```

---

## 📢 Monitored Channels

Example:

```text
it_jobs_ua
freelance_ua
python_jobs
```

File:

```text
chats.txt
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/telegram-keyword-monitor.git

cd telegram-keyword-monitor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install telethon
```

---

## ▶️ Running

```bash
python main.py
```

First launch:

```text
Enter your phone number:
+380XXXXXXXXX
```

After successful authorization:

```text
Bot started and monitoring chats...
```

---

## 📩 Example Notification

```text
New Potential Client

Chat:
Python Freelance UA

Keyword:
python

Text:
Looking for a Python developer for a long-term project.

Link:
https://t.me/example/1234
```

---

## 🛡 Duplicate Message Protection

Every processed message receives a unique identifier:

```text
chat_id + message_id
```

Example:

```text
-100123456789_456
```

This prevents duplicate alerts even after application restart.

---

## 📈 Use Cases

### 💼 Job Monitoring

Track:

- Python jobs
- C++ jobs
- Remote вакансії
- Freelance opportunities

### 🎯 Lead Generation

Monitor keywords such as:

```text
website
telegram bot
automation
developer
```

### 📢 Brand Tracking

Track mentions of:

```text
YourCompany
YourProduct
YourBrand
```

---

## 🔮 Future Improvements

- [ ] Web dashboard
- [ ] PostgreSQL support
- [ ] Docker deployment
- [ ] Multiple recipients
- [ ] AI message classification
- [ ] Sentiment analysis
- [ ] Telegram Bot interface
- [ ] Webhooks
- [ ] Advanced filtering rules

---

## 👨‍💻 Author

**Arsen** — Backend Developer 

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ArsenBo1chuk)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/Arsen_Bo1chuk)

---

## ⭐ Support

If this project helped you, consider giving it a star.