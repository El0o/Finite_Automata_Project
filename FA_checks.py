# Functions to check if the given automaton is in a certain form

def is_standard(automaton):
    """
    Returns true if the automaton is standard
    """
    if len(automaton["initial_states"]) > 1:
        return 0
    for elt in automaton["transitions"]:
        if elt[2:] in automaton["initial_states"]:
            return 0
    return 1


def is_deterministic(automaton):
    """
    Returns true if the automaton is deterministic
    """
    if len(automaton["initial_states"]) > 1:
        return 0
    for elt in automaton["transitions"]:
        for comp in automaton["transitions"][automaton["transitions"].index(elt):]:
            if (elt[:2] == comp[:2]) and (elt != comp):
                return 0
    return 1


def is_complete(automaton):
    """
    Returns true if the automaton is complete
    """
    if not is_deterministic(automaton):
        return 0
    if len(automaton["transitions"]) == (len(automaton["alphabet"])*len(automaton["states"])):
        return 1
    else:
        return 0


def yes_no(boolean):
    """
    Translate a boolean into a comprehensible string.
    """
    if boolean:
        return "Yes"
    else:
        return "No"
