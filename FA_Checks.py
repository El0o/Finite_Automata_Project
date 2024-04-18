from FA_lst import automata

def isDeterministic(automaton):
    if len(automaton["initial_states"]) > 1:
        return 0
    for elt in automaton["transitions"]:
        for comp in automaton["transitions"]:
            if ((elt[:2] == comp[:2]) and (elt != comp)):
                return 0
    return 1

def isComplete(automaton):
    if len(automaton["transitions"]) == (len(automaton["alphabet"])*len(automaton["states"])):
        return 1
    return 0

def isStandard(automaton):
    for elt in automaton["transitions"]:
        if elt[2:] in automaton["initial_states"]:
            return 0
    return 1
