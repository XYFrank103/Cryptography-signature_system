import os
import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

KEY_PATH = "keys/sender_private.pem"

def sign_document():
    if not os.path.exists(KEY_PATH):
        messagebox.showerror("Key Error", "Private key not found. Please upload keys first.")
        return

    file_path = filedialog.askopenfilename(title="Select document to sign")
    if not file_path:
        return

    try:
        with open(file_path, "rb") as f:
            data = f.read()
    except Exception as e:
        messagebox.showerror("Read Error", f"Failed to read the selected file.\n{str(e)}")
        return

    save_path = filedialog.asksaveasfilename(
        defaultextension=".sig",
        filetypes=[("Signature File", "*.sig")],
        title="Save signature as"
    )
    if not save_path:
        return

    try:
        private_key = RSA.import_key(open(KEY_PATH, "rb").read())
        hash_obj = SHA256.new(data)
        signature = pkcs1_15.new(private_key).sign(hash_obj)

        with open(save_path, "wb") as sig_file:
            sig_file.write(signature)

        messagebox.showinfo("Success", f"Signature created and saved to:\n{save_path}")

    except Exception as e:
        messagebox.showerror("Signing Error", f"An error occurred during signing.\n{str(e)}")

root = tk.Tk()
root.title("Signature System - Signer")
root.geometry("400x200")
root.resizable(False, False)

label = tk.Label(root, text="Click the button below to sign a document.", pady=20)
label.pack()

sign_button = tk.Button(root, text="Select File and Sign", command=sign_document, width=25, height=2)
sign_button.pack(pady=20)

root.mainloop()
