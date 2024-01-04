from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse('123') == '321'


def test_reverse_for_empty_str():
    assert reverse('') == ''
