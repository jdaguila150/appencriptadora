from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
from encript import encript_message
from decrypt import decrypt_message
import time
import os
import psutil
from encript import encript_message
from decrypt import decrypt_message

def generate_random_key():
    return os.urandom(32)

start_time = time.time()

mensaje = input("Ingrese el mensaje que desea cifrar: ")

start_encrypt_time = time.time()
clave_secreta = generate_random_key()
ciphertext, iv = encript_message(mensaje, clave_secreta)
end_encrypt_time = time.time()
encrypt_time = end_encrypt_time - start_encrypt_time

start_decrypt_time = time.time()
mensaje_descifrado = decrypt_message(ciphertext, iv, clave_secreta)
end_decrypt_time = time.time()
decrypt_time = end_decrypt_time - start_decrypt_time

cpu_usage = psutil.cpu_percent()
memoria = psutil.virtual_memory()
memoria_utilizada_mb = memoria.used / (1024 * 1024)

print("Mensaje cifrado:", ciphertext)
print("Mensaje descifrado:", mensaje_descifrado)
print("Tiempo de encriptación:", encrypt_time, "segundos")
print("Tiempo de desencriptación:", decrypt_time, "segundos")
print("Uso de CPU:", cpu_usage, "%")
print("Uso de memoria:", memoria_utilizada_mb, "MB")