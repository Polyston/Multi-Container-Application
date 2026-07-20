from pymongo import MongoClient

# Connects to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# db is used to access the todo list database
db = client.todo_list_db

# TodoList stores the collection for the todo list
TodoList = db.TodoList