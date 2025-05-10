# Freelancer Gig Tracker API

This is a simple RESTful API built with Flask and Flask-RESTful that allows freelancers to log, update, and manage their gigs/jobs.

## 🔧 Features

- Add new gigs with title, client name, status, and deadline
- View all gigs or a specific one by ID
- Update existing gig details
- Delete gigs
- SQLite database backend

## 📦 Tech Stack

- Python 3.x
- Flask
- Flask-RESTful
- Flask-SQLAlchemy

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/ByteBard58/My-Python-Journey/
cd Projects/Freelancer Gig Tracker API
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\Scripts\activate
```

### 3. Install the requirements
```bash
pip install -r requirements.txt
```


### 4. Run the server
```bash
python3 project.py
```

Server will run at: `http://127.0.0.1:5000`

## 🛠️ API Endpoints

| Method | Endpoint           | Description           |
|--------|--------------------|-----------------------|
| GET    | `/api/gig`         | Get all gigs          |
| POST   | `/api/gig`         | Add a new gig         |
| GET    | `/api/gig/<id>`    | Get gig by ID         |
| PATCH  | `/api/gig/<id>`    | Update gig by ID      |
| DELETE | `/api/gig/<id>`    | Delete gig by ID      |

### Example JSON for POST/PATCH:
```json
{
  "title": "Frontend Website Creation",
  "client": "John Doe",
  "status": "in progress",
  "deadline": "2025-06-01"
}
```

## Note

This API is a very basic project that I created as a way to learn REST and Flask. It is not production-focused, but still gets some work done.