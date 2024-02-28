import pyautogui
import webbrowser
import random

roullet = random.randint(1, 6)

# Desing
print('=========  YOUR RESULT =========')
print(roullet)

# Check the roulette result
if roullet == 6:
    print('OK, now say goodbye to your dignity.')

    # put a link to something they should search for
    webbrowser.open('https://github.com/fkcoffe')

    # Wait a short period of time for the page to load
    pyautogui.PAUSE = 3



# Desing
print('=========================================')

