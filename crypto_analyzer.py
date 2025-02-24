import numpy as np
from scipy.stats import entropy
from collections import Counter
import threading

class CryptoAnalyzer:
    def __init__(self):
        self.analysis_thread = None
        self.results = {}
        
    def analyze_entropy(self, data):
        """Calculate Shannon entropy of the data"""
        counts = Counter(data)
        probabilities = np.array(list(counts.values())) / len(data)
        return entropy(probabilities, base=2)
    
    def analyze_patterns(self, data, window_size=4):
        """Analyze for repeated patterns"""
        patterns = {}
        for i in range(len(data) - window_size):
            pattern = data[i:i+window_size]
            patterns[pattern] = patterns.get(pattern, 0) + 1
        return patterns
    
    def calculate_strength_score(self, entropy_score, pattern_score):
        """Calculate overall cryptographic strength"""
        max_entropy = 8.0  # Maximum entropy for byte values
        pattern_penalty = sum(count > 1 for count in pattern_score.values()) / 100
        
        strength = (entropy_score / max_entropy) * 100
        strength -= pattern_penalty
        
        return np.clip(strength, 0, 100)
    
    def async_analyze(self, data, callback):
        """Perform analysis asynchronously"""
        def analysis_task():
            entropy_score = self.analyze_entropy(data)
            patterns = self.analyze_patterns(data)
            strength = self.calculate_strength_score(entropy_score, patterns)
            
            self.results = {
                'entropy': entropy_score,
                'pattern_count': len(patterns),
                'strength_score': strength,
                'recommendation': self.get_recommendation(strength)
            }
            
            if callback:
                callback(self.results)
                
        self.analysis_thread = threading.Thread(target=analysis_task)
        self.analysis_thread.start()
        
    def get_recommendation(self, strength):
        """Get security recommendations based on strength score"""
        if strength < 60:
            return "Warning: Cryptographic strength below recommended levels"
        elif strength < 80:
            return "Acceptable strength, consider increasing key length"
        else:
            return "Strong cryptographic properties detected"
