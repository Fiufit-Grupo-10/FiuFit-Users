# content of test_sample.py
import app.main

def test_answer():
    assert app.main.inc(4) == 5


def test_nothing():
    assert app.main.inc(3) == 4
