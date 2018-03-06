import FiniteAutomatan
import State

q0 = State.State(True)
q2 = State.State(False)
q1 = State.State(False)
q3 = State.State(False)

q0.setNodes(q2, q1)
q1.setNodes(q3, q0)
q2.setNodes(q0, q3)
q3.setNodes(q1, q2)

FA = FiniteAutomatan.FiniteAutomatan()

value = "0011"

print(FA.basicDFA(value, q0))
