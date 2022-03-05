from flask import Flask, render_template, request
import json
import os
import requests

web = Flask(__name__)

HOME = None


def loadJson():
    global HOME
    with open(f"{os.getcwd()}/database/main_website.json", "r", encoding="utf-8") as temp:
        x = json.load(temp)
        HOME = x["HOME"]


def sortData(data):
    veritcal_only = []
    horizontal_only = []

    for one_dict in data:
        temp_height = int(one_dict["height"])
        temp_width = int(one_dict["width"])
        if temp_height > temp_width:
            veritcal_only.append(one_dict["url"])

    for one_dict in data:
        temp_height = int(one_dict["height"])
        temp_width = int(one_dict["width"])
        if temp_height < temp_width:
            horizontal_only.append(one_dict["url"])

    for item in horizontal_only:
        veritcal_only.append(item)

    return veritcal_only


@web.route("/", methods=['GET'])
def index():
    global HOME
    if HOME is None:
        loadJson()

    try:
        text = request.args.get("text")
    except:
        text = None

    if (text is None) or (bool(text) is False) or (len(text) == 0):
        data = requests.get(
            "https://api.thecatapi.com/v1/images/search?limit=50").json()
        sorted_list = sortData(data=data)
        return render_template("index.html",
                               many_images=True,
                               sorted_list=sorted_list,
                               HOME=HOME,
                               HOME_logo=HOME["logo"],
                               HOME_title=HOME["title"],
                               HOME_links=HOME["links"],
                               )

    else:
        sorted_list = [1, 2]  # to prevent errors if any

        data = requests.get(
            f"https://cataas.com/cat/says/{text}")

        filename1 = os.path.join(
            os.getcwd(), "web", "static", "images", "temp.png")

        with open(filename1, "wb") as fw1:
            fw1.write(data.content)

        return render_template("index.html",
                               many_images=False,
                               sorted_list=sorted_list,
                               HOME=HOME,
                               HOME_logo=HOME["logo"],
                               HOME_title=HOME["title"],
                               HOME_links=HOME["links"],
                               )


@web.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


web.run("0.0.0.0", port=4498)
