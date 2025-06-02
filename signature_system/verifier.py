import os
import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

KEY_PATH = "keys/sender_public.pem"

def verify_signature():
    if not os.path.exists(KEY_PATH):
        messagebox.showerror("Key Error", "Public key not found. Please upload keys first.")
        return

    doc_path = filedialog.askopenfilename(title="Select original document")
    if not doc_path:
        return

    sig_path = filedialog.askopenfilename(title="Select signature file", filetypes=[("Signature File", "*.sig")])
    if not sig_path:
        return

    try:
        with open(doc_path, "rb") as f:
            document_data = f.read()

        with open(sig_path, "rb") as f:
            signature_data = f.read()

        public_key = RSA.import_key(open(KEY_PATH, "rb").read())

        hash_obj = SHA256.new(document_data)
        pkcs1_15.new(public_key).verify(hash_obj, signature_data)

        messagebox.showinfo("Verification Result", "Signature is valid. The document is authentic and unmodified.")

    except (ValueError, TypeError):
        messagebox.showerror("Verification Failed", "Signature is invalid. The document may have been altered or the signature is incorrect.")

    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred during verification.\n{str(e)}")

root = tk.Tk()
root.title("Signature System - Verifier")
root.geometry("420x230")
root.resizable(False, False)

label = tk.Label(root, text="Verify a document using its signature file.", pady=20)
label.pack()

verify_button = tk.Button(root, text="Select Files and Verify", command=verify_signature, width=28, height=2)
verify_button.pack(pady=20)

root.mainloop()
