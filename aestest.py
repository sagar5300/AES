import aesencrypt
import aesdecrypt
import secrets

input = input('Enter String:')

rKey = secrets.token_hex(16)

keys = []
key = []

for i in range(0, 32, 2):
    keys.append(rKey[i:i+2])

for i in range(4):
    key.append(keys[i*4:(i*4)+4])

print()
print('Plaintext:', input)
print()
print('Key:', rKey)
print()

cipher = aesencrypt.enc(input, key)

aesdecrypt.dec(cipher, key)