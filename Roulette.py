from random import randint
import os
from time import sleep
#zmienne
money = 500
x=0
his=[]
#funkcje
def wyg():
     global money
     money2 = money-min
     money=(min*2)+money2
def prz():
     global money
     money = money-min
def wygz():
     global money
     money2 = money-min
     money=(min*14)+money2
def win():
     print("\n ---- \n losuje... \n ----")
     sleep(1)
     print("\n WIN IT'S",(his[-1]))
     sleep(0.3)
def lose():
     print("\n ---- \n losuje... \n ----")
     sleep(1)
     print("\n LOSE IT'S",(his[-1]))
     sleep(0.3)
def end():
     sleep(1.5)
     os.system('cls')

def los():
  global kr 
  kr = randint(1,100)

def upcz():
   global his
   his.append("red")

def upczr():
   global his
   his.append("black")
   
def upz():
   global his
   his.append("green")
 
os.system('cls')
print("Witamy w kasynie!")
print("Masz na koncie 500zł, celem gry jest wygrać 10,000zł ")
start=int(input("Jak chcesz zagrać wpisz 1: "))
if start==1:
 os.system('cls')

 while 1==1:
 
  print("Podaj kolor 1-3, (stan konta):",money,"zł")
  print("\n Co wypadło: ",his)
  tw = int(input("\n 1) red    - 2x (45% sznas) \n 2) black  - 2x (45% sznas)\n 3) grren - 14x (10% sznas) \n  \ntwój wybór: "))
  min = int(input("\n Ile dajesz zł: "))
  
  #czerwone
  if tw==1 and min<=money and min>0:
    los()
    if kr<45:
     wyg()
     upcz()
     win()
     end()
     
    if  kr>55:
     prz()
     upczr()
     lose()
     end()
     
    if kr<55 and kr>45:
     prz()
     upz()
     lose()
     end()
      
  #czarne
  if tw==2 and min <= money and min > 0:
     los()
     if kr<45:
      wyg()
      upczr()
      win()
      end()

     if kr>55:
      prz()
      upcz()
      lose() 
      end()
     
     if kr<55 and kr>45:
      prz() 
      upz()
      lose()
      end()
  #zielone
  if tw==3 and min<=money and min>0:
    los()
   
    if kr < 45:
     prz()
     upcz()
     lose()
     end()
     
    if kr > 55:
     prz()
     upczr()
     lose()
     end()
     
    if kr <= 55 and kr >= 45:
      wygz()
      upz()
      win()
      end()
      
  if money>=10000:
      os.system('cls')    
      print("GRATULACJE I OWACJE jak chcesz to możesz grać dalej")
      print("Już ci ładuje i zabieram 5000zł dla siebie :D")  
      money=money-5000
      sleep(5)
  if money==0:
      print("Koniec pieniędzy ")
      sleep(10)