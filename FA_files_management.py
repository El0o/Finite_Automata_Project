# Functions to handle the creation and importation of .txt files

from FA_lst import automata as og_automata
from os import listdir, path, remove


def export_automaton(automaton):
    """
    Creates (or modifies if already existing) a text file for a given automaton
    """
    # Defines file name
    filename = f"automata/INT2-2-{automaton['id']}.txt"
    # Writes into the file the characteristics of the automaton
    with open(filename, "w") as file:
        file.write(f"ID: {automaton['id']}\n")
        file.write(f"Alphabet: {', '.join(automaton['alphabet'])}\n")
        file.write(f"States: {', '.join(automaton['states'])}\n")
        file.write(f"Initial States: {', '.join(automaton['initial_states'])}\n")
        file.write(f"Final States: {', '.join(automaton['final_states'])}\n")
        file.write("Transitions:\n")
        for transition in automaton['transitions']:
            file.write(f"{transition}\n")

    print(f"Automaton successfully saved in {filename}")


def import_automaton(filename):
    """
    Returns the automaton stored in the given text file as a python dictionary
    """
    # Reads the entire file
    with open(filename, "r") as file:
        lines = file.readlines()

    automaton = {}
    transitions = []
    # Creates the keys of the dictionary and dispatches the lines' information correctly
    for line in lines:
        line = line.strip()
        if line.startswith("ID:"):
            automaton["id"] = line.split(":")[1].strip()
        elif line.startswith("Alphabet:"):
            automaton["alphabet"] = line.split(":")[1].strip().split(", ")
        elif line.startswith("States:"):
            automaton["states"] = line.split(":")[1].strip().split(", ")
        elif line.startswith("Initial States:"):
            automaton["initial_states"] = line.split(":")[1].strip().split(", ")
        elif line.startswith("Final States:"):
            automaton["final_states"] = line.split(":")[1].strip().split(", ")
        else:
            transitions.append(line)

    automaton["transitions"] = transitions

    return automaton


def import_all_automata():
    """
    Returns a dictionary list of every automata present in the "automata" directory
    """
    automata_lst = []
    for filename in listdir("automata"):
        file = path.join("automata", filename)
        automata_lst.append(import_automaton(file))
    print("Automata successfully imported.")
    return automata_lst


def get_automaton(automata_lst, a_id):
    """
    Returns the automaton if present in the automata list, otherwise returns None
    """
    automaton = next((a for a in automata_lst if a["id"] == a_id), None)
    return automaton


def fond_txt(automaton):
    """
    Returns true if the text version of the given automaton is found in the "automata" directory
    """
    for filename in listdir("automata"):
        with open(path.join("automata", filename), "r") as file:
            id_line = file.readline()
            if id_line.split(":")[1].strip() == automaton["id"]:
                return 1
    return 0


def reset_automata_folder():
    """
    Deletes all text files and replaces them with the original test automata (given for this project)
    """
    for filename in listdir("automata"):
        file = path.join("automata", filename)
        remove(file)
    for automaton in og_automata:
        export_automaton(automaton)
