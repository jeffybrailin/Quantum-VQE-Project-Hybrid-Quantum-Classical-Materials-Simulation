from qiskit.algorithms.minimum_eigensolvers import VQE
from qiskit.algorithms.optimizers import COBYLA
from qiskit.primitives import Estimator

def run_vqe(qubit_operator, ansatz):
    """
    Run VQE to find the minimum eigenvalue of the qubit operator.
    """
    optimizer = COBYLA(maxiter=200)
    estimator = Estimator()

    vqe = VQE(
        estimator=estimator,
        ansatz=ansatz,
        optimizer=optimizer
    )

    result = vqe.compute_minimum_eigenvalue(qubit_operator)
    return result
