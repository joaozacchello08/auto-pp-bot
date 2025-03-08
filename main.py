from time import sleep
from functions import abrir_ea_app, fazer_dme, fechar_ea_app, abrir_its_over_page

while True:
    print("eae dog, bora fazer dme")
    qtde_dmes = int(input("quantos dmes vc quer fazer? "))
    already_completed_dmes = 0

    # se o cara n digitar nada
    if qtde_dmes == 0:
        print("vsf entao pae")
        sleep(3)
        break

    abrir_ea_app()

    print()

    for i in range(qtde_dmes):
        if i == 14: # antisoftban
            fechar_ea_app()
            abrir_ea_app()

        fazer_dme()
        already_completed_dmes += 1

        print(f"ja fez {already_completed_dmes} dmes")

        if already_completed_dmes == qtde_dmes:
            abrir_its_over_page()

    quit_msg = input("\ndeseja continuar? (s/n)")
    if quit_msg != "s":
        print()
        continue
    else:
        break
