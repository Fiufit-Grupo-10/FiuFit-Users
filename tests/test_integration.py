def test_post(test_app):
    data = {"email": "t@gmail.com", "username": "user"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "email": "t@gmail.com",
        "username": "user",
        "height": None,
        "weight": None,
        "gender": None,
        "target": None,
        "interests": [],
    }


# def test_put(test_app):
#     data = {"email": "t@gmail.com","username": "user", "height": "180","weight": "75","gender": "male", "target": "fat loss","interests": ["crossfit"]}
#     response = test_app.put(url="/users", json=data)
#     assert response.status_code == 200
#     assert response.json() == {
#         "email": "t@gmail.com",
#         "username": "user",
#         "height": 180,
#         "weight": 75,
#         "gender": "male",
#         "target": "fat loss",
#         "interests": ["crossfit"]
#     }
