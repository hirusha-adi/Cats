import os
from threading import Thread

from flask import Flask, render_template

app = Flask(__name__,
            template_folder=f"{os.getcwd()}/src/website/templates",
            static_folder=f"{os.getcwd()}/src/website/static")


@app.route('/bot')
def index():
    return render_template("index.html")


@app.route('/bot/help')
def help():
    return render_template("help.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def run():
    app.run(host='0.0.0.0', port=8090)


def starWebServer():
    t = Thread(target=run)
    t.start()
