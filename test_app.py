from app import greeting


def test_greeting_returns_expected_text():
    assert greeting() == "Hello, I am Selma :)"
