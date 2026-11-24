from dopy_tui.model.task import Task

class TaskList:
    def __init__(self):
        self._list = []

    def add_task(self, text):
        self._list.append(Task(text))

    def toggle_index(self, index):
        self._list[index].toggle_done()

    def remove_index(self, index):
        self._list.pop(index)

    def get_len(self):
        return len(self._list)

    def to_dict(self):
        dict = {}
        for i in range(len(self._list)):
            dict[i] = self._list[i].to_dict()
        return dict

    def from_dict(self, dictionary):
        for task_nr in range(len(dictionary)):
            self._list.append(Task.from_dict(dictionary[task_nr]))

    def __str__(self):
        i = 0
        acc = ""
        for task in self._list:
            acc += f"[{i}]{task}\n"
            i += 1
        acc = acc.rstrip()
        return acc
