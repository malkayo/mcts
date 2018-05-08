import random
from mcts import mctsSearch
from copy import deepcopy

MCTS_PLAYER = 1


class TicTacToeState:
    """ A state of the game, i.e. the game board.
            Squares in the board are in this arrangement
            012
            345
            678
            where 0 = empty, 1 = player 1 (X), 2 = player 1 (O)

            According to
            https://math.stackexchange.com/questions/2444744/probability-of-winning-tic-tac-toe-game/2444768#2444768
            the probability of winning if player 1 is 0.58
            this is useful during debugging with two random players
    """

    def __init__(self, state_vector, current_player):
        # represents the state of the environment
        self.state_vector = state_vector

        # current player
        self.current_player = current_player

        # indicates if state is terminal
        # reward received when reaching this state
        self.terminal, self.reward = self.get_terminal_reward(
            self.current_player)

        # available actions from this state
        self.available_actions = self.available_actions()

    def available_actions(self):
        actions = []
        for i in range(len(self.state_vector)):
            if self.state_vector[i] == 0:
                actions.append(i)
        return actions

    def act(self, action):
        # write down the chosen action to new state vector
        new_state_vector = self.state_vector
        new_state_vector[action] = self.current_player

        # switch players
        if self.current_player == 1:
            next_player = 2
        else:
            next_player = 1

        # create the new state
        next_state = TicTacToeState(new_state_vector, next_player)

        return next_state

    def get_terminal_reward(self, player):
        # return whether the state is terminal and the related reward

        terminal_configs = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

        for (x, y, z) in terminal_configs:
            if (self.state_vector[x] == self.state_vector[y] and
                    self.state_vector[y] == self.state_vector[z]):

                if self.state_vector[x] == 0:
                    pass
                elif self.state_vector[x] == MCTS_PLAYER:
                    return (True, 1.0)  # player wins
                else:
                    return (True, -1.0)  # player looses

        if self.available_actions() == []:
            return (True, 0.0)  # draw
        else:
            return (False, 0.0)  # not final

    def print_state(self):
        s = ""
        for i in range(9):
            s += ".XO"[self.state_vector[i]]
            if i % 3 == 2:
                s += "\n"
        print s


def main():
    initial_state_vector = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # set up initial state
    state = TicTacToeState(
        state_vector=initial_state_vector, current_player=MCTS_PLAYER)

    while not state.terminal:
        # print("Main loop")  # DEBUG
        state.print_state()

        if state.current_player == MCTS_PLAYER:
            # if False:
            selected_action = mctsSearch(deepcopy(state))
        else:
            selected_action = random.choice(state.available_actions)

        print("player {} chooses {}".format(
            state.current_player, selected_action))

        state = state.act(selected_action)
    state.print_state()

    # win = False
    # if state.current_player == MCTS_PLAYER:
    #     if state.reward > 0:
    #         win = True
    # else:
    #     if state.reward < 0:
    #         win = True

    return state.reward > 0


if __name__ == "__main__":
    random.seed(1234)

    reward_sum = 0.
    nb_sim = 100
    for i in range(nb_sim):
        result = main()
        print("win?: {}".format(result))
        reward_sum += result
    print("average reward {}".format(reward_sum / nb_sim))


# class Environment:
#     def __init__(self):
#         pass

#     def available_actions():
#         actions = []
#         return actions

#     def act(state, action):
#         new_state_vector = None
#         reward = None
#         terminal_bool = False
#         next_state = State(new_state_vector, reward, terminal_bool)
#         return next_state
