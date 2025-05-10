from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,fields,marshal,marshal_with,abort,reqparse,Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dataholder.db"
db = SQLAlchemy(app)
api = Api(app)

class Data(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(200),nullable=False)
  client = db.Column(db.String(100),nullable=False)
  status = db.Column(db.String(20),nullable=False,server_default="in-progress")
  deadline = db.Column(db.String(10),nullable=False)

  def __repr__(self):
    return f"Job Title:{self.title}, client:{self.client}"
  
data_args = reqparse.RequestParser()
data_args.add_argument("title",type=str,help="title of the job is required",required=True)
data_args.add_argument("client",type=str,help="client is required",required=True)
data_args.add_argument("status",type=str,help="status is required",required=True)
data_args.add_argument("deadline",type=str,help="deadline is required (in string)",required=True)

resource_fields = {
  'id':fields.Integer,
  'title':fields.String,
  'client':fields.String,
  'status':fields.String,
  'deadline':fields.String
}

class Gigs(Resource):
  @marshal_with(resource_fields)
  def get(self):
    gigs = Data.query.all()
    return gigs
  
  def post(self):
    args = data_args.parse_args()
    gig = Data(title=args["title"],client=args["client"],status=args["status"],deadline=args["deadline"])
    db.session.add(gig)
    db.session.commit()
    return {
      "message":"New Gig Created successfully",
      "new gig": marshal(gig,resource_fields)
    }

class Gig(Resource):
  @marshal_with(resource_fields)
  def get(self,id):
    gig = Data.query.get(id)
    if not gig:
      abort(404,message="User of that id was not found")
    return gig
  
  def patch(self,id):
    gig = Data.query.get(id)
    if not gig:
      abort(404,message="User of that id was not found")
    args = data_args.parse_args()
    gig.title = args["title"]
    gig.client = args["client"]
    gig.status = args["status"]
    gig.deadline = args["deadline"]
    db.session.commit()
    gigv2 = Data.query.get(id)
    return {
      "message": f"Gig (id: {id}) was updated successfully",
      "current form": marshal(gigv2,resource_fields)
    }, 201
  
  def delete(self,id):
    gig = Data.query.get(id)
    if not gig:
      abort(404,message="User of that id was not found")
    db.session.delete(gig)
    db.session.commit()
    gigs = Data.query.all()
    return {
      "message" : f"The Gig (id: {id}) was deleted successfully",
      "current data" : marshal(gigs, resource_fields)
    }, 200
  
api.add_resource(Gigs,"/api/gig")
api.add_resource(Gig,"/api/gig/<int:id>")

@app.route("/")
def index():
  return render_template("index.html")

if __name__=="__main__":
  with app.app_context():    # Remove this block after the database is created (line 94 & 95)
    db.create_all()       
  app.run(debug=True)
    
