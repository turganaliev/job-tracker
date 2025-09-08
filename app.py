import json
import os
import uuid
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

USER_DATA_FOLDER = 'user_data'
if not os.path.exists(USER_DATA_FOLDER):
    os.makedirs(USER_DATA_FOLDER)

def get_user_data_path():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    filename = f"{session['user_id']}.json"
    return os.path.join(USER_DATA_FOLDER, filename)

def load_user_jobs():
    path = get_user_data_path()
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return json.load(f)

def save_user_jobs(jobs):
    path = get_user_data_path()
    with open(path, 'w') as f:
        json.dump(jobs, f, indent=4)

@app.route('/')
def index():
    jobs = load_user_jobs()
    return render_template('index.html', jobs=jobs)

@app.route('/add', methods=['POST'])
def add():
    jobs = load_user_jobs()
    new_job = {
        "company": request.form['company'],
        "title": request.form['title'],
        "status": request.form['status'],
        "notes": request.form['notes']
    }
    jobs.append(new_job)
    save_user_jobs(jobs)
    return redirect(url_for('index'))

@app.route('/delete/<int:job_id>')
def delete(job_id):
    jobs = load_user_jobs()
    if 0 <= job_id < len(jobs):
        jobs.pop(job_id)
    save_user_jobs(jobs)
    return redirect(url_for('index'))

@app.route('/edit/<int:job_id>', methods=['GET', 'POST'])
def edit(job_id):
    jobs = load_user_jobs()
    if not (0 <= job_id < len(jobs)):
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        jobs[job_id]['company'] = request.form['company']
        jobs[job_id]['title'] = request.form['title']
        jobs[job_id]['status'] = request.form['status']
        jobs[job_id]['notes'] = request.form['notes']
        save_user_jobs(jobs)
        return redirect(url_for('index'))
    else:
        return render_template('edit.html', job=jobs[job_id], job_id=job_id)

if __name__ == '__main__':
    app.run(debug=True)