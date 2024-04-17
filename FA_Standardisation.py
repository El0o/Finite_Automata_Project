from FA_lst import automata
from FA_dict_management import create_automaton_txt

def standardisation (Autom):
    #Standardisation of the automaton
    As = automata[Autom]
    b= len(As['transitions'])
    for k in range(len(As['initial_states'])):
        for i in range(b):
            if As['transitions'][i][0] == As['initial_states'][k]:
                keep=As['transitions'][i][1] + As['transitions'][i][2]
                As['transitions'][i]="i"
                As['transitions'][i]=As['transitions'][i]+keep
    As['initial_states']="i"
    Init = ["i"]
    As["states"] = As["states"] + Init

    #Creation of a text document with the new automaton // Use of fct from Fa_dict
    create_automaton_txt(As)
    return As
