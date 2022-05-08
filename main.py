import ast
from attr import has
import functions

team = []
total_damage_dealt = [0, 0, 0, 0, 0, 0]
hps = [0, 0, 0, 0, 0, 0]
physical_attacks = [0, 0, 0, 0, 0, 0]
physical_defenses = [0, 0, 0, 0, 0, 0]
special_attacks = [0, 0, 0, 0, 0, 0]
special_defenses = [0, 0, 0, 0, 0, 0]
speeds = [0, 0, 0, 0, 0, 0]

our_team = ["Ditto", "Zacian", "Zapdos", "Landorus-Therian", "Kyogre", "Grimmsnarl"]
our_used_pokemon = ast.literal_eval(input("Which pokemon are you choosing? "))
total_damage = [0, 0, 0, 0, 0, 0]
our_hps = [155, 195, 165, 165, 175, 202]
our_physical_attacks = [61, 244, 85, 197, 94, 125]
our_physical_defenses = [68, 135, 105, 110, 111, 122]
our_special_attacks = [68, 90, 177, 112, 202, 103]
our_special_defenses = [68, 135, 111, 100, 160, 101]
our_speeds = [110, 173, 167, 157, 156, 81]

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
    enemy_hp = int(input("How much hp does your enemy have? "))/100
    
    if not name in team:
        team.append(name)

    names = []

    for p in pokemon:
        names.append(p[0])

    if not name in names:
        num_of_types = int(input("How many types does the pokemon have? "))
        types = []
        stats = []
        evs = [0, 0, 0, 0, 0, 0]
        for i in range(0, num_of_types):
            types.append(input(f"Input the {i+1}. type of the pokemon: ").upper())
        for i in range(0, 6):
            stats.append(int(input(f"Input the {i+1}. stat of the pokemon: ")))

        pokemon.append([name, types, stats, evs])
        index = -1
    else:
        for p in range(0, len(pokemon)):
            if pokemon[p][0] == name:
                type = pokemon[p][1]
                stats = pokemon[p][2]
                evs = pokemon[p][3]
                index = p

    print(pokemon[index])
    pokemon_list = pokemon.copy()
    types = pokemon[index][1]
    stats = pokemon[index][2]
    evs = pokemon[index][3]

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
    print("")
    print("")

    our_pokemon = input("Which pokemon are you using? ")

    if our_pokemon in ["Zapdos", "Landorus-Therian", "Grimmsnarl"]:
        has_status_moves = True
    else:
        has_status_moves = False

    for pokemon in pokemon_list:
        if pokemon[0] == our_pokemon:
            our_types = pokemon[1]
            our_base_stats = pokemon[2]
            our_evs = pokemon[3]

    our_stats = [our_hps[our_team.index(our_pokemon)], our_physical_attacks[our_team.index(our_pokemon)], our_physical_defenses[our_team.index(our_pokemon)], our_special_attacks[our_team.index(our_pokemon)], our_special_attacks[our_team.index(our_pokemon)], our_speeds[our_team.index(our_pokemon)]]

    used_light_screen = 0
    used_reflect = 0
    used_stealth_rock = 0
    has_status_effect = 0
    if "Grimmsnarl" in our_used_pokemon:
        used_reflect = input("Is reflect currently active? ")
        used_light_screen = input("Is light screen currently active? ")
    if "Landorus-Therian" in our_used_pokemon:
        used_stealth_rock = input("Is stealth rock currently active? ")
    if "Grimmsnarl" in our_used_pokemon or "Kyogre" in our_used_pokemon or "Zapdos" in our_used_pokemon:
        has_status_effect = input("Does your opponent have any status effect? ")
    if used_reflect == "1":
        used_reflect = True
    else:
        used_reflect = False
    if used_light_screen == "1":
        used_light_screen = True
    else:
        used_light_screen = False
    if used_stealth_rock == "1":
        used_stealth_rock = True
    else:
        used_stealth_rock = False
    if has_status_effect == "1":
        has_status_effect = True
    else:
        has_status_effect = False

    our_physical_attack_multiplier = float(input("What is your physical attack multiplier? "))
    our_special_attack_multiplier = float(input("What is your special attack multiplier? "))
    physical_defense_multiplier = float(input("What is your opponents physical defense mulitplier? "))
    special_defense_multiplier = float(input("What is your opponents special defense multiplier? "))

    file = open("our_moves.txt","r")
    our_moves = file.readlines()
    file.close()

    for p in our_moves:
        try:
            p.replace("\n", "")
        except:
            pass

    for i in range(0, len(our_moves)):
        our_moves[i] = ast.literal_eval(our_moves[i])

    if has_status_effect:
        our_moves[our_moves.index(["Ice Beam", 90, 1, "ICE", "SPECIAL", 1.2, ["Kyogre"]])][-2] = 1
        our_moves[our_moves.index(["Scald", 80, 1, "WATER", "SPECIAL", 1.15, ["Kyogre"]])][-2] = 1

    legal_moves = []
    for move in our_moves:
        if our_pokemon in move[-1]:
            legal_moves.append(move)

    damages = []
    stab_attacks = []
    type_attacks = []
    others_attacks = []
    theoretical_damages = []
    move_values = []
    others = float(input("What are the other factors (number)? "))
    weather = input("What is the weather? ").upper()
    hp = functions.base_hp(stats[0])
    real_hp = hp * enemy_hp

    for move in our_moves:
        attacking_pokemon = move[-1]
        for pokemon in attacking_pokemon:
            for p in pokemon_list:
                if p[0] == pokemon:
                    attributes = p
            if not move in legal_moves:
                others = 1

                if weather == "RAINY":
                    if move[3] == "WATER":
                        others *= 1.5
                    if move[3] == "FIRE":
                        others *= 0.5
                elif weather == "SUNNY":
                    if move[3] == "WATER":
                        others *= 0.5
                    if move[3] == "FIRE":
                        others *= 1.5

                if move[3] in attributes[1]:
                    stab = 1.5
                else:
                    stab = 1
                
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
                
                stab_attacks.append(stab)
                type_attacks.append(type)
                others_attacks.append(others)
                if move[4] == "SPECIAL":
                    damages.append(functions.damage(functions.base_ev(attributes[2][1], our_evs[1]), functions.base_ev(stats[2], evs[2])*special_defense_multiplier, stab, type, others, move[1])[0])
                elif move[4] == "PHYSICAL":
                    damages.append(functions.damage(functions.base_ev(attributes[2][3], our_evs[3]), functions.base_ev(stats[4], evs[4])*physical_defense_multiplier, stab, type, others, move[1])[0])
                elif move[4] == "STATUS":
                    damages.append(0)
                else:
                    print("Couldn't find type for the attack: " + move[0])

                theoretical_damages.append(damages[-1]/real_hp)
            else:
                others = 1

                if weather == "RAINY":
                    if move[3] == "WATER":
                        others *= 1.5
                    if move[3] == "FIRE":
                        others *= 0.5
                elif weather == "SUNNY":
                    if move[3] == "WATER":
                        others *= 0.5
                    if move[3] == "FIRE":
                        others *= 1.5

                if move[3] in our_types:
                    stab = 1.5
                else:
                    stab = 1
                
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
                
                stab_attacks.append(stab)
                type_attacks.append(type)
                others_attacks.append(others)
                if move[4] == "SPECIAL":
                    damages.append(functions.damage(functions.base_ev(our_stats[1], our_evs[1])*our_special_attack_multiplier, functions.base_ev(stats[2], evs[2])*special_defense_multiplier, stab, type, others, move[1])[0])
                elif move[4] == "PHYSICAL":
                    damages.append(functions.damage(functions.base_ev(our_stats[3], our_evs[3])*our_physical_attack_multiplier, functions.base_ev(stats[4], evs[4])*physical_defense_multiplier, stab, type, others, move[1])[0])
                elif move[4] == "STATUS":
                    damages.append(0)
                else:
                    print("Couldn't find type for the attack: " + move[0])

                theoretical_damages.append(damages[-1]/real_hp)

    for move in our_moves:
        if functions.can_do_move(our_used_pokemon, move):
            if move[0] == "Reflect" and used_reflect:
                move_values.append(0)
            elif move[0] == "Light Screen" and used_light_screen:
                move_values.append(0)
            elif move[0] == "Stealth Rock" and used_stealth_rock:
                move_values.append(0)
            elif move[0] == "Thunder Wave" and has_status_effect:
                move_values.append(0)
            else:
                if move in legal_moves:
                    move_values.append((((damages[our_moves.index(move)]/hp)*0.77)+1)*move[5])
                else:
                    move_values.append(((((damages[our_moves.index(move)]/hp)*0.77)+1)*move[5])/2)
        else:
            move_values.append(0)

    attack = our_moves[move_values.index(max(move_values))]
    print(attack)

    stab = stab_attacks[damages.index(max(damages))]
    type = type_attacks[damages.index(max(damages))]
    others = others_attacks[damages.index(max(damages))]
    print(attack[0] + ": " + str(max(move_values)))
    print(move_values)

    damage = float(input("How much damage did you deal? "))
    total_damage_dealt[team.index(name)] += damage
    crit = int(input("Did you do a critical hit (1 or 0)? "))
    if crit == 1:
        real_damage = damage*hp/1.5
    else:
        real_damage = damage*hp

    if attack[4] == "PHYSICAL":
        physical_defenses[team.index(name)] = int(functions.defense(real_damage, our_stats[1]*our_physical_attack_multiplier, stab, type, others, attack[1]))
        print("Enemy's physical defense: " + str(physical_defenses[team.index(name)]))
    elif attack[4] == "SPECIAL":
        special_defenses[team.index(name)] = int(functions.defense(real_damage, our_stats[1]*our_special_attack_multiplier, stab, type, others, attack[1]))
        print("Enemy's special defense: " + str(special_defenses[team.index(name)]))

    if False:
        legal_moves = []
        for move in our_moves:
            if our_pokemon in move[-1]:
                legal_moves.append(move)
        damages = []
        stab_attacks = []
        type_attacks = []
        others_attacks = []
        for move in legal_moves:
            others = 1

            if weather == "RAINY":
                if move[3] == "WATER":
                    others *= 1.5
                if move[3] == "FIRE":
                    others *= 0.5
            elif weather == "SUNNY":
                if move[3] == "WATER":
                    others *= 0.5
                if move[3] == "FIRE":
                    others *= 1.5

            if move[3] in our_types:
                stab = 1.5
            else:
                stab = 1
            
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
            
            stab_attacks.append(stab)
            type_attacks.append(type)
            others_attacks.append(others)
            if move[4] == "SPECIAL":
                damages.append(functions.damage(our_stats[1]*our_special_attack_multiplier, special_defenses[team.index(name)]*special_defense_multiplier, stab, type, others, move[1])[0])
            elif move[4] == "PHYSICAL":
                damages.append(functions.damage(our_stats[1]*our_physical_attack_multiplier, physical_defenses[team.index(name)]*physical_defense_multiplier, stab, type, others, move[1])[0])
            elif move[4] == "STATUS":
                damages.append(0)
            else:
                print("Couldn't find type for the attack: " + move[0])

        attack = legal_moves[damages.index(max(damages))]
        stab = stab_attacks[damages.index(max(damages))]
        type = type_attacks[damages.index(max(damages))]
        others = others_attacks[damages.index(max(damages))]
        print(attack[0] + ": " + str(int(max(damages))/hp))



    if functions.end_game(total_damage, total_damage_dealt):
        break
    break
