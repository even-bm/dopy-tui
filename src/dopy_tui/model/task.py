class Task:
    def __init__(self, text = "", done = False):
        self._text = text
        self._done = done

    def toggle_done(self):
        self._done = not self._done

    def get_status(self):
        return self._done

    def get_text(self):
        return self._text

    def to_dict(self):
        return {"text" : self._text, "done" : self._done}
    
    @staticmethod
    def from_dict(dictionary):
        return Task(dictionary["text"], dictionary["done"])

    def __str__(self):
        return f"{self._text}{" (Done)" if self._done else ""}"


