# Interface of the software
from FA_files_management import *
from FA_display import *

print("Launching...")
automata = import_all_automata()
print("\n\nWelcome to the Finite Automata Toolbox !")

while True:
    entry = input("\nPlease enter the id of the automaton you want to work on (type [q] to quit): ")
    if entry == "q" or entry == "Q":
        print("Goodbye !")
        break
    auto = next((a for a in automata if a["id"] == entry), None)
    if auto is None:
        print("Automaton not found :/")
    else:
        print("Automaton n°{id}:".format(id=auto["id"]))
        display_table(auto)
        print("\nStandard: {ans}".format(ans="?"), end="    ")
        print("Complete: {ans}".format(ans="?"), end="    ")
        print("Deterministic: {ans}".format(ans="?"), end="    ")
        print("Minimal: {ans}".format(ans="?"))

        _ = input("\nSoon : menu with what you can do (press [Enter ↵] to return to main menu)")
