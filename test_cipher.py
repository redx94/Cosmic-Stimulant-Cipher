import unittest
from cosmic_cipher import generate_cosmic_seed, chaotic_to_keystream, encrypt, decrypt, encrypt_authenticated, decrypt_authenticated
from chaotic_generator import generate_stellar_sequence, check_sequence_quality

class TestCosmicCipher(unittest.TestCase):
    def test_quantum_seed_generation(self):
        seed, quantum_used = generate_cosmic_seed(bytes=16)
        self.assertIsInstance(seed, int)
        self.assertGreaterEqual(seed.bit_length(), 120)  # Allow for leading zeros
        
    def test_encryption_decryption(self):
        test_cases = [
            "Hello, World! 🌎",
            "特殊文字テスト",
            "🌌✨🚀",
            "A" * 1000  # Test long messages
        ]
        
        seed, _ = generate_cosmic_seed()
        seq = generate_stellar_sequence(seed, length=10000)
        keystream = chaotic_to_keystream(seq)
        
        for text in test_cases:
            with self.subTest(text=text):
                ciphertext = encrypt(text, keystream)
                decrypted = decrypt(ciphertext, keystream)
                self.assertEqual(text, decrypted)
    
    def test_security_checks(self):
        with self.assertRaises(ValueError):
            generate_cosmic_seed(bytes=8)  # Too few bytes
        
        with self.assertRaises(ValueError):
            chaotic_to_keystream([], bits_per_value=33)  # Invalid bits
            
        with self.assertRaises(ValueError):
            encrypt("", "1010")  # Empty plaintext
            
        with self.assertRaises(ValueError):
            decrypt("1234", "1010")  # Invalid binary

    def test_authenticated_encryption(self):
        """Test HMAC authentication and IV support."""
        key, _, iv = generate_cosmic_seed()
        message = "Secret message 🔒"
        
        encrypted = encrypt_authenticated(message, key, iv)
        self.assertIn('mac', encrypted)
        self.assertIn('iv', encrypted)
        
        decrypted = decrypt_authenticated(encrypted, key)
        self.assertEqual(message, decrypted)
        
        # Test tampering detection
        encrypted['ciphertext'] = encrypted['ciphertext'][:-1] + '1'
        with self.assertRaises(ValueError):
            decrypt_authenticated(encrypted, key)
    
    def test_sequence_quality(self):
        """Test chaotic sequence quality checks."""
        seed, _ = generate_cosmic_seed()[:2]
        sequence = generate_stellar_sequence(seed, quality_check=True)
        
        # Verify sequence properties
        self.assertTrue(check_sequence_quality(sequence))

if __name__ == '__main__':
    unittest.main()
