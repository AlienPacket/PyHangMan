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
    try:
      with open("./wordlist/pokemon.txt") as pokemon_file:
        list_of_pokemon = pokemon_file.readlines()
        str_to_guess = choice(list_of_pokemon).lower().strip()
        return str_to_guess
    except FileNotFoundError:
      print("File 'pokemon.txt' not found in the directory wordlist.")
      exit()
  elif mode == 'g':
    try:
      with open("./wordlist/ghibli.txt") as ghibli_file:
        list_of_ghibli = ghibli_file.readlines()
        str_to_guess = choice(list_of_ghibli).lower().strip()
        return str_to_guess
    except FileNotFoundError:
      print("File 'ghibli.txt' not found in the directory wordlist.")
      exit()
  else:
    try:
      with open("./wordlist/custom.txt") as custom_file:
        list_of_custom = custom_file.readlines()
        str_to_guess = choice(list_of_custom).lower().strip()
        return str_to_guess
    except FileNotFoundError:
      print("File 'custom.txt' not found in the directory wordlist.")
      exit()


#Continue to prompt if there is a wrong input(word or not alphabetic character)
def take_char():
  char = input("Insert a letter: ")
  while not char.isalpha() or len(char) > 1:
    char = input("You have to insert a letter[a-z]: ")
  return char.lower()


def display_entered_letters(prev_letters: list):
  print()
  print("Letters already entered:", end="")
  for letter in prev_letters:
    print(f" {letter}", end="")
  print("\n\n")


def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')
  #print("\x1B[H\x1B[2J\x1B[3J", end="", flush=True)



def game_loop(attempts: int, dashed_list: list, string_to_guess: str):
  prev_letters = []
  while attempts < len(ART) - 1 and "".join(dashed_list) != string_to_guess:
    print(ART[attempts]+ '\n')
    print("".join(dashed_list))
    if prev_letters:
      display_entered_letters(prev_letters)
    char = take_char()
    if char in prev_letters:
      print("You already typed this letter.")
      continue
    prev_letters.append(char)

    if char in string_to_guess:
      for i in range(len(string_to_guess)):
        if string_to_guess[i] == char:
          dashed_list[i] = char
    else:
      attempts += 1
     
    print("".join(dashed_list))


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
  game_loop(attempts, dashed_list, string_to_guess)



main()