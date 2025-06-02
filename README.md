# Signature System

This project simulates a **digital signature verification system** for electronic documents (e.g., contracts or agreements). It is designed to model the signature and verification process based on the **PKCS#1 standard**, using **RSA (2048-bit)** and **SHA256**. This system demonstrates how digital signatures can be used to ensure document **authenticity** and **integrity**.

It includes two standalone GUI applications:

- **Signer:** Selects a document, signs it using a private RSA key, and saves the `.sig` signature file.
- **Verifier:** Selects a document and its signature file, then verifies the signature using the corresponding RSA public key.

---

## Protocol Overview

This project implements **PKCS#1 v1.5 digital signature and verification** using the RSA algorithm. The workflow is as follows:

1. The signer generates a SHA256 hash of the document.
2. The hash is signed using the RSA private key.
3. The signature is saved as a separate `.sig` file.
4. The verifier loads the document and `.sig` file, hashes the document, and compares it against the decrypted signature using the RSA public key.

This process allows users to verify that the document was signed by a trusted source and that its content has not been altered.

---

## Project Structure

```
signature_system/
├── generate_keys.py           # Generate RSA key pair (2048-bit)
├── signer.py                  # Sign documents and save .sig files
├── verifier.py                # Verify signatures against documents
├── keys/
│   ├── sender_private.pem     # RSA private key (used for signing)
│   └── sender_public.pem      # RSA public key (used for verification)
└── README.md
```

---

## How to Use

### 1. Generate RSA Keys (Run Once)
```bash
python generate_keys.py
```
- This will create `sender_private.pem` and `sender_public.pem` inside the `keys/` directory.

### 2. Sign a Document
```bash
python signer.py
```
- Choose a document (e.g., `.txt`, `.pdf`) from your system.
- Choose where to save the `.sig` file using a Save As dialog.
- The `.sig` file stores the digital signature.

### 3. Verify a Signed Document
```bash
python verifier.py
```
- Select the original document file.
- Select its corresponding `.sig` file.
- The application will show a popup indicating whether the signature is valid.

---

## Dependencies

- Python 3.x
- PyCryptodome
- tkinter (built-in for most Python installations)

Install dependencies with:
```bash
pip install pycryptodome
```

---

## Security Features

- **Digital Signature (PKCS#1 v1.5):** Ensures the authenticity and integrity of a document.
- **RSA-2048 Key Pair:** Provides a robust level of security for signing and verification.
- **SHA256 Hashing:** Creates a strong, collision-resistant fingerprint of the document.
- **Key Flexibility:** Users can upload `sender_private.pem` and `sender_public.pem` with their own RSA key pairs (PEM format).

---

## Notes

- The signature file (`.sig`) only allows for verification of the document’s integrity and origin.
- It does **not** contain or encrypt the original document content.
- This system does **not** support file encryption/decryption.

---

## Author

Zekai Yin (for academic coursework, PSB7031CE Cryptography Module)

---

This project was developed as part of a university assignment to demonstrate secure document signing and signature verification using Python, RSA, and SHA256 in compliance with PKCS#1.
