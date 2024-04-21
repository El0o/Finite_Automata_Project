# All functions related to word recognition

def read_word():
    """
    Reads a word
    """
    return input("Type a word: ")


def new_word(word):
    """
    Returns the word minus its first letter
    """
    nword = ""
    for i in range(1, len(word)):
        nword += word[i]
    return nword


def recognize_word(automaton, word):
    """
    Returns true if the word is recognised by the given automaton
    """
    lenth = len(word)
    lastplace = ""
    initword = word

    for i in range(len(automaton['initial_states'])):
        place = automaton['initial_states'][i]
        # We will test by starting with every initial states.
        if word == "" and i == len(automaton['initial_states']):
            if lastplace in automaton['final_states']:
                return True
            else:
                return False
        else:
            if word == "" and (lastplace in automaton['final_states']):
                return True
            else:
                if len(word) < len(initword):
                    word = initword
                # This is the comparison algorithm. We check if there is a transition corresponding to our starting state and our letter.
                for k in range(lenth):
                    for j in automaton['transitions']:
                        if place + word[0] == j[0] + j[1]:
                            place = j[2]
                            word = new_word(word)
                            # We store the final state of the word we just check, to verify if it is a final state of the automaton.
                            if word == "":
                                lastplace = place
                            break
    if automaton != "":
        return False
    else:
        return True


def word_recognition(automaton):
    """
    Enters word recognition mode (continuously ask the user for a word to recognize until they type [/end]
    """
    word = ""
    print("Write [/end] to exit word recognition.")
    while word != "/end":
        word = read_word()
        if word == "/end":
            break
        test = recognize_word(automaton, word)
        if test:
            print(f"The word {word} is recognised by the automaton n°{automaton['id']}")
        else:
            print(f"The word {word} is not recognised by the automaton n°{automaton['id']}")
