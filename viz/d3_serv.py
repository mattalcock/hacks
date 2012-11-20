from flask import Flask, url_for, redirect, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/pingraph/')
def pingraph():
    return render_template('nodes.html')

@app.route('/grid/')
def grid():
    return render_template('grid.html')

@app.route('/timeline/')
def timeline():
    return render_template('timeline.html')

@app.route('/drilldown/')
def drilldown():
    return render_template('drilldown.html')


if __name__ == "__main__":
    app.debug = True
    app.run()