import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Operator, Statevector
from qiskit.extensions import UnitaryGate

class QuantumSimulator:
    def __init__(self, num_qubits=8):
        self.num_qubits = num_qubits
        self.qr = QuantumRegister(num_qubits)
        self.cr = ClassicalRegister(num_qubits)
        self.circuit = QuantumCircuit(self.qr, self.cr)
        
    def create_entangled_state(self):
        """Create maximally entangled state"""
        self.circuit.h(self.qr[0])
        for i in range(1, self.num_qubits):
            self.circuit.cx(self.qr[0], self.qr[i])
            
    def apply_quantum_oracle(self, key_bits):
        """Apply key-dependent quantum oracle"""
        oracle_matrix = self._create_oracle_matrix(key_bits)
        oracle_gate = UnitaryGate(oracle_matrix)
        self.circuit.append(oracle_gate, self.qr)
        
    def _create_oracle_matrix(self, key_bits):
        """Create quantum oracle based on key"""
        dim = 2 ** self.num_qubits
        matrix = np.eye(dim, dtype=complex)
        for i in range(dim):
            if bin(i).count('1') % 2 == int(key_bits[i % len(key_bits)]):
                matrix[i, i] = -1
        return matrix
        
    def simulate_decoherence(self, time_steps=100):
        """Simulate quantum decoherence"""
        state = Statevector.from_instruction(self.circuit)
        final_state = state.evolve(self._decoherence_channel(), time_steps)
        return np.array(final_state.data)
        
    def _decoherence_channel(self):
        """Create decoherence channel"""
        dim = 2 ** self.num_qubits
        channel = np.eye(dim, dtype=complex) * 0.9
        channel += np.random.normal(0, 0.1, (dim, dim))
        return Operator(channel)
