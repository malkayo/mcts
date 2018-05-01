import random

from mcts import mctsSearch
from copy import deepcopy

MCTS_PLAYER = 1


class State:
    def __init__(self, state_vector, reward, terminal_bool, action,
                 available_actions):
        # represents the state of the environment
        self.state_vector = state_vector

        # indicates if state is terminal
        self.terminal = terminal_bool

        # reward received when reaching this state
        self.reward = reward

        # action used to get to this state from the previous state
        self.action = action

        # available actions from this state
        self.available_actions = available_actions


class Environment:
    def __init__(self):
        pass

    def available_actions():
        actions = []
        return actions

    def act(state, action):
        new_state_vector = None
        reward = None
        terminal_bool = False
        next_state = State(new_state_vector, reward, terminal_bool)
        return next_state


class OXO(Environment):
    """ A state of the game, i.e. the game board.
            Squares in the board are in this arrangement
            012
            345
            678
            where 0 = empty, 1 = player 1 (X), 2 = player 2 (O)
    """

    def __init__(self):
        # Game board: 0 = empty, 1 = player 1, 2 = player 2
        self.initial_state_vector = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        available_actions = self.available_actions(self.initial_state_vector)

        self.initial_state = State(
            self.initial_state_vector, 0, False, None, available_actions)

        # current player
        self.current_player = 1

        self.verbose = True

    def available_actions(self, state_vector):
        actions = []
        for i in range(len(state_vector)):
            if state_vector[i] == 0:
                actions.append(i)
        return actions

    def act(self, state, action):
        # write down the chosen action to new state vector
        new_state_vector = state.state_vector
        new_state_vector[action] = self.current_player

        # create the new state
        (terminal_bool, reward) = self.get_terminal_reward(
            new_state_vector, MCTS_PLAYER)
        available_actions = self.available_actions(new_state_vector)
        next_state = State(new_state_vector, reward,
                           terminal_bool, action, available_actions)
        # switch player
        if self.current_player == 1:
            self.current_player = 2
        else:
            self.current_player = 1

        return next_state

    def get_terminal_reward(self, state_vector, player):
        # self.print_state(state_vector)  # DEBUG

        # return whether the state is terminal and the related reward

        terminal_configs = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for (x, y, z) in terminal_configs:
            if (state_vector[x] == state_vector[y] == state_vector[z]):

                if state_vector[x] == 0:
                    pass
                elif state_vector[x] == player:
                    if self.verbose:
                        pass
                        # print("player {} wins".format(MCTS_PLAYER))
                    return (True, 1.0)  # player wins
                else:
                    if self.verbose:
                        pass
                        # print("player {} loses".format(MCTS_PLAYER))
                    return (True, -1.0)  # player looses

        if self.available_actions(state_vector) == []:
            if self.verbose:
                pass
                # print("it's a draw!")
            return (True, 0.0)  # draw
        else:
            return (False, 0.0)  # not final

    def print_state(self, state_vector):
        s = ""
        for i in range(9):
            s += ".XO"[state_vector[i]]
            if i % 3 == 2:
                s += "\n"
        print s


def main():
    env = OXO()  # define which kind of environment
    state = env.initial_state  # set up initial state

    while not state.terminal:
        # print("Main loop")  # DEBUG
        env.print_state(state.state_vector)

        if env.current_player == MCTS_PLAYER:
            selected_action = mctsSearch(deepcopy(state), deepcopy(env))
        else:
            available_actions = env.available_actions(state.state_vector)
            selected_action = random.choice(available_actions)

        print("player {} chooses {}".format(
            env.current_player, selected_action))

        state = env.act(state, selected_action)
    env.print_state(state.state_vector)

    return state.reward


if __name__ == "__main__":
    reward_sum = 0.
    nb_sim = 10
    for i in range(nb_sim):
        result = main()
        print("result:{}".format(result))
        reward_sum += result
    print("average reward {}".format(reward_sum / nb_sim))
