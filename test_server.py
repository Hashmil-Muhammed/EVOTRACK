from main import app
from fastapi.testclient import TestClient
import traceback

client = TestClient(app)
try:
    response = client.get('/')
    print("Status:", response.status_code)
    print("Text:", response.text)
except Exception as e:
    traceback.print_exc()
