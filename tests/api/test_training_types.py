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
