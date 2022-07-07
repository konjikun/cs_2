import random

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    item = random.choice(['takenoko','kinoko'])
    return('今日は{0}いかがですか'.format(item))

app.debug = True
app.run()
