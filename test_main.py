"""Unit tests for the FastAPI endpoints in main.py."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "it works !"}


def test_addition():
    """Test the addition endpoint."""
    response = client.get("/addition", params={"a": 5, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"result a+b=": 8, "developer": "Dev1"}


def test_soustraction_positive():
    """Test subtraction with positive numbers."""
    response = client.get("/soustraction", params={"a": 10, "b": 4})
    assert response.status_code == 200
    assert response.json() == {"resultat": 6.0}


def test_soustraction_negative_and_decimals():
    """Test subtraction resulting in negative and decimal values."""
    response = client.get("/soustraction", params={"a": 2.5, "b": 5.0})
    assert response.status_code == 200
    assert response.json() == {"resultat": -2.5}


def test_soustraction_invalid_params():
    """Test subtraction with invalid query parameters."""
    response = client.get("/soustraction", params={"a": "abc", "b": 2})
    assert response.status_code == 422


def test_multiply():
    """Test the multiplication endpoint."""
    response = client.post("/multiply", params={"a": 4, "b": 6})
    assert response.status_code == 200
    assert response.json() == {"result a*b=": 24, "developer": "Dev2"}


def test_divide_normal():
    """Test division with a non-zero divisor."""
    response = client.post("/divide", params={"a": 10, "b": 2})
    assert response.status_code == 200
    assert response.json() == {"result a/b=": 5.0, "developer": "Leader"}


def test_divide_by_zero():
    """Test division when divisor is zero."""
    response = client.post("/divide", params={"a": 10, "b": 0})
    assert response.status_code == 200
    assert response.json() == {"error": "Division by zero is not allowed"}


def test_update_item():
    """Test updating an item."""
    response = client.put("/update/1", params={"name": "Laptop"})
    assert response.status_code == 200
    assert response.json() == {
        "message": "Item 1 updated successfully",
        "new_name": "Laptop",
    }


def test_delete_item():
    """Test deleting an item."""
    response = client.delete("/remove/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Item 1 deleted successfully"}
