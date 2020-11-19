from flask import render_template #render template feature is built into flask 
from app import app
from app.models.event_list import events #import model - data for the application doesnt mean its a database

@app.route('/') #listen on / route then return something
def index():
    return render_template('index.html', title='Home', events=events)


@app.route('/planner')
def planner():
    return render_template('planner.html', title="Planner", events=events)



#model is the data, view is html and controller is the controller.py file allowing us to do GET requests on routes - controller ties view and model together