import unittest
from steganography.core import xor_encrypt, xor_decrypt, to_binary_string, from_binary_string
from steganography.encryption import aes_encrypt, aes_decrypt

class TestXOR(unittest.TestCase):
    def test_xor_encrypt_decrypt(self):
        msg = "hello world"
        key = "abc123"
        binary = xor_encrypt(msg, key)
        success, result = xor_decrypt(binary, key)
        self.assertTrue(success)
        self.assertEqual(result, msg)

    def test_xor_wrong_key(self):
        msg = "secret"
        key = "key1"
        wrong_key = "key2"
        binary = xor_encrypt(msg, key)
        success, result = xor_decrypt(binary, wrong_key)
        self.assertFalse(success)

class TestAES(unittest.TestCase):
    def test_aes_encrypt_decrypt(self):
        msg = "hello secure world"
        password = "mystrongpassword"
        token = aes_encrypt(msg, password)
        result = aes_decrypt(token, password)
        self.assertEqual(result, msg)

    def test_aes_wrong_password(self):
        msg = "secure data"
        token = aes_encrypt(msg, "pass123")
        with self.assertRaises(Exception):
            aes_decrypt(token, "wrongpass")

class TestBinaryUtils(unittest.TestCase):
    def test_binary_conversion(self):
        msg = "testing123"
        binary = to_binary_string(msg)
        decoded = from_binary_string(binary)
        self.assertEqual(decoded[:len(msg)], msg)

if __name__ == "__main__":
    unittest.main()
