# Functions to handle the creation and importation of .txt files

from os import listdir, path


def export_automaton(automaton):
    """
    Creates a .txt file for a given automaton
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

    print(f"Automaton successfully saved as {filename}.")


def import_automaton(filename):
    """
    Returns the automaton stored in the .txt file as a python dictionary
    """
    # Reads the content of the file
    with open(filename, "r") as file:
        lines = file.readlines()

    # Extracts automaton information from the lines
    automaton_info = {}
    transitions = []
    for line in lines:
        line = line.strip()
        if line.startswith("ID:"):
            automaton_info["id"] = line.split(":")[1].strip()
        elif line.startswith("States:"):
            automaton_info["states"] = line.split(":")[1].strip().split(", ")
        elif line.startswith("Alphabet:"):
            automaton_info["alphabet"] = line.split(":")[1].strip().split(", ")
        elif line.startswith("Initial States:"):
            automaton_info["initial_states"] = line.split(":")[1].strip().split(", ")
        elif line.startswith("Final States:"):
            automaton_info["final_states"] = line.split(":")[1].strip().split(", ")
        elif line == "Transitions:":
            continue
        else:
            transitions.append(line)

    # Formats transitions if necessary
    if transitions:
        automaton_info["transitions"] = transitions
    else:
        automaton_info["transitions"] = []

    return automaton_info


def import_all_automata():
    """
    Returns a dictionary list of every automaton present in the "automata" folder
    """
    automata_lst = []
    for filename in listdir("automata"):
        f = path.join("automata", filename)
        automata_lst.append(import_automaton(f))
    print("Automata successfully imported.")
    return automata_lst
