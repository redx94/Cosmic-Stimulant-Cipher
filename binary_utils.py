def text_to_binary(text):
    """Convert text to binary string using UTF-8 encoding."""
    return ''.join(format(byte, '08b') for byte in text.encode('utf-8'))

def binary_to_text(binary):
    """Convert binary string back to text using UTF-8 decoding."""
    byte_list = [int(binary[i:i+8], 2) for i in range(0, len(binary), 8)]
    return bytes(byte_list).decode('utf-8', errors='replace')
