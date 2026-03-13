try:
    from qiskit_aer.noise import NoiseModel, depolarizing_error, pauli_error
except ImportError:
    NoiseModel = None

def get_noise_model(p_reset=0.01, p_meas=0.01, p_gate1=0.001, p_gate2=0.01):
    """
    Simulate noise: bit flip, phase flip, depolarizing noise using Qiskit Aer.
    """
    if NoiseModel is None:
        raise ImportError("qiskit_aer is not installed or available.")
        
    noise_model = NoiseModel()

    # Depolarizing errors
    error_1q = depolarizing_error(p_gate1, 1)
    error_2q = depolarizing_error(p_gate2, 2)
    
    # Pauli errors (bit flip / phase flip) - simplified representation
    bit_flip = pauli_error([('X', p_meas), ('I', 1 - p_meas)])
    phase_flip = pauli_error([('Z', p_reset), ('I', 1 - p_reset)])

    # Add errors to the noise model
    noise_model.add_all_qubit_quantum_error(error_1q, ['u1', 'u2', 'u3', 'rx', 'ry', 'rz'])
    noise_model.add_all_qubit_quantum_error(error_2q, ['cx'])
    
    return noise_model
