"""
Unit Tests for FastAPI Application
"""

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


class TestHealthEndpoints:
    """Test health check endpoints"""

    def test_root_endpoint(self):
        """Test root endpoint returns healthy status"""
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert data["version"] == "1.0.0"

    def test_health_endpoint(self):
        """Test health endpoint returns healthy status"""
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"


class TestItemsEndpoints:
    """Test items CRUD endpoints"""

    def test_list_items_empty(self):
        """Test listing items when empty"""
        response = client.get("/items")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_create_item(self):
        """Test creating a new item"""
        item_data = {
            "name": "Test Item",
            "description": "A test item",
            "price": 9.99,
            "is_active": True
        }
        response = client.post("/items", json=item_data)
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Test Item"
        assert data["price"] == 9.99
        assert "id" in data
        assert "created_at" in data

    def test_get_item_not_found(self):
        """Test getting non-existent item"""
        response = client.get("/items/99999")
        assert response.status_code == 404

    def test_delete_item_not_found(self):
        """Test deleting non-existent item"""
        response = client.delete("/items/99999")
        assert response.status_code == 404


class TestUsersEndpoints:
    """Test users endpoints"""

    def test_create_user(self):
        """Test creating a new user"""
        user_data = {
            "username": "testuser",
            "email": "test@example.com",
            "password": "securepassword123"
        }
        response = client.post("/users", json=user_data)
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == "testuser"
        assert data["email"] == "test@example.com"
        assert "password" not in data  # Password should not be returned

    def test_list_users(self):
        """Test listing users"""
        response = client.get("/users")
        assert response.status_code == 200
        assert isinstance(response.json(), list)


class TestValidation:
    """Test input validation"""

    def test_create_item_invalid_price(self):
        """Test creating item with invalid price"""
        item_data = {
            "name": "Test Item",
            "price": "not_a_number"
        }
        response = client.post("/items", json=item_data)
        assert response.status_code == 422  # Validation error

    def test_create_item_missing_required(self):
        """Test creating item without required fields"""
        item_data = {
            "description": "Missing name and price"
        }
        response = client.post("/items", json=item_data)
        assert response.status_code == 422


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
