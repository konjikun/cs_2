from flask import Flask
app=Flask(__name__)
@app.route('/test')
def iniad():
  return 'I am iniad'
@app.route('/')
def toyo():
  return 'you are toyo'
@app.route('/hello')
def univ():
  return 'they are univ'
app.debug=True
app.run()