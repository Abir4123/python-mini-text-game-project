a =input('Welcome to the GAME  Press any key to start')

points=0

d=input("press (h) to know about the game")

if d == "h":
    print("welcome to instructions the rules are simple, you will be given some questions that you have to answer, (please write all the answers in lowercase letters) ")



q1 =input("what is the best programming language out there?: ")
b = "python"

if q1 == b.lower() :
    print("CORRECT!!")
    points+=1
else:
    print("opps its wrong!!")

q2 =input("What is the name of the fastest animal on earth?: ")

q2ans = ("cheetah")

if q2 == q2ans:
    print("CORRECT!!")
    points+=1
else:
    print("opps its wrong!!")


q3 =input("Who is the father of the nation?: ")

q3ans=("bangabandhu")

if q3 == q3ans:
    print("CORRECT!!")
    points+=1
else:
    print("opps its wrong!!")


print("CONGRATS you passed your total points are " +str(points), )

