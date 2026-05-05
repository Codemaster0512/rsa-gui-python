# RSA Logic File

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def get_keys():
    p = 3
    q = 11
    n = p * q
    phi = (p - 1) * (q - 1)

    e = 7
    while gcd(e, phi) != 1:
        e += 1

    d = mod_inverse(e, phi)
    return e, d, n

def encrypt_message(message, e, n):
    return (message ** e) % n

def decrypt_message(cipher, d, n):
    return (cipher ** d) % n