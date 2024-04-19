from FA_lstest import automata

#reading of a word
def read_word():
    return input("Type a word: ")

#function that change a word, we remove the first letter of it
def new_word (word):
    nword=""
    for i in range(1,len(word)):
        nword += word[i]
    return nword


#function that reconise if a word is recognised by a given automaton
def recognize_word (automaton, word):
    lenth = len(word)
    lastplace = ""
    initword = word

    for i in range(len(automaton['initial_states'])):
        place = automaton['initial_states'][i]
        #We will test by starting with every initial states.
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
                #This is the comparison algorithm. We check if there is a transition corresponding to our depart state and our letter.
                for k in range(lenth):
                    for j in automaton['transitions']:
                        if place + word[0] == j[0] + j[1]:
                            place = j[2]
                            word = new_word(word)
                            #We store the final state of the word we just check, to verify if it is a final state of the automaton.
                            if word == "":
                                lastplace=place
                            break
    if automaton != "":
        return False
    else:
        return True

#The main function that will permit to continously ask the user to enter a word until he wants to stop.
def word_recognition (automaton):
    word=""
    print("Write : end if you want to stop testing")
    while word != "end":
        word = read_word()
        if word == "end":
            break
        test = recognize_word(automaton,word)
        if test == True:
            print("The word",word,"is recognised by the automaton n°",automaton['id'])
        else:
            print("The word", word, "is not recognised by the automaton n°", automaton['id'])
    print("The test is finished.")



print(automata[4])
word_recognition(automata[4])



