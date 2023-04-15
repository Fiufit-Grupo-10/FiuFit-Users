def test_post_user(test_app):
    data = {"uid": "10", "email": "t@gmail.com", "username": "user"}
    response = test_app.post(url="/users", json=data)
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
        "user_type": None,
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
        "user_type": "athlete",
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
        "latitude": 100,
        "longitude": 100,
        "user_type": "athlete",
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
        "latitude": 100,
        "longitude": 100,
        "user_type": "athlete",
    }

def test_get_users(test_app):
    response = test_app.get(url="/users")
    assert response.status_code == 200
    assert response.json() == [{
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
        "latitude": 100,
        "longitude": 100,
        "user_type": "athlete",
    }]

def test_get_user_fail(test_app):
    response = test_app.get(url="/users/25")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "User 25 not found" 
    }

def test_get_trainingtypes(test_app):
    response = test_app.get(url="/trainingtypes")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "Cardio",
            "descr": "Entrenamientos relacionados a la resistencia aerobica",
        },
        {"name": "Fuerza", "descr": "Entrenamientos relacionados a ganar fuerza"},
        {"name": "HIIT", "descr": "Entrenamientos HIIT"},
        {
            "name": "Tonificación",
            "descr": "Entrenamientos relacionados a tonificar los músculos",
        },
        {"name": "Baile", "descr": "Entrenamientos con musica"},
        {"name": "Kickboxing", "descr": "Entrenamientos de pelea"},
        {"name": "Pilates", "descr": "Entrenamientos de pilates"},
        {"name": "Mediatación", "descr": "Entrenamientos de meditación"},
        {"name": "Estirar", "descr": "Entrenamientos de estiramiento"},
        {"name": "Yoga", "descr": "Entrenamientos de Yoga"},
        {"name": "Spinning", "descr": "Entrenamientos de spinning"},
        {"name": "Cinta", "descr": "Entrenamientos de cinta"},
    ]


def test_post_admin(test_app):
    data = {"uid": "20", "email": "admin@gmail.com", "username": "admin"}
    response = test_app.post(url="/admins", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "uid": "20",
        "email": "admin@gmail.com",
        "username": "admin",
    }


def test_get_admin(test_app):
    response = test_app.get(url="/admins/20")
    assert response.status_code == 200
    assert response.json() == {
        "uid": "20",
        "email": "admin@gmail.com",
        "username": "admin",
    }
    
def test_get_admin_fail(test_app):
    response = test_app.get(url="/admins/25")
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Admin 25 not found" 
    }


def test_get_admins(test_app):
    response = test_app.get(url="/admins")
    assert response.status_code == 200
    assert response.json() == [
        {
            "uid": "20",
            "email": "admin@gmail.com",
            "username": "admin",
        }
    ]
