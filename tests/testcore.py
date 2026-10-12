
import unittest
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image
from cryptography.fernet import InvalidToken

from steganography.core import (
    encrypt_image,
    decrypt_image,
    to_binary_string,
    from_binary_string,
)
from steganography.encryption import aes_encrypt, aes_decrypt


class TestImageSteganography(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.image_path = Path(self.temp_dir.name) / "test_image.png"

        # Create a temporary image for testing.
        image = Image.fromarray(
            np.full((100, 100, 3), 128, dtype=np.uint8)
        )
        image.save(self.image_path)

    # Successful encryption and decryption tests

    def test_xor_mode_encrypt_decrypt(self):
        message = "hello world"

        output_path = encrypt_image(
            self.image_path, message, "abc123", method="xor"
        )

        self.assertTrue(Path(output_path).exists())

        success, result = decrypt_image(
            output_path, "abc123", method="xor"
        )

        self.assertTrue(success)
        self.assertEqual(result, message)

    def test_aes_encrypt_decrypt(self):
        message = "hello secure world"
        password = "mystrongpassword"

        token = aes_encrypt(message, password)
        result = aes_decrypt(token, password)

        self.assertEqual(result, message)

    def test_aes_wrong_password(self):
        token = aes_encrypt("secure data", "pass123")

        with self.assertRaises(InvalidToken):
            aes_decrypt(token, "wrongpass")

    # Binary conversion tests

    def test_binary_conversion(self):
        message = "testing123"

        binary = to_binary_string(message)

        self.assertEqual(len(binary), len(message) * 8)
        self.assertEqual(from_binary_string(binary), message)

    # Image-handling edge cases

    def test_empty_message(self):
        output_path = encrypt_image(
            self.image_path, "", "key", method="xor"
        )

        success, result = decrypt_image(
            output_path, "key", method="xor"
        )

        self.assertTrue(success)
        self.assertEqual(result, "")

    def test_message_too_large(self):
        large_message = "A" * 5000

        with self.assertRaises(ValueError):
            encrypt_image(
                self.image_path, large_message, "key", method="xor"
            )

    def test_invalid_image_path(self):
        missing_path = Path(self.temp_dir.name) / "missing.png"

        with self.assertRaises((FileNotFoundError, OSError)):
            encrypt_image(
                missing_path, "hello", "key", method="xor"
            )

    def test_corrupted_image(self):
        corrupted_path = Path(self.temp_dir.name) / "corrupted.png"
        corrupted_path.write_bytes(b"This is not a valid image")

        with self.assertRaises((OSError, ValueError)):
            encrypt_image(
                corrupted_path, "hello", "key", method="xor"
            )

    def test_invalid_image_content_with_png_extension(self):
        invalid_path = Path(self.temp_dir.name) / "invalid.png"
        invalid_path.write_text("not a real PNG image")

        with self.assertRaises((OSError, ValueError)):
            encrypt_image(
                invalid_path, "hello", "key", method="xor"
            )


if __name__ == "__main__":
    unittest.main()
