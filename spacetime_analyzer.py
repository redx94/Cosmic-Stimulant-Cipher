import numpy as np
from scipy import signal
from scipy.fft import fft2, ifft2

class SpacetimeAnalyzer:
    def __init__(self):
        self.dimensions = 4  # 3 space + 1 time
        self.metrics = {}
        
    def create_spacetime_metric(self, sequence):
        """Create a spacetime metric from the sequence"""
        length = len(sequence)
        size = int(np.ceil(length ** (1/3)))  # Cube root for 3D space
        
        # Reshape into 4D spacetime grid
        grid = np.zeros((size, size, size, size))
        for i in range(min(length, size**3)):
            x, y, z = i % size, (i//size) % size, i//(size**2)
            t = int(abs(sequence[i]) * (size-1))
            grid[t, x, y, z] = sequence[i]
            
        return grid
        
    def detect_gravitational_waves(self, metric):
        """Detect wave-like patterns in spacetime metric"""
        # Calculate 4D FFT
        freq_domain = fft2(metric)
        
        # Find peak frequencies
        peaks = np.sort(np.abs(freq_domain.flatten()))[-10:]
        
        # Calculate wave characteristics
        wavelengths = 1 / (peaks + 1e-10)
        amplitudes = np.abs(peaks)
        
        return wavelengths, amplitudes
        
    def calculate_curvature(self, metric):
        """Calculate spacetime curvature"""
        gradients = np.gradient(metric)
        return np.mean([np.linalg.norm(g) for g in gradients])
        
    def find_symmetries(self, metric):
        """Find symmetries in spacetime structure"""
        symmetries = {
            'time_reversal': np.allclose(metric, metric[::-1]),
            'spatial_rotation': np.allclose(metric, np.rot90(metric)),
            'scale_invariance': self._check_scale_invariance(metric)
        }
        return symmetries
        
    def _check_scale_invariance(self, metric, scales=[2, 4]):
        """Check if pattern remains similar at different scales"""
        original_spectrum = np.abs(fft2(metric))
        for scale in scales:
            scaled = signal.resize(metric, tuple(s//scale for s in metric.shape))
            scaled_spectrum = np.abs(fft2(scaled))
            if not np.allclose(original_spectrum[:scaled_spectrum.shape[0]], 
                             scaled_spectrum, rtol=0.1):
                return False
        return True
        
    def analyze_sequence(self, sequence):
        """Perform complete spacetime analysis"""
        metric = self.create_spacetime_metric(sequence)
        wavelengths, amplitudes = self.detect_gravitational_waves(metric)
        curvature = self.calculate_curvature(metric)
        symmetries = self.find_symmetries(metric)
        
        self.metrics = {
            'wavelengths': wavelengths,
            'amplitudes': amplitudes,
            'curvature': curvature,
            'symmetries': symmetries,
            'complexity': self._calculate_complexity(wavelengths, curvature)
        }
        return self.metrics
        
    def _calculate_complexity(self, wavelengths, curvature):
        """Calculate overall spacetime complexity"""
        wave_complexity = np.std(wavelengths)
        curvature_factor = np.tanh(curvature)  # Normalize to [0,1]
        return (wave_complexity + curvature_factor) / 2
