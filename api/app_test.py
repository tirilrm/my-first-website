from app import process_query


def test_knows_about_dinosaurs():
    assert process_query(
        "dinosaurs") == "Dinosaurs ruled the Earth 200 million years ago"


def test_does_not_know_about_asteroids():
    assert process_query(
        "asteroids") == "Unknown"


def test_knows_team_name():
    assert process_query(
        "What is your name?") == "Ak_Tiril"


def test_largest_number():
    assert process_query(
        "largest: 30, 50, 40?") == "50"


def test_product_of_two_numbers():
    assert process_query(
        "10 multiplied by 20") == "200"


def test_of_sum_of_two_numbers():
    assert process_query(
         "57 plus 18") == "75"


def test_minus():
    assert process_query(
        "64 minus 59") == "5"
