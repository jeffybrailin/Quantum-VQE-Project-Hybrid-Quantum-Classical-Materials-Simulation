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
    problem = build_h2()

    print("Mapping to Qubit Hamiltonian...")
    qubit_operator = get_qubit_operator(problem)
    
    # Qiskit Nature operators have num_spin_orbitals, and map to a specific number of qubits
    num_qubits = qubit_operator.num_qubits
    print(f"Number of qubits: {num_qubits}")

    print("Creating Ansatz...")
    ansatz = create_ansatz(num_qubits)

    print("Running VQE...")
    result = run_vqe(qubit_operator, ansatz)

    print(f"Ground state energy: {result.eigenvalue}")

if __name__ == "__main__":
    main()
