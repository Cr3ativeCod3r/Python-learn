#biblioteki
from random import randint
import os
from time import sleep
#zmienne
hajs,i,tempm,hajs2 = 2500,1,0,0
#funkcje`
def shot_save():
   global hajs,i,tempm,hajs2,stawka
   i=i*2
   print("\nPIF")
   sleep(0.8)
   print("PAF")
   hajs2=hajs-stawka
   tempm0=(stawka*i)-stawka
   tempm=(stawka*i)
   print("\nALIVEEEE Do you take profit: ",tempm0,"zł")

def shot_die(): 
   global hajs,stawka,i,hajs2,tempm
   i,hajs2,tempm=1,0,0
   print("\nPIF")
   sleep(0.8)
   print("PAF")
   print("\nDIEEEEEEEE HA! HA! HA! HA!")
   sleep(2)
   hajs = hajs-stawka
   os.system('cls')
def los():
  global kr,pr
  kr=randint(1,3)
  pr=randint(1,3)
def krnotpr():
   global kr,pr,still
   if kr!=pr:
     shot_save()
     still=int(input("\n0-Take 1-Shot: "))

  
#GUI 
def gui():
  global hajs,stawka
  print("| Witam w rosyjskiej ruletce! | | Każdy strzał to 30% na śmierć | | Za każdym strzałem możesz wziąć więcej!!! | \n| Cel to wygrać 100,000zł |")
  print("\nStan konta: ",hajs,"zł")
  stawka = int(input("Za ile zł grasz: "))

#game
while 1==1:
  os.system('cls')
  gui()
  if stawka>0 and stawka<=hajs:
   still=int(input("\n1-Shot 0-Stop: "))
   while still==1:
    los()
    krnotpr()
    if kr==pr:
     shot_die()
     break
    if still==0:
     hajs=hajs2+tempm
     print("stop")
     i,hajs2,tempm=1,0,0
     os.system('cls')
     break