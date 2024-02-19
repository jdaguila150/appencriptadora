import os
from encript import encript_message
from decrypt import decrypt_message
import time
import psutil

def generate_random_key():
    return os.urandom(32)

while True:
    print("\nMenú:")
    print("1. Encriptar y desencriptar al mismo tiempo")
    print("2. Solo encriptar")
    print("3. Solo desencriptar")
    opcion = input("Ingrese el número de la opción que desea ejecutar (1, 2 o 3): ")

    if opcion == "1":
        mensaje = input("Ingrese el mensaje que desea encriptar y desencriptar: ")

        start_time = time.time()

        clave_secreta = generate_random_key()
        start_encrypt_time = time.time()
        ciphertext, iv = encript_message(mensaje, clave_secreta)
        end_encrypt_time = time.time()
        encrypt_time = end_encrypt_time - start_encrypt_time

        start_decrypt_time = time.time()
        mensaje_descifrado = decrypt_message(ciphertext, iv, clave_secreta)
        end_decrypt_time = time.time()
        decrypt_time = end_decrypt_time - start_decrypt_time

        print("Mensaje cifrado:", ciphertext)
        print("Mensaje descifrado:", mensaje_descifrado)
        print("Tiempo de encriptación:", encrypt_time, "segundos")
        print("Tiempo de desencriptación:", decrypt_time, "segundos")

        break

    elif opcion == "2":
        mensaje = input("Ingrese el mensaje que desea cifrar: ")
        
        clave_secreta_bytes = generate_random_key()
        clave_secreta_hex = clave_secreta_bytes.hex()  
        
        print("Se ha generado una nueva clave secreta aleatoria", clave_secreta_hex)
        
        start_time = time.time()

        start_encrypt_time = time.time()
        ciphertext, iv = encript_message(mensaje, clave_secreta_bytes)
        ciphertext = ciphertext.hex()
        iv = iv.hex()
        end_encrypt_time = time.time()
        encrypt_time = end_encrypt_time - start_encrypt_time
        print("Mensaje cifrado:", ciphertext)
        print("Esta es tu Iv:", iv)
        print("Esta es tu clave secreta:", clave_secreta_hex)
        print("Tiempo de encriptación:", encrypt_time, "segundos")

        break

    elif opcion == "3":
        ciphertext = input("Ingrese el mensaje que desea descifrar: ")
        iv = input("Ingrese su IV: ")
        clave_secreta_texto_plano = input("Ingrese la clave secreta: ")

        try:
            start_decrypt_time = time.time()
            iv_bytes = bytes.fromhex(iv)
            clave_secreta_bytes = bytes.fromhex(clave_secreta_texto_plano)
            ciphertext = bytes.fromhex(ciphertext)
            mensaje_descifrado = decrypt_message(ciphertext, iv_bytes, clave_secreta_bytes)
            end_decrypt_time = time.time()
            decrypt_time = end_decrypt_time - start_decrypt_time
            print("Mensaje descifrado:", mensaje_descifrado)
            print("Tiempo de encriptación:", decrypt_time, "segundos")
        except ValueError:
            print("Error: El IV y la clave secreta deben estar en formato hexadecimal.")

        break

    else:
        print("Opción inválida. Por favor, ingrese 1, 2 o 3.")

# Monitoreo de recursos
cpu_usage = psutil.cpu_percent()
memoria = psutil.virtual_memory()
memoria_utilizada_mb = memoria.used / (1024 * 1024)

print("Uso de CPU:", cpu_usage, "%")
print("Uso de memoria:", memoria_utilizada_mb, "MB")
