from pathlib import Path

class Handler:
    def __init__(self, datapath: Path):
        self._data_dir = datapath
        self._data_file = datapath / "list.csv"

    def save_dict(self, dictionary):
        self._data_dir.mkdir(parents=True, exist_ok=True)
        with open(self._data_file, "w", encoding="utf-8") as f:
            for task in dictionary:
                f.write(f"{dictionary[task]["text"].replace(";", ":")};{dictionary[task]["done"]}\n")

    def load_dict(self):
        dictionary = {}
        i = 0
        try:
            with open(self._data_file, "r", encoding="utf-8") as f:
                for line in f:
                    text, done = line.strip().split(";")
                    dictionary[i] = {"text" : text, "done" : done == "True"}
                    i += 1
        except FileNotFoundError:
            pass
        return dictionary
