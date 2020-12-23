from random import randint

from app.counter import add


def test_counter():
    """
    Generate two random integers between 0 and 100,
      then add them together to get their total and
      test to see if our custom "add" function returns
      the same value.
    """
    randomInt1 = randint(0, 100)
    randomInt2 = randint(0, 100)
    total = randomInt1 + randomInt2
    result = add(randomInt1, randomInt2)
    assert result == total
