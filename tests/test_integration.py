def test_post(test_app):
    data = {"uid": "10","email": "t@gmail.com", "username": "user"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "uid": "10",
        "email": "t@gmail.com",
        "username": "user",
        "height": None,
        "weight": None,
        "gender": None,
        "target": None,
        "interests": [],    
    }


def test_put(test_app):
    data = {"uid": "10","email": "t@gmail.com","username": "user", "height": "180","weight": "75","gender": "male", "target": "fat loss","interests": ["Cardio","Fuerza"]}
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
        "interests": ["Cardio","Fuerza"]
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
        "interests": ["Cardio","Fuerza"]
    }    