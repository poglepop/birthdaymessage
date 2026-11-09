from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import datetime

# Initialize the API application
app = FastAPI()

# 1. Mock Database: An in-memory list to store people
# Each item will have an id, name, surname, dob, relationship, and importance

db = [
    {"item_id": 1, "name": "John", "surname": "Doe", "dob": datetime.datetime(1990, 11, 15), "relationship": "Friend", "importance": 5},
    {"item_id": 2, "name": "Jane", "surname": "Smith", "dob": datetime.datetime(1985, 11, 10), "relationship": "Family", "importance": 10},
    {"item_id": 3, "name": "Alice", "surname": "Johnson", "dob": datetime.datetime(2009, 10, 20), "relationship": "Colleague", "importance": 3},
    {"item_id": 4, "name": "Neville", "surname": "Clarkson", "dob": datetime.datetime(1978, 11, 25), "relationship": "Colleague", "importance": 3},
    {"item_id": 5, "name": "Bob", "surname": "Brown", "dob": datetime.datetime(1992, 11, 5), "relationship": "Friend", "importance": 4},
    {"item_id": 6, "name": "Charlie", "surname": "Davis", "dob": datetime.datetime(1988, 7, 12), "relationship": "Family", "importance": 8},
    {"item_id": 7, "name": "Diana", "surname": "Evans", "dob": datetime.datetime(1995, 9, 30), "relationship": "Colleague", "importance": 6},
    {"item_id": 8, "name": "Ethan", "surname": "Foster", "dob": datetime.datetime(1991, 2, 18), "relationship": "Friend", "importance": 7}, 

]

# 2. Pydantic Models for Data Validation
class Item(BaseModel):
    name: str
    description: Optional[str] = None

# --- READ (Root) ---
@app.get("/")
def read_root():
    return {"message": "Welcome to my Python API!", "status": "active"}

# --- CREATE ---
@app.post("/items/")
def create_item(item: Item):
    # Generate a new ID based on the last item in the list
    new_id = db[-1]["item_id"] + 1 if db else 1
    
    new_item = {
        "item_id": new_id,
        "name": item.name,
        "description": item.description
    }
    db.append(new_item)
    return {"message": "Item created successfully", "data": new_item}

# --- READ (All Items) ---
@app.get("/items/")
def read_all_items():
    return {"items": db}

# --- READ (Single Item by ID) ---
@app.get("/items/{item_id}")
def read_item(item_id: int):
    # Search for the item in our mock database
    for item in db:
        if item["item_id"] == item_id:
            return item
    # If not found, return a 404 error
    raise HTTPException(status_code=404, detail="Item not found")

# --- UPDATE ---
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for item in db:
        if item["item_id"] == item_id:
            item["name"] = updated_item.name
            item["description"] = updated_item.description
            return {"message": "Item updated successfully", "data": item}
    
    raise HTTPException(status_code=404, detail="Item not found")

# --- DELETE ---
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(db):
        if item["item_id"] == item_id:
            deleted_item = db.pop(index)
            return {"message": "Item deleted successfully", "data": deleted_item}
            
    raise HTTPException(status_code=404, detail="Item not found")

# --- COUNT ENDPOINT ---
@app.get("/items/count")
def get_items_count():
    # len() returns the total number of elements in the mock database list
    total_count = len(db)
    return {"total_items": total_count}