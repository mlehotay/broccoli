from flask import Flask, render_template, request
import pandas as pd
import pickle

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
