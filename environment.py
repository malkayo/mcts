class State:
    def __init__(self, state_vector, reward, terminal_bool, action):
        # represents the state of the environment
        self.state_vector = state_vector

        # indicates if state is terminal
        self.terminal = terminal_bool

        # reward received when reaching this state
        self.reward = reward

        # action used to get to this state from the previous state
        self.action = action


class Environment:
    def __init__(self):
        pass

    def available_actions(state):
        actions = []
        return actions

    def act(state, action):
        new_state_vector = None
        reward = None
        terminal_bool = False
        next_state = State(new_state_vector, reward, terminal_bool)
        return next_state
