from qiskit.circuit.library import TwoLocal

def create_ansatz(num_qubits):
    """
    Create a parameterized quantum circuit using TwoLocal ansatz.
    """
    ansatz = TwoLocal(
        num_qubits=num_qubits,
        rotation_blocks="ry",
        entanglement_blocks="cx",
        reps=2
    )

    return ansatz
