from random import randint

from PrimeGenerator import get_random_n_bit_prime


def calculate_n_param(prime_bit_len: int) -> int:
    """
    Calculates a random number for the n param of the fiat-shamir algorithm.
    :param prime_bit_len: the bit length of the generated int
    :return: the n number used for the algorithm.
    """
    p = get_random_n_bit_prime(prime_bit_len)
    q = get_random_n_bit_prime(prime_bit_len)
    n = p * q

    return n


def generate_key(secret: str, n: int) -> int:
    """
    Generates Fiat-Shamir public key
    :param secret: the secret
    :param n: product of 2 random prime numbers
    :return: generated public key for the algorithm.
    """
    x = __convert_secret_to_int(secret)
    return pow(x, 2, n)


def fiat_shamir(secret: str, public_key: int, n: int) -> bool:
    """
    Validates the secret with the key iteration number of times
    :param secret: the secret info
    :param public_key: key to test against
    :param n: product of 2 prime numbers
    :return: whether the identity is accepted
    """
    x = __convert_secret_to_int(secret)
    p_r = randint(1, n - 1)
    p_t = pow(p_r, 2, n)
    v_c = randint(0, 1)
    p_s = (p_r * (x ** v_c)) % n
    return pow(p_s, 2, n) == (p_t * (public_key ** v_c)) % n


def __convert_secret_to_int(secret: str) -> int:
    """
    Converts the secret string to integer value
    :param secret: the string secret
    :return: the secret in int form
    """
    return int.from_bytes(bytes(secret, 'utf-8'), byteorder="big")
