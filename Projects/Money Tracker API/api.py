from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_restful import fields, marshal, marshal_with, Api, Resource, reqparse
from zoneinfo import ZoneInfo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datahub.db"
db = SQLAlchemy(app)
api = Api(app)

class Bank(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  amount = db.Column(db.Integer, nullable=False)
  date = db.Column(db.DateTime, default=lambda: datetime.now(ZoneInfo("Asia/Dhaka")))

  def __repr__(self):
    return f"{self.amount} {self.date}"
  
log_args = reqparse.RequestParser()
log_args.add_argument("amount",type=int,required=True,help="Amount is required")

log_parser = {
  "id":fields.Integer,
  "amount":fields.Integer,
  "date":fields.DateTime
}

class Logs(Resource):
  def get(self):
    logs = Bank.query.all()
    total = sum(entry.amount for entry in logs)
    return {
      "Current Log": marshal(logs,log_parser),
      "Total Current Balance": total,
      "Info":"All currency is in BDT"
    }
  
  def post(self):
    args = log_args.parse_args()
    new_log = Bank(amount=args["amount"],date=datetime.now(ZoneInfo("Asia/Dhaka")))
    db.session.add(new_log)
    db.session.commit()
    return {
      "message":"Successfully added new log",
      "added data": marshal(new_log,log_parser),
      "Info":"All currency is in BDT"
    },201

class Log(Resource):
  def get(self,id):
    log = Bank.query.get_or_404(id)
    return {
      "Log of the specific id": marshal(log,log_parser),
      "Info":"All currency is in BDT"
    }
  
  def patch(self,id):
    args = log_args.parse_args()
    log = Bank.query.get_or_404(id)
    log.amount = args["amount"]
    log.date = datetime.now(ZoneInfo("Asia/Dhaka"))
    db.session.commit()
    logv2 = Bank.query.get(id)
    return {
      "message":f"successfully updated log {id}",
      "current form": marshal(logv2,log_parser),
      "Info":"All currency is in BDT"
    }
  
  def delete(self,id):
    log = Bank.query.get_or_404(id)
    db.session.delete(log)
    db.session.commit()
    logs = Bank.query.all()
    return {
      "message":f"successfully deleted log {id}",
      "current data":marshal(logs, log_parser),
      "Info":"All currency is in BDT"
    }

api.add_resource(Logs,"/api")
api.add_resource(Log,"/api/<int:id>")

@app.route("/")
def index():
  return "API Version of Money Tracker 💰"

if __name__=="__main__":
  app.run(debug=True)