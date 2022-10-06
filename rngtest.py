import random
import time


def rng(n):
    return random.randint(2 ** (n - 1), 2 ** n)


def prime_number_generator(product_of_ab):
    prime_list = []

    for i in range(product_of_ab + 1):
        prime_list.append(i)

    prime_list[0] = 0
    prime_list[1] = 0

    p = 2
    while p * p <= product_of_ab:
        # If prime[p] is not changed, then it is a prime
        if p != 0:
            # Update all multiples of p to zero
            for i in range(p * 2, product_of_ab + 1, p):
                prime_list[i] = 0

        p += 1

    updated_primes = list(filter(lambda x: x != 0, prime_list))
    print("Possible prime numbers less than " + str(product_of_ab) + ": ")
    print(*updated_primes)
    return random.choice(updated_primes)


bit_size = int(input("Enter the number of bits(Max 10-bit): "))
start = time.time()
random_number_a = rng(bit_size)
random_number_b = rng(bit_size)

while random_number_b == random_number_a:
    random_number_b == rng(bit_size)

product = random_number_a * random_number_b
print("A: ", random_number_a)
print("B: ", random_number_b)
print("Product of A and B: ", product)

random_prime = prime_number_generator(product)
print("Random prime:", random_prime)

m = product - random_prime
print("M value: ", m)
e = m + random_number_a
print("E value: ", e)
d = m + random_number_b
print("D value", d)
n = int(((e * d) - random_prime) / m)
print("N value: ", n)
# print(type(n))
q = pow(random_prime, -1, mod=n)
print("Q value: ", q)
message = int(input("Enter message: "))
cipher = pow((message * q), 1, n)
print("Cipher text: ", cipher)

Dmessage = (cipher * e * d) % n
print("Message Value after decryption: ", Dmessage)
end = time.time()
print("Time taken:", end - start)



