from flask import Flask,request,redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datahub.db"
db = SQLAlchemy(app)

class Bank(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  amount = db.Column(db.Integer, nullable=False)
  date = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Dhaka")))

  def __repr__(self):
    return f"{self.amount} {self.date}"

@app.route("/", methods=["GET","POST"])
def index():
  if request.method=="POST":
    try:
      amount_user = int(request.form["amount"])
    except ValueError:
      return "Please enter a valid amount in integer"
    new_amount = Bank(amount=amount_user)

    try:
      db.session.add(new_amount)
      db.session.commit()
      return redirect("/")
    except:
      return "Something wrong happened while adding the log"
  else:
    all_log = Bank.query.order_by(Bank.date).all()
    total = sum(entry.amount for entry in all_log)
    return render_template("index.html",log=all_log,total=total)
    

@app.route("/delete/<int:id>")
def delete(id):
  selected = Bank.query.get_or_404(id)
  try:
    db.session.delete(selected)
    db.session.commit()
    return redirect("/")
  except:
    return "Something went south while deleting the log"
  
@app.route("/update/<int:id>",methods=["GET","POST"])
def update(id):
  selected = Bank.query.get_or_404(id)

  if request.method == "POST":
    try: 
      selected.amount = int(request.form["amount"])
    except ValueError:
      return "Please enter a valid amount in integer" 

    try:
      db.session.commit()
      return redirect("/")
    except:
      return "Something went south while updating the log"
  else:
    return render_template("update.html",selected=selected)
  
if __name__=="__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)