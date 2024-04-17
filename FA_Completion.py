from FA_lst import automata


def completion(Autom):
    Ac = automata[Autom]
    # Creation of a list that will keep track of which state we need to add
    P = []
    # Research of which states needs to be added

    for j in range(len(Ac['states'])):
        P.append([])
        for i in Ac['transitions']:
            if i[0] == Ac['states'][j] and i[1] in Ac['alphabet']:
                P[j].append(i[1])

        # organisation of the transition that will be added
        # We start with a list that will keep track of the initial state and the letter of the transition

    for k in range(len(P)):
        p = []
        for m in Ac['alphabet']:
            if m not in P[k]:
                p.append(m)
        P[k] = p
        f = str(k)
        P[k].append(f)
        P[k].reverse()

        # Finally we create the new transitions,
        # the ones that start with an existing state and the ones that comes from P

    add = []
    for n in range(len(P)):
        toadd = ""
        for l in range(1, len(P[n])):
            toadd = P[n][0]
            toadd = toadd + P[n][l]
            toadd = toadd + "P"
            add.append(toadd)

    for o in Ac['alphabet']:
        toadd = "P" + o + "P"
        add.append(toadd)

        # We update our automaton

    Ac['transitions'] = Ac['transitions'] + add
    Ac['states'].append("P")
    return Ac
