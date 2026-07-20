from pydantic import BaseModel

# Validates input data entered into the todo list endpoints
class TodoItem(BaseModel):
    title: str
    description: str

# Validates the data returned from the todo list endpoints
class TodoItemResponse(BaseModel):
    id: str
    title: str
    description: str