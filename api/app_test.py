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


def test_primes():
    assert process_query(
        "primes: 71, 51, 15, 44, 62") == "[71]"


def test_primes_2():
    assert process_query(
        "primes: 89, 7, 44, 93, 34") == "[89, 7]"


def test_primes_3():
    assert process_query(
        "primes: 9, 7, 60, 30, 23") == "[7, 23]"


def test_multiple_primes():
    assert process_query(
        "primes: 37, 82, 75, 57, 41") == "[37, 41]"


# def test_square_and_cube():
#     assert process_query(
#         "square and a cube: 2162, 676, 64, 27, 1834, 2176, 3954") == "64"
