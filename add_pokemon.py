import ast

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
    evs = [0, 0, 0, 0, 0, 0]
    for i in range(0, num_of_types):
        types.append(input(f"Input the {i+1}. type of the pokemon: ").upper())
    for i in range(0, 6):
        stats.append(int(input(f"Input the {i+1}. stat of the pokemon: ")))

    pokemon.append([name, types, stats, evs])
else:
    print("The pokemon has already been registered.")

for p in range(0, len(pokemon)):
    pokemon[p] = str(pokemon[p])
    pokemon[p] += "\n"
file = open("pokemon.txt","w")
file.writelines(pokemon)
file.close()
