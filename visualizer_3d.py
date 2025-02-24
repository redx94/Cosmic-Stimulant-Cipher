import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Advanced3DVisualizer:
    def __init__(self):
        self.figure = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.figure.add_subplot(111, projection='3d')
        self.canvas = None
        
    def create_3d_phase_space(self, x_seq, y_seq, z_seq=None):
        """Create 3D phase space visualization"""
        self.ax.clear()
        if z_seq is None:
            z_seq = np.diff(x_seq)  # Use derivative as third dimension
            
        self.ax.scatter(x_seq[:-1], y_seq[:-1], z_seq, 
                       c=z_seq, cmap='viridis', 
                       marker='.', s=1, alpha=0.6)
        
        self.ax.set_title("3D Phase Space Analysis")
        self.ax.set_xlabel("X Dimension")
        self.ax.set_ylabel("Y Dimension")
        self.ax.set_zlabel("Z Dimension")
        
    def animate_rotation(self, frame):
        """Animate the 3D plot rotation"""
        self.ax.view_init(elev=20, azim=frame)
        return self.ax,
    
    def embed_in_widget(self, parent_widget, animate=True):
        """Embed the 3D visualization in a tkinter widget"""
        if self.canvas is None:
            self.canvas = FigureCanvasTkAgg(self.figure, master=parent_widget)
            
        if animate:
            ani = animation.FuncAnimation(self.figure, self.animate_rotation,
                                        frames=np.arange(0, 360, 2),
                                        interval=50, blit=True)
        
        self.canvas.draw()
        return self.canvas.get_tk_widget()
