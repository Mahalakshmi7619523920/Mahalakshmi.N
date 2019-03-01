import random
l=("p","r","s")
while True:
     u=input("Choose rock, paper or scissors:     \n")
     c=random.choice(l)
     print("you choose: ",u,"and computer choose: ",c)
     if u=="e":
     print("Bye!...... GAME OVER......")
     exit()
   elif c==u:
       print("Its a tie!...")
   elif c=="s" and u=="r":
   	   print("you won!!...")
   elif c=="p" and u=="s":
   	   print("you won!...")
   elif c=="r" and u=="p":
       print("you won!...")	  
   elif c=="s" and u=="p":
       print("you lost!..")
   elif c=="p" and u=="r":
       print("you lost!...")
   elif c=="r" and u=="s":
       print("you lost!...") 