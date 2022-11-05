# Libraries
import time
import os
import openai
import pathlib

# Colors
class colors:
    HEADER = '\033[1;35m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKCYANL = '\033[1;36m'
    OKGREEN = '\033[92m'
    OKGREENL = '\033[1;32m' 
    OKREDL = '\033[1;31m' 
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# API OpenAI
openai.api_key = ""

# Functions
def banner():
    clear()
    print(colors.OKREDL  + """

▀█████████▄   ▄██████▄   ▄██████▄     ▄█   ▄█▄    ▄████████ ▄██   ▄   
  ███    ███ ███    ███ ███    ███   ███ ▄███▀   ███    ███ ███   ██▄ 
  ███    ███ ███    ███ ███    ███   ███▐██▀     ███    █▀  ███▄▄▄███ 
 ▄███▄▄▄██▀  ███    ███ ███    ███  ▄█████▀      ███        ▀▀▀▀▀▀███ 
▀▀███▀▀▀██▄  ███    ███ ███    ███ ▀▀█████▄    ▀███████████ ▄██   ███ 
  ███    ██▄ ███    ███ ███    ███   ███▐██▄            ███ ███   ███ 
  ███    ███ ███    ███ ███    ███   ███ ▀███▄    ▄█    ███ ███   ███ 
▄█████████▀   ▀██████▀   ▀██████▀    ███   ▀█▀  ▄████████▀   ▀█████▀  
                                     ▀                                   
    """ + colors.ENDC)
    print(colors.WARNING + "Booksy (Books Summary) v.1.0 - Resúmenes de libros hechos por una IA | " + colors.OKGREEN + "Autor: " + colors.WARNING + "pablokbg | " + colors.OKGREEN + "Página web: " + colors.WARNING + "https://pablokbg.com\n" + colors.ENDC)

def progress():
    banner()
    print("[" + colors.WARNING + "*" + colors.ENDC + "] Enviando petición ...")
    time.sleep(3)
    
def clear():
    os.system("cls")

def end():
    banner()
    print("[" + colors.OKGREEN + "✓" + colors.ENDC + "] Petición finalizada.")
    time.sleep(3)

def error():
    banner()
    print("[" + colors.FAIL + "x" + colors.ENDC + "] Error, no se esperaba esa respuesta.")

def exit():
    banner()
    exit=input("[" + colors.HEADER + "?" + colors.ENDC + "] Deseas salir de Booksy [S/N]: ")
    exit=exit.upper()

    if exit == "S":
        clear()
        banner()
        print("[" + colors.WARNING + "*" + colors.ENDC + "] Saliendo ...")
        time.sleep(3)
        
    elif exit == "N":
        clear()
        banner()
        print("[" + colors.WARNING + "*" + colors.ENDC + "] Volviendo al menu ...")
        time.sleep(3)
        clear()
        main()
    else:
        clear()
        banner()
        error()
     
def main():
    banner()
    topic=input("[" + colors.OKCYAN + ">" + colors.ENDC + "] Introduce el título del libro a resumir: ")
    clear()

    # Send request
    progress()
    clear()

    # Request OpenAI
    response=openai.Completion.create(
    model="text-davinci-002",
    prompt="Quiero que me resumas el libro de " + topic,
    temperature=0.6,
    max_tokens=400,
    top_p=1,
    frequency_penalty=1,
    presence_penalty=1
    )

    # Format request
    answer= response.choices[0].text.strip()
    
    # End request
    end()
    clear()

    banner()
    print(colors.UNDERLINE + "Resumen:" + colors.ENDC)
    print("\n" + answer + "\n")

    def save():
        save=input("[" + colors.HEADER + "?" + colors.ENDC + "] Quieres guardar el resumen del libro " + colors.BOLD + colors.OKREDL + topic + colors.ENDC + " en un archivo .txt [S/N]: ")
        save=save.upper()

        match save:
            case "S":
                clear()
                banner()
                print("[" + colors.WARNING + "*" + colors.ENDC + "] Guardando ...")
                time.sleep(3)
                pathlib.Path(topic + ".txt").write_text(answer)
                clear()
                exit()
            case "N":
                clear()
                exit()
            case _:
                clear()
                error()
    
    save()

# Booksy
main()








