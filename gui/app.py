# gui/app.py

import os
import sys
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Import encryption functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from steganography.core import encrypt_image, decrypt_image

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

class SteganographyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🖼️ Image Steganography")
        self.geometry("700x640")
        self.resizable(False, False)

        self.selected_image_path = None

        # ---------- Title ----------
        ctk.CTkLabel(self, text="🔐 Welcome to Steganography Tool",
                     font=("Arial Rounded MT Bold", 24), text_color="#00FFAB").pack(pady=20)

        # ---------- Main Frame ----------
        self.main_frame = ctk.CTkFrame(self, corner_radius=15)
        self.main_frame.pack(padx=30, pady=10, fill="both", expand=True)

        # Image selection
        ctk.CTkLabel(self.main_frame, text="Select an image", font=("Arial", 16)).pack(pady=(20, 5))
        ctk.CTkButton(self.main_frame, text="📁 Browse Image", command=self.select_image).pack(pady=5)

        # Message entry
        self.message_entry = ctk.CTkEntry(self.main_frame, placeholder_text="💬 Enter your secret message", width=500)
        self.message_entry.pack(pady=10)

        # Key entry
        self.key_entry = ctk.CTkEntry(self.main_frame, placeholder_text="🔑 Enter encryption key", width=500, show="*")
        self.key_entry.pack(pady=10)

        # Method selection
        self.method = ctk.StringVar(value="aes")
        ctk.CTkLabel(self.main_frame, text="Select encryption method:").pack(pady=(10, 0))
        ctk.CTkRadioButton(self.main_frame, text="🔒 AES", variable=self.method, value="aes").pack()
        ctk.CTkRadioButton(self.main_frame, text="⚙️ XOR", variable=self.method, value="xor").pack()

        # Action buttons
        ctk.CTkButton(self.main_frame, text="🔐 Encrypt & Save Image", fg_color="#00A9FF",
                      hover_color="#0084C6", command=self.encrypt).pack(pady=15)

        ctk.CTkButton(self.main_frame, text="🔍 Decrypt Message", fg_color="#FF6F61",
                      hover_color="#D64F42", command=self.decrypt).pack()

        # Status label
        self.status_label = ctk.CTkLabel(self.main_frame, text="", wraplength=550,
                                         font=("Arial", 14), justify="center")
        self.status_label.pack(pady=15)

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png *.jpg *.jpeg")])
        if file_path:
            self.selected_image_path = file_path
            self.status_label.configure(text=f"📌 Selected: {os.path.basename(file_path)}", text_color="lightblue")

    def encrypt(self):
        if not self.selected_image_path:
            messagebox.showwarning("No Image", "Please select an image first.")
            return

        message = self.message_entry.get()
        key = self.key_entry.get()
        method = self.method.get()

        if not message or not key:
            messagebox.showwarning("Input Missing", "Message and key are required.")
            return

        try:
            output_path = encrypt_image(self.selected_image_path, message, key, method)
            self.status_label.configure(text=f"[✅] Image saved at:\n{output_path}", text_color="green")

        except Exception as e:
            self.status_label.configure(text=f"[❌] Encryption failed: {str(e)}", text_color="red")

    def decrypt(self):
        if not self.selected_image_path:
            messagebox.showwarning("No Image", "Please select an image first.")
            return

        key = self.key_entry.get()
        method = self.method.get()

        if not key:
            messagebox.showwarning("Input Missing", "Key is required to decrypt.")
            return

        try:
            success, message = decrypt_image(self.selected_image_path, key, method)
            if success:
                self.status_label.configure(text=f"[✅] Message Decrypted:\n{message}", text_color="lightgreen")
            else:
                self.status_label.configure(text=f"[❌] Decryption failed:\n{message}", text_color="orange")
        except Exception as e:
            self.status_label.configure(text=f"[❌] Error: {str(e)}", text_color="red")


if __name__ == "__main__":
    app = SteganographyApp()
    app.mainloop()
