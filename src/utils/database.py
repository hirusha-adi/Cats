import json


class Embeds:
    with open("database/embeds.json", "r", encoding="utf-8") as _file:
        _data = json.load(_file)
        common = _data["common"]
