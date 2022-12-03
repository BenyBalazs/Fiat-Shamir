from FiatShamir import calculate_n_param, generate_key, fiat_shamir


def fiat_shamir_main():
    n = calculate_n_param(15)
    secret = "A majmok a fán ugrálnak!"
    public_key = generate_key(secret, n)
    print(fiat_shamir(secret, public_key, n))


if __name__ == '__main__':
    fiat_shamir_main()
