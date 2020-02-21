from flask import Flask, render_template, request
from data.db import FoodPrefs
from foods import food_grid, food_survey

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    foods = food_grid()
    return render_template('index.html', table_rows=foods)

@app.route('/recommend', methods=['POST'])
def recommend():
    args = request.form
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    FoodPrefs(ip, args).save()
    return render_template('recommend.html')

@app.route('/survey')
def survey():
    survey = food_survey()
    return render_template('survey.html', table_rows=survey)

@app.route('/thankyou', methods=['POST'])
def thankyou():
    args = request.form
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    FoodPrefs(ip, args).save()
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run()
