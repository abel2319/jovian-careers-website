from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title': 'Data Analyst',
    'location': 'Cotonou',
    'salary':'1500$'
  },
  {
    'id':2,
    'title': 'Data Scientist',
    'location': 'Cotonou',
    'salary':'2000$'
  },
{
    'id':3,
    'title': 'Data Business Intelligen',
    'location': 'Porto-Novo',
    'salary':'1750$'
  },
{
    'id':4,
    'title': 'Data Engineer',
    'location': 'Lagos',
    'salary':'2500$'
  }
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def get_job_api():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)