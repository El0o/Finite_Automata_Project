from FA_operations import *
from FA_checks import *
from FA_files_management import *
from FA_lst import automata


for i in range(44):
    auto = automata[i]
    if not is_standard(auto):
        export_automaton(standardization(auto))
    if not is_deterministic(auto):
        export_automaton(determinization(auto))
    if not is_complete(auto):
        export_automaton(completion(auto))
    export_automaton(complementary_automaton(auto))
    export_automaton(minimization(auto)[0])
