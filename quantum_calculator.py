#!/usr/bin/env python3
"""
Quantum Calculator - Basic quantum computing operations simulator
"""

import math
import random


class QubitState:
    """Represents a quantum bit state using probability amplitudes."""
    
    def __init__(self):
        """Initialize qubit to |0⟩ state."""
        self.alpha = complex(1.0, 0.0)  # Amplitude for |0⟩
        self.beta = complex(0.0, 0.0)   # Amplitude for |1⟩
    
    def normalize(self):
        """Ensure the state is normalized."""
        norm = math.sqrt(abs(self.alpha)**2 + abs(self.beta)**2)
        if norm > 0:
            self.alpha /= norm
            self.beta /= norm
    
    def get_probabilities(self):
        """Calculate measurement probabilities."""
        prob_0 = abs(self.alpha) ** 2
        prob_1 = abs(self.beta) ** 2
        return prob_0, prob_1
    
    def measure_state(self):
        """Simulate measurement and return result."""
        prob_0, prob_1 = self.get_probabilities()
        rand_val = random.random()
        
        if rand_val < prob_0:
            self.alpha = complex(1.0, 0.0)
            self.beta = complex(0.0, 0.0)
            return 0
        else:
            self.alpha = complex(0.0, 0.0)
            self.beta = complex(1.0, 0.0)
            return 1


class QuantumOperations:
    """Quantum gate operations for single qubits."""
    
    @staticmethod
    def apply_hadamard(qubit):
        """Apply Hadamard transformation to create superposition."""
        sqrt_half = 1.0 / math.sqrt(2)
        new_alpha = sqrt_half * (qubit.alpha + qubit.beta)
        new_beta = sqrt_half * (qubit.alpha - qubit.beta)
        qubit.alpha = new_alpha
        qubit.beta = new_beta
        qubit.normalize()
    
    @staticmethod
    def apply_not_gate(qubit):
        """Apply NOT gate (Pauli-X) - flip the qubit."""
        temp = qubit.alpha
        qubit.alpha = qubit.beta
        qubit.beta = temp
    
    @staticmethod
    def apply_phase_flip(qubit):
        """Apply Pauli-Z gate - phase flip."""
        qubit.beta = -qubit.beta
    
    @staticmethod
    def apply_rotation_x(qubit, angle):
        """Rotate around X-axis by given angle (radians)."""
        cos_half = math.cos(angle / 2)
        sin_half = math.sin(angle / 2)
        
        new_alpha = cos_half * qubit.alpha - complex(0, sin_half) * qubit.beta
        new_beta = cos_half * qubit.beta - complex(0, sin_half) * qubit.alpha
        
        qubit.alpha = new_alpha
        qubit.beta = new_beta
        qubit.normalize()


class QuantumCalc:
    """Main calculator interface for quantum operations."""
    
    def __init__(self):
        """Initialize the quantum calculator."""
        self.operations = QuantumOperations()
    
    def create_qubit(self):
        """Create a new qubit in |0⟩ state."""
        return QubitState()
    
    def superposition(self, qubit):
        """Create equal superposition state."""
        self.operations.apply_hadamard(qubit)
        return qubit
    
    def flip_qubit(self, qubit):
        """Flip qubit state."""
        self.operations.apply_not_gate(qubit)
        return qubit
    
    def measure(self, qubit):
        """Measure qubit and return classical result."""
        return qubit.measure_state()


def demonstrate_quantum_calc():
    """Run demonstration of quantum calculator features."""
    print("Quantum Calculator Demonstration")
    print("-" * 50)
    
    calc = QuantumCalc()
    
    # Create and measure a qubit
    q = calc.create_qubit()
    print(f"Initial probabilities: P(0)={q.get_probabilities()[0]:.3f}, P(1)={q.get_probabilities()[1]:.3f}")
    
    # Apply Hadamard gate
    calc.superposition(q)
    print(f"After Hadamard: P(0)={q.get_probabilities()[0]:.3f}, P(1)={q.get_probabilities()[1]:.3f}")
    
    # Measure
    result = calc.measure(q)
    print(f"Measurement outcome: |{result}⟩")


if __name__ == "__main__":
    demonstrate_quantum_calc()
