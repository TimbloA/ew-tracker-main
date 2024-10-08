from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)
db = Database('database.db')


@app.route('/')
def list_ews():
    ews = db.get_ews()
    print(ews)
    return render_template('list.html', ews=ews)

@app.route('/add', methods=['POST'])
def add_ew():
    task = request.form.get('task')
    beak = request.form.get('beak')
    dueDate = request.form.get('dueDate')
    subject = request.form.get('subject')
    if task:
        db.create_ew(task, beak, subject, dueDate) 
    return redirect('/')


# EXTRA CREDIT
@app.route('/<int:id>')
def view_ew(id):
    """
    TO IMPLEMENT
    """
    pass