import json

themes = json.load(open("data/themes.json"))


def get_all_themes():
    return themes["themes"]
