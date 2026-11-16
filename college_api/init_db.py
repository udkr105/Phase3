"""Recreate and seed the college departments and students tables."""

from connection import getSqliteConnection


def main():
    """Reset both tables, insert the sample records, and print row counts."""
    connection = getSqliteConnection()
    try:
        connection.execute("PRAGMA foreign_keys = ON")
        connection.execute("BEGIN")
        with connection:
            connection.execute("DROP TABLE IF EXISTS students")
            connection.execute("DROP TABLE IF EXISTS departments")
            connection.execute(
                """CREATE TABLE departments (
                    DepartmentId INTEGER PRIMARY KEY,
                    DepartmentName TEXT NOT NULL
                )"""
            )
            connection.execute(
                """CREATE TABLE students (
                    StudentId INTEGER PRIMARY KEY,
                    StudentName TEXT NOT NULL,
                    DepartmentId INTEGER,
                    FOREIGN KEY (DepartmentId) REFERENCES departments (DepartmentId)
                )"""
            )
            department_count = connection.executemany(
                "INSERT INTO departments (DepartmentId, DepartmentName) VALUES (?, ?)",
                [
                    (1, "Computer Science"),
                    (2, "Electrical Engineering"),
                    (3, "Mechanical Engineering"),
                    (4, "Mathematics"),
                    (5, "Physics"),
                ],
            ).rowcount
            student_count = connection.executemany(
                "INSERT INTO students (StudentId, StudentName, DepartmentId) VALUES (?, ?, ?)",
                [
                    (101, "Alice Johnson", 1),
                    (102, "Bob Smith", 2),
                    (103, "Carol Lee", 3),
                    (104, "David Brown", 4),
                    (105, "Emily White", 5),
                ],
            ).rowcount
    finally:
        connection.close()

    print(f"Inserted {department_count} rows into departments.")
    print(f"Inserted {student_count} rows into students.")


if __name__ == "__main__":
    main()