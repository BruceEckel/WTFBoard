from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', columns=5, rows=8)

if __name__ == '__main__':
    app.run()
