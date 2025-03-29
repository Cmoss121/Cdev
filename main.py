
import colorama 
from colorama import Fore, Back, Style, init
import sys
import time
import os

while True:
    print(f"""{Style.BRIGHT + Fore.MAGENTA}

    MADE BY CMOSS AKA CDEV

     ██████╗██████╗ ███████╗██╗   ██╗
    ██╔════╝██╔══██╗██╔════╝██║   ██║
    ██║     ██║  ██║█████╗  ██║   ██║
    ██║     ██║  ██║██╔══╝  ╚██╗ ██╔╝
    ╚██████╗██████╔╝███████╗ ╚████╔╝ 
     ╚═════╝╚═════╝ ╚══════╝  ╚═══╝  

    [1] IP LOOKUP

    [2] EXIT         

    [3] NUKE BOT
    """)

    command = input(f" {Fore.MAGENTA}CDEV: ")

    if command == "2":
        exit()

    if command == "1":
        from ddos_script import run_ddos
        run_ddos()

    if command == "3":
        token = input("need ur token this isn't a logger: ")
        try:
            print("Starting bot...")
            from bott import run_bot
            run_bot(token)
        except Exception as e:
            print(f"Error starting bot: {str(e)}")

# I was fucking high while making this 😭
