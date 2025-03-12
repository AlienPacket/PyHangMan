from random import choice
from ascii_art import ART

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
def take_char():
  char = input("Insert a letter: ")
  while not char.isalpha() or len(char) > 1:
    char = input("You have to insert a letter[a-z]: ")
  return char.lower()


def main():
  attempts = 0
  mode = take_mode()

  #Continue to show the prompt  if user enter a wrong input
  while not mode[0]:
    print(mode[1]+ '\n')
    mode = take_mode()
  print("Loading mode...\n\n")
    
  string_to_guess = take_word(mode[1])
  dashed_str = len(string_to_guess)*'-'

#Game loop. Later will become a function
  while attempts < 7 or dashed_str != string_to_guess:
    print(ART[attempts]+ '\n')
    print(dashed_str)
    char = take_char()


    
  
main()