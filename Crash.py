import os
from time import sleep
from random import randint
s=1
ur=1.00
money=5000
game=1
ls=[]
def crash():
 global n,p,s,money,track,ur,how,game,i
 while game==1:
   if n<=3:
     x=randint(1,100)
     y=randint(1,100)
   if n>3:
     x=randint(1,200)
     y=randint(1,200)
   if x==y:
     print("CRASHED AT ",round(n,2))
     money=money-how
     sleep(2)
     ls.append(round(n,2))
     os.system('cls')
     game=0
   print(round(n,2),"\nYour money: ",round(track))
   n=n+0.01
   track=how*n
   sleep(p)
   os.system('cls')
   if n>1.2:
     p=0.2
   if n>1.2:
     p=0.1
   if n>2:
     p=0.05
   if n>3:
     p=0.01
   if ur==round(n,2):
    print("You won: ",round(track,2))
    money=money-how+track
    ls.append(round(n,2))
    sleep(3)
    os.system('cls')
    game=0
     
while s==1:
 game=1
 i=1
 n=1.00
 p=0.3
 print("Masz: ",round(money))
 print("Ostatnie rundy: ",ls)
 ur=float(input("\nDo ilu grasz (np. 1.64): "))
 how=int(input("Za ile: "))
 if how>0 and how<=money:
  track=how
  os.system('cls')
  crash()
 else:
  os.system('cls')
  print("Zla kwota")