import hashlib
import hmac
import secrets
import quantumrandom as qr
import numpy as np
from typing import Tuple, Dict, Union
from quantum_field_generator import QuantumFieldGenerator
from dark_entropy_collector import DarkEntropyCollector

def generate_cosmic_seed(bytes: int = 16, fallback: bool = True) -> Tuple[int, bool]:
    """Generate quantum random seed with fallback to PRNG."""
    if bytes < 16:
        raise ValueError("Minimum 16 bytes required for security")
    
    quantum_used = True
    try:
        random_bytes = qr.random_bytes(bytes)
    except Exception:
        if not fallback:
            raise
        quantum_used = False
        random_bytes = secrets.token_bytes(bytes)
    
    dark_collector = DarkEntropyCollector()
    entropy = dark_collector.collect_dark_entropy(bytes * 8)
    seed = int(hashlib.sha3_256(entropy.tobytes()).hexdigest(), 16)
    return seed % (2**(8*bytes)), quantum_used

def text_to_binary(text: str) -> str:
    """Convert text to binary using UTF-8."""
    return ''.join(format(byte, '08b') for byte in text.encode('utf-8'))

def binary_to_text(binary: str) -> str:
    """Convert binary back to text using UTF-8."""
    if not all(bit in '01' for bit in binary):
        raise ValueError("Invalid binary string")
    byte_list = [int(binary[i:i+8], 2) for i in range(0, len(binary), 8)]
    return bytes(byte_list).decode('utf-8')

def chaotic_to_keystream(sequence: np.ndarray, bits_per_value: int = 8, use_quantum_field: bool = False) -> str:
    """Convert chaotic sequence to binary keystream."""
    if not 1 <= bits_per_value <= 32:
        raise ValueError("bits_per_value must be between 1 and 32")
    
    if use_quantum_field:
        qfg = QuantumFieldGenerator()
        sequence = qfg.generate_quantum_potential(sequence)
        fluctuations = qfg.generate_vacuum_fluctuations(len(sequence))
        sequence += fluctuations
        sequence = sequence / np.max(np.abs(sequence))
    
    keystream = []
    scale = 2**bits_per_value
    for val in sequence:
        fractional = abs(val - int(val))
        byte_val = int(fractional * scale)
        keystream.append(format(byte_val, f'0{bits_per_value}b'))
    return ''.join(keystream)

def encrypt(plaintext: str, keystream: str) -> str:
    """Encrypt plaintext using XOR with keystream."""
    if not plaintext:
        raise ValueError("Plaintext cannot be empty")
    
    binary = text_to_binary(plaintext)
    if len(keystream) < len(binary):
        raise ValueError("Keystream too short")
    
    return ''.join('1' if a != b else '0' 
                  for a, b in zip(binary, keystream[:len(binary)]))

def decrypt(ciphertext: str, keystream: str) -> str:
    """Decrypt ciphertext using XOR with keystream."""
    return binary_to_text(encrypt(ciphertext, keystream))

def encrypt_authenticated(message: str, key: int, iv: int = None) -> Dict[str, str]:
    """Encrypt with authentication."""
    if iv is None:
        iv = secrets.randbits(128)
    
    # Generate keystream from key and IV
    from chaotic_generator import generate_stellar_sequence
    sequence = generate_stellar_sequence(key ^ iv, length=len(message) * 8 // 6 + 100)
    keystream = chaotic_to_keystream(sequence)
    
    # Encrypt
    ciphertext = encrypt(message, keystream)
    
    # Create HMAC
    mac = hmac.new(key.to_bytes(32, 'big'), 
                   ciphertext.encode(), 
                   hashlib.sha256).hexdigest()
    
    return {
        'ciphertext': ciphertext,
        'mac': mac,
        'iv': hex(iv)[2:]  # Remove '0x' prefix
    }

def decrypt_authenticated(encrypted: Dict[str, str], key: int) -> str:
    """Decrypt with authentication verification."""
    # Verify HMAC
    expected_mac = hmac.new(key.to_bytes(32, 'big'),
                           encrypted['ciphertext'].encode(),
                           hashlib.sha256).hexdigest()
    
    if not hmac.compare_digest(expected_mac, encrypted['mac']):
        raise ValueError("Message authentication failed")
    
    # Generate keystream
    iv = int(encrypted['iv'], 16)
    from chaotic_generator import generate_stellar_sequence
    sequence = generate_stellar_sequence(key ^ iv)
    keystream = chaotic_to_keystream(sequence)
    
    # Decrypt
    return decrypt(encrypted['ciphertext'], keystream)
