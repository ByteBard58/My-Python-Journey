# 💰 Personal Money Tracker (Flask + SQLite)

A simple web app to track your daily saved money using Flask and SQLAlchemy. Perfect for students or anyone who wants to keep an eye on their savings without any external app.

---
## Little bit of background
This is my personal story. I try to save some money everyday from the pocket money I get from my parents and store it in a bag. When I need to count the money, things go messy pretty often. So I wanted to use my own coding skills to create something which can help me to keep track of my savings. 

It is a project which is inspired form my own life and solves a real-life problem. I hope you can find it useful too :)

## 📌 Features

- Add daily saved amount (in BDT)
- View all entries with date & amount
- See total balance in real time
- Edit or delete any entry
- Dark-themed UI for clean visuals

---


## 🛠 Tech Stack

- Python
- Flask
- SQLite (via SQLAlchemy)
- HTML/CSS (with Jinja2)

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/ByteBard58/My-Python-Journey
cd Projects/Money tracker Webapp
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the app
```bash
python3 app.py
```

### 4. Open in browser
Visit [Localhost 5000](http://127.0.0.1:5000) in your browser.

---

## 🗃 Database Schema

- `id` – primary key
- `amount` – saved money (in BDT)
- `date` – date of entry (auto-filled with Asia/Dhaka timezone)

---

## 🌐 Folder Structure

```
money-tracker/
│
├── templates/
│   ├── index.html
│   └── update.html
│
├── static/         # (optional, if you add custom CSS later)
│
├── app.py
├── datahub.db      # Auto-created on first run
└── README.md
```

---


