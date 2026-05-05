import tkinter as tk
from rsa import encrypt_message, decrypt_message, get_keys

e, d, n = get_keys()

def encrypt():
    try:
        message = int(entry.get())
        cipher = encrypt_message(message, e, n)
        encrypted_value.config(text=str(cipher))
    except:
        encrypted_value.config(text="Invalid input")

def decrypt():
    try:
        cipher = int(encrypted_value.cget("text"))
        message = decrypt_message(cipher, d, n)
        decrypted_value.config(text=str(message))
    except:
        decrypted_value.config(text="Error")

root = tk.Tk()
root.title("RSA Encryption GUI")
root.geometry("400x300")

tk.Label(root, text="Enter Message:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)
tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

tk.Label(root, text=f"Public Key: ({e}, {n})").pack(pady=5)
tk.Label(root, text=f"Private Key: ({d}, {n})").pack(pady=5)

tk.Label(root, text="Encrypted:").pack()
encrypted_value = tk.Label(root, text="")
encrypted_value.pack()

tk.Label(root, text="Decrypted:").pack()
decrypted_value = tk.Label(root, text="")
decrypted_value.pack()

root.mainloop()