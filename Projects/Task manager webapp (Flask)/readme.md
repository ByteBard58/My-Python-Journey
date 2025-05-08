# Flask Todo App

A simple Todo web application built using **Flask**, **SQLite**, and **Jinja2 templating**.  
Part of my hands-on learning journey with Python and Flask.

## Features

- Add and delete todo items
- Display todo list with creation dates
- Lightweight SQLite backend
- Clean HTML templates using Jinja2

## Tech Stack

- Python 3
- Flask
- SQLite
- HTML (Jinja2)


## Getting Started

### Clone the repo

```bash
git clone https://github.com/ByteBard58/My-Python-Journey/
cd Projects/Task manager webapp (Flask)
```

### Set up virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create the database

```bash
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()
```

### Run the app

```bash
flask run
```

Then visit [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Folder Structure

```
Task Manager webapp (Flask)/
├── app.py
├── templates/
│   └── base.html
│   └── index.html
│   └── update.html
├── instance/
│   └── test.db (excluded from Git)
├── requirements.txt
└── README.md
```

## Notes

- The database (`test.db`) is ignored using `.gitignore` to keep the repo clean.
- If you face `sqlite3.OperationalError`, make sure you initialized the DB correctly and the URI has the correct path: `sqlite:///instance/test.db`
