# tests using pytest
from fastapi.testclient import TestClient
import httpx

# importing the sys module
import sys        
 
# inserting the mod.py directory at 
# position 1 in sys.path
sys.path.insert(1, '/workspace/fastapi-rest/')    

from main import app

def test_read_main():
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello World'}
