import ast
import functions

while True:
    index = 0

    file = open("pokemon.txt", "r")
    pokemon = file.readlines()
    file.close()

    for p in pokemon:
        try:
            p.replace("\n", "")
        except:
            pass

    for i in range(0, len(pokemon)):
        pokemon[i] = ast.literal_eval(pokemon[i])

    name = input("Input your opposing pokemon: ")

    names = []

    for p in pokemon:
        names.append(p[0])

    if not name in names:
        num_of_types = int(input("How many types does the pokemon have? "))
        types = []
        stats = []
        for i in range(0, num_of_types):
            types.append(input(f"Input the {i+1}. type of the pokemon: ").upper())
        for i in range(0, 6):
            stats.append(int(input(f"Input the {i+1}. stat of the pokemon: ")))

        pokemon.append([name, types, stats])
        index = -1
    else:
        for p in range(0, len(pokemon)):
            if pokemon[p][0] == name:
                type = pokemon[p][1]
                stats = pokemon[p][2]
                index = p

    print(pokemon[index])
    types = pokemon[index][1]
    stats = pokemon[index][2]
    pokemons = pokemon.copy()

    for p in range(0, len(pokemon)):
        pokemon[p] = str(pokemon[p])
        pokemon[p] += "\n"

    file = open("pokemon.txt","w")
    file.writelines(pokemon)
    file.close()



    effective = functions.effective(types)

    print("")
    print("")
    print("The following types are super effective:")
    print(effective[0])
    print("")
    print("The following types are very effective:")
    print(effective[1])
    print("")
    print("The following types are effective:")
    print(effective[2])
    print("")
    print("The following types are not very effective:")
    print(effective[3])
    print("")
    print("The following types are not at all effective:")
    print(effective[4])
    print("")
    print("The following types don't deal any damage:")
    print(effective[5])

    file = open("our_moves.txt","r")
    moves = file.readlines()
    file.close()
    damages = []

    for p in moves:
        try:
            p.replace("\n", "")
        except:
            pass

    for i in range(0, len(moves)):
        moves[i] = ast.literal_eval(moves[i])

    weather = input("What is the weather? ").upper()

    our_pokemon = input("What pokemon are you using? ")
    our_physical_attack_multiplier = float(input("What is your physical attack multiplier? "))
    our_special_attack_multiplier = float(input("What is your special attack multiplier? "))
    physical_defense_multiplier = float(input("What is your opponents physical defense multiplier? "))
    special_defense_multiplier = float(input("What is your opponents special defense multiplier? "))
    
    for p in range(0, len(pokemons)):
        if our_pokemon == pokemons[p][0]:
            our_types = pokemons[p][1]
            our_stats = pokemons[p][2]

    our_attack = our_stats[1]

    stab = 1
    type = 1
    others = float(input("What are the other modifiers (number): "))
    other = others
    legal_moves = []
    for move in moves:
        if our_pokemon in move[-1]:
            legal_moves.append(move)
    for move in legal_moves:
        others = other
        if move[3] in effective[0]:
            type = 4
        elif move[3] in effective[1]:
            type = 2
        elif move[3] in effective[2]:
            type = 1
        elif move[3] in effective[3]:
            type = 0.5
        elif move[3] in effective[4]:
            type = 0.25
        else:
            type = 0

        if weather == "RAINY" or weather == "RAIN":
            if move[3] == "WATER":
                others *= 1.5
            elif move[3] == "FIRE":
                others *= 0.5
        elif weather == "SUNNY":
            if move[3] == "WATER":
                others *= 0.5
            elif move[3] == "FIRE":
                others *= 1.5

        if move[3] in our_types:
            stab = 1.5
        else:
            stab = 1
        
        if move[4] == "PHYSICAL":
            damages.append(functions.damage(our_stats[1]*our_physical_attack_multiplier, stats[1]*physical_defense_multiplier, stab, type, others, move[1])[0])
        elif move[4] == "SPECIAL":
            damages.append(functions.damage(our_stats[1]*our_special_attack_multiplier, stats[1]*special_defense_multiplier, stab, type, others, move[1])[0])
        else:
            damages.append(0)

    move = legal_moves[damages.index(max(damages))]

    if move[3] in effective[0]:
        type = 4
    elif move[3] in effective[1]:
        type = 2
    elif move[3] in effective[2]:
        type = 1
    elif move[3] in effective[3]:
        type = 0.5
    elif move[3] in effective[4]:
        type = 0.25
    else:
        type = 0

    others = other

    if weather == "RAINY" or weather == "RAIN":
        if move[3] == "WATER":
            others *= 1.5
        elif move[3] == "FIRE":
            others *= 0.5
    elif weather == "SUNNY":
        if move[3] == "WATER":
            others *= 0.5
        elif move[3] == "FIRE":
            others *= 1.5

    if move[3] in our_types:
        stab = 1.5
    else:
        stab = 1

    print(legal_moves)
    print(damages)
    print("")
    print(move[0])
    print(max(damages))
    print("")

    damage = float(input("How much damage did you deal? "))/100
    hp = functions.base_hp(stats[0])
    schaden = hp*damage
    defense = int(functions.defense(schaden, our_attack, stab, type, others, move[1]))
    print(defense)

    break
