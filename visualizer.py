import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CipherVisualizer:
    def __init__(self):
        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        
    def create_attractor_plot(self, x_seq, y_seq):
        """Create an interactive Hénon map attractor plot"""
        self.plot.clear()
        self.plot.plot(x_seq, y_seq, '.', markersize=1, color='blue', alpha=0.5)
        self.plot.set_title("Hénon Map Attractor")
        self.plot.set_xlabel("X Coordinate")
        self.plot.set_ylabel("Y Coordinate")
        self.plot.grid(True, linestyle='--', alpha=0.3)
        self.figure.tight_layout()
        
    def create_entropy_plot(self, sequence, bins=50):
        """Create entropy distribution visualization"""
        self.plot.clear()
        self.plot.hist(sequence, bins=bins, density=True, alpha=0.7)
        self.plot.set_title("Entropy Distribution")
        self.plot.set_xlabel("Value")
        self.plot.set_ylabel("Frequency")
        self.plot.grid(True, linestyle='--', alpha=0.3)
        self.figure.tight_layout()
        
    def embed_in_widget(self, parent_widget):
        """Embed the visualization in a tkinter widget"""
        canvas = FigureCanvasTkAgg(self.figure, master=parent_widget)
        canvas.draw()
        return canvas.get_tk_widget()
