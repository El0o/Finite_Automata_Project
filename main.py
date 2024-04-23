# Interface of the software
from FA_files_management import *
from FA_display import *
from FA_operations import *
from FA_checks import *
from FA_recognise import *


def main():
    """
    The main program.
    """

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
            auto = deepcopy(automaton)
            previous_auto = []
            not_done_yet = True
            while not_done_yet:
                # Displaying the automaton, its info and the menu's options
                display_automaton_menu(auto, previous_auto != [])

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
                            str1 = "Completing"
                            str2 = "Completion"
                            if not is_deterministic(auto):
                                str1 = "Determinizing and completing"
                                str2 = "Determinization and completion"
                            print(f"{str1}...\n")
                            previous_auto.append(auto)
                            auto = completion(auto)
                            print(f"{str2} done.\n")

                    case "M":  # Minimization
                        if auto['id'][-1] == "M":
                            print("This automaton has already been minimized.\n")
                        else:
                            str1 = "Minimizing"
                            str2 = "Minimization"
                            if not is_deterministic(auto):
                                str1 = "Determinizing, completing and minimizing"
                                str2 = "Determinization, completion and minimization"
                            elif not is_complete(auto):
                                str1 = "Completing and minimizing"
                                str2 = "Completion and minimization"
                            print(f"{str1}...\n")
                            # previous_auto.append(auto)
                            # auto = minimization(auto)
                            print(f"{str2} done.\n")

                    case "I":  # Building of the complementary automaton
                        print("Building...\n")
                        previous_auto.append(auto)
                        auto = complementary_automaton(auto)
                        print("Complementary automaton built.\n")

                    case "W":  # Word recognition menu
                        print("Entering word recognition...")
                        word_recognition(auto)
                        print("\nExiting word recognition...")

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


print("Launching...")
try:
    main()
except KeyboardInterrupt:
    print("\nGoodbye !")
