# appencriptadora


# Scripts de Encriptación y Desencriptación

Este repositorio contiene tres scripts Python relacionados con el cifrado y descifrado de mensajes utilizando el algoritmo AES (Advanced Encryption Standard).

## Funcionalidades

- `main.py`: Script principal que permite al usuario ingresar un mensaje, lo encripta utilizando una clave aleatoria generada y luego lo desencripta para verificar su funcionalidad.

- `encript.py`: Contiene la función `encript_message`, que toma un mensaje y una clave como entrada, lo encripta utilizando AES y devuelve el texto cifrado y el IV (Initialization Vector).

- `decrypt.py`: Contiene la función `decrypt_message`, que toma el texto cifrado, el IV y la clave como entrada, y devuelve el mensaje original desencriptado.

## Ejecución

Para ejecutar el script principal `main.py`, simplemente ejecuta el siguiente comando en tu terminal:

```
python iain.py
```
- Opción 1:
Esto solicitará al usuario que ingrese un mensaje. El mensaje será encriptado y luego desencriptado utilizando las funciones definidas en `encript.py` y `decrypt.py`.
- Opción 2:
Esto solicitará al usuario que ingrese un mensaje el cual será encriptado y mostrado en un formato hexadecimal para posteriormente poder ser procesado mas sencillamente en el desencriptado.
- Opción 3:
Esto solicitará al usuario el mensaje cifrado, su IV y su cave secreta, de esta manera se podrá desencriptar el mensaje.
- Sin embargo, tambien es posible ejecutar el código desde el siguiente link

https://replit.com/join/gbmsapogwg-aguilaortegajos

## Dependencias

Este proyecto depende de la biblioteca `cryptography` para manejar las peticiones de encriptación, que puede instalarse utilizando pip:

```
pip install cryptography
```

Ademas del uso de la biblioteca `psutil` para obtener la información relacionada con el uso de los recursos de equipo, puede instalarse utilizando pip:

```
pip install psutil
```

## Uso

1. Ejecuta el script principal `main.py`.
2. Selecciona la opción 1,2 o 3
3. Ingresa los datos que solicite la consola
4. Se encriptara y desencriptará si se seleccionó la opción 1; se encriptará si se seleccionó la opción 2; se podrá desencriptar si es que se escoje la opción 3

