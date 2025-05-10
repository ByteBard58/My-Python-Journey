# === Import necessary libraries ===

from flask import Flask, render_template, request, redirect  # Flask core + HTML rendering + handling form input + redirection
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy: ORM to interact with the database using Python classes
from datetime import datetime, timezone  # For generating timestamps in UTC


# === App & Database Setup ===

app = Flask(__name__)  # Create Flask app instance (tells Flask: "this file is the starting point")

# Configure the database URI: using SQLite, storing data in a file named 'test.db' in the project folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

# Initialize the SQLAlchemy database instance with this Flask app
db = SQLAlchemy(app)


# === Database Model ===

# Define the 'Todo' model (structure of our table)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique task ID (auto-incremented)
    content = db.Column(db.String(200), nullable=False)  # The actual task description (max 200 chars, cannot be empty)
    date_created = db.Column(db.DateTime, default=datetime.now(timezone.utc))  # Auto-generated timestamp (UTC)

    def __repr__(self):
        return f"Task {self.id}"  # When we print a Todo object, it shows like: Task 1, Task 2, etc.


# === Routes (Pages/Endpoints) ===

# Homepage Route → http://localhost:5000/
@app.route("/")
def index():
    return render_template("index.html")  # Load the homepage template (usually just a landing page or link hub)


# A secondary route just for example → http://localhost:5000/huh
@app.route("/huh")
def next_page():
    return render_template("huh.html")  # Loads a different page (maybe used as a demo or joke page)


# Main TODO Page → http://localhost:5000/task_master
@app.route("/task_master", methods=["GET", "POST"])
def task_m():
    if request.method == "POST":
        # If the user submits a form to add a task
        task_content = request.form["content"].strip()  # Get the 'content' field from the form and trim spaces

        if not task_content:
            return "You must write something to specify the task"  # Prevent empty submissions

        # Create a new task object with the content
        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)  # Add it to the current DB session
            db.session.commit()       # Save changes to the database
            return redirect("/task_master")  # Reload the page to show the updated task list
        except:
            return "There was an issue out there"  # Fallback message if something breaks during DB operation

    else:
        # If the user just visits the page (GET request)
        tasks = Todo.query.order_by(Todo.date_created).all()  # Fetch all tasks, sorted by creation time
        return render_template("tm.html", tasks=tasks)  # Send the task list to 'tm.html' to render


# Delete a task → http://localhost:5000/task_master/delete/<id>
@app.route("/task_master/delete/<int:id>")
def delete(id):
    # Try to fetch the task by its ID, or throw 404 if not found
    task_to_del = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_del)  # Mark it for deletion
        db.session.commit()             # Commit to database
        return redirect("/task_master")  # Redirect back to main task page
    except:
        return "Something went wrong while deleting the task"  # If DB operation fails


# Update/Edit a task → http://localhost:5000/task_master/update/<id>
@app.route("/task_master/update/<int:id>", methods=["GET", "POST"])
def update(id):
    task = Todo.query.get_or_404(id)  # Fetch the task by ID or show 404 if it doesn’t exist

    if request.method == "POST":
        # User has submitted the updated content
        task.content = request.form["content"].strip()  # Update the content with new value
        if not task.content:
            return "You must write something to specify the task"

        try:
            db.session.commit()  # Save changes to the database
            return redirect("/task_master")  # Go back to task list
        except:
            return "Something went wrong while updating the task"  # On DB commit error

    else:
        # User is visiting the update page (GET request)
        return render_template("update.html", task=task)  # Show the form pre-filled with current task


# === Entry Point ===

# Run the app only if this file is being run directly (not imported)
if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask dev server with debugging enabled (for auto reload + error logs)
