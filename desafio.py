# Importações de bibliotecas necessarias para o desafio
import pyautogui 
import webbrowser
import time

# Variavel para amazenar o nome
nome = pyautogui.prompt(text='Digite seu nome')

# Abrir o navegador no site espesifico
webbrowser.open(' https://cursoautomacao.netlify.app/')
time.sleep(2)

# Click na tela do navegador e rola para baixo
pyautogui.moveTo(570,285, duration=2)
pyautogui.scroll(-620)
time.sleep(2)

# Encontra a local para digita o nome
nome_alerta = pyautogui.locateCenterOnScreen('nome_alerta.png')
pyautogui.click(nome_alerta)
pyautogui.typewrite(nome)
time.sleep(2)

# Click no alerta
alerta = pyautogui.locateCenterOnScreen('alerta.png')
pyautogui.click(alerta)
time.sleep(2)
pyautogui.hotkey('Enter')

# Subir tela
time.sleep(0.5)
pyautogui.scroll(630)

# Secção de downloand
time.sleep(0.5)
pyautogui.scroll(-2000)

# Excel
pyautogui.click(172,407, duration=2)

# PDF
pyautogui.click(378,405, duration=2)

time.sleep(2)
pyautogui.alert(text='Você terminou!')
