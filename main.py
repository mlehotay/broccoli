from flask import Flask, render_template, request
from data.db import FoodPrefs

app = Flask(__name__, template_folder='templates')

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
    db_status = FoodPrefs(ip, args).save()
    return render_template('thankyou.html', status=db_status)

if __name__ == '__main__':
    app.run()
