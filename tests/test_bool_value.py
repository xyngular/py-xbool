from xbool import bool_value


def test_bool_true_values():
    true_values = [
        True,
        "t",
        "True",
        "T",
        "1",
        "true",
        ' true ',
        object()
    ]

    for test_value in true_values:
        assert bool_value(test_value) is True


def test_bool_false_values():
    false_values = [
        None,
        False,
        "f",
        "False",
        "F",
        "0",
        "false",
        '',
        ' false ',
    ]

    for test_value in false_values:
        assert bool_value(test_value) is False

