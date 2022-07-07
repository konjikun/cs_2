import random

from flask import Flask
app = Flask(__name__)

take_cou = 0
kinoko_cou = 0

@app.route('/')
def index():
    if take_cou > kinoko_cou:
        return'タケノコの価値'

    elif take_cou < kinoko_cou:
        return 'キノコの価値'
    
    else:
        '引き分け'

app.debug = True
app.run()