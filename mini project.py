import tkinter as tk
from tkinter import messagebox
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64

class SecureDataHandler:
    def __init__(self):
        self.key = get_random_bytes(32)  # AES-256 key
        self.iv = get_random_bytes(16)   # Initialization Vector

    def encrypt_text(self, text):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        padded_text = text + (16 - len(text) % 16) * ' '  # Proper padding
        encrypted_data = cipher.encrypt(padded_text.encode())
        return base64.b64encode(self.iv + encrypted_data).decode()

    def decrypt_text(self, encrypted_text):
        raw_data = base64.b64decode(encrypted_text)
        iv, encrypted_data = raw_data[:16], raw_data[16:]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data).decode().rstrip()  # Ensure proper unpadding
        return decrypted_data

class DigitalSignature:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.private_key = self.key.export_key()
        self.public_key = self.key.publickey().export_key()

    def sign_text(self, text):
        private_key = RSA.import_key(self.private_key)
        hash_value = SHA256.new(text.encode())
        signature = pkcs1_15.new(private_key).sign(hash_value)
        return base64.b64encode(signature).decode()

    def verify_signature(self, text, signature):
        public_key = RSA.import_key(self.public_key)
        hash_value = SHA256.new(text.encode())
        try:
            pkcs1_15.new(public_key).verify(hash_value, base64.b64decode(signature))
            return "Signature Verified!"
        except ValueError:
            return "Signature Verification Failed!"

class SecureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Data Handling")
        self.root.geometry("500x600")
        
        self.data_handler = SecureDataHandler()
        self.signer = DigitalSignature()

        tk.Label(root, text="Enter Text:").pack()
        self.text_entry = tk.Text(root, height=5, width=50)
        self.text_entry.pack()

        tk.Button(root, text="Encrypt", command=self.encrypt_text).pack(pady=5)
        tk.Button(root, text="Decrypt", command=self.decrypt_text).pack(pady=5)
        tk.Button(root, text="Sign", command=self.sign_text).pack(pady=5)
        tk.Button(root, text="Verify Signature", command=self.verify_signature).pack(pady=5)
        
        tk.Label(root, text="Output:").pack()
        self.output_entry = tk.Text(root, height=5, width=50)
        self.output_entry.pack()
    
    def encrypt_text(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        encrypted_text = self.data_handler.encrypt_text(text)
        self.output_entry.delete("1.0", tk.END)
        self.output_entry.insert("1.0", encrypted_text)

    def decrypt_text(self):
        encrypted_text = self.text_entry.get("1.0", tk.END).strip()
        try:
            decrypted_text = self.data_handler.decrypt_text(encrypted_text)
            self.output_entry.delete("1.0", tk.END)
            self.output_entry.insert("1.0", decrypted_text)
        except Exception as e:
            messagebox.showerror("Error", "Decryption failed! Invalid input or incorrect key.")
    
    def sign_text(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        signature = self.signer.sign_text(text)
        self.output_entry.delete("1.0", tk.END)
        self.output_entry.insert("1.0", signature)
    
    def verify_signature(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        signature = self.output_entry.get("1.0", tk.END).strip()
        result = self.signer.verify_signature(text, signature)
        messagebox.showinfo("Verification Result", result)

root = tk.Tk()
app = SecureApp(root)
root.mainloop()
