from pricing import apply_discount


def test_launch_discount():
    assert apply_discount(100) == 90
