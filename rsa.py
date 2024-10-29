import time
import random
from sympy import isprime
import matplotlib.pyplot as plt

# Function to generate large prime numbers
def generate_large_prime(bits=16):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# Function to calculate the modular inverse (used for decryption key calculation)
def modular_inverse(e, phi):
    def extended_gcd(a, b):
        if a == 0:
            return (b, 0, 1)
        gcd, x1, y1 = extended_gcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return gcd, x, y
    
    gcd, x, _ = extended_gcd(e, phi)
    return x % phi

# RSA Key Generation
def generate_rsa_keys(bits=16):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose a public exponent
    e = 65537  # Common choice for e
    d = modular_inverse(e, phi)
    
    return (e, n), (d, n)  # (public_key, private_key)

# RSA Encryption
def encrypt(plain_text, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in plain_text]

# RSA Decryption
def decrypt(cipher_text, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in cipher_text])

# Measure decryption time
def measure_decryption_time(cipher_text, private_key):
    start_time = time.time()
    decrypt(cipher_text, private_key)
    end_time = time.time()
    return end_time - start_time

# Main function
def main():
    public_key, private_key = generate_rsa_keys(bits=16)
    message = "Hi this is Rikhil"
    
    # Encrypt the message
    cipher_text = encrypt(message, public_key)
    print(f"Encrypted Message: {cipher_text}")
    
    # Measure decryption times
    decryption_times = []
    for _ in range(100):  # Repeat to gather timing data
        decryption_times.append(measure_decryption_time(cipher_text, private_key))
    
    # Plot timing data
    plt.plot(decryption_times, label="Decryption Time")
    plt.xlabel("Attempt")
    plt.ylabel("Time (seconds)")
    plt.title("RSA Decryption Timing Analysis")
    plt.legend()
    plt.show()

    # Display decrypted message
    decrypted_message = decrypt(cipher_text, private_key)
    print(f"Decrypted Message: {decrypted_message}")

# Run the main function
if __name__ == "__main__":
    main()
