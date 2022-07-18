from  flask import Flask
from shared.db import db
from resource.job_description_sql import JobDescription

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///RecruitmentPortalDb.db'
db.init_app(app)


@app.route('/',methods=['GET'])
def index():

    return "home page"

if __name__ == '__main__':

    with app.app_context():
        jd = JobDescription()
        db.create_all()
    app.run()