"""FastAPI application for arithmetic and item operations."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """Return a basic health/welcome message."""
    return {"message": "it works !"}


@app.get("/addition")
def add_numbers(a: int, b: int):
    """Add two integers."""
    return {"result a+b=": a + b, "developer": "Dev1"}


@app.post("/multiply")
def multiply_numbers(a: int, b: int):
    """Multiply two integers."""
    return {"result a*b=": a * b, "developer": "Dev2"}


@app.post("/divide")
def divide_numbers(a: int, b: int):
    """Divide two integers, preventing division by zero."""
    if b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result a/b=": a / b, "developer": "Leader"}


@app.delete("/remove/{item_id}")
def delete_item(item_id: int):
    """Delete an item by ID."""
    return {"message": f"Item {item_id} deleted successfully"}


@app.put("/update/{item_id}")
def update_item(item_id: int, name: str):
    """Update an item's name by ID."""
    return {"message": f"Item {item_id} updated successfully", "new_name": name}


@app.get("/soustraction")
def soustraction(a: float, b: float):
    """Return the difference between two numbers."""
    return {"resultat": a - b}
