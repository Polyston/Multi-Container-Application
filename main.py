from fastapi import FastAPI
from routes import todo_router

# A FastAPI instance is created
app = FastAPI()

# The router used for the todo list is added to the FastAPI instance
app.include_router(todo_router)