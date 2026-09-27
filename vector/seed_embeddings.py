import json
from pathlib import Path

from typing_extensions import dataclass_transform

from vector.embedding import get_embedding

data_file = "data/themes.json"


def seed_embeddings():
    with open(data_file, "r", encoding="utf-8") as file:
        themes = json.load(file)

    for theme in themes["themes"]:
        text = f"{theme['name']}. {theme['description']}"
        embedding = get_embedding(text)
        theme["embedding"] = embedding.tolist()

    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(
            themes,
            file,
            indent=2,
            ensure_ascii=False,
        )


if __name__ == "__main__":
    seed_embeddings()
