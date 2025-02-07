import qiskit
from sys import version
from qiskit_ibm_runtime import QiskitRuntimeService
#QiskitRuntimeService.save_account(channel = 'ibm_quantum', token ='xxxxx...xxxxx')

print(f"Python version = {version}")

service = QiskitRuntimeService(channel = "ibm_quantum")
backend = service.backend(name = 'ibm_brisbane')

print(f"Qiskit version:= {qiskit.__version__}")
print(f"Using backend {backend.name}:- number of qbits is: {backend.num_qubits}")




#import sys
#
#print("Python version")
#print(sys.version)
#print("Version info.")
#print(sys.version_info)

