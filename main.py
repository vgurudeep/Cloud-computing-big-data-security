import os
import time
import random

file_name = input("Enter the file name: ")
key = int(input("Enter the key value: "))
no_of_bits = int(input("Enter the number of bits to be shifted: "))
random_number = random.randint(2**(no_of_bits-1), 2**no_of_bits)

original_data = []
reversed_data = []
leftshifted_data = []
xored_data = []
decrypt = []
bite = []
bit = []
start_time = time.time()


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


file_stats = os.stat(file_name)
file_size = int(file_stats.st_size)

plain_file = open(file_name, "rb")

byte_count = 0
chunk = 0

while byte_count != int(file_size):

    byte = plain_file.read(1)
    bite.append(byte)
    converted_byte = int.from_bytes(byte, "big")

    original_data.append(converted_byte)

    level1_encryption = reversing_bits(converted_byte)  # Level 1 encryption

    reversed_data.append(level1_encryption)

    level2_encryption = circular_left_shift(level1_encryption, no_of_bits)  # Level 2 encryption

    leftshifted_data.append(level2_encryption)

    level3_encryption = level2_encryption ^ key  # Level 3 encryption

    xored_data.append(level3_encryption)
# Writing the encrypted data to 2 different files
    if byte_count < int(file_size / 2):
        encrypted_file = open("Encrypted_file1.txt", "a")
        encrypted_file.write(str(level3_encryption) + "\n")
    else:
        encrypted_file = open("Encrypted_file2.txt", "a")
        encrypted_file.write(str(level3_encryption) + "\n")

    byte_count += 1

made_file = open("remade.jpg", 'wb')
with open("Encrypted_file1.txt") as file:
    for line in file:
        data = int(line.rstrip())
        decryption_lvl_1 = data ^ key
        decryption_lvl_2 = circular_right_shift(decryption_lvl_1, no_of_bits)
        decryption_lvl_3 = reversing_bits(decryption_lvl_2)
        decrypt.append(decryption_lvl_3)
        strbit = str(decryption_lvl_3)
        byte = str.encode(strbit)
        bit.append(byte)
        made_file.write(byte)

with open("Encrypted_file2.txt") as file:
    for line in file:
        data = int(line.rstrip())
        decryption_lvl_1 = data ^ key
        decryption_lvl_2 = circular_right_shift(decryption_lvl_1, no_of_bits)
        decryption_lvl_3 = reversing_bits(decryption_lvl_2)
        decrypt.append(decryption_lvl_3)
        strbit = str(decryption_lvl_3)
        byte = str.encode(strbit)
        bit.append(byte)
        made_file.write(byte)

end_time = time.time()

elapsed_time = end_time-start_time
print("Time taken to encrypt: ", elapsed_time, "seconds")

print("Raw data: ", *bite)
print("Raw data after decryption: ", *bit)

# print("The original data converted to int: ", *original_data)
# print("The value after last lvl decryption: ",*decrypt)
# print("The data after reversing the bits: ", *reversed_data)
# print("The data after performing circular left shift: ", *leftshifted_data)
# print("The data after performing XOR with the key: ", *xored_data)


