import random
import os
from art import logo, vs
from game_data import data


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
game_continue = True
account_b = random.choice(data)

while game_continue:

    def format_data(account):
        name = account["name"]
        description = account["description"]
        country = account["country"]
        return f"{name}, a {description} , from {country}"


    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who haves more follower? Type 'A' or 'B' ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    os.system('clear')
    print(logo)
    if is_correct:
        score += 1
        print(f"You are Right! Current Score: {score}")
    else:
        game_continue = False
        print(f"Sorry you are Wrong. Final Score: {score}")