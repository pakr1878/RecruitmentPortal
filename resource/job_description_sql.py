from shared.db import db

class JobDescription(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), unique = False, nullable = False)
    pd_name = db.Column(db.String(100), unique = False, nullable = False)
    project_title = db.Column(db.String(100), unique = False, nullable = False)
    openings = db.Column(db.Integer, nullable = False)
    openings_filled = db.Column(db.Integer, nullable = False)
    price_low_range = db.Column(db.Integer, nullable = False)
    price_high_range = db.Column(db.Integer, nullable = False)
    project_start = db.Column(db.DateTime, nullable = False)
    project_end = db.Column(db.DateTime, nullable = False)
    location = db.Column(db.String(100), unique = False, nullable = False)
    project_details = db.Column(db.String(200), unique = False, nullable = False)
    unit = db.Column(db.Integer, nullable = False)
    project_description = db.Column(db.String(200), unique = False, nullable = True)
    jd_description = db.Column(db.String(200), unique = False, nullable = False)
    jd_status = db.Column(db.String(200), unique = False, nullable = False)

