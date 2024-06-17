# Todo Application

This is a Todo application split into two components: Frontend and backend.

The frontend application is built with React and Redux Toolkit. See `src/`.

The backend application, i.e. server side of the application, is built with Python using FastAPI for api routes
and pydantic for typing object models. Server is running with uvicorn.


## To run the application
- Start backend from `backend/`:
  - Install either with poetry: `poetry install` or using pip: `pip install -r requirements.txt`
  - Run either with poetry `poetry run python main.py` or `python main.py`
  - Backend creates and uses a JSON file as database located in `~/json_db/todo.json` or with Windows `C:Users\[user]\json_db\todo.json`
- Start frontend from root `/`
  - Install with npm: `npm install`
  - Run with npm: `npm run dev`
