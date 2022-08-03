import random
print("                   NUMBER GUESSING GAME")
print("      **************Rules Of The Game***************")
print("1.You will be given 5 chances to guess the correct number")
print("2.For correct guess you will earn 1 point and lose 1 point for wrong guess")
print("3.MAXIMUM SCORE:5 ")
print("4.MINIMUM SCORE:0")
print("*******************************************************************************")
print("*******************************************************************************")
print()
print("Input the Upper And Lower bound according to you.")
print()
lb = int(input("Enter the lower bound of the range : "))
print()
ub = int(input("Enter the upper bound of the range : "))
generated_number = random.randint(lb,ub)    # generates random number in the range
score=5
i=5
while i>=1:
    print()
    guessed=int(input("Enter the number between "+ str(lb)+" and "+ str(ub)+": "))
    i=i-1
    if guessed==generated_number :
              print()
              print("*************************************************************************************")
              print("*************************************************************************************")
              print()
              print("                        Congratulations,you have won!!!                              ")
              print()
              print("Your Guess is Correct and You have taken %d attempts for the right answer."%(5-i))
              print("YOUR FINAL SCORE:"+str(score))   # generate final score
              print()
              print("*************************************************************************************")
              print("*************************************************************************************")
              break
    elif(guessed>generated_number ):
              print()
              print("Guessed number is greater than generated number")
              score=score-1
              if i > 0:
                  print("Sorry,Try another chance!")
                  print("You have %d chances pending out of 5" % (i))

    elif(guessed<generated_number ):
              print()
              print("Guessed number is lesser than generated number")
              score=score-1
              if i>0 :
                  print("Sorry,Try another chance!")
                  print("You have %d chances pending out of 5" % (i))


    
if(score==0) :
    print()
    print("*************************************************************************************")
    print("*************************************************************************************")
    print("**********************Your chances hace been exhausted.******************************")
    print("                         OOPS!!!YOU LOSE THE GAME                                    ")
    print()

    score=score-1
    if score<0:    # final score will not be less than 0
        score=0
    print("**SCOREBOARD**")
    print("***YOUR FINAL SCORE:"+str(score)+"****")
