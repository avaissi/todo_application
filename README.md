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
  - To add new todos: Press Add Todo-button
  - To mark an item complete click the checkbox
  - To unmark an item click the filled checkbox
  - To delete a todo item click the X-button
  - To edit a todo item double click the item's content text and press enter or click aside the text field

### Application screenshot

![todo_application_screenshot](https://github.com/avaissi/todo_application/assets/2530247/c4298dc4-1318-4892-9785-f4013cc5a101)
