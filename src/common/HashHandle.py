import hashlib
import base64

# Hashing password
def hash_password(user_password):
    hashed_password = hashlib.md5()
    hashed_password.update(user_password.encode("utf-8"))
    return hashed_password.hexdigest()

# Encoding and decoding NIC and telephone numbers
def encode(encode_text):
    base64_bytes = base64.b64encode(encode_text.encode('ascii'))
    base64_message = base64_bytes.decode('ascii')
    return base64_message


def decode(decode_text):
    message_bytes = base64.b64decode(decode_text.encode('ascii'))
    message = message_bytes.decode('ascii')
    return message
