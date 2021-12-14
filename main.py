#Made By zSkiddoh
#Date Creation: 14/12/2021

import requests
import time
import os
import colorama
from colorama import Fore

os.system('cls')

class colores:
    Red          = "\033[31m"
    Green        = "\033[32m"
    Blue         = "\033[34m"
    White        = "\033[97m"

print()
username = input('\033[32m{+} Introduzca nombre de usuario: \033[97m')
os.system("cls")

#1
instagram = f'https://www.instagram.com/{username}'

#2
facebook = f'https://www.facebook.com/{username}'

#3
twitter = f'https://www.twitter.com/{username}'

#4
youtube = f'https://www.youtube.com/{username}'

#5
blogger = f'https://{username}.blogspot.com'

#6
reddit = f'https://www.reddit.com/user/{username}'

#7
wordpress = f'https://{username}.wordpress.com'

#8
pinterest = f'https://www.pinterest.com/{username}'

#9
github = f'https://www.github.com/{username}'

#10
tumblr = f'https://{username}.tumblr.com'

#11
steam = f'https://steamcommunity.com/id/{username}'

#12
soundcloud = f'https://soundcloud.com/{username}'

#13
medium = f'https://medium.com/@{username}'

#14
vk = f'https://vk.com/{username}'

#15
aboutme = f'https://about.me/{username}'

#16
imgur = f'https://imgur.com/user/{username}'

#17
spotify = f'https://open.spotify.com/user/{username}'

#18
last_fm = f'https://last.fm/user/{username}'

#19
pastebin = f'https://pastebin.com/u/{username}'

#20
roblox = f'https://www.roblox.com/user.aspx?username={username}'

#21
wattpad = f'https://www.wattpad.com/user/{username}'

#22
canva = f'https://www.canva.com/{username}'

WEBS = [
instagram, facebook, twitter, youtube, blogger, reddit, wordpress, pinterest, github, tumblr, steam, soundcloud, medium,
vk, aboutme, imgur, spotify, last_fm, pastebin, roblox, wattpad, canva
]

def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')
    return inner_function

GREEN = outer_func('\033[92m')
RED = outer_func('\033[31m')
WHITE = outer_func('\033[97m')

def banner():
    print(colores.White + """

 ████████╗░█████╗░░█████╗░██╗░░░░░
 ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
 ░░░██║░░░██║░░██║██║░░██║██║░░░░░
 ░░░██║░░░██║░░██║██║░░██║██║░░░░░
 ░░░██║░░░╚█████╔╝╚█████╔╝███████╗
 ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝
        Made By zSkiddoh#0666
  """)

def busqueda():
    print(f'\033[92m[+] Buscando Informacion De: {username}')
    time.sleep(0.5)
    print('.......')
    time.sleep(0.5)
    print('.......\n')
    time.sleep(5)

    os.system("cls")

    count = 0
    match = True
    for url in WEBS:
        r = requests.get(url)

        if r.status_code == 200:
            if match == True:
                WHITE('[+] Resultados de la Busqueda')
                print()
                match = False
            if username in r.text:
                print(colores.Green + f'Resultado Valido: \033[97mUsuario Detectado')
                GREEN(f'{url}\n')
            else:
                print(colores.Red + f'Resultado Invalido: \033[97mUsuario No Detectado')
                GREEN(f'{url}\n')
        count += 1

    total = len(WEBS)
    print(Fore.RED + f'Busqueda Finalizada')
    print(Fore.WHITE + f'¡Gracias por usar la tool!')
    input()

if __name__=='__main__':
    banner()
    busqueda()
