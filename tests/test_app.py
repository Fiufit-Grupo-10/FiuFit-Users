def test_ping(test_app):
    response = test_app.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"ping": "pong"}


def test_post(test_app):
    data = {"email": "t@gmail.com", "username": "user", "password": "pass"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "email": "t@gmail.com",
        "username": "user",
        "password": "pass",
    }
