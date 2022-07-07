from flask import Flask
app = Flask(__name__)

kinoko_count = 0
takenoko_count = 0

@app.route('/')
def index():
    if kinoko_count > takenoko_count: 
        return '{} vs {}できのこの勝ち！'.format(kinoko_count, takenoko_count)
    elif kinoko_count < takenoko_count:
        return '{} vs {}でタケノコの勝ち！'.format(takenoko_count, kinoko_count)
    else:
        return '引き分け！どちらもがんばって！'

@app.route('/takenoko')
def takenoko():
    global takenoko_count
    takenoko_count += 1
    return 'タケノコへの投票ありがとうございました'

@app.route('/kinoko')
def kinoko():
    global kinoko_count
    kinoko_count += 1
    return 'きのこへの投票ありがとうございました'

app.debug = True
app.run()
