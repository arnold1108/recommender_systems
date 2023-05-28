# Importing the necessary libraries 
from flask import Flask, request 
from flask_sqlalchemy import SQLAlchemy 

# Creating a flask application with SQLite database 
app = Flask(__name__) #flask application instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://doadmin:AVNS_vWLEej9H5dTNBPPsHGI@tajji-postgresql-db-do-user-12384628-0.b.db.ondigitalocean.com:25060/testdb?sslmode=require' #database URI for the SQLAlchemy database object
db = SQLAlchemy(app) #SQLAlchemy database

# Defining attributes of the SQLAlchemy database columns 
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    certification_required = db.Column(db.String(50), nullable=False)
    skill_level_required = db.Column(db.String(50), nullable=False)
    experience_required = db.Column(db.Integer, nullable=False)
    work_preference = db.Column(db.String(50), nullable=False)
    
# Creating a route function to handle HTTP POST requests to create a new Job object 
@app.route('/jobs', methods=['POST', 'GET'])
def create_job():
    data = request.form
    experience_required = data.get('experience_required', '')
    if not experience_required:
        return 'experience_required value is required'
    new_job = Job(skill=data.get('skill', ''), 
                  location=data.get('location'), 
                  certification_required=data.get('certification_required', ''),
                  skill_level_required=data.get('skill_level_required', ''),
                  experience_required=experience_required,
                  work_preference=data.get('work_preference', '')
            )
    db.create_all()
    db.session.add(new_job)
    db.session.commit()
    return "Job created successfully"

# Start the code in debugging mode enabled if the script is being tun as the main program
if __name__ == '__main__':
    app.run(debug=True) 