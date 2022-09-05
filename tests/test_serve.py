from serve.file import get_value


def test_get_true_value():
    assert get_value(True) == "나는 올바른 값이야"


def test_get_false_value():
    assert get_value(False) == "나는 잘못된 값이야"
