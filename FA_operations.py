# Functions that operate on an automaton and returns another one on which the operation is done
from FA_checks import *
from copy import deepcopy


def standardization(automaton):
    """
    Returns the standard version of the automaton
    """
    a_standard = deepcopy(automaton)
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
    a_deter = deepcopy(automaton)
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

                new_transitions.append([start, a, target])
        nb_state += 1

    for s in to_treat_states:
        state = delimiter.join(s)
        new_states.append("{}".format(state))

    for f in a_deter["final_states"]:
        for s in to_treat_states:
            if f in s and s not in new_finals:
                final = delimiter.join(s)
                new_finals.append(final)

    a_deter["initial_states"] = [delimiter.join(to_treat_states[0])]
    a_deter["states"] = new_states
    a_deter["final_states"] = new_finals
    a_deter["transitions"] = new_transitions
    a_deter["id"] = a_deter["id"] + "D"

    return a_deter


def completion(automaton):
    """
    Returns the complete version of the automaton
    """
    if not is_deterministic(automaton):
        autom = automaton
        a_complete = determinization(autom)
        if is_complete(a_complete):
            return a_complete
    else:
        a_complete = deepcopy(automaton)
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
    """
    Returns the automaton accepting the complementary language of the given automaton
    """
    if not is_complete(automaton):
        autom = automaton
        inverse_automaton = completion(autom)
    else:
        inverse_automaton = deepcopy(automaton)
    new_final = []
    for state in automaton['states']:
        if state not in automaton['final_states']:
            new_final.append(state)
    inverse_automaton['final_states'] = new_final
    inverse_automaton['id'] = automaton['id'] + "I"

    return inverse_automaton


def are_distinguishable(elt1, elt2, P_previous, automaton):
    """
    Returns true if the two elements are distinguishable
    """
    alphabet = deepcopy(automaton["alphabet"])
    for a in alphabet:
        i = 0
        t1 = ''
        t2 = ''
        while (t1 == '' or t2 == '') and (i < len(automaton["transitions"])):
            if automaton["transitions"][i][1] == a:
                if automaton["transitions"][i][0] == elt1:
                    t1 = automaton["transitions"][i][2]
                    i += 1
                if automaton["transitions"][i][0] == elt2:
                    t2 = automaton["transitions"][i][2]
                    i += 1
                else:
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


def roman_nb(integer):
    """
    Return the roman number version of the integer
    """
    roman = ['0', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV']
    if integer > 15:
        return "blep"
    return roman[integer]


def minimization(automaton):
    """
    Return the minimal version of the automaton
    """
    if is_complete(automaton):
        a_mini = deepcopy(automaton)
    else:
        a_mini = deepcopy(completion(automaton))

    if len(a_mini["final_states"]) > 0:
        P_next = [deepcopy(a_mini["final_states"]), []]
        temp = 1
    else:
        P_next = [[]]
        temp = 0
    for s in a_mini["states"]:
        if s not in a_mini["final_states"]:
            P_next[temp].append(s)
    if not P_next[temp]:
        P_next.pop(temp)
    P_previous = []
    while P_previous != P_next:
        P_previous = P_next
        P_next = []

        for partition in P_previous:
            if len(partition) > 1:
                for elt1 in partition[:1]:
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
                                P_next.append([elt1])
                            if not is_in2:
                                P_next.append([elt2])

                        else:
                            is_in1 = 0
                            is_in2 = 0
                            for p in P_next:
                                if elt1 in p:
                                    is_in1 = 1
                                    index1 = P_next.index(p)
                                    break
                                elif elt2 in p:
                                    is_in2 = 1
                                    index2 = P_next.index(p)
                                    break
                            if is_in1:
                                if elt2 not in P_next[index1]:
                                    P_next[index1].append(elt2)
                            elif is_in2:
                                if elt1 not in P_next[index2]:
                                    P_next[index2].append(elt1)
                            else:
                                P_next.append([elt1, elt2])

            else:
                P_next.append(partition)

    a_mini["id"] = automaton["id"] + "M"
    a_mini["states"] = []
    for i in range(len(P_next)):
        if a_mini["initial_states"][0] in P_next[i]:
            a_mini["initial_states"] = ["{}".format(roman_nb(i))]
            break
    for i in range(len(P_next)):
        a_mini["states"].append("{}".format(roman_nb(i)))
    new_finals = []
    for f in a_mini["final_states"]:
        for i in range(len(P_next)):
            if f in P_next[i] and str(i) not in new_finals:
                new_finals.append("{}".format(roman_nb(i)))
    a_mini["final_states"] = new_finals

    new_transitions = []
    nb = 0
    for i in range(len(P_next)):
        for t in a_mini["transitions"]:
            if len(P_next[i]):
                if P_next[i][0] == t[0]:
                    new_transitions.append([])
                    new_transitions[nb].append("{}".format(roman_nb(i)))
                    new_transitions[nb].append("{}".format(t[1]))
                    for j in range(len(P_next)):
                        if t[2] in P_next[j]:
                            new_transitions[nb].append("{}".format(roman_nb(j)))
                            break
                    nb += 1
    a_mini["transitions"] = new_transitions

    S_equivalence = "The new states have the following correspondence: \n"
    for i in range(len(P_next)):
        S_equivalence = S_equivalence + ("- {} : ".format(roman_nb(i))) + ("{}".format(', '.join(P_next[i]))) + "\n"

    return [a_mini, S_equivalence]

automaton = {
        "id": "4",
        "alphabet": ["a"],
        "states": ["0", "1"],
        "initial_states": ["0"],
        "final_states": [],
        "transitions": [
            ["0", "a", "1"]
        ]
    }

minimization(automaton)
