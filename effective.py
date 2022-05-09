import ast
import functions

file = open("pokemon.txt","r")
pokemon = file.readlines()
file.close()

for p in pokemon:
    try:
        p.replace("\n", "")
    except:
        pass

for i in range(0, len(pokemon)):
    pokemon[i] = ast.literal_eval(pokemon[i])

opponent = input("Which pokemon does your opponent use? ")

for p in pokemon:
    if p[0] == opponent:
        types = p[1]

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
