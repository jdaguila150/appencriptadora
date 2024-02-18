from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os


def decrypt_message(ciphertext, iv, key):
  cipher = Cipher(algorithms.AES(key),
                  modes.CBC(iv),
                  backend=default_backend())
  decryptor = cipher.decryptor()

  padded_data = decryptor.update(ciphertext) + decryptor.finalize()

  unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
  original_message = unpadder.update(padded_data) + unpadder.finalize()

  return original_message.decode('utf-8') 