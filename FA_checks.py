# Functions to check if the given automaton is in a certain form

checks_output = ""


def is_standard(automaton, explicit_mode=False):
    """
    Returns true if the automaton is standard. If explicit mode is on, then the variable "checks_output"
    is modified to contain an explanation.
    """
    if explicit_mode:
        global checks_output
    if len(automaton["initial_states"]) > 1:
        if explicit_mode:
            checks_output = "More than one initial states were found."
        return 0
    for elt in automaton["transitions"]:
        if elt[2:] in automaton["initial_states"]:
            if explicit_mode:
                checks_output = "Transitions towards the initial state were found."
            return 0
    if explicit_mode:
        checks_output = "There is a unique initial state with no transitions towards it."
    return 1


def is_deterministic(automaton, explicit_mode=False):
    """
    Returns true if the automaton is deterministic. If explicit mode is on, then the variable "checks_output"
    is modified to contain an explanation.
    """
    if explicit_mode:
        global checks_output
    if len(automaton["initial_states"]) > 1:
        if explicit_mode:
            checks_output = "More than one initial states were found."
        return 0
    for elt in automaton["transitions"]:
        for comp in automaton["transitions"][automaton["transitions"].index(elt):]:
            if (elt[:2] == comp[:2]) and (elt != comp):
                if explicit_mode:
                    checks_output = "Multiple transitions from the same state with the same letter towards different states were found."
                return 0
    if explicit_mode:
        checks_output = "There is a unique initial state and, for any state, every transitions uses a different letter."
    return 1


def is_complete(automaton, explicit_mode=False):
    """
    Returns true if the automaton is complete. If explicit mode is on, then the variable "checks_output"
    is modified to contain an explanation.
    """
    if explicit_mode:
        global checks_output
    if not is_deterministic(automaton):
        if explicit_mode:
            checks_output = "The automaton is not deterministic."
        return 0
    if len(automaton["transitions"]) >= (len(automaton["alphabet"])*len(automaton["states"])):
        if explicit_mode:
            checks_output = "Every states have at least one transition for each letter of the alphabet."
        return 1
    else:
        if explicit_mode:
            checks_output = "One or more states don't have transitions for every letter of the alphabet."
        return 0
