"""Serve student and department information from the college database."""

from flask import Flask, jsonify

from connection import getSqliteConnection

app = Flask(__name__)


@app.route("/studentDepartments", methods=["GET"])
def student_departments():
    connection = getSqliteConnection()
    try:
        rows = connection.execute(
            """SELECT students.StudentName, departments.DepartmentName
               FROM students
               JOIN departments ON students.DepartmentId = departments.DepartmentId
               ORDER BY students.StudentId"""
        ).fetchall()
    finally:
        connection.close()

    return jsonify([
        {"StudentName": student_name, "DepartmentName": department_name}
        for student_name, department_name in rows
    ])


@app.route("/departments", methods=["GET"])
def departments():
    connection = getSqliteConnection()
    try:
        rows = connection.execute(
            "SELECT DepartmentId, DepartmentName FROM departments ORDER BY DepartmentId"
        ).fetchall()
    finally:
        connection.close()

    return jsonify([
        {"DepartmentId": department_id, "DepartmentName": department_name}
        for department_id, department_name in rows
    ])


if __name__ == "__main__":
    app.run(debug=True)