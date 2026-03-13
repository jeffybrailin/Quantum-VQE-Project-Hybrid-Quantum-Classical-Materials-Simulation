import sys
import os

# Add the 'src' directory to the path so we can import our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from chemistry.molecule_builder import build_h2
from chemistry.hamiltonian import get_qubit_operator
from vqe.ansatz import create_ansatz
from vqe.vqe_runner import run_vqe

def main():
    print("Building H2 molecule...")
    problem, qubit_op = build_h2()

    if problem is not None:
        print("Mapping to Qubit Hamiltonian...")
        qubit_op = get_qubit_operator(problem)
    else:
        print("Using fallback pre-mapped Qubit Hamiltonian.")
    
    # Qiskit Nature operators have num_spin_orbitals, and map to a specific number of qubits
    num_qubits = qubit_op.num_qubits
    print(f"Number of qubits: {num_qubits}")

    print("Creating Ansatz...")
    ansatz = create_ansatz(num_qubits)

    print("Running VQE...")
    result = run_vqe(qubit_op, ansatz)

    print(f"Ground state energy: {result.eigenvalue}")

if __name__ == "__main__":
    main()
