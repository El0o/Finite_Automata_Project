# Function to display the tables

from texttable import Texttable
from FA_checks import *


def display_table(automaton):
    """
    Displays a given automaton as a table, with initial states indicated with "⟶" and final states with "⟵" ("⟷" meaning both final & initial)
    """
    table = Texttable()
    table.set_deco(Texttable.HLINES | Texttable.VLINES)
    table.set_chars(['—', '│', '┼', '—'])
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

        state_cell += f"   {state}"
        new_row.append(state_cell)
        for a in automaton["alphabet"]:
            cell = ""
            for tr in automaton["transitions"]:
                if (tr[0] == state) and (tr[1] == a):
                    cell += f"{tr[2]},"
            if cell != "":
                cell = cell[:-1]
            new_row.append(cell)
        table.add_row(new_row)

    print(table.draw())


def display_checks_info(automaton):
    """
    Displays the information
    """
    print(f"\nStandard: {yes_no(is_standard(automaton))}", end="    ")
    print(f"Deterministic: {yes_no(is_deterministic(automaton))}", end="    ")
    print(f"Complete: {yes_no(is_complete(automaton))}", end="    ")
    print("Minimal: ?\n")


def yes_no(boolean):
    """
    Translates a boolean into a comprehensible string
    """
    if boolean:
        return "Yes"
    else:
        return "No "
