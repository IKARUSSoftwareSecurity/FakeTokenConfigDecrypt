import base64
from Crypto.Cipher import Blowfish
import sys

"""
Decrypts the config file for the Fake-TextSecure Online Banking Trojan.

@author: bachmann.s 2014
"""

if len(sys.argv) != 3:
    print("Usage: %s blfs.key config.cfg" % sys.argv[0])
    sys.exit(1)
    
iv = "12345678"
key = "".join(list(map(lambda x: x[2:], map(hex, map(ord, open(sys.argv[1]).read())))))[:50]
ciphertext = base64.b64decode(open(sys.argv[2]).read())

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)

print(cipher.decrypt(ciphertext).decode("UTF-8"))