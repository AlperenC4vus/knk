#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from time import sleep
from random import random
from threading import Thread as a



print("""
_░▒███████
░██▓▒░░▒▓██
██▓▒░__░▒▓██___██████
██▓▒░____░▓███▓__░▒▓██
██▓▒░___░▓██▓_____░▒▓██
██▓▒░_______________░▒▓██
_██▓▒░______________░▒▓██
__██▓▒░____________░▒▓██
___██▓▒░__________░▒▓██
____██▓▒░________░▒▓██
_____██▓▒░_____░▒▓██
______██▓▒░__░▒▓██
_______█▓▒░░▒▓██
_________░▒▓██
_______░▒▓██
_____░▒▓██
""")

print("ENTER'A BAS--> ")

input()

print("""\033[1;31m
███╗░░██╗██╗░░░██╗██████╗░██╗░░██╗░█████╗░███╗░░██╗
████╗░██║██║░░░██║██╔══██╗██║░░██║██╔══██╗████╗░██║
██╔██╗██║██║░░░██║██████╔╝███████║███████║██╔██╗██║
██║╚████║██║░░░██║██╔══██╗██╔══██║██╔══██║██║╚████║
██║░╚███║╚██████╔╝██║░░██║██║░░██║██║░░██║██║░╚███║
╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝""")




liste = ["Love you", "LOve you", "LoVe you", "LovE you", "Love You", "Love yOu", "Love yoU"]






for i in liste*10:
     print("\r", f"[{i}]", end="")
     sleep(0.11)





def knk():

    print()


    sleep(00.99999999999999999999999999999999999999999999999)


t = a(target=knk)

t.start()


print("\n\n")
while t.is_alive:
     
    soru = input("Beni seviyormusun ? E/h => ")

    if soru.lower() == "h" or soru.lower() == "hayir" or soru.lower() == "hayır":

           with open(f"Cidden beni sevmiyormusun{random()}.txttl", "a+") as f:
                  f.write("ÜZÜLDÜM")
              
    
    elif soru.lower() == "evet" or soru.lower() == "e":
          print("Duyduğuma sevindim knk")
          break
    else:
         
        print(f"{soru} Hatalı knk geçerli birşey gir ")
    



