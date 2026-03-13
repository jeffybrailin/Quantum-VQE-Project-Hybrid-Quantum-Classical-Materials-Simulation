# Quantum VQE Project — Hybrid Quantum-Classical Materials Simulation

## 1. Introduction
This project builds a hybrid quantum-classical pipeline using the Variational Quantum Eigensolver (VQE) to compute the ground-state energy of small molecules. It demonstrates quantum chemistry simulation, noise-aware quantum computing, and scalable candidate screening.

## 2. Quantum Chemistry Theory
The project maps molecular structures (like H2, LiH) into Fermionic Hamiltonians, which are then mapped to Qubit Hamiltonians using the Jordan-Wigner transformation (via `qiskit-nature`).

## 3. VQE Algorithm Explanation
VQE is a hybrid optimization algorithm. A parameterized quantum circuit (ansatz) prepares a trial state. A classical optimizer (e.g., COBYLA) updates the parameters to minimize the expectation value of the Qubit Hamiltonian.

## 4. Installation
Install the project dependencies using pip:
```bash
pip install -r requirements.txt
```

## 5. Running Experiments
To run the benchmark H2 simulation:
```bash
python src/experiments/run_h2_benchmark.py
```
Expected ground state energy output is approximately -1.137 Hartree.

## 6. Results and Analysis
* Implementation uses a parameterized `TwoLocal` ansatz.
* Baseline tests perform noiseless simulations using Qiskit `Estimator` primitives.

## 7. Future Work
* Integration with real quantum hardware.
* Implementation of quantum error mitigation strategies using `qiskit-aer`.
* ML surrogate model for fast prediction of molecular properties using `scikit-learn`.
