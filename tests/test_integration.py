def test_post_user(test_app):
    data = {"email": "t@gmail.com", "username": "user"}
    response = test_app.post(url="/users/10", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "uid": "10",
        "email": "t@gmail.com",
        "username": "user",
        "birthday": None,
        "level": None,
        "latitude": None,
        "longitude": None,
        "height": None,
        "weight": None,
        "gender": None,
        "target": None,
        "trainingtypes": [],
        "user_type": None
    }


def test_put_user(test_app):
    data = {
        "email": "t@gmail.com",
        "username": "user",
        "height": "180",
        "weight": "75",
        "gender": "M",
        "target": "fat loss",
        "trainingtypes": ["Cardio", "Fuerza"],
        "birthday": "1999-12-21",
        "level": "pro",
        "latitude": "100",
        "longitude": "100",
        "user_type": "athlete"
    }
    response = test_app.put(url="/users/10", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "uid": "10",
        "email": "t@gmail.com",
        "username": "user",
        "height": 180,
        "weight": 75,
        "gender": "M",
        "target": "fat loss",
        "trainingtypes": ["Cardio", "Fuerza"],
        "birthday": "1999-12-21",
        "level": "pro",
        "latitude": 100.0,
        "longitude": 100.0,
        "user_type": "athlete"
    }


def test_get_user(test_app):
    response = test_app.get(url="/users/10")
    assert response.status_code == 200
    assert response.json() == {
        "uid": "10",
        "email": "t@gmail.com",
        "username": "user",
        "height": 180,
        "weight": 75,
        "gender": "M",
        "target": "fat loss",
        "trainingtypes": ["Cardio", "Fuerza"],
        "birthday": "1999-12-21",
        "level": "pro",
        "latitude": 100.0,
        "longitude": 100.0,
        "user_type": "athlete"
    }


def test_get_trainingtypes(test_app):
    response = test_app.get(url="/trainingtypes")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Cardio",
            "desc": "Entrenamientos relacionados a la resistencia aerobica",
        },
        {"name": "Fuerza", "desc": "Entrenamientos relacionados a ganar fuerza"},
        {"name": "HIIT", "desc": "Entrenamientos HIIT"},
        {
            "name": "Tonificación",
            "desc": "Entrenamientos relacionados a tonificar los músculos",
        },
        {"name": "Baile", "desc": "Entrenamientos con musica"},
        {"name": "Kickboxing", "desc": "Entrenamientos de pelea"},
        {"name": "Pilates", "desc": "Entrenamientos de pilates"},
        {"name": "Mediatación", "desc": "Entrenamientos de meditación"},
        {"name": "Estirar", "desc": "Entrenamientos de estiramiento"},
        {"name": "Yoga", "desc": "Entrenamientos de Yoga"},
        {"name": "Spinning", "desc": "Entrenamientos de spinning"},
        {"name": "Cinta", "desc": "Entrenamientos de cinta"},
    ]
