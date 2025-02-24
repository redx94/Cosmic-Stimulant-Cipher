import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import matplotlib.pyplot as plt
from cosmic_cipher import *

class CosmicCipherUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Cosmic Cipher")
        
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        tools_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Tools", menu=tools_menu)
        
        self.text = tk.Text(self.root, wrap=tk.WORD)
        self.text.grid(row=0, column=0, columnspan=4)
        
        self.qfg = QuantumFieldGenerator()
        self.dark_collector = DarkEntropyCollector()
        
        # Add quantum feature toggles
        self.quantum_field_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.root, text="Use Quantum Field", 
                       variable=self.quantum_field_var).grid(row=1, column=4)
        
        self.dark_entropy_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.root, text="Use Dark Entropy",
                       variable=self.dark_entropy_var).grid(row=1, column=5)
        
        # Add visualization tools
        tools_menu = self.menu.children['tools']
        tools_menu.add_command(label="Show Quantum Fields", command=self.show_quantum_fields)
        tools_menu.add_command(label="Show Dark Entropy", command=self.show_dark_entropy)
        tools_menu.add_command(label="Show Casimir Effect", command=self.show_casimir_effect)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                content = file.read()
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text.get(1.0, tk.END)
                file.write(content)

    def process(self):
        seed = self.text.get(1.0, tk.END).strip()
        if not seed:
            messagebox.showwarning("Warning", "Please enter a seed value")
            return
        sequence_x, sequence_y = generate_stellar_sequence(
            seed, use_dark_entropy=self.dark_entropy_var.get())
        keystream = chaotic_to_keystream(
            sequence_x, use_quantum_field=self.quantum_field_var.get())
        self.current_sequence = keystream
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, keystream)

    def show_quantum_fields(self):
        if not hasattr(self, 'current_sequence'):
            messagebox.showwarning("Warning", "Generate a key first")
            return
        field1, field2, corr = self.qfg.create_entangled_fields(self.current_sequence)
        plt.figure(figsize=(10, 6))
        plt.plot(field1[:100], label='Field 1')
        plt.plot(field2[:100], label='Field 2')
        plt.title(f"Entangled Quantum Fields (Correlation: {corr:.3f})")
        plt.legend()
        plt.show()

    def show_dark_entropy(self):
        if not hasattr(self, 'current_sequence'):
            messagebox.showwarning("Warning", "Generate a key first")
            return
        entropy = self.dark_collector.collect_dark_entropy(1000)
        plt.figure(figsize=(10, 6))
        plt.plot(entropy)
        plt.title("Dark Energy Entropy Distribution")
        plt.show()

    def show_casimir_effect(self):
        if not hasattr(self, 'current_sequence'):
            messagebox.showwarning("Warning", "Generate a key first")
            return
        field1, field2, _ = self.qfg.create_entangled_fields(self.current_sequence)
        force = self.qfg.calculate_casimir_effect((field1, field2))
        plt.figure(figsize=(8, 4))
        plt.axhline(y=force, color='r', label=f'Casimir Force: {force:.2e}')
        plt.title("Casimir Effect Between Quantum Fields")
        plt.legend()
        plt.show()
