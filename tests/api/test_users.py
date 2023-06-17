def test_post_user(test_app):
    data = {"uid": "10", "email": "t@gmail.com", "username": "user"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 201
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
        "image_url": None,
        "token": None,
        "blocked": False,
        "certified": False,
    }


def test_post_user_uid_fail(test_app):
    data = {"uid": "10", "email": "t2@gmail.com", "username": "user2"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 409
    assert response.json() == {"detail": "User with uid: 10 already exists"}


def test_post_user_username_fail(test_app):
    data = {"uid": "11", "email": "t2@gmail.com", "username": "user"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 409
    assert response.json() == {"detail": "User with username: user already exists"}


def test_post_user_email_fail(test_app):
    data = {"uid": "11", "email": "t@gmail.com", "username": "user2"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 409
    assert response.json() == {"detail": "User with email: t@gmail.com already exists"}


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
        "image_url": "image.com",
        "token": "token_example",
        "blocked": "False",
        "certified": "False",
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
        "image_url": "image.com",
        "token": "token_example",
        "blocked": False,
        "certified": False,
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
        "image_url": "image.com",
        "token": "token_example",
        "blocked": False,
        "certified": False,
    }


def test_get_users_admin(test_app):
    response = test_app.get(url="/users?admin=true&skip=0&limit=2")
    assert response.status_code == 200
    assert response.json() == [
        {
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
            "image_url": "image.com",
            "token": "token_example",
            "blocked": False,
            "certified": False,
        }
    ]


def test_get_users_user(test_app):
    response = test_app.get(url="/users?admin=false&skip=0&limit=2&username=us")
    assert response.status_code == 200
    assert response.json() == [
        {
            "username": "user",
            "birthday": "1999-12-21",
            "user_type": "athlete",
            "image_url": "image.com",
            "gender": "M",
            "email": "t@gmail.com",
            "token": "token_example",
            "certified": False,
            "uid": "10",
        }
    ]


def test_get_user_fail(test_app):
    response = test_app.get(url="/users/25")
    assert response.status_code == 404
    assert response.json() == {"detail": "User 25 not found"}


def test_put_user_username_and_email(test_app):
    data = {
        "email": "t2@gmail.com",
        "username": "user2",
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
        "image_url": "image.com",
        "token": "token_example",
        "certified": False,
    }
    response = test_app.put(url="/users/10", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "uid": "10",
        "email": "t2@gmail.com",
        "username": "user2",
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
        "image_url": "image.com",
        "token": "token_example",
        "blocked": False,
        "certified": False,
    }


def test_post_user_followers(test_app):
    data = {"uid": "11", "email": "t1@gmail.com", "username": "user1"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 201
    data = {"uid": "13", "email": "t3@gmail.com", "username": "user3"}
    response = test_app.post(url="/users", json=data)
    assert response.status_code == 201

    response = test_app.post(url="/users/11/followers/10")
    assert response.status_code == 201
    assert response.json() == {"followed_uid": "11", "follower_uid": "10"}


def test_get_user_followers(test_app):
    response = test_app.post(url="/users/11/followers/13")
    assert response.status_code == 201

    response = test_app.get(url="/users/11/followers")
    assert response.status_code == 200
    assert response.json() == ["10", "13"]


def test_get_user_following(test_app):
    response = test_app.get(url="/users/10/following")
    assert response.status_code == 200
    assert response.json() == ["11"]


def test_delete_user_follower(test_app):
    response = test_app.delete(url="/users/11/followers/10")
    assert response.status_code == 200

    response = test_app.get(url="/users/11/followers")
    assert response.status_code == 200
    assert response.json() == ["13"]


def test_patch_user(test_app):
    data = [{"uid": "10", "blocked": "true"}, {"uid": "11", "blocked": "true"}]
    response = test_app.patch(url="/users", json=data)

    assert response.status_code == 200
    assert response.json() == [
        {
            "uid": "10",
            "email": "t2@gmail.com",
            "username": "user2",
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
            "image_url": "image.com",
            "token": "token_example",
            "blocked": True,
            "certified": False,
        },
        {
            "uid": "11",
            "email": "t1@gmail.com",
            "username": "user1",
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
            "blocked": True,
            "certified": False,
        },
    ]
