import json

import pytest

from app1.api.crud import users


def test_create_note(test_app, monkeypatch):
    test_request_payload = {"name": "nikolay", "email": "something else","password": "password else"}
    test_response_payload = {"id": 1, "name": "nikolay", "email": "something else", "password": "password else"}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(users, "post", mock_post)

    response = test_app.post("/users/", data=json.dumps(test_request_payload),)

    assert response.status_code == 201
    assert response.json() == test_response_payload