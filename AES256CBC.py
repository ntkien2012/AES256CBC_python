import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.padding import PKCS7

class AES256CBC:
    _block_size = 16
    _backend = default_backend()

    @staticmethod
    def encrypt(txt, password):
        """
        Encrypt plaintext with AES-256-CBC.
        Prepends a random IV to the ciphertext.
        """
        iv = os.urandom(AES256CBC._block_size)
        cipher = Cipher(algorithms.AES(password.encode()), modes.CBC(iv), backend=AES256CBC._backend)
        encryptor = cipher.encryptor()

        padder = PKCS7(AES256CBC._block_size * 8).padder()
        padded_txt = padder.update(txt.encode()) + padder.finalize()

        encrypted = encryptor.update(padded_txt) + encryptor.finalize()
        return base64.b64encode(iv + encrypted).decode()

    @staticmethod
    def decrypt(encrypted_txt, password):
        """
        Decrypt AES-256-CBC ciphertext.
        Expects the IV to be prepended to the ciphertext.
        """
        try:
            encrypted_data = base64.b64decode(encrypted_txt)
            iv = encrypted_data[:AES256CBC._block_size]
            ciphertext = encrypted_data[AES256CBC._block_size:]

            cipher = Cipher(algorithms.AES(password.encode()), modes.CBC(iv), backend=AES256CBC._backend)
            decryptor = cipher.decryptor()

            decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = PKCS7(AES256CBC._block_size * 8).unpadder()
            decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

            return decrypted.decode()

        except Exception as e:
            print(f"Decryption failed: {e}")
            return None

    @staticmethod
    def generate_password():
        """
        Generate a 32-character password for AES-256.
        """
        return base64.b64encode(os.urandom(24)).decode()[:32]

# Example usage
if __name__ == "__main__":
    password = AES256CBC.generate_password()
    print(f"Generated Password: {password}")

    txt = "Hello, World!"
    print(f"Original Text: {txt}")

    encrypted = AES256CBC.encrypt(txt, password)
    print(f"Encrypted Text: {encrypted}")

    decrypted = AES256CBC.decrypt(encrypted, password)
    print(f"Decrypted Text: {decrypted}")

    assert decrypted == txt, "Decryption failed!"
