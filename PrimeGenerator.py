from math import sqrt
from random import randrange


def get_random_n_bit_prime(n: int) -> int:
    """
    Generates a random n bit length number
    :param n: the bit length of the prime number
    :return: randomly generated n bit length prime number
    """
    num = __generate_n_bit_random_number(n)
    while not __is_prime_number(num):
        num = __generate_n_bit_random_number(n)

    return num


def __generate_n_bit_random_number(n: int) -> int:
    """
    Generates a random n bit length prime number
    :param n: the bit length of the number
    :return: randomly generated n bit length number
    """
    return randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def __is_prime_number(n: int) -> bool:
    """
    Validates weather the number is prime
    :param n: the number for validation
    :return: the input number is prime or not
    """
    prime_flag = 0
    if n > 1:
        for i in range(2, int((sqrt(n) + 1))):
            if n % i == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False
    else:
        return False
