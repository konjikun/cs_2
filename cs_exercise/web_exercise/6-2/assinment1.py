from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    t = datetime.now()
    if t.hour >= 5 and t.hour <12:
        return 'Good Morning!'
    elif t.hour >= 12 and t.hour <17:
        return ('Good Afternoon!')
    else:
        return ('Good Evening!')

app.debug = True
app.run()