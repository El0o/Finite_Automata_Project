# Functions that operate on an automaton and returns another one on which the operation is done
from FA_checks import *


def standardization(automaton):
    """
    Returns the standard version of the automaton
    """
    a_standard = automaton.copy()
    nb_tr = len(a_standard['transitions'])
    for k in range(len(a_standard['initial_states'])):
        for i in range(nb_tr):
            if a_standard['transitions'][i][0] == a_standard['initial_states'][k]:
                keep = [a_standard['transitions'][i][1], a_standard['transitions'][i][2]]
                a_standard['transitions'][i] = ["i", keep[0], keep[1]]
    new_tr = []
    for j in a_standard['transitions']:
        if j not in new_tr:
            new_tr.append(j)
    a_standard['transitions'] = new_tr
    a_standard['initial_states'] = "i"
    init = ["i"]
    a_standard["states"] = init + a_standard["states"]
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

    nb_state = 0
    delimiter = "."
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
                start = delimiter.join(current_state)
                target = delimiter.join(temp)
                new_transitions.append("{}{}{}".format(start, a, target))
        nb_state += 1

    for s in to_treat_states:
        state = delimiter.join(s)
        new_states.append("{}".format(state))

    for f in a_deter["final_states"]:
        for s in to_treat_states:
            if f in s and s not in new_finals:
                final = delimiter.join(s)
                new_finals.append(final)

    a_deter["initial_states"] = delimiter.join(to_treat_states[0])
    a_deter["states"] = new_states
    a_deter["final_states"] = new_finals
    a_deter["transitions"] = new_transitions
    a_deter["id"] = a_deter["id"] + "D"

    return a_deter


def completion(automaton):
    """
    Returns the complete version of the automaton
    """
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

    new_tr = []

    for n in range(len(new_state)):
        for l in range(1, len(new_state[n])):
            toad = [new_state[n][0], new_state[n][l], "P"]
            new_tr.append(toad)

    for o in a_complete['alphabet']:
        toad = ["P", o, "P"]
        new_tr.append(toad)

        # We update our automaton

    a_complete['transitions'] += new_tr
    a_complete['states'].append("P")
    a_complete["id"] = a_complete["id"] + "C"

    return a_complete


def complementary_automaton(automaton):
    if not is_complete(automaton):
        inverse_automaton = completion(automaton)
    else:
        inverse_automaton = automaton.copy()
    new_final = []
    for i in range(len(inverse_automaton['states']) - 1):
        if not inverse_automaton['states'][i] in inverse_automaton['final_states']:
            new_final.append(i)
    if "P" in inverse_automaton['states']:
        new_final.append("P")
    inverse_automaton['final_states'] = new_final
    inverse_automaton['id'] = automaton['id'] + "I"

    return inverse_automaton


def are_distinguishable(elt1, elt2, P_previous, automaton):
    alphabet = automaton["alphabet"].copy()
    for a in alphabet:
        t1 = []
        t2 = []
        i = 0
        while (t1 == [] or t2 == []) and (i < len(automaton["transitions"])):
            if automaton["transitions"][i][1] == a:
                if automaton["transitions"][i][0] == elt1:
                    t1 = [automaton["transitions"][i][2]]
                    i += 1
                if automaton["transitions"][i][0] == elt2:
                    t2 = [automaton["transitions"][i][2]]
                    i += 1
                else:
                    i += 1

        for p in P_previous:
            if t1 in p:
                t1 = P_previous.index(p)
                break
        for p in P_previous:
            if t2 in p:
                t2 = P_previous.index(p)
                break

        if t1 != t2:
            return 1

    return 0


def minimization(automaton):
    """
    Return the minimal version of the automaton
    """
    if is_complete(automaton):
        a_mini = automaton.copy()
    else:
        a_mini = completion(automaton).copy()

    P_next = [automaton["final_states"].copy(), []]
    for s in automaton["states"]:
        if s not in automaton["final_states"]:
            P_next[1].append(s)
    P_previous = []

    while P_previous != P_next:
        P_previous = P_next
        P_next = []

        for partition in P_previous:
            if len(partition) > 1:
                for elt1 in partition:
                    for elt2 in partition[partition.index(elt1) + 1:]:

                        if are_distinguishable(elt1, elt2, P_previous, a_mini):
                            is_in1 = 0
                            is_in2 = 0
                            for p in P_next:
                                if elt1 in p:
                                    is_in1 = 1
                                elif elt2 in p:
                                    is_in2 = 1
                                if is_in1 and is_in2:
                                    break
                            if not is_in1:
                                P_next.append(elt1)
                            if not is_in2:
                                P_next.append(elt2)

                        else:
                            is_in1 = 0
                            is_in2 = 0
                            for p in P_next:
                                if elt1 in p:
                                    is_in1 = P_next.index(p)
                                    break
                                elif elt2 in p:
                                    is_in2 = P_next.index(p)
                                    break
                            if is_in1 and elt2 not in P_next[is_in1]:
                                P_next[is_in1].append(elt2)
                            elif is_in2 and elt1 not in P_next[is_in2]:
                                P_next[is_in2].append(elt1)
                            else:
                                P_next.append([elt1, elt2])

            else:
                P_next.append(partition)

    a_mini["id"] = a_mini["id"][0] + "MCD"
    a_mini["states"] = []
    for i in range(len(P_next)):
        if a_mini["initial_states"] in P_next[i]:
            a_mini["initial_states"] = "{}".format(i)
        a_mini["states"].append("{}".format(i))
    new_finals = []
    for f in a_mini["final_states"]:
        for i in range(len(P_next)):
            if f in P_next[i]:
                new_finals.append("{}".format(i))
    a_mini["final_states"] = new_finals

    new_transitions = []
    nb = 0
    for i in range(len(P_next)):
        for t in a_mini["transitions"]:
            if P_next[i][0] == t[0]:
                new_transitions[nb].append("{}", "{}".format(i, t[1]))
                for j in range(len(P_next)):
                    if t[2] in P_next[j]:
                        new_transitions[nb].append("{}".format(j))
                        break
                nb += 1
    a_mini["transitions"] = new_transitions

    return a_mini