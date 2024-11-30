from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'Id' : 1,
        'Title' : 'Data Analyst',
        'Location' : 'San Francisco',
        'Salary' : 100000
    },
    {
        'Id' : 2,
        'Title' : 'Data Scientist',
        'Location' : 'NY',
        'Salary' : 100560
    },
    {
        'Id' : 3,
        'Title' : 'FrontEnd Engineer',
        'Location' : 'Remote',
        'Salary' : 70000
    },
    {
        'Id' : 4,
        'Title' : 'BackEnd Engineer',
        'Location' : 'Dallas',
        'Salary' : 146000,
    }
]

@app.route('/')
def index():
    return render_template('home1.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)