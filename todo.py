"""A tiny command-line todo manager."""

import json
import sys
from pathlib import Path

DATA_FILE = Path.home() / ".todo-cli.json"


def load_tasks():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


def save_tasks(tasks):
    DATA_FILE.write_text(json.dumps(tasks, indent=2))


def add_task(text):
    tasks = load_tasks()
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print(f"Added: {text}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, 1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['text']}")


def done_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Done: {tasks[index - 1]['text']}")
    else:
        print("Invalid task number.")


def delete_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Deleted: {removed['text']}")
    else:
        print("Invalid task number.")


def main():
    if len(sys.argv) < 2:
        print("Usage: todo.py [add|list|done|delete] [args]")
        return
    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done" and len(sys.argv) > 2:
        done_task(int(sys.argv[2]))
    elif cmd == "delete" and len(sys.argv) > 2:
        delete_task(int(sys.argv[2]))
    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()
