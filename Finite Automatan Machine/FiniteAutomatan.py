import State

class FiniteAutomatan:

    def __init__(self):
        pass

    def basicDFA(self, string, State):
        # First and Second Program
        for i in string:
            if int(i) == 0:
                State = State.zeroNode
            elif int(i) == 1:
                State = State.oneNode
            else:
                return "ERROR: incorrect input"


        if State.isFinal:
            return 'The string passes the test! :)'
        else:
            return 'The string fails the test :('


    def MooreMachine(self, string, State):
        display = ''
        for i in string:
            display += State.output
            if int(i) == 0:
                State = State.zeroNode
            elif int(i) == 1:
                State = State.oneNode
            else:
                return "ERROR"

        return display

    def NealyMachine(self, string, State):
        display = ''
        for i in string:
            if int(i) == 0:
                display += State.zeroOutput
                State = State.zeroNode
            elif int(i) == 1:
                display += State.oneOutput
                State = State.oneNode
            else:
                return "ERROR"

        return display
