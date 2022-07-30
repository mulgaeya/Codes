from Question import Question 

questionPrompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple/Blue\n(c) Black\n\n", 
    "What color are bananas?\n(a) Green\n(b) Blue\n(c) Yellow\n\n"
]

questions = [
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c")
]


def runTest(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("\nYou got " + str(score) + "/" + str(len(questions)) + " correct")

runTest(questions)