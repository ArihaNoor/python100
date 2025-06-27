#KBC 

questions = [
    "Who is the Founder of Pakistan?",
    "Who discovered America?",
    "Capital of Pakistan is?"
]

answers = [
    ["Allama Iqbal", "Liaqat Ali Khan", "Quaid e Azam"],
    ["Columbus", "Jane", "Einstein"],
    ["Karachi", "Lahore", "Islamabad"]
]

correct_Answers = ["C", "A", "C"]

amount = [200000, 303000, 506000]

def KBC():
    totalAmount = 0
    for index, question in enumerate(questions):  
        print(question)
        print("Options:", answers[index]) 
        userAnswer = input("Enter Your Answer (A, B, or C): ").strip().upper()
        if userAnswer == correct_Answers[index]:  
            totalAmount += amount[index]
            print(f"Correct! You have won {amount[index]}. Total amount: {totalAmount}")
        else:
            print("Wrong answer!")
    print(f"Game over! You won a total of {totalAmount}.")

KBC()