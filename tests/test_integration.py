def test_post_user(test_app):
    data = {"uid": "10","email": "t@gmail.com", "username": "user"}
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
        "interests": [],    
    }


def test_put_user(test_app):
    data = {"uid": "10",
            "email": "t@gmail.com",
            "username": "user",
            "height": "180",
            "weight": "75",
            "gender": "male",
            "target": "fat loss",
            "interests": ["Cardio","Fuerza"],
            "birthday": "21-12-1999",
            "level": "pro", 
            "latitude": "100",
            "longitude": "100"
        }
    response = test_app.put(url="/users", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "uid": "10",
        "email": "t@gmail.com",
        "username": "user",
        "height": 180,
        "weight": 75,
        "gender": "male",
        "target": "fat loss",
        "interests": ["Cardio","Fuerza"],
        "birthday": "21-12-1999",
        "level": "pro", 
        "latitude": "100",
        "longitude": "100"
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
        "gender": "male",
        "target": "fat loss",
        "interests": ["Cardio","Fuerza"],
        "birthday": "21-12-1999",
        "level": "pro", 
        "latitude": "100",
        "longitude": "100"
    }
    
def test_get_interests(test_app):
    response = test_app.get(url="/interests")
    assert response.status_code == 200
    assert response.json() == [{'name': 'Cardio', 'desc': 'Entrenamientos relacionados a la resistencia aerobica'},
        {'name': 'Fuerza', 'desc': 'Entrenamientos relacionados a ganar fuerza'},
        {'name': 'HIIT', 'desc': 'Entrenamientos HIIT'},
        {'name': 'Tonificación', 'desc': 'Entrenamientos relacionados a tonificar los músculos'},
        {'name': 'Baile', 'desc': 'Entrenamientos con musica'},
        {'name': 'Kickboxing', 'desc': 'Entrenamientos de pelea'},
        {'name': 'Pilaes', 'desc': 'Entranamientos de pilates'}, 
        {'name': 'Mediatación', 'desc': 'Entrenamientos de meditación'}, 
        {'name': 'Estirar', 'desc': 'Entrenamientos de estiramiento'},
        {'name': 'Yoga', 'desc': 'Entrenamientos de Yoga'},
        {'name': 'Spinning', 'desc': 'Entrenamientos de spinning'}, 
        {'name': 'Cinta', 'desc': 'Entrenamientos de cinta'}]
    
