# Repeat after me Game
from __future__ import annotations
import sys
import time
import random
from pathlib import Path
from typing import List
from playsound import playsound

class Sound:
    def __init__(self, sound_path: Path, sound_name: str) -> None:
        self.sound_path = sound_path
        self.sound_name = sound_name

    def __repr__(self) -> str:
        return (f"{self.sound_name}")


class SoundList(List[Sound]):
    """ Creates a list of Sound type objects"""
    def append(self, __object: Sound) -> None:
        return super().append(__object)

    def __repr__(self) -> str:
        return (f"{list(self)}")

class Player:
    def __init__(self, name) -> None:
        self.player_name = name
        self.score = 0


class Display:
    def display_rules(self) -> Player:
        print("#"*55 + " REPEAT AFTER ME "+ "#"*55)
        print(" "*45 + "#"*15 + " RULES "+ "#"*15)
        print("""You will be shown a pattern of letters from set (A, S, D, F) along with their sounds.
        You are required to repeat the whole pattern. If you do it correctly you gain one point. If you 
        fail to repeat it correctly you lose.\n""")

        player_name = input("Please enter your name: ")

        player = Player(player_name)

        return player

class Game:
    def __init__(self)-> None:
        pass

    def appender(
        self, 
        sound_list: SoundList[Sound], 
        sounds: list[Sound], 
        pattern: str
        ) -> SoundList:
        """This method appends a random letter to the pattern"""
        # get random sound object from the list of sounds
        random_letter = random.choice(sounds)

        # append to sound list
        sound_list.append(random_letter)

        # return the pattern
        return pattern+random_letter.sound_name

    def sound_player(self, sound_list: SoundList[Sound]):
        """This method plays the sound of each letter in the pattern"""
        for sound in sound_list:
            # print each letter and play its sound
            print(sound.sound_name, end=" ", flush= True)
            playsound(sound.sound_path)

    def run(self):
        """This is the driver method, which combines everything."""
        # creating an empty sound list
        sound_list = SoundList()

        # creating objects of sounds
        sound_A = Sound(sound_path="Repeat-After-Me/sounds/soundA.wav", sound_name='A')
        sound_S = Sound(sound_path="Repeat-After-Me/sounds/soundS.wav", sound_name='S')
        sound_D = Sound(sound_path="Repeat-After-Me/sounds/soundD.wav", sound_name='D')
        sound_F = Sound(sound_path="Repeat-After-Me/sounds/soundF.wav", sound_name='F')

        # list of sounds to be passed to sound appender method
        sounds = [sound_A, sound_S, sound_D, sound_F]

        # object of display
        d = Display()

        # get the player object
        player = d.display_rules()
        input("\nPress Enter to begin...")
        pattern = ""

        while True:
            # Clear the screen by printing several newlines.
            print('\n' * 60) 

            # getting the pattern
            pattern = self.appender(
                sound_list=sound_list,
                sounds=sounds, 
                pattern=pattern
            )

            # playing the sound of each letter in pattern
            self.sound_player(sound_list)

            # waiting for a second
            time.sleep(1)

            # clearing the screen
            print('\n' * 60)

            # asking player to enter the pattern
            print('Enter the pattern:')
            response = input('> ').upper()

            # if player's response doesn't match
            # with the patterns
            # show the pattern
            if response != pattern:
                print("Incorrect!")
                print("The pattern was", pattern)
            
            # else print "correct" and increament the player score
            else:
                print("Correct!")
                player.score +=1

            # play the sound of the pattern again
            self.sound_player(sound_list)

            # if response was not correct
            # print the player's score
            # and exit the game
            if response != pattern:
                print(f"\nYou scored {player.score} points.")
                print(f"\nThanks for playing, {player.player_name}!")
                break

        time.sleep(1)
        
if __name__ == "__main__":
    g = Game()
    s = g.run()
        
