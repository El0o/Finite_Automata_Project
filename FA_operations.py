# Functions that operate on an automaton and returns another one on which the operation is done
from FA_checks import *


def standardization(automaton):
    """
    Returns the standard version of the automaton
    """
    a_standard = automaton.copy()
    b = len(a_standard['transitions'])
    for k in range(len(a_standard['initial_states'])):
        for i in range(b):
            if a_standard['transitions'][i][0] == a_standard['initial_states'][k]:
                keep = a_standard['transitions'][i][1] + a_standard['transitions'][i][2]
                a_standard['transitions'][i] = "i"
                a_standard['transitions'][i] = a_standard['transitions'][i] + keep
    a_standard['initial_states'] = "i"
    init = ["i"]
    a_standard["states"] = a_standard["states"] + init
    a_standard["id"] = a_standard["id"] + "S"

    return a_standard


def determinization(automaton):
    """
    Returns the deterministic version of the automaton
    """
    a_deter = automaton.copy()
    new_states = []
    new_transitions = []
    new_finals = []

    to_treat_states = [a_deter["initial_states"]]
    for t in a_deter["transitions"]:
        if "$" in t:
            a_deter["alphabet"].append("$")
            break

    nb_state = 0
    while nb_state != len(to_treat_states):
        current_state = to_treat_states[nb_state]
        for a in a_deter["alphabet"]:
            temp = []
            for i in current_state:
                for t in a_deter["transitions"]:
                    if t[0] == i and t[1] == a:
                        if t[2] not in temp:
                            temp.append(t[2])
            if temp and temp not in to_treat_states:
                to_treat_states.append(temp)
            if temp:
                new_transitions.append("{}{}{}".format(nb_state, a, to_treat_states.index(temp)))
        nb_state += 1

    for i in range(len(to_treat_states)):
        new_states.append("{}".format(i))

    for f in a_deter["final_states"]:
        for s in to_treat_states:
            if f in s and s not in new_finals:
                new_finals.append(to_treat_states.index(s))

    a_deter["initial_states"] = "0"
    a_deter["states"] = new_states
    a_deter["final_states"] = new_finals
    a_deter["transitions"] = new_transitions
    if "$" in a_deter["alphabet"]:
        a_deter["alphabet"].remove("$")

    a_deter["id"] = a_deter["id"] + "D"

    return a_deter


def completion(automaton):
    """
    Returns the complete version of the automaton
    """
    if not is_deterministic(automaton):
        a_complete = determinization(automaton)
    else:
        a_complete = automaton.copy()
    # Creation of a list that will keep track of which states we need to add
    new_state = []

    # Research of which states need to be added
    for j in range(len(a_complete['states'])):
        new_state.append([])
        for i in a_complete['transitions']:
            if i[0] == a_complete['states'][j] and i[1] in a_complete['alphabet']:
                new_state[j].append(i[1])

    # Organisation of the transition that will be added

        # We start with a list that will keep track of the initial state and the letter of the transition

    for k in range(len(new_state)):
        p = []
        for m in a_complete['alphabet']:
            if m not in new_state[k]:
                p.append(m)
        new_state[k] = p
        f = str(k)
        new_state[k].append(f)
        new_state[k].reverse()

        # Finally we create the new transitions,
        # the ones that start with an existing state and the ones that comes from P (new_state)

    add = []
    for n in range(len(new_state)):
        for l in range(1, len(new_state[n])):
            toad = new_state[n][0]
            toad = toad + new_state[n][l]
            toad = toad + "P"
            add.append(toad)

    for o in a_complete['alphabet']:
        toad = "P" + o + "P"
        add.append(toad)

        # We update our automaton

    a_complete['transitions'] = a_complete['transitions'] + add
    a_complete['states'].append("P")
    a_complete["id"] = a_complete["id"] + "C"

    return a_complete


def complementary_automaton(automaton):
    if not is_complete(automaton):
        inverse_automaton = completion(automaton)
    else:
        inverse_automaton = automaton.copy()
    new_final = []
    for i in range(len(inverse_automaton['states'])-1):
        if not inverse_automaton['states'][i] in inverse_automaton['final_states']:
            new_final.append(i)
    if "P" in inverse_automaton['states']:
        new_final.append("P")
    inverse_automaton['final_states'] = new_final
    inverse_automaton['id'] = inverse_automaton['id'] + "I"

    return inverse_automaton
