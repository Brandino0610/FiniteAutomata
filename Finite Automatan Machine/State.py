
class State():

    # Initializer for basic DFA and NFA
    def __init__(self, final):
        self.isFinal = final

    # Initializer for MooreMachine
    # def __init__(self, output):
    #     self.output = output

    # Initializer for NealyMachine
    # def __init__(self, zeroOutput, oneOutput):
    #     self.zeroOutput = zeroOutput
    #     self.oneOutput = oneOutput

    def setNodes(self, zero, one):
        self.zeroNode = zero
        self.oneNode = one
