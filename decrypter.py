from Crypto.Cipher import AES
import base64
import os


def decrypter_method(given_file_path, given_pass_path):
    try:
        file_in = open(given_file_path, "rb")
        nonce, tag, ciphertext = [file_in.read(x) for x in (16, 16, -1)]

        pass_file = open(given_pass_path, "rb")
        given_key_and_extension = pass_file.read()
        pass_file.close()
        crypted_key_and_extension = given_key_and_extension.split(b"(-!tfei)")
        #Checkpoint1
        #print(crypted_key_and_extension)
        given_key = crypted_key_and_extension[0]
        file_extension_bytes = crypted_key_and_extension[1]
        #Checkpoint2
        #print(type(given_key))
        #print(type(file_extension_bytes))
        file_extension = str(file_extension_bytes, "UTF-8")
        cipher = AES.new(given_key, AES.MODE_EAX, nonce)
        data = cipher.decrypt_and_verify(ciphertext, tag)
        file_decrypted = open(given_file_path, 'w', encoding="UTF-8")
        file_decrypted.write(data.decode('UTF-8'))
        file_decrypted.close()

        file = open(given_file_path, 'rb')
        byte = file.read()
        file.close()

        file_name_origin = given_file_path.split("/")[-1].split(".")[0]
        os.mkdir(f"Decrypted {file_name_origin}")
        decodeit = open(f'Decrypted {file_name_origin}/Decrypted New File.{file_extension}', 'wb')
        decodeit.write(base64.b64decode(byte))
        decodeit.close()
        file_in.close()

    except():
        print("Something went wrong")
