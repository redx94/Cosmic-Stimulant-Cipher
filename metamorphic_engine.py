import numpy as np
from scipy.optimize import minimize
import hashlib

class MetamorphicEngine:
    def __init__(self):
        self.evolution_history = []
        self.fitness_threshold = 0.85
        self.generation = 0
        
    def evolve_parameters(self, sequence, metrics):
        """Evolve cipher parameters based on performance metrics"""
        current_fitness = self._calculate_fitness(metrics)
        self.evolution_history.append(current_fitness)
        
        if current_fitness < self.fitness_threshold:
            new_params = self._optimize_parameters(sequence, metrics)
            self.generation += 1
            return new_params
        return None
        
    def _calculate_fitness(self, metrics):
        """Calculate fitness score from metrics"""
        weights = {
            'complexity': 0.4,
            'curvature': 0.3,
            'wave_strength': 0.3
        }
        
        scores = {
            'complexity': metrics['complexity'],
            'curvature': np.tanh(metrics['curvature']),
            'wave_strength': np.mean(metrics['amplitudes'])
        }
        
        return sum(weights[k] * scores[k] for k in weights)
        
    def _optimize_parameters(self, sequence, metrics):
        """Optimize cipher parameters using gradient descent"""
        def objective(params):
            a, b = params
            return -self._simulate_sequence_quality(sequence, a, b)
            
        result = minimize(
            objective,
            x0=[1.4, 0.3],  # Initial Hénon map parameters
            bounds=[(1.0, 1.8), (0.1, 0.5)],
            method='Nelder-Mead'
        )
        
        return {
            'a': result.x[0],
            'b': result.x[1],
            'generation': self.generation,
            'fitness': -result.fun
        }
        
    def _simulate_sequence_quality(self, sequence, a, b):
        """Simulate sequence quality with new parameters"""
        # Calculate sequence properties
        entropy = self._calculate_entropy(sequence)
        lyapunov = self._estimate_lyapunov(sequence, a, b)
        
        # Combine metrics
        quality = (entropy * 0.6 + lyapunov * 0.4)
        return quality
        
    def _calculate_entropy(self, sequence):
        """Calculate Shannon entropy of sequence"""
        hist, _ = np.histogram(sequence, bins=50, density=True)
        hist = hist[hist > 0]
        return -np.sum(hist * np.log2(hist))
        
    def _estimate_lyapunov(self, sequence, a, b):
        """Estimate Lyapunov exponent"""
        diffs = np.diff(sequence)
        return np.mean(np.log(np.abs(2 * a * sequence[:-1])))
        
    def get_evolution_summary(self):
        """Get summary of evolution progress"""
        if not self.evolution_history:
            return "No evolution history available"
            
        return {
            'generations': self.generation,
            'fitness_trend': self.evolution_history,
            'current_fitness': self.evolution_history[-1],
            'improvement': (self.evolution_history[-1] / self.evolution_history[0] - 1) * 100
        }
