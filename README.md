# todo-cli

A tiny command-line + GUI todo manager written in Python.

## Features

- Command-line interface (`todo.py`)
- Tkinter GUI (`todo_gui.py`)
- Tasks shared between CLI and GUI via `~/.todo-cli.json`
- Add, list, mark done, delete tasks

## Usage

### CLI

    python3 todo.py add "Buy milk"
    python3 todo.py list
    python3 todo.py done 1

### GUI

    python3 todo_gui.py

## Requirements

- Python 3.8+ (Tkinter comes bundled with most Python installs)

On Debian/Kali, if Tkinter is missing:

    sudo apt install python3-tk

## License

MIT
