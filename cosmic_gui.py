import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText
import pyperclip
import matplotlib.pyplot as plt
from cosmic_cipher import generate_cosmic_seed, generate_stellar_sequence, chaotic_to_keystream, encrypt, decrypt
from visualizer import CipherVisualizer
from quantum_enhancer import QuantumEnhancer
from visualizer_3d import Advanced3DVisualizer
from crypto_analyzer import CryptoAnalyzer
from neural_analyzer import NeuralAnalyzer
from key_stretcher import KeyStretcher
from quantum_spacetime_interface import QuantumSpacetimeInterface

class CosmicCipherUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cosmic Stimulant Cipher")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Create main sections
        self.create_menu()
        self.create_key_section()
        self.create_mode_section()
        self.create_io_section()
        self.create_status_bar()
        self.configure_grid()
        
        # Initialize state
        self.update_labels()
        self.current_sequence = None
        self.status_var.set("Ready")
        self.visualizer = CipherVisualizer()
        self.operation_history = []
        self.quantum_enhancer = QuantumEnhancer()
        self.visualizer_3d = Advanced3DVisualizer()
        self.crypto_analyzer = CryptoAnalyzer()
        self.neural_analyzer = NeuralAnalyzer()
        self.key_stretcher = KeyStretcher()
        self.quantum_spacetime = QuantumSpacetimeInterface()

    def create_menu(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        # File menu
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load Input", command=self.load_input)
        file_menu.add_command(label="Save Output", command=self.save_output)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Tools menu
        tools_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Tools", menu=tools_menu)
        tools_menu.add_command(label="Generate Quantum Key", command=self.generate_key)
        tools_menu.add_command(label="Visualize Attractor", command=self.visualize_attractor)
        tools_menu.add_command(label="Clear All", command=self.clear_all)
        
        # Add visualization submenu
        visual_menu = tk.Menu(tools_menu, tearoff=0)
        tools_menu.add_cascade(label="Visualizations", menu=visual_menu)
        visual_menu.add_command(label="Attractor Plot", command=self.show_attractor)
        visual_menu.add_command(label="Entropy Distribution", command=self.show_entropy)
        visual_menu.add_command(label="Operation History", command=self.show_history)

        # Add advanced analysis menu
        analysis_menu = tk.Menu(tools_menu, tearoff=0)
        tools_menu.add_cascade(label="Analysis", menu=analysis_menu)
        analysis_menu.add_command(label="3D Visualization", command=self.show_3d_visual)
        analysis_menu.add_command(label="Crypto Strength", command=self.analyze_crypto)
        analysis_menu.add_command(label="Quantum Enhancement", command=self.enhance_quantum)
        analysis_menu.add_command(label="Neural Analysis", command=self.show_neural_analysis)
        analysis_menu.add_command(label="Key Stretching", command=self.stretch_current_key)

        # Add quantum-spacetime menu
        quantum_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Quantum-Spacetime", menu=quantum_menu)
        quantum_menu.add_command(label="Enhance Sequence", command=self.enhance_sequence)
        quantum_menu.add_command(label="Security Assessment", command=self.show_security)
        quantum_menu.add_checkbutton(label="Auto-Evolution", 
                                   variable=tk.BooleanVar(value=True),
                                   command=self.toggle_evolution)

        # Help menu
        help_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)
        help_menu.add_command(label="Usage Guide", command=self.show_usage)

    def create_key_section(self):
        key_frame = ttk.LabelFrame(self.root, text="Key Management")
        key_frame.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
        
        ttk.Label(key_frame, text="Key (hex):").pack(side=tk.LEFT, padx=5)
        self.key_entry = ttk.Entry(key_frame, width=50)
        self.key_entry.pack(side=tk.LEFT, padx=5)
        
        ttk.Button(key_frame, text="Generate Key", command=self.generate_key).pack(side=tk.LEFT, padx=5)
        ttk.Button(key_frame, text="Copy Key", command=self.copy_key).pack(side=tk.LEFT, padx=5)

    def create_mode_section(self):
        self.mode_var = tk.StringVar(value="Encrypt")
        mode_frame = ttk.LabelFrame(self.root, text="Operation Mode")
        mode_frame.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky="ew")
        
        ttk.Radiobutton(mode_frame, text="Encrypt", variable=self.mode_var, 
                       value="Encrypt", command=self.update_labels).pack(side=tk.LEFT, padx=20)
        ttk.Radiobutton(mode_frame, text="Decrypt", variable=self.mode_var,
                       value="Decrypt", command=self.update_labels).pack(side=tk.LEFT, padx=20)

    def create_io_section(self):
        # Input section
        input_frame = ttk.LabelFrame(self.root, text="Input")
        input_frame.grid(row=2, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        self.input_text = ScrolledText(input_frame, height=10)
        self.input_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Process button
        ttk.Button(self.root, text="Process", command=self.process).grid(row=3, column=0, columnspan=4, pady=10)
        
        # Output section
        output_frame = ttk.LabelFrame(self.root, text="Output")
        output_frame.grid(row=4, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        self.output_text = ScrolledText(output_frame, height=10)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def create_status_bar(self):
        self.status_var = tk.StringVar(value="Ready")
        status = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status.grid(row=5, column=0, columnspan=4, sticky="ew")

    def configure_grid(self):
        self.root.grid_columnconfigure(0, weight=1)
        for i in [2, 4]:  # Rows with text areas
            self.root.grid_rowconfigure(i, weight=1)

    def process(self):
        """Enhanced process method with better error handling and validation"""
        try:
            key_hex = self.key_entry.get().strip()
            if not self.validate_key(key_hex):
                return
            
            input_data = self.input_text.get("1.0", tk.END).strip()
            if not input_data:
                messagebox.showwarning("Warning", "Please enter text to process")
                return
            
            # Generate or retrieve sequence
            if not self.current_sequence:
                seed = int(key_hex, 16)
                self.current_sequence, _ = generate_stellar_sequence(seed)
            
            keystream = chaotic_to_keystream(self.current_sequence)
            
            # Process based on mode
            mode = self.mode_var.get()
            result = encrypt(input_data, keystream) if mode == "Encrypt" else decrypt(input_data, keystream)
            
            # Update output
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert("1.0", result)
            self.status_var.set(f"{mode}ion successful")
            
            # Add to operation history
            self.operation_history.append({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'mode': mode,
                'success': True
            })
            
        except Exception as e:
            self.operation_history.append({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'mode': self.mode_var.get(),
                'success': False,
                'error': str(e)
            })
            messagebox.showerror("Error", f"Processing failed: {str(e)}")
            self.status_var.set("Error during processing")

    def validate_key(self, key_hex):
        """Validate the key format and length"""
        if not key_hex:
            messagebox.showerror("Error", "Please provide a key")
            return False
        try:
            if len(key_hex) != 32 or not all(c in '0123456789abcdefABCDEF' for c in key_hex):
                raise ValueError("Invalid key format")
            return True
        except ValueError:
            messagebox.showerror("Error", "Key must be 32 hexadecimal characters")
            return False

    def visualize_attractor(self):
        """Enhanced visualization with more options"""
        key_hex = self.key_entry.get().strip()
        if not self.validate_key(key_hex):
            return
            
        try:
            seed = int(key_hex, 16)
            x_seq, y_seq = generate_stellar_sequence(seed, length=10000)
            
            plt.figure(figsize=(8, 6))
            plt.plot(x_seq, y_seq, '.', markersize=1, color='blue', alpha=0.5)
            plt.title("Hénon Map Attractor Visualization")
            plt.xlabel("X Coordinate")
            plt.ylabel("Y Coordinate")
            plt.grid(True, linestyle='--', alpha=0.3)
            
            # Add interactive controls
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            messagebox.showerror("Visualization Error", str(e))

    def show_usage(self):
        """Show detailed usage instructions"""
        usage_text = """
How to use Cosmic Stimulant Cipher:

1. Key Management:
   - Generate a new key using the "Generate Quantum Key" button
   - Or enter a 32-character hexadecimal key manually
   - Use "Copy Key" to save the key for later use

2. Encryption/Decryption:
   - Choose mode (Encrypt/Decrypt)
   - Enter or load text to process
   - Click "Process" to perform the operation

3. Visualization:
   - Use "Visualize Attractor" to see the chaotic pattern
   - The pattern is unique to your current key

4. File Operations:
   - Load input from text files
   - Save output to text files
   - Copy/paste using clipboard
"""
        messagebox.showinfo("Usage Guide", usage_text)

    def clear_all(self):
        """Clear all fields and reset state"""
        self.key_entry.delete(0, tk.END)
        self.input_text.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        self.current_sequence = None
        self.status_var.set("All fields cleared")

    def show_attractor(self):
        """Show attractor visualization in a new window"""
        if not self.current_sequence:
            messagebox.showwarning("Warning", "Generate a key first")
            return
            
        top = tk.Toplevel(self.root)
        top.title("Attractor Visualization")
        self.visualizer.create_attractor_plot(self.current_sequence, self.current_sequence_y)
        plot_widget = self.visualizer.embed_in_widget(top)
        plot_widget.pack(fill=tk.BOTH, expand=True)

    def show_entropy(self):
        """Show entropy distribution in a new window"""
        if not self.current_sequence:
            messagebox.showwarning("Warning", "Generate a key first")
            return
            
        top = tk.Toplevel(self.root)
        top.title("Entropy Distribution")
        self.visualizer.create_entropy_plot(self.current_sequence)
        plot_widget = self.visualizer.embed_in_widget(top)
        plot_widget.pack(fill=tk.BOTH, expand=True)

    def show_history(self):
        """Display operation history"""
        history_text = "\n".join(
            f"{op['timestamp']} - {op['mode']}: {'Success' if op['success'] else 'Failed'}"
            for op in self.operation_history
        )
        messagebox.showinfo("Operation History", history_text or "No operations performed yet")

    def show_3d_visual(self):
        """Show 3D visualization window"""
        if not self.current_sequence:
            messagebox.showwarning("Warning", "Generate a key first")
            return
            
        top = tk.Toplevel(self.root)
        top.title("3D Phase Space Analysis")
        self.visualizer_3d.create_3d_phase_space(
            self.current_sequence,
            np.roll(self.current_sequence, 1)
        )
        plot_widget = self.visualizer_3d.embed_in_widget(top, animate=True)
        plot_widget.pack(fill=tk.BOTH, expand=True)

    def analyze_crypto(self):
        """Perform cryptographic analysis"""
        if not self.current_sequence:
            messagebox.showwarning("Warning", "Generate a key first")
            return
            
        def update_results(results):
            top = tk.Toplevel(self.root)
            top.title("Cryptographic Analysis")
            
            text = f"""
Entropy Score: {results['entropy']:.2f}
Pattern Uniqueness: {results['pattern_count']}
Overall Strength: {results['strength_score']:.2f}%

Recommendation: {results['recommendation']}
"""
            label = ttk.Label(top, text=text, padding=20)
            label.pack()
            
        self.crypto_analyzer.async_analyze(self.current_sequence, update_results)

    def enhance_quantum(self):
        """Apply quantum enhancement to current sequence"""
        if not self.current_sequence:
            messagebox.showwarning("Warning", "Generate a key first")
            return
            
        try:
            self.current_sequence = self.quantum_enhancer.enhance_sequence(self.current_sequence)
            self.status_var.set("Quantum enhancement applied successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Quantum enhancement failed: {str(e)}")

    def show_neural_analysis(self):
        """Show neural network analysis results"""
        if not self.current_sequence:
            messagebox.showwarning("Warning", "Generate a key first")
            return
            
        def update_analysis(results):
            if 'error' in results:
                messagebox.showerror("Analysis Error", results['error'])
                return
                
            top = tk.Toplevel(self.root)
            top.title("Neural Network Analysis")
            
            text = f"""
Neural Analysis Results:
----------------------
Randomness Score: {results['randomness_score']:.3f}
Pattern Strength: {results['pattern_score']:.3f}
Predictability: {results['predictability']:.3f}

Recommendation: {results['recommendation']}
"""
            label = ttk.Label(top, text=text, padding=20)
            label.pack()
            
        self.neural_analyzer.analyze_async(self.current_sequence, update_analysis)

    def stretch_current_key(self):
        """Apply key stretching to current key"""
        key_hex = self.key_entry.get().strip()
        if not self.validate_key(key_hex):
            return
            
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Key Stretching")
        progress_var = tk.DoubleVar()
        
        ttk.Label(progress_window, text="Stretching key...").pack(pady=10)
        progress_bar = ttk.Progressbar(progress_window, variable=progress_var, maximum=100)
        progress_bar.pack(pady=10, padx=20, fill=tk.X)
        
        def update_progress(value):
            progress_var.set(value)
            
        try:
            stretched_key = self.key_stretcher.stretch_key(key_hex, update_progress)
            self.key_entry.delete(0, tk.END)
            self.key_entry.insert(0, stretched_key)
            self.status_var.set("Key stretched successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Key stretching failed: {str(e)}")
        finally:
            progress_window.destroy()

    def enhance_sequence(self):
        """Apply quantum-spacetime enhancements"""
        if not self.current_sequence:
            messagebox.showwarning("Warning", "Generate a key first")
            return
            
        try:
            self.current_sequence = self.quantum_spacetime.enhance_cipher_sequence(
                self.current_sequence
            )
            self.status_var.set("Quantum-spacetime enhancement applied")
        except Exception as e:
            messagebox.showerror("Error", f"Enhancement failed: {str(e)}")
            
    def show_security(self):
        """Show security assessment"""
        if not self.current_sequence:
            messagebox.showwarning("Warning", "Generate a key first")
            return
            
        try:
            metrics, new_params = self.quantum_spacetime.analyze_and_evolve(
                self.current_sequence
            )
            assessment = self.quantum_spacetime.get_security_assessment(metrics)
            
            top = tk.Toplevel(self.root)
            top.title("Security Assessment")
            
            text = f"""
Quantum-Spacetime Security Assessment
-----------------------------------
Quantum Strength: {assessment['scores']['quantum_strength']:.2f}%
Spacetime Complexity: {assessment['scores']['spacetime_complexity']:.2f}%
Dark Entropy Level: {assessment['scores']['dark_entropy']:.2f}%
Pattern Resistance: {assessment['scores']['pattern_resistance']:.2f}%

Overall Security: {assessment['overall']:.2f}%

Recommendation: {assessment['recommendation']}
"""
            if new_params:
                text += f"\nParameters evolved (Generation {new_params['generation']})"
                
            label = ttk.Label(top, text=text, padding=20)
            label.pack()
            
        except Exception as e:
            messagebox.showerror("Error", f"Assessment failed: {str(e)}")
            
    def toggle_evolution(self):
        """Toggle automatic parameter evolution"""
        self.quantum_spacetime.evolution_enabled = not self.quantum_spacetime.evolution_enabled
        status = "enabled" if self.quantum_spacetime.evolution_enabled else "disabled"
        self.status_var.set(f"Automatic evolution {status}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CosmicCipherUI(root)
    root.mainloop()
