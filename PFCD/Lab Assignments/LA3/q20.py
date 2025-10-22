def sieve_primes(limit=100):
    sieve = [True] * (limit + 1)
    sieve[0], sieve[1] = False, False

    for num in range(2, int(limit**0.5) + 1):
        if sieve[num]:
            for multiple in range(num*num, limit + 1, num):
                sieve[multiple] = False

    return [num for num, is_prime in enumerate(sieve) if is_prime]

print(sieve_primes())
