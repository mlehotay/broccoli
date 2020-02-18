from flask import Flask, render_template, request
import pandas as pd
import pickle

#from flask import request
#request.environ.get('HTTP_X_REAL_IP', request.remote_addr)


app = Flask(__name__, template_folder='templates')
#pipe = pickle.load(open('model/pipe.pkl', 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    args = request.form
    return render_template('result.html')

if __name__ == '__main__':
    app.run()
