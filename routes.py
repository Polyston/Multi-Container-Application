from fastapi import APIRouter, status, HTTPException
from schemas import TodoItem, TodoItemResponse
from database import TodoList
from bson import ObjectId

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

# Endpoint used to get a single todo entry by id
@todo_router.get("/todos{id}", response_model=TodoItemResponse, status_code=status.HTTP_200_OK)
def get_todo_entry(id: str):

    # Stores the document with the desired todo entry if the passed id matches an existing id
    retrieved_todo_document = TodoList.find_one({"_id": ObjectId(id)})

    # If the id passed is not found, retrieved_todo_document is empty and an error is raised
    if not retrieved_todo_document:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="The entered todo id does not exist")
    
    # The data from the retrieved todo_entry along with the document id is validated by the response model and returned
    return {"id": id, "title": retrieved_todo_document["title"], "description": retrieved_todo_document["description"]}
