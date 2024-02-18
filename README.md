# appencriptadora


# Scripts de Encriptación y Desencriptación

Este repositorio contiene tres scripts Python relacionados con el cifrado y descifrado de mensajes utilizando el algoritmo AES (Advanced Encryption Standard).

## Funcionalidades

- `main.py`: Script principal que permite al usuario ingresar un mensaje, lo encripta utilizando una clave aleatoria generada y luego lo desencripta para verificar su funcionalidad.

- `encript.py`: Contiene la función `encript_message`, que toma un mensaje y una clave como entrada, lo encripta utilizando AES y devuelve el texto cifrado y el IV (Initialization Vector).

- `decrypt.py`: Contiene la función `decrypt_message`, que toma el texto cifrado, el IV y la clave como entrada, y devuelve el mensaje original desencriptado.

## Ejecución

Para ejecutar el script principal `index.py`, simplemente ejecuta el siguiente comando en tu terminal:

```
python iain.py
```

Esto solicitará al usuario que ingrese un mensaje. El mensaje será encriptado y luego desencriptado utilizando las funciones definidas en `encript.py` y `decrypt.py`.

## Dependencias

Este proyecto depende de la biblioteca `cryptography`, que puede instalarse utilizando pip:

```
pip install cryptography
```

## Uso

1. Ejecuta el script principal `main.py`.
2. Ingresa el mensaje que deseas encriptar cuando se te solicite.
3. El mensaje será encriptado y luego desencriptado automáticamente.
4. Se mostrará el mensaje original y el mensaje desencriptado para verificar la funcionalidad.

