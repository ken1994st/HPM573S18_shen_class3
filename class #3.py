class Node:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def get_expected_cost(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

# two chanceNode

class ChanceNode(Node):
    def __init__(self, name, cost, probs, future_nodes):
        Node.__init__(self, name, cost)
        self.probs = probs
        self.future_nodes = future_nodes

    def get_expected_cost(self):
        exp_cost = self.cost # the expected cost of this node including the cost of visiting this node
        i = 0 # index to iterate over probabilities
        for thisNode in self.future_nodes:
            exp_cost += self.probs[i] * thisNode.get_expected_cost()
            i += 1

        return exp_cost



class TerminalNode(Node):
    def __init__(self, name, cost):
        Node.__init__(self, name, cost)

    def get_expected_cost(self):
        return self.cost

class DecisionNode(Node):
    def __init__(self, name, cost, future_nodes):
        Node.__init__(self, name, cost)
        self.future_nodes = future_nodes  #list of future node objects

    def get_expected_cost(self):
        """return the expected cost of associated future nodes"""
        outcomes = dict() # dictionary to store expected cost of future nodes
        for thisNode in self.future_nodes:
            outcomes[thisNode.name] = thisNode.get_expected_cost()

        return outcomes

#creating terminal node T1

T1 = TerminalNode('T1', 10)
T2 = TerminalNode('T2', 20)
T3 = TerminalNode('T3', 30)
T4 = TerminalNode('T4', 40)
T5 = TerminalNode('T5', 50)
T6 = TerminalNode('T6', 60)

C2FutureNodes = [T1, T2, T3]
C2 = ChanceNode('C2', 15, [0.1, 0.2, 0.7], C2FutureNodes)

C1FutureNodes = [C2, T4]
C1 = ChanceNode('C1', 0, [0.5, 0.5], C1FutureNodes)

C3FutureNodes =[T5, T6]
C3 = ChanceNode('C3', 0, [0.2,0.8], C3FutureNodes)

D1FutureNodes =[C1, C3]
D1 = DecisionNode('D1', 0, D1FutureNodes)

print(D1.get_expected_cost())
