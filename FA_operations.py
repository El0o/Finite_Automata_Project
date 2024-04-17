# Functions that operate on an automaton and returns another one on which the operation is done

def standardisation(automaton):
    """
    Returns the standard version of the automaton
    """
    a_standard = automaton
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

    return a_standard


def completion(automaton):
    """
    Returns the complete version of the automaton
    """
    a_complete = automaton
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
        toad = ""
        for l in range(1, len(new_state[n])):
            toad = new_state[n][0]
            toad = toad + new_state[n][l]
            toad = toad + "new_states"
            add.append(toad)

    for o in a_complete['alphabet']:
        toad = "P" + o + "P"
        add.append(toad)

        # We update our automaton

    a_complete['transitions'] = a_complete['transitions'] + add
    a_complete['states'].append("P")

    return a_complete
