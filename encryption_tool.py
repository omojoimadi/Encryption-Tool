import customtkinter as ctk
from cryptography.fernet import Fernet
from tkinter import filedialog, messagebox
import os

# --- Core encryption/decryption logic ---
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Success", "Encryption key generated and saved as key.key")

def load_key():
    if not os.path.exists("key.key"):
        messagebox.showerror("Error", "No key file found! Generate a key first.")
        return None
    with open("key.key", "rb") as key_file:
        return key_file.read()

def encrypt_file():
    key = load_key()
    if key is None:
        return
    filepath = filedialog.askopenfilename(title="Select File to Encrypt")
    if not filepath:
        return

    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    encrypted_filename = filepath + ".encrypted"

    with open(encrypted_filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    os.remove(filepath)  # delete original file
    messagebox.showinfo("Success", f"File encrypted:\n{os.path.basename(encrypted_filename)}")

def decrypt_file():
    key = load_key()
    if key is None:
        return
    filepath = filedialog.askopenfilename(title="Select File to Decrypt", filetypes=[("Encrypted Files", "*.encrypted")])
    if not filepath:
        return

    fernet = Fernet(key)
    with open(filepath, "rb") as enc_file:
        encrypted = enc_file.read()

    try:
        decrypted = fernet.decrypt(encrypted)
    except Exception:
        messagebox.showerror("Error", "Invalid key or corrupted file!")
        return

    decrypted_filename = filepath.replace(".encrypted", "")

    with open(decrypted_filename, "wb") as dec_file:
        dec_file.write(decrypted)

    os.remove(filepath)  # delete encrypted file
    messagebox.showinfo("Success", f"File decrypted:\n{os.path.basename(decrypted_filename)}")


# --- GUI setup ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Encryption Tool")
app.geometry("400x300")

title_label = ctk.CTkLabel(app, text=" File Encryption Tool", font=("Helvetica", 20, "bold"))
title_label.pack(pady=20)

generate_key_button = ctk.CTkButton(app, text="Generate Key", command=generate_key)
generate_key_button.pack(pady=10)

encrypt_button = ctk.CTkButton(app, text="Encrypt File", command=encrypt_file)
encrypt_button.pack(pady=10)

decrypt_button = ctk.CTkButton(app, text="Decrypt File", command=decrypt_file)
decrypt_button.pack(pady=10)

exit_button = ctk.CTkButton(app, text="Exit", command=app.destroy)
exit_button.pack(pady=10)

app.mainloop()
