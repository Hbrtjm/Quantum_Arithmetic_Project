from qiskit import QuantumCircuit

# Template for now, I will implement this later

def qft(circuit: QuantumCircuit, num_qubits: int, inverse: bool = False,do_swaps: bool = True) -> QuantumCircuit:
    """
    Apply the Quantum Fourier Transform (QFT) on the first `num_qubits` qubits of `circuit`.

    Parameters
    ----------
    circuit : QuantumCircuit
        The host circuit to which QFT gates will be appended.
    num_qubits : int
        The number of qubits (starting from qubit 0) on which to perform the QFT.
    inverse : bool, optional
        If True, apply the inverse QFT instead of the forward transform.
        Default is False.
    do_swaps : bool, optional
        If True, include the final qubit-swap operations to reverse the order of qubits.
        Default is True.

    Returns
    -------
    QuantumCircuit
        The same `circuit` instance with QFT gates appended.
    """
    # 1. Apply Hadamard and controlled‑phase rotations (qft_rotations)
    # 2. Optionally apply swap_registers if do_swaps is True
    # 3. Reverse operations if inverse is True
    return circuit

