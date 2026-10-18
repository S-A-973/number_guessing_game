import random

def get_user_input(prompt):
    while True:
        try:
            user_guess = int(input(prompt))
            if 0 < user_guess <= 10:
                return user_guess
            else:
                print("please enter an integer between 0 and 10")
        except ValueError:
            print("Please enter an integer")

def get_random_number():
    number = random.randint(1, 10)
    return number

def game_score(x, y):
    difference = abs(x - y)
    
    if difference == 0:
        return 10
    elif difference <= 2:
        return 8
    elif difference <= 4:
        return 6
    elif difference <= 6:
        return 4
    elif difference <= 4:
        return 2
    else:
        return 0

    
def main():   
    
    total_score = 0
    rounds = 5
    while rounds > 0:
        round_score = game_score(get_user_input("Guess a number: "), get_random_number())
        total_score += round_score
        rounds -= 1
        print(f"Number of rounds remaining {rounds}, Total score: {total_score}")

main()
    


    



