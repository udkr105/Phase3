# Business Task Manager

A small Flask to-do app for adding, viewing, and deleting tasks in a browser.

## Features

- Add tasks with a task name, priority (High, Medium, Low), category (Work,
  Personal, Health), and due date.
- All fields are required; task names may contain up to 200 characters.
- View tasks in a table sorted by due date, earliest first.
- Delete individual tasks using the Delete button on each row.

Tasks are stored in an in-memory list as dictionaries with the keys `task`,
`priority`, `category`, and `due_date`. There is no database or persistent
storage: stopping or restarting the server, including an automatic debug reload,
clears all tasks. Tasks are shared by all visitors to the same server process.

## Requirements

- Python 3 with `venv` and pip available.
- Flask, installed in the virtual environment below.

## Setup

Open a terminal in the project directory. On Linux or macOS, create and activate
a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

If the `venv` directory already exists, skip creation and just activate it.

Install the dependency into the active environment:

```bash
python -m pip install flask
```

## Run

With the virtual environment activated, run:

```bash
python app.py
```

Open <http://127.0.0.1:5000> in your browser. Fill in all four fields and select
**Add Task** to create a task. Select **Delete** on a row to remove it.

Press `Ctrl+C` in the terminal to stop the server. To leave the virtual
environment afterward, run:

```bash
deactivate
```

The app runs Flask's development server with debug mode enabled. Use it for
local development only, not production.

## Project Files

- [app.py](app.py): Flask routes, input validation, and in-memory task storage.
- [templates/index.html](templates/index.html): Task form, table, and page styling.