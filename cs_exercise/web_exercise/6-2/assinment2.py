from flask import Flask
from datetime import datetime

app = Flask(__name__)

count = []
votes =[]
t = datetime.now()

@app.route('/history')
def index():
    sum = ''
    for x in votes:
        sum += x + '<br>'
    return sum
    
@app.route('/takenoko')
def takenoko():

    result1 = str(t) + 'たけのこに投票されました'
    votes.append(result1)
    return 'タケノコへの投票ありがとうございました' 

@app.route('/kinoko')
def kinoko():
    result2 = str(t) + 'きのこに投票されました'
    votes.append(result2)
    return 'きのこへの投票ありがとうございました' 
    
app.debug = True
app.run()