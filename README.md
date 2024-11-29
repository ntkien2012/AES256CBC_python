# AES-256-CBC Encryption and Decryption in Python

This Python script provides a simple implementation of AES-256-CBC encryption and decryption using the `cryptography` library. It includes methods for encrypting and decrypting plaintext, as well as generating a secure password for encryption.

## Features
- AES-256 encryption in CBC mode.
- Secure padding using PKCS7.
- Automatic IV (Initialization Vector) generation and prepending.
- Base64 encoding for easy storage and transmission of encrypted data.
- Password generation for 256-bit encryption.

---

## Requirements
Make sure you have Python installed and the following libraries:
- `cryptography`

Install the required library using pip:
```bash
pip install cryptography
```

---

## Usage

### Class: `AES256CBC`
This class provides static methods to encrypt and decrypt text, as well as generate a secure password for encryption.

### Methods

#### `encrypt(txt, password)`
Encrypts plaintext using AES-256-CBC. The IV is generated randomly and prepended to the ciphertext.

- **Parameters**:
  - `txt` (str): The plaintext to encrypt.
  - `password` (str): A 32-character password for encryption.

- **Returns**:
  - `str`: The Base64-encoded encrypted text.

#### `decrypt(encrypted_txt, password)`
Decrypts AES-256-CBC ciphertext. The IV is extracted from the encrypted text.

- **Parameters**:
  - `encrypted_txt` (str): The Base64-encoded encrypted text.
  - `password` (str): The password used for decryption.

- **Returns**:
  - `str`: The decrypted plaintext, or `None` if decryption fails.

#### `generate_password()`
Generates a 32-character random password suitable for AES-256 encryption.

- **Returns**:
  - `str`: A 32-character password.

---

## Example

```python
from aes256cbc import AES256CBC  # Import the AES256CBC class

# Generate a password
password = AES256CBC.generate_password()
print(f"Generated Password: {password}")

# Original plaintext
txt = "Hello, World!"
print(f"Original Text: {txt}")

# Encrypt the plaintext
encrypted = AES256CBC.encrypt(txt, password)
print(f"Encrypted Text: {encrypted}")

# Decrypt the ciphertext
decrypted = AES256CBC.decrypt(encrypted, password)
print(f"Decrypted Text: {decrypted}")

# Assert that decryption matches the original plaintext
assert decrypted == txt, "Decryption failed!"
```

---

## How It Works
1. **Encryption**:
   - A random IV is generated.
   - The plaintext is padded using PKCS7 to match the block size of 16 bytes.
   - The plaintext is encrypted with AES-256-CBC using the provided password and IV.
   - The IV is prepended to the ciphertext, and the result is Base64-encoded.

2. **Decryption**:
   - The Base64-encoded string is decoded.
   - The IV is extracted from the first 16 bytes.
   - The ciphertext is decrypted using the password and extracted IV.
   - The decrypted text is unpadded and returned as plaintext.

3. **Password Generation**:
   - A 32-character password is generated from a 24-byte random sequence encoded in Base64.

---

## Notes
- Ensure the password used for encryption and decryption is the same.
- The generated password is 256 bits (32 characters) for AES-256.
- The IV is randomly generated for each encryption, ensuring secure and unique ciphertext for identical plaintext.
