from flask import Flask, render_template, request
import pandas as pd
import pickle

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
    # save data
    return render_template('thankyou.html', address=ip, data=args)

if __name__ == '__main__':
    app.run()
