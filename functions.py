from pyautogui import press, write, click
from time import sleep
from random import randint

def abrir_ea_app():
    # abrir opera
    press('win');sleep(0.1)
    write('opera gx', interval=0.05)
    press('enter');sleep(5)

    # abrir ea app
    click(354, 54);sleep(0.1)
    write("https://www.ea.com/ea-sports-fc/ultimate-team/web-app/", interval=0.05);sleep(0.1)
    press('enter');sleep(20) # carregar a login page
    click(1359, 636);sleep(15) # clicar em login
    click(121, 88);sleep(5) # pale tools
    click(96, 336);sleep(5) # clicar em sbc
    click(700, 201);sleep(5) # clicar em favoritos

def fazer_dme():
    click(769, 402);sleep(randint(4, 8)) # clicar no dme
    click(1651, 650);sleep(randint(4, 7)) # clicar em template
    click(1364, 1005);sleep(randint(2, 6)) # clicar em submit
    click(984, 763);sleep(3) # claim rewards

def fechar_ea_app():
    click(1899, 13);sleep(5)

def abrir_its_over_page():
    click(354, 54);sleep(0.1)
    write("https://i.imgur.com/kAVivzu.png", interval=0.05);sleep(0.1)
    press('enter')
