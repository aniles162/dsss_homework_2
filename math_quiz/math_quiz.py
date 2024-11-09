import random


def get_number(min_value, max_value):
    """
    Random integer.
    Generates a random integer within the range min_value and max_value.
    """
    return random.randint(min_value, max_value)


def get_operator():

    """
    Chooses a random arithmetic operator.
    """
    return random.choice(['+', '-', '*'])


def gen_math_problem(num1, num2, op):

    """ 
    Creates a mathematically problem and calculates the solution.
    """
    problem = f"{num1} {op} {num2}"
    if op == '+': answer = num1 + num2   # operator was swapped from - to +
    elif op == '-': answer = num1 - num2 # operator was swapped from + to -
    else: answer = num1 * num2
    return problem, answer

def math_quiz():

    """
    Runs the math quiz.
    """
    score = 0 # score: Initialize the score to zero.
    total_questions = 5 # total_questions: number of quetions in the game. has to be an integer!
    

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")


    # for-loop through the number of questions
    for _ in range(total_questions):

        # Getting two random numbers and a random operator
        num1 = get_number(1, 10); num2 = get_number(1, 5); op = get_operator() # num2 has to be integer



        PROBLEM, ANSWER = gen_math_problem(num1, num2, op) # Creates a math problem and calculates the correct answer
        print(f"\nQuestion: {PROBLEM}") #   and prints the problem to the user
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

         # Error handling 
        while True:
            try:
                # try to change useranswer to integer
                useranswer = int(useranswer)
                break  # if the input was successfully changed to integer, leave the loop
            except ValueError:
                # if the input was no integer, print an error message
                print("Invalid input! Please enter a valid integer.")
                useranswer = input("Your answer: ")  # ask again for user input

        #  tests if the user's answer is correct
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}") # Displays the final score at the end of the game.

if __name__ == "__main__":
    math_quiz()
