from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Python Devloper',
        'location': 'remote',
        'salary': 100000
    },
    {
        'id': 2,
        'title': 'Javascipt Devloper',
        'location': 'Delhi',
        'salary': 100000
    },
    {
        'id': 3,
        'title': 'Cpp Devloper',
        'location': 'Bangalore',
        'salary': 100000
    },
]


@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def return_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
