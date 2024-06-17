import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import todos

request_origins = ["http://localhost:5173"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=request_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todos.router)


@app.get("/")
async def get_root():
    return {"Hello": "World"}


def main():
    uvicorn.run(app, host="127.0.0.1", port=5000)


if __name__ == '__main__':
    main()
