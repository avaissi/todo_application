# Todo Application

This is a Todo application split into two components: Frontend and backend.

The frontend application is built with React and Redux Toolkit. See `src/`.

The backend application, i.e. server side of the application, is built with Python using FastAPI for api routes
and pydantic for typing object models. Server is running with uvicorn.


## To run the application
- Start backend:
  - Install
  - Run from `backend/`: `python main.py`
- Run from root: `npm install` and `npm run dev`

- Replace `plugin:@typescript-eslint/recommended` to `plugin:@typescript-eslint/recommended-type-checked` or `plugin:@typescript-eslint/strict-type-checked`
- Optionally add `plugin:@typescript-eslint/stylistic-type-checked`
- Install [eslint-plugin-react](https://github.com/jsx-eslint/eslint-plugin-react) and add `plugin:react/recommended` & `plugin:react/jsx-runtime` to the `extends` list
