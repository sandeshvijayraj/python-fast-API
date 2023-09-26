from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_app():
    bodies = [
        {
            "data": {
                "title": "test",
                "description": "testd",
                "attachment": []
            },
            "expected_status": 200,
            "expected_data": {
                "title": "test",
                "description": "testd",
                "attachment": []
            }
        },
        {
            "data": {
                "title": "test"
            },
            "expected_status": 422,
        },
    ]

    for body in bodies:
        response = client.put('/jiraTicket', json=body['data'])
        assert response.status_code == body['expected_status']
        if 'expected_data' in body:
            assert response.json() == body['expected_data']
