#!/usr/bin/python3
##############
from random import *
import os
u_pswd=input("donnez le mot de passe:")
lett=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','@','_','-','!','?','.']
pwd=""
while(pwd!=u_pswd):
    pwd=""
    for letter in range(len(u_pswd)):
        guess_pwd=lett[randint(0,41)]
        pwd=str(guess_pwd)+str(pwd)
        print(pwd)
        print("chargement.....")
        os.system("cls")
print("mot de passe:",pwd)
