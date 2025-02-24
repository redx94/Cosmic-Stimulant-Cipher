# Cosmic Stimulant Cipher

A quantum-inspired encryption system that leverages principles from quantum field theory and cosmology to create a robust and future-proof cipher.

## Features

- **Quantum Field Generation**: Simulates vacuum fluctuations and quantum potentials
- **Dark Entropy Collection**: Utilizes cosmic expansion and dark matter effects
- **Advanced Visualization**: View attractors, quantum entropy, and Casimir effects
- **DNA-based Key Expansion**: Biological-inspired key strengthening
- **Quantum Simulation**: Entanglement and decoherence effects

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

## Enhanced GUI Usage

The application now includes a full-featured graphical interface:

1. Launch the GUI:
```bash
python cosmic_gui.py
```

2. Key Management:
   - Generate a quantum random key automatically
   - Input custom hexadecimal keys
   - Copy keys to clipboard

3. Features:
   - File import/export support
   - Visualization of chaotic attractor
   - Real-time status updates
   - Error handling and validation

4. Requirements:
   - Install additional dependencies:
```bash
pip install -r requirements.txt
```

## Enhanced GUI Features

The graphical interface now includes:

1. Advanced Key Management:
   - Quantum random key generation
   - Key validation and format checking
   - One-click key copying

2. Visualization Tools:
   - Interactive Hénon map attractor display
   - Real-time visualization updates
   - Chaotic pattern analysis

3. Improved User Experience:
   - Clear error messages and validation
   - Status updates for all operations
   - Comprehensive usage guide
   - File import/export capabilities

4. Security Features:
   - Key format validation
   - Secure key generation
   - Clear-all functionality for sensitive data

For detailed usage instructions, see the Help menu in the application.

## Security Notice

This is a prototype implementation and should not be used for production without thorough security analysis and enhancements.
