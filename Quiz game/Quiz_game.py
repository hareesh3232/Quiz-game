#python quoiz game

questions=("How many elements are in perdoic table? :",
           "Which animal lays the largest egg?:",
           "What is the most abutant gas in the Earth's atmosphere?:",
           "How many bones are in human body?:",
           "which planet in the solar system is hottest:?")

options=(("A.116","B.117","C.118","D.119"),
         ("A.Whale ","B. Corcodile","C. Elephant","D. Ostrich"),
         ("A.Nitrogen","B. Oxygen","C. CO2","D. Hydrogen"),
         ("A.206","B.207","C.208","D.209"),
         ("A.Mercury","B.Venus ","C. Earth ","D.Mars"))

answer=("C","D","A","A","B")
guesses=[]
score = 0
question_num=0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter (A,B,,C,D):").upper()
    guesses.append(guess)
    if guess==answer[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answer[question_num]} is the correct answer")
    question_num +=1

print(f"The total number of correct answer:{score}")

if score==5:
    print("congratulation! All your answers are correct ")
else :
    print("Better luck next time  ")

