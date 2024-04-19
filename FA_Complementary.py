from FA_lstest import automata
from FA_operations import *
from FA_checks import *
from FA_recognise import *

#function that will creates the complementary automaton.
def complementary_automaton (automaton):
    #we start by cheking what kind of automaton we have, and thus determinise and complete it if needed.
    if is_deterministic(automaton) == 1 and is_complete(automaton) == 0:
        completion(automaton)
    elif is_complete(automaton) == 0:
        determinization_and_completion_automaton(automaton)
    #Ones the automaton is in the correct form we transform the finals states into non finale states and vise versa.
    new_final=[]
    for i in range(len(automaton['states'])-1):
        if not int(automaton['states'][i]) in automaton['final_states']:
            new_final.append(i)
    if "P" in automaton['states']:
        new_final.append("P")
    automaton['final_states']=new_final
    return automaton

#function that will create the complementary automaton of a given one, and allow to test words for the new automaton.
def complementary_automata_test (automaton):
    complementary_automaton(automaton)
    word_recognition(automaton)


