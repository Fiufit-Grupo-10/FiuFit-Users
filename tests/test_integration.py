def test_post(test_app):
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


def test_put(test_app):
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


def test_get(test_app):
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