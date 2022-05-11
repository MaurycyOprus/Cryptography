import sympy
import random
import math


def generate_n_phi():
    p = sympy.randprime(10, 50)
    q = sympy.randprime(10, 50)
    while p == q:
        q = sympy.randprime(10, 50)

    n_val = p * q
    phi_val = (p - 1) * (q - 1)
    return n_val, phi_val


def nwd(inp_phi):
    while True:
        x = random.randint(3, 20)
        if math.gcd(inp_phi, x) == 1:
            break
    return x


def generate_d(inp_e, inp_phi):
    while True:
        d_val = random.randint(inp_phi-200, inp_phi+200)
        if (inp_e * d_val - 1) % inp_phi == 0:
            break
    return d_val


def encode_rsa(e_val, n_val):
    words = basic_text.split(" ")
    chars = []
    for word in words:
        x = list(word)
        for i in x:
            chars.append(ord(i)**e_val % n_val)
    return chars


def decode_rsa(text_to_decode, d_val, n_val):
    decoded = []
    for i in text_to_decode:
        decoded.append(chr(i ** d_val % n_val))
    return decoded


basic_text = "at that time the name of abraham was not wellknown so the promise came true only after it was written " \
             "down not before "

if __name__ == '__main__':
    n, phi = generate_n_phi()
    e = nwd(phi)
    print("phi: " + str(phi))
    print("e: " + str(e))
    print("n: " + str(n))
    d = generate_d(e, phi)
    print("Klucz publiczny (e: " + str(e) + ", n: " + str(n) + ")")
    print("Klucz prywatny (d: " + str(d) + ", n: " + str(n) + ")")
    encoded_text = encode_rsa(e, n)
    print(encoded_text)
    decoded_text = decode_rsa(encoded_text, d, n)
    print(decoded_text)


