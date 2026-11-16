# College API

Run the following commands from the `college_api` directory on Linux or macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install flask
python init_db.py
python boilerCode.py
```

`init_db.py` drops and recreates both tables, replacing their existing data with
the sample records. Run it only when you want to initialize or reset the database.
The connection helper uses `studentDB.db` in the current working directory, so
run both scripts from `college_api`.

The API is available at <http://127.0.0.1:5000/studentDepartments> and
<http://127.0.0.1:5000/departments>. The root URL returns 404. Press Ctrl+C to
stop the development server.