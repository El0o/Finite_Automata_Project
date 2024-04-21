# Function to display the tables

from texttable import Texttable
from FA_checks import *


def get_table(automaton):
    """
    Returns the given automaton as a table, with initial states indicated with "⟶" and final states with "⟵" ("⟷" meaning both final & initial)
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

    return table.draw()


def yes_no(boolean):
    """
    Translates a boolean into a comprehensible string
    """
    if boolean:
        return "Yes."
    else:
        return "No."


def get_checks_info(automaton):
    """
    Returns the checks outputs for the given automaton
    """

    ans = is_standard(automaton, 1)
    info = f"Standard: {yes_no(ans[0])} {ans[1]}\n\n"

    ans = is_deterministic(automaton, 1)
    info += f"Deterministic: {yes_no(ans[0])} {ans[1]}\n\n"

    ans = is_complete(automaton, 1)
    info += f"Complete: {yes_no(ans[0])} {ans[1]}"

    return info


def display_automaton_menu(automaton, previous):
    """
    Configures the display of the table on one side and the checks information on the other
    """
    displayer = Texttable()
    displayer.set_deco(Texttable.BORDER)
    displayer.set_chars([' ', ' ', ' ', ' '])
    displayer.set_header_align(["l", "l"])
    displayer.set_cols_valign(["m", "m"])
    displayer.set_max_width(0)

    displayer.header([f"Automaton n°{automaton['id']}:\n", " "])

    menu_options  = "[S] - Standardize this automaton            "
    menu_options += "[D] - Determinize this automaton          \n"
    menu_options += "[C] - Complete this automaton               "
    menu_options += "[M] - Minimize this automaton             \n"
    menu_options += "[I] - Build the complementary automaton     "
    menu_options += "[W] - Enter word recognition mode         \n"
    menu_options += "[T] - Export this automaton in a text file  "
    if previous:
        menu_options += "[P] - Return to previous automaton        \n"
    menu_options += "[R] - Return to automaton selection       "

    col2 = get_checks_info(automaton) + "\n\n\n\n" + menu_options

    displayer.add_row([get_table(automaton), col2])

    print(displayer.draw())


