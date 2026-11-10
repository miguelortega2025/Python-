#  To-Do List (Python CLI)

A simple command-line to-do list app that **persists tasks in a JSON file** between runs.

Built as a **Level 4** Python practice exercise, focused on:
- Reading/writing files
- Error handling with `try/except`
- Working with JSON
- Program structure with functions and a `main()`

---

##  Features

- Show all tasks with `[x]` / `[ ]` markers
- Add new tasks (rejects empty or duplicate titles)
- Mark tasks as done
- Remove tasks
- Automatic save to `tasks.json` on every change
- Safe loading: handles missing files, invalid JSON, and I/O errors

---

##  Usage

```bash
python todo.py
```

You'll see an interactive menu:

```
--- TO-DO LIST ---
1. Show tasks
2. Add task
3. Mark as done
4. Remove task
5. Exit
Choose an option (1-5):
```

Tasks are stored in `tasks.json` in the same folder:

```json
[
  { "title": "Buy milk", "done": false },
  { "title": "Study Python", "done": true }
]
```

---

##  Functions overview

| Function | Description |
|---|---|
| `load_tasks(filename)` | Loads tasks from JSON; returns `[]` if the file is missing or invalid |
| `save_tasks(tasks, filename)` | Writes tasks to JSON with `indent=2` and `ensure_ascii=False` |
| `add_task(tasks, title)` | Adds a task; rejects empty or duplicate titles |
| `mark_done(tasks, title)` | Marks a task as done (case-insensitive match) |
| `remove_task(tasks, title)` | Removes a task by title |
| `show_tasks(tasks)` | Prints all tasks with `[x]` / `[ ]` markers |
| `main()` | Interactive menu loop |

---

##  Full Source Code — `todo.py`

```python
# todo.py
import json
import os


FILENAME = "tasks.json"


def load_tasks(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            print("Warning: file has unexpected format, starting empty.")
            return []
        return data
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: could not load tasks ({e}). Starting empty.")
        return []


def save_tasks(tasks, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Error saving tasks: {e}")


def add_task(tasks, title):
    title = title.strip()
    if not title:
        print("Title cannot be empty ")
        return False
    if any(t["title"].lower() == title.lower() for t in tasks):
        print("Task already exists ")
        return False
    tasks.append({"title": title, "done": False})
    print(f"Added: {title} ")
    return True


def mark_done(tasks, title):
    title = title.strip().lower()
    for t in tasks:
        if t["title"].strip().lower() == title:
            t["done"] = True
            print(f"Marked as done: {t['title']} ")
            return True
    print("Task not found ")
    return False


def remove_task(tasks, title):
    title = title.strip().lower()
    for i, t in enumerate(tasks):
        if t["title"].strip().lower() == title:
            tasks.pop(i)
            print(f"Removed: {t['title']} ")
            return True
    print("Task not found ")
    return False


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, t in enumerate(tasks, start=1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['title']}")


def main():
    tasks = load_tasks(FILENAME)

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Mark as done")
        print("4. Remove task")
        print("5. Exit")

        option = input("Choose an option (1-5): ").strip()

        if option == "1":
            show_tasks(tasks)
        elif option == "2":
            title = input("Task title: ")
            if add_task(tasks, title):
                save_tasks(tasks, FILENAME)
        elif option == "3":
            title = input("Which task to mark as done? ")
            if mark_done(tasks, title):
                save_tasks(tasks, FILENAME)
        elif option == "4":
            title = input("Which task to remove? ")
            if remove_task(tasks, title):
                save_tasks(tasks, FILENAME)
        elif option == "5":
            save_tasks(tasks, FILENAME)
            print("Goodbye! ")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()
```

---

##  Error handling

- **Missing file** → starts with an empty list
- **Invalid JSON** → prints a warning and starts empty
- **Write errors** → caught with `OSError`
- **Empty or duplicate titles** → rejected in `add_task`
- **Case-insensitive matching** → `mark_done` and `remove_task` ignore case and leading/trailing spaces

---

##  Requirements

- Python 3.7+
- No external libraries (only `json` and `os` from the standard library)

---

##  Example session

```
--- TO-DO LIST ---
1. Show tasks
2. Add task
3. Mark as done
4. Remove task
5. Exit
Choose an option (1-5): 2
Task title: Study Python
Added: Study Python 

--- TO-DO LIST ---
Choose an option (1-5): 1
1. [ ] Study Python

--- TO-DO LIST ---
Choose an option (1-5): 3
Which task to mark as done? study python
Marked as done: Study Python 

--- TO-DO LIST ---
Choose an option (1-5): 1
1. [x] Study Python
```
---

## 📄 License

This project is for learning purposes. Feel free to use it however you like.
