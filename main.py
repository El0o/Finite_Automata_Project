# Interface of the software
from FA_files_management import *
from FA_display import *
from FA_operations import *
from FA_checks import *


def main():
    """
    The main program.
    """
    print("Launching...")
    # Importing the automata from the text files
    automata = import_all_automata()

    while True:
        # Main menu (automaton selection)
        print("\n\nWelcome to the Finite Automata Toolbox !")
        entry = input("\nPlease enter the id of the automaton you want to work on (type [Q] to quit)\n\n>> ").upper()

        if entry == "RESET":  # To reset the content of the automata folder
            print("Do you really want to reset the automata folder ? Only the test automata given for the project will be kept. (y/n)")
            entry = input(">> ").upper()
            if entry == "Y" or entry == "YES":
                reset_automata_folder()
                print("Operation successful. Please restart the program.")
                break
            else:
                print("Operation aborted. Please restart the program.")
                break

        if entry == "Q":
            # End of program
            print("Goodbye !")
            break

        automaton = get_automaton(automata, entry)
        if automaton is None:
            print("Automaton not found :/")
        else:
            # Automaton menu
            auto = automaton.copy()
            previous_auto = []
            not_done_yet = True
            while not_done_yet:
                # Displaying the automaton, its info and the menu's options
                print(f"Automaton n°{auto['id']}:\n")
                display_table(auto)
                display_checks_info(auto)

                print("[S] - Standardize this automaton          ", end="  ")
                print("[D] - Determinize this automaton          ")
                print("[C] - Complete this automaton             ", end="  ")
                print("[M] - Minimize this automaton             ")
                print("[I] - Build the complementary automaton   ", end="  ")
                print("[W] - Enter word recognition mode         ")
                print("[T] - Export this automaton in a text file", end="  ")
                if previous_auto != []:
                    print("[P] - Return to previous automaton        ")
                print("[R] - Return to automaton selection       ")

                while True:
                    entry = input("\n>> ").upper()
                    if entry in ["S", "D", "C", "M", "I", "W", "T", "R", "P"]:
                        break
                    print("Statement not recognized. Please type one of the above letter to do something.")

                match entry:
                    case "S":  # Standardization
                        if is_standard(auto):
                            print("This automaton is already standard.\n")
                        else:
                            print("Standardizing...\n")
                            previous_auto.append(auto)
                            auto = standardization(auto)
                            print("Standardization done.\n")

                    case "D":  # Determinization
                        if is_deterministic(auto):
                            print("This automaton is already deterministic.\n")
                        else:
                            print("Determinazing...\n")
                            previous_auto.append(auto)
                            auto = determinization(auto)
                            print("Determinazation done.\n")

                    case "C":  # Completion
                        if is_complete(auto):
                            print("This automaton is already complete.\n")
                        else:
                            print("Completing...\n")
                            previous_auto.append(auto)
                            auto = completion(auto)
                            print("Completion done.\n")

                    case "M":  # Minimization
                        print("Minimization stuff")  # Fonctions en cours de développement

                    case "I":  # Building of the complementary automaton
                        print("Complementary stuff")  # Fonctions en cours de développement

                    case "W":  # Word recognition menu
                        print("Word recognition stuff")  # À faire

                    case "T":  # Text file creation
                        if fond_txt(auto):
                            print("Automaton's text file already exists.\n")
                        else:
                            export_automaton(auto)
                            if get_automaton(automata, auto["id"]) is None:
                                automata.append(auto)

                    case "R":  # What needs to be done before coming back to main menu
                        # First, ask for every previous & current automaton if they need to be saved
                        for unsaved in reversed(previous_auto + [auto]):
                            if not fond_txt(unsaved):
                                while True:
                                    entry = input(f"Do you want to save automaton n°{unsaved['id']} ? (y/n)\n>> ").upper()
                                    if entry == "Y" or entry == "YES":
                                        export_automaton(unsaved)
                                        if get_automaton(automata, unsaved["id"]) is None:
                                            automata.append(unsaved)
                                        break
                                    elif entry == "N" or entry == "NO":
                                        break
                                    else:
                                        print("Statement not recognized. Please type [Y] or [N].")
                        # Then quit the automaton menu
                        not_done_yet = False

                    case "P":  # What needs to be done before going back to the previous automaton
                        # If no previous automaton, does nothing
                        if previous_auto != []:
                            # Asking first if the current automaton needs to be saved
                            if not fond_txt(auto):
                                while True:
                                    entry = input(f"Do you want to save automaton n°{auto['id']} ? (y/n)\n>> ").upper()
                                    if entry == "Y" or entry == "YES":
                                        export_automaton(auto)
                                        if get_automaton(automata, auto["id"]) is None:
                                            automata.append(auto)
                                        break
                                    elif entry == "N" or entry == "NO":
                                        break
                                    else:
                                        print("Statement not recognized. Please type [Y] or [N].")
                            # Going back to the previous automaton
                            auto = previous_auto[-1]
                            previous_auto.pop()


try:
    main()
except KeyboardInterrupt:
    print("\nGoodbye !")
