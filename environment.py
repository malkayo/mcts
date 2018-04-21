class State:
    def __init__(self, state_vector, terminal_bool):
        # represents the state of the environment
        self.state_vector = state_vector

        # indicates if state is terminal
        self.terminal = terminal_bool


class Environment:
    def __init__(self):
        pass

    def available_actions(state):
        actions = []
        return actions

    def act(state, action):
        next_state = None
        reward = 0
        return next_state, reward
