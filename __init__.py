from crypt import methods

from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, add_application_to_db

app = Flask(__name__)


@app.route('/')
def index():
    jobs = load_jobs_from_db()
    return render_template('home1.html', jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()
    jobs_list = [dict(job) for job in jobs]
    return jsonify(jobs_list)

@app.route('/app_forms')
def list_apps():
    return render_template('application_forms.html')

@app.route('/jobs/apply', methods=["post"])
def apply_job():
    data = request.form
    add_application_to_db(data)
    return render_template('application_submitted.html', application=data)

if __name__ == '__main__':
    app.run(debug=True)