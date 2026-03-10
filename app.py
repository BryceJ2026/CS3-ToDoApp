# pip install flask
#pip install flask-sqlalchemy

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create Flask app instance
app = Flask(__name__)

#Create SQLite database instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskks.db'
db = SQLAlchemy(app)


# Define model of to-do list TASK object
class Task(db.Model):
    #db.Column represents a col in the database
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), )



#Flask route to display all tasks
@app.route('/', methods=['GET', 'POST'])
def index():

if request.method == 'POST':
        task_content = request.form('content')
        new_task = Task
#Add new Task to database
        try :
             db.session.add(new_task)
             db.session.commit()
             return redirect('/')
        except:
             return 'Error adding task!'
        
        #Select all Taks from database
        all_tasks = Task query.all()
return render__template('index.html'. tasks=all_tasks)
# Create the database in the man method
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host= '0.0.0.0', port= 5000, debug=True)


