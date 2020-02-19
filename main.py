from datetime import datetime
from flask import Flask, render_template, request
from datetime import datetime
import pandas as pd
import pickle
import uuid

app = Flask(__name__, template_folder='templates')
#pipe = pickle.load(open('model/pipe.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    args = request.form
    return render_template('recommend.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

@app.route('/thankyou', methods=['POST'])
def thankyou():
    args = request.form
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    save_userdata(ip, args)
    return render_template('thankyou.html', address=ip, data=args)

def save_userdata(ip, args):
    with open(f'data/userdata/{uuid.uuid4().hex}.txt', 'w') as f:
        f.write(f'{datetime.now()}\n')
        f.write(f'{ip}\n')
        f.write(f'{args}\n')

if __name__ == '__main__':
    app.run()
