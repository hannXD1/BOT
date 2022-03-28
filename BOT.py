import requests

import threading

import sys

import datetime

import os

saat_ini = datetime.datetime.now()

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati

os.system("clear")
def banner():
    print("""

______  __        ______________  _________
___  / / /        __  ___/___  / / /___    |
__  /_/ / _____________ \ __  /_/ / __  /| |
_  __  /  _/_____/____/ / _  __  /  _  ___ |
/_/ /_/           /____/  /_/ /_/   /_/  |_|

WELLCOME MEMEK

MY ACCOUNT
GitHub: https://github.com/Miko-Gejet
FB: www.facebook.com/mikoperusakmemeq

FOLLOW MY GITHUB & ACCOUNT FACEBOOK:)

""")

def run(link, token):

    while True:

        headers = {

            'authority': 'graph.facebook.com',

            'cache-control': 'max-age=0',

            'sec-ch-ua-mobile': '?0',

            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36',

        }

        try:

          response = requests.post(f'https://graph.facebook.com/me/feed?link={link}&published=0&access_token={token}', headers=headers)

          print(response.text)

        except:

          sys.exit()

def main():

    banner()

    print(saat_ini)
    
    print('┌───────────────────────────────────┐')
    #link = input('Link Posts : ')
    token = input('├──[•] Token facebook : ')

   # token = input('Token FB : ')
    link = input('├──[•] Link postingan : ')
    print('└───────────────────────────────────┘')

    number_thread = int(input('Mau share sampe berapa : (Ketik Aja 5) '))

    for i in range(number_thread):
        thread = threading.Thread(target=run, args=(link, token))
        #print('N O A H',thread.start())
        thread.start()

if __name__ == '__main__':

    main()
