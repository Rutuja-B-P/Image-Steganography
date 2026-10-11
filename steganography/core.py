# steganography/core.py

from PIL import Image
import numpy as np
from pathlib import Path
from .encryption import aes_encrypt, aes_decrypt

END_TAG = "$$END$$"

# Always save output here
SAVE_DIR = Path(__file__).resolve().parent.parent / "hided_imgs"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

def to_binary_string(message: str) -> str:
    return "".join(f"{ord(c):08b}" for c in message)

def from_binary_string(bits: str) -> str:
    return "".join(chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8))

def encrypt_image(image_path, message, key, method="xor"):
    img = Image.open(image_path)
    if img.mode not in ["RGB", "RGBA"]:
        img = img.convert("RGB")
    pixels = np.array(img, dtype=np.uint8)

    # Encrypt message
    if method == "aes":
        encrypted_message = aes_encrypt(message, key) + END_TAG
    else:
        encrypted_message = message + END_TAG

    binary_message = to_binary_string(encrypted_message)

    if len(binary_message) > pixels.size:
        raise ValueError("Message too large for image.")

    flat_pixels = pixels.flatten().astype(np.int16)
    for i in range(len(binary_message)):
        flat_pixels[i] = (flat_pixels[i] & ~1) | int(binary_message[i])

    modified_pixels = np.clip(flat_pixels, 0, 255).astype(np.uint8)
    modified_pixels = modified_pixels.reshape(pixels.shape)

    # Save image inside hided_imgs folder with same name as original
    output_path = SAVE_DIR / (Path(image_path).stem + "_encrypted.png")
    Image.fromarray(modified_pixels).save(output_path, format="PNG")

    return output_path  # 🔁 Changed return value (was: Image object)

def decrypt_image(image_path, key, method="xor"):
    img = Image.open(image_path)
    pixels = np.array(img, dtype=np.uint8)

    binary_message = "".join(str(pixel & 1) for pixel in pixels.flatten())

    raw_text = from_binary_string(binary_message)
    if END_TAG not in raw_text:
        return False, "No message found."

    extracted = raw_text.split(END_TAG)[0]

    try:
        if method == "aes":
            decrypted = aes_decrypt(extracted, key)
        else:
            decrypted = extracted
        return True, decrypted
    except Exception as e:
        return False, f"Decryption failed: {str(e)}"
