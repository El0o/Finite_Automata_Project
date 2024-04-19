from FA_lstest import automata
from FA_operations import *
from FA_checks import *
from FA_recognise import *
from FA_display import *

def complementary_automaton (automaton):
    if is_deterministic(automaton) == 1 and is_complete(automaton) == 0:
        completion(automaton)
    elif is_complete(automaton) == 0:
        determinization_and_completion_automaton(automaton)
    new_final=[]
    for i in range(len(automaton['states'])-1):
        if not int(automaton['states'][i]) in automaton['final_states']:
            new_final.append(i)
    if "P" in automaton['states']:
        new_final.append("P")
    automaton['final_states']=new_final
    return automaton

def complementary_automata_test (automaton):
    complementary_automaton(automaton)
    word_recognition(automaton)

def display_complete_dererministic_automaton(automaton):
    complementary_automaton(automaton)
    display_table(automaton)


