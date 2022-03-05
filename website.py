import json

from web.server import web

with open("database/settings.json", "r", encoding="utf-8") as f:
    data = json.load(f)

try:
    host = str(data["websites"]["main"]["host"])
except:
    host = "0.0.0.0"

try:
    port = str(data["websites"]["main"]["port"])
except:
    port = 4498


def runWebServer():
    web.run(host, port=port)


runWebServer()
