import random
import os
import sys
import pickle

os.chdir('Guess-The-Movie')

with open(file="./movies/movies_dict.pkl", mode="rb") as f:
    MOVIES = pickle.load(f)

class SetUp:
    def get_movie(self):
        movie = random.choice(list(MOVIES))
        # movie = list(movie)
        query = ""
        for i, c in enumerate(movie):
            if c == " ":
                query += '/'

            # elif not c.isalpha():
            #     query += c
            #     movie[i] = '_'

            else:
                query += '_'

        # movie = "".join(movie)

        return movie, query
             
class Game:
    def __init__(self) -> None:
        pass

    def run(self):
        while True:
            hint_count = 3
            bollywood = list('BOLLYWOOD')
            s = SetUp()
            answer, question = s.get_movie()
            movie_key = answer
            answer = list(answer.lower())

            wrong_guesses = ""
            print("Guess the name of this movie.")
            print("""Instructions:
            1. Enter any english letter or a number.
            2. Type 'hint' to get hint.
            3. Type 'quit' to quit the game.
            """)
            print("BOLLYWOOD")
            print(question + f" {' '*20}Hints:{hint_count} | Wrong Guesses: {wrong_guesses}")

            while True:
                if not any(char.isalnum() for char in answer):
                    print(f"\nAnswer: {movie_key}")
                    print(f"You guessed it correct!")
                    print("#"*60)
                    print("\n"*2)
                    break

                if not bollywood:
                    print("You have lost!")
                    print(f"\n Answer: {movie_key}\n")
                    break

                response = input('>').lower()

                if response == "quit":
                    print(f"Answer: {movie_key}")
                    sys.exit()

                elif response == "hint":
                    if hint_count == 3:
                        if "".join(answer).isnumeric():
                            while True:
                                hint = random.choice(answer)
                                if hint.isnumeric():
                                    break

                        else:
                            while True:
                                hint = random.choice(answer)
                                if hint.isalpha():
                                    break

                        while hint in answer:
                            pos = answer.index(hint)
                            answer[pos] = "_"
                            question = list(question)
                            question[pos] = hint
                        hint_count -= 1
                        question = "".join(question)
                        print("".join(bollywood))
                        print(question + f" {' '*20}Hints:{hint_count} | Wrong Guesses: {wrong_guesses}")

                    elif hint_count == 2:
                        hint_count -= 1
                        print(f"Movie was released in {MOVIES[movie_key][1]}")

                    elif hint_count == 1:
                        hint_count -= 1
                        print(f"Lead actor's name is: {MOVIES[movie_key][0]}")

                    else:
                        print("You have used up all your hints!")
                        

                elif response in answer:
                    while response in answer:
                        pos = answer.index(response)
                        answer[pos] = "_"
                        question = list(question)
                        question[pos] = response

                    question = "".join(question)
                    print("".join(bollywood))
                    print(question + f" {' '*20}Hints:{hint_count} | Wrong Guesses: {wrong_guesses}")

                else:
                    bollywood.pop(0)
                    wrong_guesses += " "+response.upper()
                    print("".join(bollywood))
                    print(question + f" {' '*20}Hints:{hint_count} | Wrong Guesses: {wrong_guesses}")
                    
game = Game()
game.run()

