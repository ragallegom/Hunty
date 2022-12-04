from fastapi.testclient import TestClient

from main import app

"""
    Unit Test
"""

client = TestClient(app)

def test_read_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Prueba técnica Hunty"}