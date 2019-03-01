import random
l=("p","r","s")
cscore=0
youscore=0
while True:
     u=input("Choose rock, paper or scissors:     \n")
     c=random.choice(l)
     print("you choose: ",u,"and computer choose: ",c)
     if cscore==5 or youscore==5:
     	print("Bye!...... GAME OVER......")
     	print ("youscore=",youscore)
     	print("computerscore=",cscore)
     	exit()
     elif c==u:
     	print("Its a tie!...")
     elif c=="s" and u=="r":
   	    print("you won!!...")
   	    youscore=youscore+1
     elif c=="p" and u=="s":
   	    print("you won!...")
   	    youscore=youscore+1
     elif c=="r" and u=="p":
        print("you won!...")
        youscore=youscore+1	  
     elif c=="s" and u=="p":
        print("you lost!..")
        cscore=cscore+1
     elif c=="p" and u=="r":
        print("you lost!...")
        cscore=cscore+1
     elif c=="r" and u=="s":
        print("you lost!...")
        cscore=cscore+1 