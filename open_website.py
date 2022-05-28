import webbrowser
import pyautogui
import time

pokemon = input("Pokemon: ").lower()
pokemon = list(pokemon)

webbrowser.open_new('https://pokemondb.net/pokedex/all')
time.sleep(2)

pyautogui.click(900, 570)
for letter in pokemon:
    pyautogui.press(letter)
time.sleep(1)

pyautogui.moveTo(670, 680)
pyautogui.dragTo(1540, 680, 3, button='left')

pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1000, 50)
pyautogui.hotkey('ctrl', 'v')
pyautogui.dragTo(100, 50, 2, button='left')
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'w')

pyautogui.click(1500, 500)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)
pyautogui.press('enter')
