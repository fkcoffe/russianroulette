import pyautogui
import webbrowser
import random

roleta = random.randint(1, 6)

# Desenho
print('=========  SEU RESULTADO =========')
print(roleta)

# Verifica o resultado da roleta
if roleta == 6:
    print('OK, agora diga adeus a sua dignidade.')

    # Abre um navegador da web e faz uma pesquisa
    webbrowser.open('https://github.com/fkcoffe')

    # Aguarda um curto período de tempo para a página carregar
    pyautogui.PAUSE = 3



# Desenho
print('=========================================')

