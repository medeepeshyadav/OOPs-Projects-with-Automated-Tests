import random
import os
import sys
import pickle
import colors

os.chdir('Guess-The-Movie')

with open(file="./movies/movies_dict.pkl", mode="rb") as f:
    MOVIES = pickle.load(f)

class SetUp:
    def get_movie(self):
        """ 
        Selects a movie at random from the movie dataset
        and prepares the quiz for player
        """
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

        return movie, query
             
class Game:
    def __init__(self) -> None:
        pass

    def run(self):
        """
        Uses the SetUp class to prepare quiz for the player
        and runs the game
        """
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
            print(colors.OKCYAN+question+colors.ENDC + f" {' '*20}Hints:{colors.WARNING+str(hint_count)+colors.ENDC} | Wrong Guesses: {colors.FAIL+wrong_guesses+colors.ENDC}")

            while True:
                if not any(char.isalnum() for char in answer):
                    print(f"\nAnswer: {colors.OKGREEN+movie_key+colors.OKGREEN}")
                    print(colors.OKGREEN+"You guessed it correct!"+colors.ENDC)
                    print("#"*60)
                    print("\n"*2)
                    break

                if not bollywood:
                    print(colors.FAIL+"You have lost!"+colors.ENDC)
                    print(f"\n Answer: {colors.OKGREEN+movie_key+colors.ENDC}\n")
                    break

                response = input('>').lower()

                if response == "quit":
                    print(f"Answer: {colors.OKGREEN+movie_key+colors.ENDC}")
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
                        print(colors.OKCYAN+question+colors.ENDC + f" {' '*20}Hints:{colors.WARNING+str(hint_count)+colors.ENDC} | Wrong Guesses: {colors.FAIL+wrong_guesses+colors.ENDC}")

                    elif hint_count == 2:
                        hint_count -= 1
                        print(f"Movie was released in {colors.WARNING+str(MOVIES[movie_key][1])+colors.ENDC}")

                    elif hint_count == 1:
                        hint_count -= 1
                        print(f"Lead actor's name is: {colors.WARNING+MOVIES[movie_key][0]+colors.ENDC}")

                    else:
                        print(colors.WARNING+"You have used up all your hints!"+colors.ENDC)
                        

                elif response in answer:
                    while response in answer:
                        pos = answer.index(response)
                        answer[pos] = "_"
                        question = list(question)
                        question[pos] = response

                    question = "".join(question)
                    print("".join(bollywood))
                    print(colors.OKCYAN+question+colors.ENDC + f" {' '*20}Hints:{colors.WARNING+str(hint_count)+colors.ENDC} | Wrong Guesses: {colors.FAIL+wrong_guesses+colors.ENDC}")

                else:
                    bollywood.pop(0)
                    wrong_guesses += " "+response.upper()
                    print("".join(bollywood))
                    print(colors.OKCYAN+question+colors.ENDC + f" {' '*20}Hints:{colors.WARNING+str(hint_count)+colors.ENDC} | Wrong Guesses: {colors.FAIL+wrong_guesses+colors.ENDC}")
                    
game = Game()
game.run()

