from dopy_tui.model.tasklist import TaskList

def cli(handler):
    run = True
    taskList = TaskList()
    taskList.from_dict(handler.load_dict())

    def try_index(inp: str) -> int | None:
        while True:
            if inp == "q":
                return
            if inp.isdigit():
                if 0 <= int(inp) < taskList.get_len():
                    return int(inp)
            inp = input("Invalid index! Try again. ('q' to cancel): ")
        
    while run:
        print(taskList)
        inp = input("Add/Toggle/Remove/Quit [a/t/r/q]").lower()
        match inp:
            case "a":
                taskList.add_task(input("Task text: "))
            case "t":
                index = try_index(input("Index to toggle: "))
                if index != None:
                    taskList.toggle_index(index)
            case "r":
                index = try_index(input("Index to remove: "))
                if index != None:
                    taskList.remove_index(index)
            case "q":
                run = False
            case _:
                print("Input not recognized!")
        handler.save_dict(taskList.to_dict())
