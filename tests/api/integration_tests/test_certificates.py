def test_post_certificate(test_app):
    data = {
        "uid": "100",
        "email": "t100@gmail.com",
        "username": "user100",
        "birthday": None,
        "level": None,
        "latitude": None,
        "longitude": None,
        "height": None,
        "weight": None,
        "gender": None,
        "target": None,
        "trainingtypes": [],
        "user_type": None,
        "image_url": None,
        "token": None,
        "blocked": False,
        "certified": False,
    }
    user = test_app.post(url="/users", json=data)
    assert user.status_code == 201
    assert user.json() == {
        "uid": "100",
        "email": "t100@gmail.com",
        "username": "user100",
        "birthday": None,
        "level": None,
        "latitude": None,
        "longitude": None,
        "height": None,
        "weight": None,
        "gender": None,
        "target": None,
        "trainingtypes": [],
        "user_type": None,
        "image_url": None,
        "token": None,
        "blocked": False,
        "certified": False,
    }

    certificate = {"state": None, "link": "video.com"}
    response = test_app.post(url="/certificates/100", json=certificate)
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "uid": "100",
        "state": None,
        "link": "video.com",
    }


def test_put_certificate(test_app):
    data = {
        "uid": "100",
        "email": "t100@gmail.com",
        "username": "user100",
    }
    user = test_app.post(url="/users", json=data)
    assert user.status_code == 201

    certificate = {"state": None, "link": "video.com"}
    response = test_app.post(url="/certificates/100", json=certificate)
    assert response.status_code == 201

    certificate = {"state": True, "link": "video.com"}
    response = test_app.put(url="/certificates/100/1", json=certificate)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "uid": "100",
        "state": True,
        "link": "video.com",
    }

    user = test_app.get(url="/users/100")
    assert user.status_code == 200
    assert user.json() == {
        "uid": "100",
        "email": "t100@gmail.com",
        "username": "user100",
        "birthday": None,
        "level": None,
        "latitude": None,
        "longitude": None,
        "height": None,
        "weight": None,
        "gender": None,
        "target": None,
        "trainingtypes": [],
        "user_type": None,
        "image_url": None,
        "token": None,
        "blocked": False,
        "certified": True,
    }


def test_get_certificate(test_app):
    data = {
        "uid": "100",
        "email": "t100@gmail.com",
        "username": "user100",
    }
    user = test_app.post(url="/users", json=data)
    assert user.status_code == 201

    certificate = {"state": None, "link": "video.com"}
    response = test_app.post(url="/certificates/100", json=certificate)
    assert response.status_code == 201

    response = test_app.get(url="/certificates/100")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "uid": "100",
        "state": None,
        "link": "video.com",
    }


def test_get_certificates(test_app):
    data = {
        "uid": "100",
        "email": "t100@gmail.com",
        "username": "user100",
    }
    user = test_app.post(url="/users", json=data)
    assert user.status_code == 201

    certificate = {"state": None, "link": "video.com"}
    response = test_app.post(url="/certificates/100", json=certificate)
    assert response.status_code == 201

    response = test_app.get(url="/certificates")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "uid": "100", "state": None, "link": "video.com"}
    ]
