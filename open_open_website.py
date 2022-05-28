import pyautogui
import ast
import time

name = input("Pokemon: ")

pyautogui.click(1780, 40)
pyautogui.moveTo(1830, 80)
pyautogui.dragTo(1730, 80, 0.2, button='left')
pyautogui.click(730, 380)

for letter in list("& python_path 'program_path'"):
    pyautogui.press(letter)
pyautogui.press('enter')

time.sleep(1)
for p in list(name):
    pyautogui.press(p)
pyautogui.press('enter')
all_stats = input("Stats: ")
all_stats = "['" + all_stats.replace(" ", "', '").replace("\t", "', '") + "']"
all_stats = ast.literal_eval(all_stats)
all_stats.remove(all_stats[-7])

types = []
stats = []

for s in all_stats:
    try:
        test = int(s)
        stats.append(int(s))
    except:
        types.append(s)

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

names = []
for p in pokemon:
    names.append(p[0])

if not name in names:
    pokemon.append([name, types, stats, [0, 0, 0, 0, 0, 0]])
else:
    print("The pokemon has already been registered.")

for p in range(0, len(pokemon)):
    pokemon[p] = str(pokemon[p])
    pokemon[p] += "\n"
file = open("pokemon.txt","w")
file.writelines(pokemon)
file.close()
