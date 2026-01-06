import random
print("WELCOME TO COMPUTER GUESS GAME")
print("---------------------------------------------\n")
print("1.computer will guess a number between 1 and 50")
print("2.You have only 5 chances to guess the number")
print("3.each time you enter a number,one chance is used")
print("4.If your guess is higher,message will say'greater'")
print("5.If your guess is lower,message will say'lesser'")
print("6.If your guess correctly,you win the game")
print("7.After the game,you can choose to play again")
print("----------------------------------------------")
computer_guess=random.randint(1,50)
ans='y'
while ans !='n':
 count=1
 while count<=5:
   user_1=int(input("find the number guessed by computer :"))
   count=count+1
   if user_1 > computer_guess:
      print("it is greater than the guessed number")
   elif user_1 < computer_guess:
      print("it is lesser than the guessed number")
   elif user_1 == computer_guess:
      print("yes you found it") 
      break
   
 if count > 5:
   print("your turn is over")
   print("computer guess number is:",computer_guess)
 print("Do you want to play again?(Y/N)")
 ans=input().lower()
 if ans =='n':
   break  
print("---------------------------------\n")
print("Thanks for playing the computer guess game")
print("hope you enjoyed the game")
print("----------------------------------")