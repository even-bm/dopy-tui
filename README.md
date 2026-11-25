# dopy-tui
**v0.1.1**

dopy-tui is a todo-app written in Python. It is currently a cli-only and TUI is planned.

## Usage
**To run:**

From ```src/```
``` bash
python -m dopy_tui
```

The program runs on a loop displaying your todo-list, and prompting you for a command.

**Commands:**
- *A* - Add a new task
- *T* - Toggle a task
- *R* - Remove a task
- *Q* - Quit

The program automatically saves your list to ```~/.local/share/dopy-tui/```

## Requirements
- Python 3.12+
- Linux/Unix

## Known issues
- Corrupt data file may crash program
- TUI (curses) not implemented yet
