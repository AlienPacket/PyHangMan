from random import choice

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
      str_to_guess = choice(list_of_pokemon).lower()

    return str_to_guess

    

def main():

  
  attempts = 0
  mode = take_mode()

  #Continue to show the prompt  if user enter a wrong input
  while not mode[0]:
    print(mode[1])
    mode = take_mode()
  print("Loading mode...")
    
  string_to_guess = take_word(mode[1])
  print(string_to_guess)


main()