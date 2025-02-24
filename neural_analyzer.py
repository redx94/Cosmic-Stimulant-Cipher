import numpy as np
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
import threading

class NeuralAnalyzer:
    def __init__(self):
        self.model = self._create_model()
        self.scaler = MinMaxScaler()
        self.analysis_thread = None
        
    def _create_model(self):
        """Create a neural network for sequence analysis"""
        model = keras.Sequential([
            keras.layers.Dense(128, input_shape=(100,), activation='relu'),
            keras.layers.Dropout(0.2),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(32, activation='relu'),
            keras.layers.Dense(3, activation='softmax')  # [randomness, pattern_strength, predictability]
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy')
        return model
        
    def prepare_sequence(self, sequence):
        """Prepare sequence for neural analysis"""
        # Extract features: windows of 100 points
        windows = np.lib.stride_tricks.sliding_window_view(sequence, 100)
        return self.scaler.fit_transform(windows)
        
    def analyze_async(self, sequence, callback):
        """Perform neural analysis asynchronously"""
        def analysis_task():
            try:
                data = self.prepare_sequence(sequence)
                predictions = self.model.predict(data)
                
                results = {
                    'randomness_score': float(np.mean(predictions[:, 0])),
                    'pattern_score': float(np.mean(predictions[:, 1])),
                    'predictability': float(np.mean(predictions[:, 2])),
                    'recommendation': self._get_recommendation(predictions)
                }
                
                if callback:
                    callback(results)
                    
            except Exception as e:
                if callback:
                    callback({'error': str(e)})
                    
        self.analysis_thread = threading.Thread(target=analysis_task)
        self.analysis_thread.start()
        
    def _get_recommendation(self, predictions):
        """Generate recommendations based on neural analysis"""
        avg_pred = np.mean(predictions, axis=0)
        if avg_pred[0] > 0.7:  # High randomness
            return "Excellent cryptographic properties detected"
        elif avg_pred[1] > 0.5:  # Strong patterns
            return "Warning: Detectable patterns present"
        else:
            return "Acceptable cryptographic strength"
