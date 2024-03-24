import requests
from replit import clear

# ANSI COLOR CODE
RED_TEXT = "\033[0;31m"
GREEN_TEXT = "\033[0;32m"
WHITE_TEXT = "\033[0;37m"
RESET_TEXT = "\033[0m"

url = "https://random-word-api.herokuapp.com/word"
response = requests.get(url)

if response.status_code == 200:
    answer = response.json()[0].lower()
else:
    print("\033[0;31mUnable to load word from API{RESET_TEXT}")
    answer = "apple"  # default word

# Hangman ascii art
hangman = [
    r"""
    ________
    |/      |
    |      
    |      
    |     
    |      
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |    
    |     
    |      
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |       |
    |       |
    |     
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |      \|
    |       |
    |      
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      /
    |
    |___
""",
    r"""
    ________
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \
    |
    |___
""",
]

# Game status variables
cnt = 0
length = len(answer)
current_guesses = ["_"] * length
res = "".join(current_guesses)


def input_only_alpha():
    data = input("Guess a letter: ")
    while not data.isalpha() or len(data) != 1:
        data = input("Please input only a single alphabet letter: ")
    return data.lower()


# Game main logic
while res != answer and cnt < len(hangman):
    clear()
    print(hangman[cnt])
    print(f"{WHITE_TEXT}{res}{RESET_TEXT}")

    guess = input_only_alpha()
    flag = True

    for i in range(length):
        if guess == answer[i] and answer[i] != current_guesses[i]:
            current_guesses[i] = guess
            flag = False
    if flag:
        cnt += 1
    res = "".join(current_guesses)

# Result Output
if res == answer:
    print(f"{GREEN_TEXT}{answer}{RESET_TEXT}")
else:
    print(f"{RED_TEXT}{answer}{RESET_TEXT}")
