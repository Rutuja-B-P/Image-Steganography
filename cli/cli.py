# cli/cli.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import argparse
from pathlib import Path
from steganography.core import encrypt_image, decrypt_image

def main():
    parser = argparse.ArgumentParser(description="Image Steganography CLI Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Encrypt command
    enc = subparsers.add_parser("encrypt", help="Encrypt a message into an image")
    enc.add_argument("image", help="Path to input image")
    enc.add_argument("output", help="Path to output image (will be saved as PNG)")
    enc.add_argument("message", help="The message to hide")
    enc.add_argument("key", help="Encryption key (XOR or AES)")
    enc.add_argument("--method", choices=["xor", "aes"], default="xor", help="Encryption method (default: xor)")

    # Decrypt command
    dec = subparsers.add_parser("decrypt", help="Decrypt a message from an image")
    dec.add_argument("image", help="Path to encrypted image")
    dec.add_argument("key", help="Decryption key")
    dec.add_argument("--method", choices=["xor", "aes"], default="xor", help="Decryption method (default: xor)")

    args = parser.parse_args()

    if args.command == "encrypt":
        output_path = Path(args.output)
        try:
            img = encrypt_image(args.image, args.message, args.key, method=args.method)
            img.save(output_path, format="PNG")
            print(f"[✅] Encrypted image saved to {output_path}")
        except Exception as e:
            print(f"[❌] Encryption failed: {e}")

    elif args.command == "decrypt":
        try:
            success, message = decrypt_image(args.image, args.key, method=args.method)
            if success:
                print("[✅] Message Decrypted:")
                print(message)
            else:
                print(f"[❌] {message}")
        except Exception as e:
            print(f"[❌] Decryption failed: {e}")

if __name__ == "__main__":
    main()
