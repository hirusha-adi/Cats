import json


class Embeds:
    with open("database/other.json", "r", encoding="utf-8") as _file:
        _data = json.load(_file)
        common = _data["common"]
        commands = _data["commands"]


class Settings:
    with open("database/settings.json", "r", encoding="utf-8") as _file:
        _data = json.load(_file)
        main = _data["main"]
