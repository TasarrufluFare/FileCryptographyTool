from Crypto.Cipher import AES
import base64
from Crypto.Random import get_random_bytes
import os


def encrypter_method(given_file_path):
    file_name_origin_extension = given_file_path.split("/")[-1]
    file_name_origin = file_name_origin_extension.split(".")[0]
    file_extension = file_name_origin_extension.split(".")[1]
    with open(given_file_path, "rb") as file2string:
        converted_string = base64.b64encode(file2string.read())
    data = converted_string
    file2string.close()

    key = get_random_bytes(32)
    seperator = b'(-!tfei)'
    file_extension_bytes = bytes(file_extension, 'ANSI')
    os.mkdir(f"Encrypted {file_name_origin}")
    passkey = open(f"Encrypted {file_name_origin}/passkey.txt", 'wb')
    passkey.write(key)
    passkey.write(seperator)
    passkey.write(file_extension_bytes)
    passkey.close()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(f"Encrypted {file_name_origin}/{file_name_origin}.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()
