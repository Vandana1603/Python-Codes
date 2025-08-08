def find_primes(num):
    is_prime = [True] * (num + 1)
    is_prime[0] = is_prime[1] = False
    for number in range(2, int(num**0.5) + 1):
        if is_prime[number]:
            for multiple in range(number * 2, num + 1, number):
                is_prime[multiple] = False

    primes = []
    for i in range(num + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

i=input("Enter the Limit:")
res=find_primes(int(i))
print(res)