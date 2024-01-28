#!/usr/bin/python3
##############
def presentation():
    print("hi :)")
    a = input("nom:")
    while True:
        b=input("age:")
        try:
            b=int(b)
            break
        except:
            print("age Invalid!")    
    print("lage de ",a ," est:",b)
    if b<18:
        print("yal mineur 🤣")
        exit()
########
presentation()
###############
def fonction():
    print("###############")
    while True:
        print("calculer f(x)=(x^2)+1/(x^2)-1:")
        print("x!=-1 ou x!=1")
        while True:
            x=input("x:")
            try:
                    x=float(x)
                    if x != 1 and x!=(-1):
                        break
            except:
                    print("x incorrecte!")
        
        fx=((x*x)+1)/((x*x)-1)
        
        if fx > 0 :
            print("f(x):",fx,"est positif")
        elif fx == 0:
            print("f(x):",fx,"est null")
        else:
            print("f(x):",fx,"est négatif")
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end")       
########
fonction()        
##############    
def didiw():
    print("###############")
    while True :
        while True:
            n=input("n rep de didiw:")
            try:
                n=int(n)
                break
            except:
                print("n incorrecte!")    
        i=0
        while i<n:
            print("-------")
            print(i+1,".didiwww")
            i+=1
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break
    print("end")
#######
didiw()  
##############        
def jeu():
    jeu=True
    print("###############")
    print("bien venue dans le jeu:")
    while   jeu:
        print("-------------")
        print("1.start/2.end")
        choix=int(input("> "))
        print("---------------")
        if choix == 1:
            print("choisissez troi chiffres entièr:")
            i=0
            s=0
            while i <3:
                while True:
                    n=input("# ")
                    try:
                        n=int(n)
                        break
                    except:
                        print("n incorrecte:")
                s+=n
                i+=1
            print("le score est:",s)      
            continue
        elif choix == 2:
            jeu=False 
        else:
           print("commande introuvable")
           continue
print("a bientôt") 
########
jeu()
#######################
def remplissage():
    print("###############")
    print("remplissage d'un tableau basique:")
    list=[]
    while True:
        while True:
            n=input("taille de la liste:")
            try:
                n=int(n)
                if n>0:
                    break
            except:
                print("n incorrecte!")
        for i in range(n):
            x=input(f"num {i+1}:")
            list.append(x)
        print(list)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
########
remplissage()
###################
def somme_carres():
    print("###############")
    print("la somme_carres x^(n) sans pow:")
    while True:
        while True:
            x=input("x:")
            try:
                x=float(x)
                break
            except:
                print("x incorrecte!")
        while True:
            n=input("n:")
            try:
                n=int(n)
                if n>0:
                    break
            except:
               print("n incorrecte!")
        s=1
        for i in range(n):
            s=s*x
        print("la somme:",s)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
##########
somme_carres()
##################
def palindrome():
    print("###############")
    print("trouver si le mot est palindrome:")
    while True:
        mot=input("mot:")
        mot.lower()
        not_mot=mot[::-1]
        if mot==not_mot:
            print("c un palindrome")
        else:
            print("c pas un palindrome")
            print(not_mot)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end")
###########
palindrome()
##############
def inverse():
    print("###############")
    print("inverse du tableau:")
    while True:
        liste=[]
        while True:
            n=input("taille du tableau:")
            try:
                n=int(n)
                if n>0:
                    break
            except:
               print("n incorrecte!")
        for _ in range(n):
            x=input(f"{_+1}:")
            liste.append(x)
        print("liste remplie:")
        print(liste)
        print("liste inverse:")
        i=n-1
        while i>=0:
            print(liste[i])
            i-=1
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end")       
#########
inverse()
#############
def fibonacci():
    print("###############")
    print("calculer fibonacci:")
    while True:
        arr=[]
        while True:
            n=input("n:")
            try:
                n=int(n)
                if n>0:
                    break
            except:
               print("n incorrecte:")
        if  n>=0:
            arr.append(0)
        if n>=1:
            arr.append(1)
        i=2
        while  i<=n :
            arr.append(arr[i-1]+arr[i-2])
            i+=1
        print(arr)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end")
#######
fibonacci()
#############
def occurrence():
    arr = []
    n_arr = {}
    print("###############")
    print("trouver les occurrence:")
    while True:
        n = input("n: ")
        try:
                n=int(n)
                if n>0:
                    break
        except:
               print("n incorrecte!")
    while True:
        for _ in range(n):
             x = input(f"num{_ + 1}: ")
             arr.append(x)
        print("Les éléments:")
        print(arr)
        for element in arr:
            if element in n_arr:
                n_arr[element] += 1
            else:
                n_arr[element] = 1
        print("Occurrences:")
        for key, value in n_arr.items():
            print(f"{key}: {value}")
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end")   
#######
occurrence()
##############
def math_lib():
    import math
    print("###############")
    print("calculer la racine:")
    while True:
        while True:
            n=input("le num:")
            try:
                n=float(n)
                if n>=0:
                    break
            except:
               print("n incorrecte:")
        n=math.sqrt(n)
        print("la racine est:",n)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
    ###
    print("###############")
    print("calculer le sin est cos:")
    while True:
        while True:
            x=input("nombr:")
            try:
                    x=float(x)
                    break
            except:
                    print("a incorrecte!")
        s=math.sin(x)
        c=math.cos(x)
        print(f"le sin({x}):{s} et le cos({x}):{c}")
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
    ###
    print("###############")
    print("calculer la partie entière:")
    while True:
        while True:
            x=input("le chiffre x:")
            try:
                 x=float(x)
                 break
            except:
                 print("x incorrecte!")
        x=math.trunc(x)
        print("E(x):",x)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
    ###
    print("###############")
    print("calculer le factorielle:")
    while True:
        while True:
            n=input("num:")
            try:
                n=int(n)
                if n>0:
                    break
            except:
               print("n incorrecte:")
        n=math.factorial(n)
        print( "le factorielle est:",n)
        print("")
        print("***(1.continue/2.break)***")
        op=int(input("> "))
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end")
    ###
    print("###############")
    print("calculer le pgcd(a,b):")
    while True:
        while True:
            a=input("a:")
            try:
                a=int(a)
                if a>0:
                    break
            except:
               print("a incorrecte:")
        while True:
            b=input("b:")
            try:
                b=int(b)
                if b>0:
                    break
            except:
               print("n incorrecte:")
        s=math.gcd(a,b)
        print(f"pgcd({a},{b}):",s)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
    ###
    print("###############")
    print("calculer la puissanc[x^(n)] avec pow:")
    while True:
        while True:
            x=input("x:")
            try:
                x=int(x)
                break
            except:
               print("x incorrecte!")
        while True:
            n=input("n:")
            try:
                n=int(n)
                if n>0:
                    break
            except:
               print("n incorrecte!")
        s=math.pow(a,b)
        print(f"[{a}^{b}]:",s)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
    ###
    while True:
        print("calculer ln(x):")
        while True:
            x=input ("num x>0:")
            try:
                x=float(x)
                if x>0:
                    break
            except:
                print("x incorrecte!")
        a=math.e
        f=math.log(x,a)
        print(f"ln({x}):",f)
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break    
        if op==2:
            break    
    print("end") 
########
math_lib()
#############
def sans_math():
    print("###############")
    print("calculer le pgcd sans librairie de math:")
    print("###############")
    print("calculer le factorielle:")
    while True:
        while True:
            n=input("num:")
            try:
                n=int(n)
                if n>0:
                    break
            except:
               print("n incorrecte!")
        i=1
        a=1
        while i<=n:
            a=a*i
            i+=1
        print( "le factorielle est:",a)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end")
    ###
    print("###############")
    print("calculer le pgcd(a,b):")
    while True:
        while True:
            a=input("a:")
            try:
                a=int(a)
                if a>0:
                    break
            except:
               print("a incorrecte:")
        while True:
            b=input("b:")
            try:
                b=int(b)
                if b>0:
                    break
            except:
               print("n incorrecte:")
        if a>b:
            n=a
        else:
            n=b
        i=1
        while i<=n:
            if a%i==0 and b%i==0:
                s=i
            i+=1
        print(f"pgcd({a},{b}):",s)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
    ###
    print("###############")
    print("calculer la partie entière avec ciel:")
    print("!ciel(x) c l'entrée le plus petit supérieur a x!")
    while True:
        while True:
            x=input("le chiffre x:")
            try:
                    x=float(x)
                    break
            except:
                    print("x incorrecte!")
        if x==int(x):
            print(f"le chiffre {x}est un entier.")
        else:
            x=math.ceil(x)
            if x>=0:
                print("la partie entière E(x):",x-1)
            else :
                print("la partie entière E(x):",x+1)
        print("")
        print("***(1.continue/2.break)***")
        while True:
            while True:
                op=input("> ")
                try:
                    op=int(op)
                    break
                except:
                    print("commande introuvable!")    
            if op==1 or op==2:
                break
        if op==2:
            break    
    print("end") 
########
sans_math()
############