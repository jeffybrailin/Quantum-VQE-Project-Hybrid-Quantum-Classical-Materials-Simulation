from qiskit_nature.second_q.drivers import PySCFDriver

def build_h2():
    """
    Builds the H2 molecule using PySCF and returns the problem instance.
    """
    driver = PySCFDriver(
        atom="H 0 0 0; H 0 0 0.735",
        basis="sto3g"
    )

    problem = driver.run()
    return problem
