from qiskit_nature.second_q.mappers import JordanWignerMapper

def get_qubit_operator(problem):
    """
    Map the Fermionic Hamiltonian to a Qubit Hamiltonian using Jordan Wigner.
    """
    mapper = JordanWignerMapper()
    
    # Extract the second quantized operator from the problem
    second_q_op = problem.hamiltonian.second_q_op()
    
    # Map the second quantized spatial operator to qubits
    qubit_op = mapper.map(second_q_op)
    
    return qubit_op
