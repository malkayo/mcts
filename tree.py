class Node:
    def __init__(self, parent=None, action=None, state=None):
        # parent node
        self.parent = parent
        # action taken from parent node to get to this node
        self.action = action
        # state of the environment corresponding to this node
        self.state = state

        self.nb_visits = 0  # number of times the node was visited
        self.q = 0  # uct value

        self.available_actions = state.available_actions
        self.untried_actions = self.available_actions
        self.children = []  # visited children nodes

    def is_not_fully_expanded(self):
        return len(self.untried_actions) > 0

    def add_child(self, action, child_state):
        child = Node(self, action, child_state)
        self.children.append(child)

        self.untried_actions.remove(action)

        return child

    def tree_depth(self, counter=0):
        print(self.state.state_vector)
        if self.state.terminal or not self.children:
            return counter + 1
        else:
            depths = []
            for child in self.children:
                depths.append(child.tree_depth(counter + 1))
            return max(depths)
