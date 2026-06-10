from logic_utils import build_guess_message


def test_message_reflects_easy_range():
    # Easy difficulty is 1-20, so the hint must say so -- not "1 and 100".
    msg = build_guess_message(1, 20, 5)
    assert "between 1 and 20" in msg
    assert "1 and 100" not in msg


def test_message_reflects_normal_range():
    msg = build_guess_message(1, 100, 7)
    assert "between 1 and 100" in msg


def test_message_uses_actual_upper_bound_not_hardcoded_100():
    # The original bug hardcoded 100; for any other range, 100 must not appear.
    low, high = 1, 20
    msg = build_guess_message(low, high, 3)
    assert str(high) in msg
    assert "100" not in msg


def test_message_shows_attempts_left():
    msg = build_guess_message(1, 50, 4)
    assert "Attempts left: 4" in msg
