PICS = [
r"""
  +---+
  |   |
      |
      |
      |
      |
=========
""",

r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""",

r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""",

r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""",

r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""",

r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""",

r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
]


def take_word(mode: str) -> str:
  if mode.lower() == 'p':
    with open("./wordlist/pokemon.txt") as pokemon_file:
      list_of_pokemon = pokemon_file.readlines()
      #Learn randomness to going on with the project



attempts = 0
mode = input("Select a mode:\nType 'P' for pokemon mode")
str_to_guess = take_word(mode)

