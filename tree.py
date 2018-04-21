class Node:
    def __init__(self, parent=None, action=None, state=None):
        # parent node
        self.parent = parent
        # action taken from parent node to get to this node
        self.action = action
        # state of the environment corresponding to this node
        self.state = state

        self.nb_visits = 0  # number of times the node was visited
        self.uct = 0  # uct value

        self.available_actions = state.available_actions
        self.unvisited_states = state.next_states
        self.children = []  # visited children nodes

    def is_not_fully_expanded(self):
        return len(self.unvisited_states) > 0

    def add_child(self, action, child_state):
        child = Node(self, action, child_state)
        self.children.append(child)

        self.available_actions.remove(action)
        self.unvisited_states.remove(child_state)
