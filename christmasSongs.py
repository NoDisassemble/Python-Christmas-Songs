from jingleBells import jingleBells
from rudolphReindeer import rudolphReindeer
from jingleRock import jingleBellRock

print('''
========================================================================================================
  .-._   .-._.                                                     .-.
..' (_)`-'   /         .-.       /                            .--.-'
|          /-.   ).--.`-' . ---/---.  .-. .-.  .-.    .     (  (_).-._..  .-.    .-.    .
|    _    /   | /    /   / \  /     )/   )   )(  |   / \     `-. (   )  )/   )  (   )  / \\
`.    )_.'    |/  _.(__./ ._)/     '/   /   (  `-'-'/ ._)  _    ) `-'  '/   (    `-/-'/ ._)
  `--'                 /                     `-'   /      (_.--'             `--._/  /

--------------------------------------------------------------------------------------------------------
Description: Python Christmas Music Juke Box.  Plays songs in karaoke style using winsound.Beep module.
Keywords: [Python 3, Python Christmas Songs, Python Music Player, winsound.Beep]
Dec 2016 v2.1
by
NoDisassemble.me
--------------------------------------------------------------------------------------------------------
''')

while True:
    # Catch for invalid response
    def invalid_opt():
        print("")
        print("Invalid choice")
        input("Press [Enter] to try again:")
        print("")
    # Options of Songs to choose from
    options = {"A": ["Jingle Bells", jingleBells], "B": ["Rudolph The Red Nosed Reindeer", rudolphReindeer], "C": ["Jingle Bell Rock", jingleBellRock], }
    for option in options:
        print(option+") "+options.get(option)[0])
    # User Input for Choice
    choice = input("Which song would you like to play? [A, B or C]: ")
    val = options.get(choice)
    if val is not None:
        action = val[1]
    else:
        action = invalid_opt
    action()
