import FiniteAutomatan
import State

q0 = State.State('A', 'B')
q1 = State.State('C', 'D')
q2 = State.State('E', 'F')
q3 = State.State('G', 'H')

q0.setNodes(q1, q3)
q1.setNodes(q1, q2)
q2.setNodes(q2, q3)
q3.setNodes(q0, q3)

FA = FiniteAutomatan.FiniteAutomatan()

value = '00000001101011'

print(FA.NealyMachine(value, q0))
