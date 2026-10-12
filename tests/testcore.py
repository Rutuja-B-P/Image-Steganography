
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

        # Create a simple image large enough to hold a short message.
        image = Image.fromarray(
            np.full((100, 100, 3), 128, dtype=np.uint8)
        )
        image.save(self.image_path)

    def test_xor_mode_encrypt_decrypt(self):
        message = "hello world"
        key = "abc123"

        output_path = encrypt_image(
            self.image_path, message, key, method="xor"
        )
        self.assertTrue(Path(output_path).exists())

        success, result = decrypt_image(
            output_path, key, method="xor"
        )
        self.assertTrue(success)
        self.assertEqual(result, message)

    def test_xor_mode_wrong_key(self):
        message = "secret"

        output_path = encrypt_image(
            self.image_path, message, "key1", method="xor"
        )

        # The current XOR-labelled mode does not actually use the key
        # to encrypt the message, so a different key still extracts it.
        success, result = decrypt_image(
            output_path, "key2", method="xor"
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

    def test_binary_conversion(self):
        message = "testing123"
        binary = to_binary_string(message)

        self.assertEqual(len(binary), len(message) * 8)
        self.assertEqual(from_binary_string(binary), message)

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


if __name__ == "__main__":
    unittest.main()
