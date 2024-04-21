# Functions to check if the given automaton is in a certain form


def is_standard(automaton, explicit_mode=False):
    """
    Returns true if the automaton is standard. If explicit mode is on, then the function returns
    a list[bool, str], bool being the answer and str the explanation.
    """

    if len(automaton["initial_states"]) > 1:
        if explicit_mode:
            output = [False, "More than one initial states were found."]
            return output
        return 0
    for elt in automaton["transitions"]:
        if elt[2:] in automaton["initial_states"]:
            if explicit_mode:
                output = [False, "Transitions towards the initial state were found."]
                return output
            return 0
    if explicit_mode:
        output = [True, "There is a unique initial state with no transitions towards it."]
        return output
    return 1


def is_deterministic(automaton, explicit_mode=False):
    """
    Returns true if the automaton is deterministic. If explicit mode is on, then the function returns
    a list[bool, str], bool being the answer and str the explanation.
    """

    if len(automaton["initial_states"]) > 1:
        if explicit_mode:
            output = [False, "More than one initial states were found."]
            return output
        return 0
    for elt in automaton["transitions"]:
        for comp in automaton["transitions"][automaton["transitions"].index(elt):]:
            if (elt[:2] == comp[:2]) and (elt != comp):
                if explicit_mode:
                    output = [False, "Multiple transitions from the same state with the same letter towards "
                                     "different states were found."]
                    return output
                return 0
    if explicit_mode:
        output = [True, "There is a unique initial state and, for any state, every transitions uses "
                        "a different letter."]
        return output
    return 1


def is_complete(automaton, explicit_mode=False):
    """
    Returns true if the automaton is complete. If explicit mode is on, then the function returns
    a list[bool, str], bool being the answer and str the explanation.
    """

    if not is_deterministic(automaton):
        if explicit_mode:
            output = [False, "The automaton is not deterministic."]
            return output
        return 0
    if len(automaton["transitions"]) >= (len(automaton["alphabet"])*len(automaton["states"])):
        if explicit_mode:
            output = [True, "Every states have at least one transition for each letter of the alphabet."]
            return output
        return 1
    else:
        if explicit_mode:
            output = [False, "One or more states don't have transitions for every letter of the alphabet."]
            return output
        return 0
