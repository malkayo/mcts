import math
import random
from tree import *

CP = 1
MAX_UCT = 1e10
BUDGET_LIMIT = 10
DISCOUNT_RATE = 1


def mctsSearch(s0):

    # create root node
    v0 = Node(parent=None, action=None, state=s0)
    custom_budget = int(BUDGET_LIMIT * len(s0.available_actions))
    budget = 0
    while budget < custom_budget:
        # selection + expansion
        # select or create a leaf node from the nodes
        # already contained within the search tree
        vl = tree_policy(v0)

        # simulation
        # play out the domain from a given non-terminal state
        # to produce a value estimate
        delta = default_policy(vl.state)

        # backpropagation
        backup(vl, delta)

        # increment budget counters
        budget += 1

    # return the action that leads to the best child of
    # the root node v0
    return best_child(v0, 0).action


def tree_policy(v):
    while not v.state.terminal:
        if v.is_not_fully_expanded():
            return expand(v)
        else:
            v = best_child(v, CP)
    return v


def expand(v):
    a = random.choice(v.untried_actions)

    # add a new child to v
    s_child = v.state.act(a)

    a_child = a
    v_child = v.add_child(a_child, s_child)

    return v_child


def best_child(v, cp):
    v_children = v.children
    uct_values = []

    for v_child in v_children:
        uct_values.append(get_uct(v, v_child, cp))
    # return the child with the max uct, random choice in the case of a tie
    max_uct = max(uct_values)
    max_children = [child for child, val in zip(
        v_children, uct_values) if val == max_uct]
    result = random.choice(max_children)
    return result


def get_uct(v, v_child, cp):
    if v_child.nb_visits == 0:
        return MAX_UCT
    else:
        return (v_child.q / v_child.nb_visits +
                2 * cp *
                math.sqrt(2 * math.log(v.nb_visits) / v_child.nb_visits))


def default_policy(s):
    state = s
    while not state.terminal:
        a = random.choice(state.available_actions)
        state = state.act(a)
    return state.reward


def backup(v, delta):
    step_back = 0
    while v:
        v.nb_visits += 1
        v.q += (DISCOUNT_RATE**step_back) * delta
        v = v.parent
        step_back += 1
