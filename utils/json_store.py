import json
from pathlib import Path


def read_json(filepath):
    with open(filepath, encoding="utf-8") as fp:
        return json.load(fp)


def write_json(filepath, data):
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as fp:
        json.dump(data, fp, indent=2)


def iter_json_files(folder):
    folder = Path(folder)
    folder.mkdir(parents=True, exist_ok=True)
    for filepath in sorted(folder.iterdir()):
        if filepath.is_file() and filepath.suffix == ".json":
            yield filepath
