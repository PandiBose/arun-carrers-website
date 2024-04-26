from flask import Flask, jsonify,render_template

app = Flask(__name__)

JOBS=[
  {
    'id1':1,
    'title':'Data Analyst',
    'location':'Bengaluru',
    'salary':'Rs. 10,00,000'
  },
  {
    'id1':2,
    'title':'Data Engineer',
    'location':'Bengaluru',
    'salary':'Rs. 10,00,000'
  },
  {
    'id1':3,
    'title':'Data Scientist',
    'location':'Bengaluru',
    'salary':'Rs. 10,00,000'
  }
]


@app.route('/')
def hello_world():
  return render_template("home.html",jobs=JOBS,name="Arun")

@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
