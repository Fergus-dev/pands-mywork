# attempting to recreate Andrew's prime number generator programme from memory
# Fergus McTiernan

primes = []

up_to = 1001

for candidate in range (2, up_to):
    is_prime = True
    for divisor in primes:
        if (candidate % divisor == 0):
            is_prime = False
            break

    if is_prime:
        primes.append(candidate)

print(primes)



