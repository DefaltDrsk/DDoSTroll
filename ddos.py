from colorama import Fore
import time

def botnetmamalona():
    print(Fore.CYAN + """

'########::'########:::'#######:::'######:::::'########::'########:::'#######:::::
 ##.... ##: ##.... ##:'##.... ##:'##... ##:::: ##.... ##: ##.... ##:'##.... ##::::
 ##:::: ##: ##:::: ##: ##:::: ##: ##:::..::::: ##:::: ##: ##:::: ##: ##:::: ##::::
 ##:::: ##: ##:::: ##: ##:::: ##:. ######::::: ########:: ########:: ##:::: ##::::
 ##:::: ##: ##:::: ##: ##:::: ##::..... ##:::: ##.....::: ##.. ##::: ##:::: ##::::
 ##:::: ##: ##:::: ##: ##:::: ##:'##::: ##:::: ##:::::::: ##::. ##:: ##:::: ##::::
 ########:: ########::. #######::. ######::::: ##:::::::: ##:::. ##:. #######:::::
........:::........::::.......::::......::::::..:::::::::..:::::..:::.......::::::
""")
    ddos = input("Pon la IP o pagina: " + Fore.RESET)

    try:
        while True:
            time.sleep(0.5)
            print(Fore.GREEN + "Mandando ataque al objetivo: " + ddos)
    except KeyboardInterrupt:
                            (Fore.RED + "\nSaliendo...")
botnetmamalona()

