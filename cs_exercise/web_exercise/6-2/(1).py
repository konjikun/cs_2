from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '投票サイトへようこそ'

@app.route('/takenoko')
def take():
    return 'タケノコへ'



app.debug = True
app.run()
