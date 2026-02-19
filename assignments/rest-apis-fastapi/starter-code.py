from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str = None

# In-memory storage for items
items = []

@app.get("/items")
def get_items():
    return items

# Add more endpoints here