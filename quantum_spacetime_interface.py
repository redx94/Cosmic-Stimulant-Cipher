import numpy as np
from quantum_field_generator import QuantumFieldGenerator
from dark_entropy_collector import DarkEntropyCollector
from spacetime_analyzer import SpacetimeAnalyzer
from metamorphic_engine import MetamorphicEngine

class QuantumSpacetimeInterface:
    def __init__(self):
        self.field_generator = QuantumFieldGenerator()
        self.dark_collector = DarkEntropyCollector()
        self.spacetime_analyzer = SpacetimeAnalyzer()
        self.metamorphic_engine = MetamorphicEngine()
        self.evolution_enabled = True
        
    def enhance_cipher_sequence(self, sequence):
        """Apply quantum and spacetime enhancements to cipher sequence"""
        # Generate quantum fields
        quantum_potential = self.field_generator.generate_quantum_potential(sequence)
        
        # Collect dark entropy
        dark_enhanced = self.dark_collector.enhance_sequence(sequence)
        
        # Combine enhancements
        enhanced = sequence + 0.3 * quantum_potential + 0.2 * dark_enhanced
        enhanced = enhanced / np.max(np.abs(enhanced))
        
        return enhanced
        
    def analyze_and_evolve(self, sequence):
        """Analyze sequence and evolve parameters if needed"""
        # Perform spacetime analysis
        metrics = self.spacetime_analyzer.analyze_sequence(sequence)
        
        # Check quantum field properties
        fields = self.field_generator.create_entangled_fields(sequence)
        casimir = self.field_generator.calculate_casimir_effect(fields)
        
        # Add quantum metrics
        metrics.update({
            'quantum_correlation': np.mean(fields[2]),
            'casimir_strength': abs(casimir),
            'dark_flow': np.mean(self.dark_collector.calculate_dark_flow(sequence))
        })
        
        # Evolve parameters if enabled
        if self.evolution_enabled:
            new_params = self.metamorphic_engine.evolve_parameters(sequence, metrics)
            return metrics, new_params
        return metrics, None
        
    def get_security_assessment(self, metrics):
        """Assess overall security strength"""
        scores = {
            'quantum_strength': metrics['quantum_correlation'] * 100,
            'spacetime_complexity': metrics['complexity'] * 100,
            'dark_entropy': metrics['dark_flow'] * 100,
            'pattern_resistance': (1 - sum(metrics['symmetries'].values()) / 3) * 100
        }
        
        overall_score = np.mean(list(scores.values()))
        
        return {
            'scores': scores,
            'overall': overall_score,
            'recommendation': self._get_recommendation(overall_score)
        }
        
    def _get_recommendation(self, score):
        """Generate security recommendations"""
        if score < 70:
            return "Consider increasing quantum enhancement and re-evolution"
        elif score < 85:
            return "Security level acceptable, monitor for pattern emergence"
        else:
            return "Strong quantum-spacetime properties detected"
