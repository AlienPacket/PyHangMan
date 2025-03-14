from random import choice
from ascii_art import ART
import os

def take_mode():
  mode = input("Select a mode:\nType 'P' for pokemon mode\nType 'G' for ghibli mode\nType 'C' for custom mode: ").lower()
  if mode == 'p' or mode == 'g' or mode == 'c':
    return (True, mode)
  else:
    return (False, "Incorrect type mode. Try again.")


def take_word(mode: str):
  if mode == 'p':
    with open("./wordlist/pokemon.txt") as pokemon_file:
      list_of_pokemon = pokemon_file.readlines()
      str_to_guess = choice(list_of_pokemon).lower().strip()

    return str_to_guess

#Continue to prompt if there is a wrong input(word or not alphabetic character)
def take_char(prev_letters: list):
  char = input("Insert a letter: ")


#I have to handle the case where the user enter a letter, already entered in the past
  #if char in prev_letters:
    #char = input("")



  while not char.isalpha() or len(char) > 1:
    if char in prev_letters:
      char = input("You already typed that letter, try another one: ")
    else:
      char = input("You have to insert a letter[a-z]: ")
  return char.lower()

def display_entered_letters(prev_letters: list):
  print("Letters already entered:", end="")
  for letter in prev_letters:
    print(f" {letter}", end="")
  print("\n\n")



def main():
  attempts = 0
  mode = take_mode()

  #Continue to show the prompt  if user enter a wrong input
  while not mode[0]:
    print(mode[1]+ '\n')
    mode = take_mode()
  print("Loading mode...\n\n")
    
  string_to_guess = take_word(mode[1])
  dashed_list = list(len(string_to_guess)*'-')
#Game loop. Later will become a function
  prev_letters = []
  while attempts < 6 and "".join(dashed_list) != string_to_guess:
    print(ART[attempts]+ '\n')
    print("".join(dashed_list))
    if prev_letters:
      display_entered_letters(prev_letters)
    char = take_char(prev_letters)
    prev_letters.append(char)


    if char in string_to_guess:
      for i in range(len(string_to_guess)):
        if string_to_guess[i] == char:
          dashed_list[i] = char
    else:
      attempts += 1
     
    print("".join(dashed_list))

    os.system('cls' if os.name == 'nt' else 'clear')
    #print("\x1B[H\x1B[2J\x1B[3J", end="", flush=True)
    

    
  
main()