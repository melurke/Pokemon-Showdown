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

    for p in range(0, len(pokemon)):
        pokemon[p] = str(pokemon[p])
        pokemon[p] += "\n"

    file = open("pokemon.txt","w")
    file.writelines(pokemon)
    file.close()



    effective = functions.effective(types)

    print("")
    print("")
    print("The following types are very effective:")
    print(effective[0])
    print("")
    print("The following types are effective:")
    print(effective[1])
    print("")
    print("The following types are not very effective:")
    print(effective[2])
    print("")
    print("The following types don't deal any damage:")
    print(effective[3])
    break