import os
from Crypto.PublicKey import RSA

KEY_DIR = "keys"
if not os.path.exists(KEY_DIR):
    os.makedirs(KEY_DIR)

key = RSA.generate(2048)

private_key = key.export_key()
with open(os.path.join(KEY_DIR, "sender_private.pem"), "wb") as priv_file:
    priv_file.write(private_key)

public_key = key.publickey().export_key()
with open(os.path.join(KEY_DIR, "sender_public.pem"), "wb") as pub_file:
    pub_file.write(public_key)

print("The keys has been generated!")
