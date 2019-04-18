import datetime
import json
import random


# Funkcija zaidimui
def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    score_list = get_score_list()

    while True:
        guess = int(input("guess the secret number(between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

                print("You have guessed it - congratulations! It is number " + str(secret))
                print("Attempts needed: " + str(attempts))
                break
        elif guess > secret:
            print("Your guess is not correct... try something smaller")
        elif guess < secret:
            print("Your guess is not correct... try something bigger")


# Visi spejimai
def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# Top 3 spejimai
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return top_score_list


# Zaidimas ir lygiai
while True:
    selection = input("Would you like to A) Play a new game, B) See the best scores, or C) Quit?")

    if selection.upper() == "A":
        level = input("Choose your level (easy/hard): ")
        play_game()
    elif selection.upper() == "B":
        for score_dict in get_top_scores():
            print(str(score_dict["attempts"]) + " attempts, date: " + score_dict.get("date"))
    else:
        break
