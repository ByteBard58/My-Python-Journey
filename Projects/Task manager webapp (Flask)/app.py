from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db = SQLAlchemy(app)

class Todo(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  content = db.Column(db.String(200),nullable=False)
  date_created = db.Column(db.DateTime,default=datetime.now(timezone.utc))
  def __repr__(self):
    return f"Task {self.id}"


@app.route("/", methods=["GET","POST"])
def index():
  if request.method=="POST":
    task_content = request.form["content"].strip()
    if not task_content:
      return "Blank place isn't accepted"
    new_task = Todo(content=task_content)
    try:
      db.session.add(new_task)
      db.session.commit()
      return redirect("/")
    except:
      return "Something went wrong while adding task"
  else:
    tasks = Todo.query.order_by(Todo.date_created).all()
    return render_template("index.html",tasks=tasks)
  
@app.route("/delete/<int:id>")
def deletion(id):
  task_to_kick= Todo.query.get_or_404(id)
  try:
    db.session.delete(task_to_kick)
    db.session.commit()
    return redirect("/")
  except:
    return "Something went wrong while deleting the task"

@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
  task = Todo.query.get_or_404(id)
  if request.method=="POST":
    task.content = request.form["content"].strip()
    if not task.content:
      return "Blank place isn't accepted"
    try:
      db.session.commit()
      return redirect("/")
    except:
      return "Something went wrong while updating the task"
  else:
    return render_template("update.html",task=task)

if __name__=="__main__":
  app.run(debug=True)