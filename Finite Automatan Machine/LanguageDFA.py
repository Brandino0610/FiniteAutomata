import FiniteAutomatan
import State

q0 = State.State(False)
q1 = State.State(False)
q2 = State.State(True)
q3 = State.State(False)
q4 = State.State(True)

q0.setNodes(q4, q2)
q1.setNodes(q0, q2)
q2.setNodes(q1, q3)
q3.setNodes(q4, q3)
q4.setNodes(q1, q2)

FA = FiniteAutomatan.FiniteAutomatan()

value = '001'

print(FA.basicDFA(value, q0))
