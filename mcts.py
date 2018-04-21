import math
import random
import tree
import environment

CP = 0.1
DISCOUNT_RATE = 0.95
MAX_UCT = 1e10


def mctsSearch(s0):
    # create root node
    v0 = Node(None, s0, None)

    while some_computational_budget_left:
        # selection + expansion
        # select or create a leaf node from the nodes
        # already contained within the search tree
        vl = tree_policy(v0)

        # simulation
        # play out the domain from a given non-terminal state
        # to produce a value estimate
        delta = default_policy(s(vl))

        # backpropagation
        backup(vl, delta)

        some_computational_budget_left = assess_budget()

    # return the action that leads to the best child of
    # the root node v0
    return a(best_child(v0))


def tree_policy(v):
    while not v.state.terminal:
        if v.is_not_fully_expanded():
            return expand(v)
        else:
            v = best_child(v)
    return v


def expand(v):
    a = random.choice(v.availale_actions)

    # add a new child to v
    s_child = f(get_state(v), a)
    a_child = a
    v_child = add_child(v, (s_child, a_child))

    return v_child


def best_child(v):
    v_children = children(v)
    uct_values = []

    for v_child in v_children:
        uct_value.append(get_uct(v, v_child))

    # return the child with the max uct, random choice in the case of a tie
    max_uct = max(uct_values)
    max_children = [child for child, val in zip(
        v_children, uct_values) if val == max_uct]
    v_children = random.choice(max_children)


def get_uct(v, v_child):
    if n(v_child) == 0:
        return MAX_UCT
    else:
        return (q(v_child) / n(v_child) +
                2 * CP *
                math.sqrt(2 * math.log(n(v)) / n(v_child)))


def default_policy(s):
    while is_non_terminal(s):
        a = choose_uniformly_random(possible_actions(s))
        s_new = f(s, a)
    return reward(s, a, s_new)  # ???? why not use total discounted return?


def backup(v, delta):
    while v:
        n(v) += 1
        q(v) += delta(v, p)
        v = parent(v)
