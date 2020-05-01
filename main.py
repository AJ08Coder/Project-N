from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('index.html',list = ['1','2','3'])

if __name__ == '__main__':
    app.run()
