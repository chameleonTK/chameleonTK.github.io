import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def get_key(secret):
    return hashlib.sha256(secret.encode()).digest()

def encrypt(key, raw_text):
    iv = get_random_bytes(16)
    secret = get_key(key)
    print(secret)
    cipher = AES.new(secret, AES.MODE_CBC, iv)
    
    # Pad data (PKCS7) and Encrypt
    padded_data = pad(raw_text.encode('utf-8'), AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_data)

    combined_bytes = iv + encrypted_bytes
    # Return as Base64 string
    return base64.b64encode(combined_bytes).decode('utf-8')

def decrypt(key, enc_text):
    # Decode Base64
    combined_bytes = base64.b64decode(enc_text)
    iv = combined_bytes[:16]
    encrypted_bytes = combined_bytes[16:]
    
    # Create Cipher
    secret = get_key(key)
    cipher = AES.new(secret, AES.MODE_CBC, iv)
    
    # 3. Decrypt and Unpad
    decrypted_padded = cipher.decrypt(encrypted_bytes)
    decrypted_data = unpad(decrypted_padded, AES.block_size)
    
    return decrypted_data.decode('utf-8')