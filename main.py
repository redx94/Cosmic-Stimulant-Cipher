from cosmic_cipher import (generate_cosmic_seed, encrypt_authenticated,
                         decrypt_authenticated)

def main():
    try:
        # Generate key using quantum randomness
        key, quantum_used = generate_cosmic_seed(bytes=32)
        print(f"Using {'quantum' if quantum_used else 'PRNG'} randomness")
        print(f"Generated key (hex): {key:064x}")
        
        # Test message with Unicode
        message = "Hello, Cosmic Cipher! 🌌✨"
        print(f"\nOriginal message: {message}")
        
        # Encrypt with authentication
        encrypted = encrypt_authenticated(message, key)
        print("\nEncrypted data:")
        print(f"Ciphertext: {encrypted['ciphertext'][:64]}...")
        print(f"MAC: {encrypted['mac']}")
        print(f"IV: {encrypted['iv']}")
        
        # Decrypt and verify
        decrypted = decrypt_authenticated(encrypted, key)
        print(f"\nDecrypted message: {decrypted}")
        print(f"Decryption successful: {message == decrypted}")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
