from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'Eat more broccoli!'

if __name__ == '__main__':
    app.run()
