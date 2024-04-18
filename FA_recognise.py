from FA_lstest import automata

def read_word():
    return input("Type a word: ")

def new_word (word):
    nword=""
    for i in range(1,len(word)):
        nword += word[i]
    return nword



def recognize_word (automaton, word):
    lenth = len(word)
    lastplace = ""
    initword = word

    for i in range(len(automaton['initial_states'])):
        place = automaton['initial_states'][i]
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
                for k in range(lenth):
                    for j in automaton['transitions']:
                        if place + word[0] == j[0] + j[1]:
                            place = j[2]
                            word = new_word(word)
                            if word == "":
                                lastplace=place
                            break
    if automaton != "":
        return False
    else:
        return True


def word_recognition (automaton):
    word=""
    print("Write : end if you want to stop testing")
    while word != "end":
        word = read_word()
        test = recognize_word(automaton,word)
        if test == True:
            print("The word",word,"is recognised by the automaton n°",automaton['id'])
        else:
            print("The word", word, "is not recognised by the automaton n°", automaton['id'])
    print("The test is finished.")



print(automata[4])
word_recognition(automata[4])



