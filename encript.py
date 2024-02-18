from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os


def encript_message(message, key):
  iv = os.urandom(16)

  cipher = Cipher(algorithms.AES(key),
                  modes.CBC(iv),
                  backend=default_backend())
  encryptor = cipher.encryptor()

  padder = padding.PKCS7(algorithms.AES.block_size).padder()
  padded_data = padder.update(message.encode('utf-8')) + padder.finalize()

  ciphertext = encryptor.update(padded_data) + encryptor.finalize()
  return ciphertext, iv
