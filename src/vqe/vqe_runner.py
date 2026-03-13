from qiskit_algorithms.minimum_eigensolvers import VQE
from qiskit_algorithms.optimizers import COBYLA
from qiskit.primitives import StatevectorEstimator

def run_vqe(qubit_operator, ansatz):
    """
    Run VQE to find the minimum eigenvalue of the qubit operator.
    """
    optimizer = COBYLA(maxiter=200)
    estimator = StatevectorEstimator()

    vqe = VQE(
        estimator=estimator,
        ansatz=ansatz,
        optimizer=optimizer
    )

    result = vqe.compute_minimum_eigenvalue(qubit_operator)
    return result
