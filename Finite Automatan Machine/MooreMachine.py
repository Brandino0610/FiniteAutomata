import FiniteAutomatan
import State

q0 = State.State('A')
q1 = State.State('B')
q2 = State.State('C')
q3 = State.State('D')

q0.setNodes(q1, q3)
q1.setNodes(q1, q2)
q2.setNodes(q0, q2)
q3.setNodes(q0, q2)

FA = FiniteAutomatan.FiniteAutomatan()

value = '11101010110'

print(FA.MooreMachine(value, q0))
