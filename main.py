import os
import time
import random


def circular_left_shift(value, n):
    num_bits_in_int = 8
    n = n % num_bits_in_int
    mask = (1 << num_bits_in_int) - 1
    result = (value << n) | (value >> (num_bits_in_int - n))
    result = result & mask
    return result


def circular_right_shift(value, n):
    num_bits_in_int = 8
    n = n % num_bits_in_int
    mask = (1 << num_bits_in_int) - 1
    result = (value >> n) | (value << (num_bits_in_int - n))
    result = result & mask
    return result


def reversing_bits(num):
    bit_size = 8
    binary = bin(num)
    reverse = binary[-1:1:-1]
    reverse = reverse + (bit_size - len(reverse)) * '0'
    return int(reverse, 2)


def rng():
    return random.randint(2 ** (6 - 1), 2 ** 6)


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
    # print("Possible prime numbers less than " + str(product_of_ab) + ": ")
    # print(*updated_primes)
    return random.choice(updated_primes)


def write_file(name, e, d, n):
    with open(name, 'r+') as file:
        for line in file:
            data = int(line.rstrip())
            decryption_lvl_1 = (data * e * d) % n
            decryption_lvl_2 = decryption_lvl_1 ^ key
            decryption_lvl_3 = circular_right_shift(decryption_lvl_2, no_of_bits)
            decryption_lvl_4 = reversing_bits(decryption_lvl_3)
            strbit = chr(decryption_lvl_4)
            made_file.write(strbit)


file_name = input("Enter the file name: ")
key = int(input("Enter the key value: "))
no_of_bits = int(input("Enter the number of bits to be shifted: "))

random_number_a = rng()
random_number_b = rng()

while random_number_b == random_number_a:
    random_number_b == rng()

product = random_number_a * random_number_b
random_prime = prime_number_generator(product)

m = product - random_prime
e = m + random_number_a
d = m + random_number_b
n = int(((e * d) - random_prime) / m)
q = pow(random_prime, -1, mod=n)

file_stats = os.stat(file_name)
file_size = int(file_stats.st_size)

plain_file = open(file_name, "rb+")

byte_count = -1

while byte_count != int(file_size):

    byte = plain_file.read(1)
    converted_byte = int.from_bytes(byte, "big")
    level1_encryption = reversing_bits(converted_byte)  # Level 1 encryption
    level2_encryption = circular_left_shift(level1_encryption, no_of_bits)  # Level 2 encryption
    level3_encryption = level2_encryption ^ key  # Level 3 encryption
    level4_encryption = int(pow((level3_encryption * q), 1, n))  # Level 4 encryption

    # Writing the encrypted data to 2 different files
    if byte_count < int(file_size / 2):
        encrypted_file = open("Encrypted_file1.txt", "a")
        encrypted_file.write(str(level4_encryption) + "\n")
    else:
        encrypted_file = open("Encrypted_file2.txt", "a")
        encrypted_file.write(str(level4_encryption) + "\n")

    byte_count += 1

made_file = open("remade.txt", 'w+')

write_file("Encrypted_file1.txt", e, d, n)
write_file("Encrypted_file2.txt", e, d, n)
print("Completed")
