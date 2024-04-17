# Functions to display the tables

from texttable import Texttable
from FA_dict_management import automata


def display_table(automaton):
    """
    Displays a given automaton as a table, with initial states indicated with "⟶" and final states with "⟵" ("⟷" means both final & initial)
    """
    table = Texttable()
    table.set_deco(Texttable.HLINES | Texttable.VLINES)
    table.set_chars(['—', '│', '┼', '═'])
    align = ["r"] + ["c"]*len(automaton["alphabet"])
    table.set_cols_align(align)
    head = ["  "]
    for elt in automaton["alphabet"]:
        head.append(elt)
    table.header(head)

    for state in automaton["states"]:
        new_row = []
        state_cell = ""
        if (state in automaton["initial_states"]) and (state in automaton["final_states"]):
            state_cell += "⟷"
        elif state in automaton["initial_states"]:
            state_cell += "⟶"
        elif state in automaton["final_states"]:
            state_cell += "⟵"
        else:
            state_cell += " "

        state_cell += "   {s}".format(s=state)
        new_row.append(state_cell)
        for a in automaton["alphabet"]:
            cell = ""
            for tr in automaton["transitions"]:
                if (tr[0] == state) and (tr[1] == a):
                    cell += "{s},".format(s=tr[2])
            if cell != "":
                cell = cell[:-1]
            new_row.append(cell)
        table.add_row(new_row)

    print(table.draw())


while True:
    entry = input("Enter the id of the automaton you want to display (type 'q' to quit): ")
    if entry == "q":
        break
    auto = next((a for a in automata if a["id"] == entry), None)
    if auto is None:
        print("Automaton not found")
    else:
        display_table(auto)
