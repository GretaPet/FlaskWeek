from application import app, db
from application.models import Tasks

@app.route('/add')
def add():
    new_task = Tasks(name="New Task")
    db.session.add(new_task)
    db.session.commit()
    return "Added new task to database"

@app.route('/read')
def read():
    all_tasks = Tasks.query.all()
    Tasks_string = ""
    for task in all_tasks:
        tasks_string += "<br>"+ task.name
    return tasks_string

@app.route('/update/<name>')
def update(name):
    first_task = Tasks.query.first()
    first_task.name = name
    db.session.commit()
    return first_task.name