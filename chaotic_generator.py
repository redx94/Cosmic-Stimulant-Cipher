import numpy as np
import hashlib
from typing import Tuple, Optional, List, Union
try:
    from numba import jit
    NUMBA_AVAILABLE = True
except ImportError:
    NUMBA_AVAILABLE = False

def check_sequence_quality(sequence: np.ndarray) -> bool:
    """Perform basic statistical checks on sequence."""
    if len(sequence) < 1000:
        return False
    
    # Check distribution
    hist, _ = np.histogram(sequence, bins=10)
    hist_std = np.std(hist)
    if hist_std > np.mean(hist) * 0.5:  # Allow 50% variation
        return False
    
    # Check autocorrelation
    auto_corr = np.correlate(sequence, sequence, mode='full')
    peak = auto_corr[len(sequence)]
    if np.any(auto_corr[len(sequence)+1:] > peak * 0.7):  # Max 70% correlation
        return False
    
    return True

if NUMBA_AVAILABLE:
    @jit(nopython=True)
    def _henon_iterate(x0: float, y0: float, a: float, b: float, length: int) -> np.ndarray:
        """Optimized Hénon map iteration."""
        sequence = np.zeros(length)
        x, y = x0, y0
        for i in range(length):
            x_next = 1 - a * x**2 + y
            y_next = b * x
            x, y = x_next, y_next
            sequence[i] = x
        return sequence

def generate_stellar_sequence(
    seed: int,
    length: int = 10000,
    a: float = 1.4,
    b: float = 0.3,
    quality_check: bool = False
) -> np.ndarray:
    """Generate chaotic sequence using Hénon map."""
    if not (1.07 <= a <= 1.4 and 0.2 <= b <= 0.3):
        raise ValueError("Parameters outside chaotic range")
    
    # Generate initial conditions from seed
    seed_hash = hashlib.sha256(seed.to_bytes((seed.bit_length() + 7) // 8, 'big')).digest()
    x0 = int.from_bytes(seed_hash[:16], 'big') / (2**128) * 2 - 1
    y0 = int.from_bytes(seed_hash[16:], 'big') / (2**128) * 2 - 1
    
    # Generate sequence
    x, y = x0, y0
    sequence = np.zeros(length)
    
    for i in range(length):
        x_next = 1 - a * x**2 + y
        y_next = b * x
        x, y = x_next, y_next
        sequence[i] = x
    
    if quality_check and not check_sequence_quality(sequence):
        raise ValueError("Generated sequence failed quality checks")
    
    return sequence
