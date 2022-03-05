import json
import os
from threading import Thread

from flask import Flask, render_template

app = Flask(__name__,
            template_folder=f"{os.getcwd()}/src/website/templates",
            static_folder=f"{os.getcwd()}/src/website/static")

HOME = None
HELP = None
HEADER = None
FOOTER = None


def loadJson():
    global HOME, HEADER, FOOTER, HELP
    with open(f"{os.getcwd()}/database/bot_website.json", "r", encoding="utf-8") as temp:
        x = json.load(temp)
        HOME = x["HOME"]
        HELP = x["HELP"]
        HEADER = x["HEADER"]
        FOOTER = x["FOOTER"]


@app.route('/')
def index():
    global HOME, HEADER, FOOTER
    if HOME is None:
        loadJson()

    return render_template("index.html",
                           HEADER_logo=HEADER["logo"],
                           HEADER_items_dict=HEADER["items"],
                           FOOTER_items_dict=FOOTER["items"],
                           HOME_box_title=HOME["box"]["title"],
                           HOME_box_sub_title=HOME["box"]["sub_title"],
                           HOME_box_body=HOME["box"]["body"],
                           HOME_box_bottom_paragraphs=HOME["box"]["bottom"]["paragraphs"],
                           HOME_buttons=HOME["buttons"]
                           )


@app.route('/help')
def help():
    global HELP, HEADER, FOOTER
    if HELP is None:
        loadJson()

    return render_template("help.html",
                           HEADER_logo=HEADER["logo"],
                           HEADER_items_dict=HEADER["items"],
                           FOOTER_items_dict=FOOTER["items"],
                           HELP_tables_list=HELP["tables"],
                           HELP_faq_title=HELP["faq"]["title"],
                           HELP_faq_sub_title=HELP["faq"]["sub_title"],
                           HELP_faq_items=HELP["faq"]["items"]
                           )


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


def run():
    with open(f"{os.getcwd()}/database/settings.json", "r", encoding="utf-8") as f:
        data = json.load(f)

    try:
        host = str(data["websites"]["bot"]["host"])
    except:
        host = "0.0.0.0"

    try:
        port = str(data["websites"]["bot"]["port"])
    except:
        port = 4499

    app.run(host=host, port=port)


def starWebServer():
    t = Thread(target=run)
    t.start()
