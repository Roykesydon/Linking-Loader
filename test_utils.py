from utils import hex_to_int, int_to_hex


def test_hex_to_int():
    assert -1 == hex_to_int("FFF")
    assert -2 == hex_to_int("FFE")
    assert 15 == hex_to_int("00F")


def test_int_to_hex():
    assert "FFFB" == int_to_hex(-5, 4)
    assert "B" == int_to_hex(-5)
    assert "FFEC" == int_to_hex(-20, 4)
    assert "0015" == int_to_hex(21, 4)
    assert "15" == int_to_hex(21)


if __name__ == "__main__":
    test_hex_to_int()
    test_int_to_hex()
    print("OK")
