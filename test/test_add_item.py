# tests/test_integration_example.py
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app  # or app instance, depending on your project structure


def test_add_multiple_items():
    app = create_app()
    client = app.test_client()
    

    items = ['Premier item', 'Deuxième item', 'Troisième item']
    for item in items:
        response = client.post('/add', data={'item': item})
        assert response.status_code == 302 
    response = client.get('/')
    for item in items:
        assert item.encode() in response.data