from primes import is_prime


def test_primes_true():
    assert is_prime(2)
    assert is_prime(5)
    assert is_prime(7)


def test_primes_false():
    assert not is_prime(-200)
    assert not is_prime(3.1)
    assert not is_prime(0)
    assert not is_prime(1)
    assert not is_prime(4)
    assert not is_prime(8)
