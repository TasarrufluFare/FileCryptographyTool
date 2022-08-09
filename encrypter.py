from Crypto.Cipher import AES
import base64
from Crypto.Random import get_random_bytes
import os


def encrypter_method(given_file_path):
    file_name_origin_extension = given_file_path.split("/")[-1]
    file_name_dot_split = file_name_origin_extension.split(".")

    #Getting File Name and Extension Seperated
    file_name_origin = ""

    for index in range(len(file_name_dot_split)-1):
        file_name_origin = file_name_origin + file_name_dot_split[index]

    #file_name_origin = file_name_origin_extension.split(".")[0] - This is v0.01's file name code line
    file_extension = file_name_dot_split[-1]
    #End Of Getting File Name and Extension Seperated Section

    with open(given_file_path, "rb") as file2string:
        converted_string = base64.b64encode(file2string.read())
    data = converted_string
    file2string.close()

    key = get_random_bytes(32)
    seperator = b'(-!tfei)'
    file_extension_bytes = bytes(file_extension, 'ANSI')

    path_to_create = f"Operations/{file_name_origin}/Encrypted {file_name_origin}"
    #if not os.path.exists(path_to_create):
    file_count = 0
    while os.path.exists(path_to_create):
        file_count = file_count + 1
        path_to_create = f"Operations/{file_name_origin}" + f" ({file_count})" + f"/Encrypted {file_name_origin}"

    os.makedirs(path_to_create)
    passkey = open(path_to_create+f"/passkey for {file_name_origin}.tf", 'wb')
    passkey.write(key)
    passkey.write(seperator)
    passkey.write(file_extension_bytes)
    passkey.close()
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    file_out = open(f"{path_to_create}/{file_name_origin}.bin", "wb")
    [file_out.write(x) for x in (cipher.nonce, tag, ciphertext)]
    file_out.close()
