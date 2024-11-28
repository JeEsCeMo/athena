import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


def adjust_key(key_base64: str) -> bytes:

    key_bytes = base64.b64decode(key_base64)
    if len(key_bytes) < 16:
        return key_bytes.ljust(16, b'\0')  # Rellenar con ceros hasta 16 bytes
    elif len(key_bytes) > 32:
        return key_bytes[:32]  # Truncar si excede los 32 bytes
    return key_bytes  # Devuelve la clave original si es válida


def encrypt_payment_data(data: dict, key_base64: str) -> str:
    # Ajustar la clave
    key = adjust_key(key_base64)

    # Convertir datos a bytes
    plaintext = str(data).encode('utf-8')

    # Generar un vector de inicialización (IV) aleatorio
    iv = get_random_bytes(16)

    # Crear el cifrador AES
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Cifrar los datos (con padding)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))

    # Empaquetar IV y texto cifrado, codificado en Base64
    return base64.b64encode(iv + ciphertext).decode('utf-8')


def decrypt_payment_data(encrypted_data: str, key_base64: str) -> dict:
    # Ajustar la clave
    key = adjust_key(key_base64)

    # Decodificar datos cifrados de Base64
    decoded_data = base64.b64decode(encrypted_data)

    # Extraer IV y texto cifrado
    iv = decoded_data[:16]
    ciphertext = decoded_data[16:]

    # Crear el descifrador AES
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Descifrar y eliminar padding
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    # Convertir de bytes a diccionario
    return eval(plaintext.decode('utf-8'))
