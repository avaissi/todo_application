# Todo Application Backend

This is a Todo application's server application.

This is built with Python using FastAPI for api routes
and pydantic for typing object models. Server is running with uvicorn.


## To run the application
- Start backend from `backend/`:
    - Install either with poetry: `poetry install` or using pip: `pip install -r requirements.txt`
    - Run either with poetry `poetry run python main.py` or `python main.py`
    - Backend creates and uses a JSON file as database located in `~/json_db/todo.json` or with Windows `C:Users\[user]\json_db\todo.json`
