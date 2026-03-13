from qiskit.quantum_info import SparsePauliOp

def build_h2():
    """
    Builds the H2 molecule using PySCF and returns the problem instance.
    If PySCF is unavailable (e.g. on Windows), it returns a hardcoded 
    equivalent Qubit Hamiltonian for the H2 STO-3G basis.
    """
    try:
        from qiskit_nature.second_q.drivers import PySCFDriver
        driver = PySCFDriver(
            atom="H 0 0 0; H 0 0 0.735",
            basis="sto3g"
        )
        problem = driver.run()
        return problem, None
    except ImportError:
        # Fallback to pre-computed H2 SparsePauliOp if PySCF fails to install
        qubit_op = SparsePauliOp.from_list([
            ("IIII", -0.8105479805373266),
            ("ZIII", 0.17218393261915552),
            ("IZII", 0.12054611241228686),
            ("IIZI", 0.17218393261915552),
            ("IIIZ", 0.12054611241228686),
            ("ZZII", 0.16892753870087912),
            ("ZIZI", 0.16614543256082414),
            ("ZIIZ", 0.16614543256082414),
            ("IZZI", 0.16614543256082414),
            ("IZIZ", 0.1746434305417434),
            ("IIZZ", 0.16892753870087912),
            ("XXYY", 0.045232799946057854),
            ("YYYY", 0.045232799946057854),
            ("XXXX", 0.045232799946057854),
            ("YYXX", 0.045232799946057854)
        ])
        return None, qubit_op
