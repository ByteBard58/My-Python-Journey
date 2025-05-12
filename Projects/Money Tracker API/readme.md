# 💰 Money Tracker API

A simple RESTful API built using Flask + Flask-RESTful + SQLAlchemy to track your daily saved money. Perfect for students or anyone who wants to keep an eye on their savings without any external app.


> This is the API version of the [Money Tracker webapp project](https://github.com/ByteBard58/My-Python-Journey/tree/main/Projects/Money%20tracker%20Webapp), fully built with Python and SQLite.

---

## ⚙️ Tech Stack

- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- SQLite (for storage)
- ZoneInfo (for time zone support)

---

## 📦 Setup & Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/ByteBard58/My-Python-Journey
   cd Projects/Money Tracker API
   ```

2. **Create a virtual environment (optional but recommended)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**  
   ```bash
   python app.py
   ```
   The API will be running at `http://127.0.0.1:5000`

---

## 🧪 API Endpoints

### ✅ `GET /api`

Returns all logs with the total current balance.

#### Response
```json
{
  "Current Log": [...],
  "Total Current Balance": 1500,
  "Info": "All currency is in BDT"
}
```

---

### ➕ `POST /api`

Adds a new log entry.

#### Request Body (JSON)
```json
{
  "amount": 500
}
```

#### Response
```json
{
  "message": "Successfully added new log",
  "added data": {
    "id": 1,
    "amount": 500,
    "date": "2025-05-12T15:30:00"
  },
  "Info": "All currency is in BDT"
}
```

---

### 📄 `GET /api/<id>`

Returns a specific log by ID.

---

### 🔁 `PATCH /api/<id>`

Updates the `amount` of a specific log.

#### Request Body (JSON)
```json
{
  "amount": 800
}
```

---

### ❌ `DELETE /api/<id>`

Deletes a log entry by ID.

---

## ℹ️ Notes

- All amounts are considered in **BDT (Bangladeshi Taka)**.
- Timestamps are stored in **Asia/Dhaka** timezone.
- Negative amounts are accepted if you're tracking expenses.

---
