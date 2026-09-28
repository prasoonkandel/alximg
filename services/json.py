import json

themes = json.load(open("data/themes.json"))


def get_all_themes():
    return themes["themes"]


def get_theme_by_id(id):
    return themes["themes"][id]
