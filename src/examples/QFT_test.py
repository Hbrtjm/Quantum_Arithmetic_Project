from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from QFT import qft  # wherever you defined the function

# Create a circuit with at least n qubits
n = 4
qr = QuantumRegister(n, 'q')
cr = ClassicalRegister(n, 'c')
qc = QuantumCircuit(qr, cr)

# (Optional) Initialize qr into some state

# Apply forward QFT on all qubits
qft(qc, num_qubits=n, inverse=False, do_swaps=True)

# Measure and continue...
qc.measure(qr, cr)

