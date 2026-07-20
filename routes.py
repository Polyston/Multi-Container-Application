from fastapi import APIRouter, status
from schemas import TodoItem, TodoItemResponse
from database import TodoList

# Stores routes for todo-list operations
todo_router = APIRouter()

# Endpoint used to create a new todo entry
@todo_router.post("/todos", response_model=TodoItemResponse, status_code=status.HTTP_201_CREATED)
def create_todo_entry(Todo: TodoItem):

    # Defines a dictionary to be inserted into the TodoList collection to be stored as a document
    todo_document = {
        "title": Todo.title,
        "description": Todo.description
    }

    # The result of the insertion is stored as an InsertOneResult object
    result = TodoList.insert_one(todo_document)

    # The data inserted into the TodoList collection along with the document id is validated by the response model and returned
    return {"id": str(result.inserted_id), "title": todo_document["title"], "description": todo_document["description"]}