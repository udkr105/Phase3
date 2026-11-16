"""Serve an in-memory to-do app with task creation and deletion routes."""

from datetime import date

from flask import Flask, abort, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []


@app.route("/")
def index():
    """Render the task table in ascending due-date order.

    Returns:
        str: The rendered task-page HTML.
    """
    # Preserve list indexes so sorted rows delete the correct tasks.
    task_rows = sorted(enumerate(tasks), key=lambda row: row[1]["due_date"])
    return render_template("index.html", tasks=task_rows)


@app.route("/add", methods=["POST"])
def add_task():
    """Validate submitted task fields and append a task to the in-memory list.

    Returns:
        flask.Response: A redirect to the task page after adding the task.

    Raises:
        werkzeug.exceptions.BadRequest: If a required field is missing or invalid.
    """
    task = request.form.get("task", "").strip()
    priority = request.form.get("priority", "")
    category = request.form.get("category", "")
    due_date = request.form.get("due_date", "")
    if not task or len(task) > 200:
        abort(400, description="A task name of 1 to 200 characters is required.")
    if priority not in ("High", "Medium", "Low"):
        abort(400, description="Choose a valid priority.")
    if category not in ("Work", "Personal", "Health"):
        abort(400, description="Choose a valid category.")
    try:
        due_date = date.fromisoformat(due_date).isoformat()
    except ValueError:
        abort(400, description="A valid due date is required.")
    tasks.append({"task": task, "priority": priority, "category": category, "due_date": due_date})
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    """Remove a task from the in-memory list by its current index.

    Args:
        task_id (int): The zero-based list index supplied by the route.

    Returns:
        flask.Response: A redirect to the task page after deleting the task.

    Raises:
        werkzeug.exceptions.NotFound: If the index is beyond the task list.
    """
    if task_id >= len(tasks):
        abort(404)
    tasks.pop(task_id)
    return redirect(url_for("index"))


def count_tasks_by_priority(tasks, priority):
    count = 0
    for task in tasks:
        if task['priority'] == priority:
            count += 1
    return count



if __name__ == "__main__":
    app.run(debug=True)
