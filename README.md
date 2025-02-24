# Cosmic Stimulant Cipher

A cryptographic system inspired by cosmic phenomena, combining quantum randomness and chaotic dynamics.

## Features

- Quantum random seed generation with PRNG fallback
- Chaotic sequence generation using the Hénon map
- UTF-8 support for text encryption
- XOR-based encryption with keystream

## Security Features

- 128-bit minimum quantum random seeds
- Cryptographic hashing of seeds for uniform distribution
- Parameter validation to ensure chaotic behavior
- Input validation for all operations
- Unicode support with UTF-8 encoding

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run tests:
```bash
python test_cipher.py
```

## Testing

Run the comprehensive test suite:
```bash
python -m unittest test_cipher.py -v
```

Test coverage includes:
- Quantum seed generation
- Encryption/decryption of various text types
- Edge cases and error conditions
- Long message handling
- Unicode character support

## Usage

```python
from cosmic_cipher import generate_cosmic_seed, chaotic_to_keystream, encrypt, decrypt
from chaotic_generator import generate_stellar_sequence

# Generate seed and keystream
seed = generate_cosmic_seed()
sequence = generate_stellar_sequence(seed)
keystream = chaotic_to_keystream(sequence)

# Encrypt message
message = "Hello, Cosmic Cipher! 🌌"
ciphertext = encrypt(message, keystream)

# Decrypt message
decrypted = decrypt(ciphertext, keystream)
```

## Security Notice

This is a prototype implementation and should not be used for production without thorough security analysis and enhancements.
