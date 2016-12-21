
from jingleBells import jingleBells
from rudolphReindeer import rudolphReindeer

print('''
  .-._   .-._.                                                     .-.
..' (_)`-'   /         .-.       /                            .--.-'
|          /-.   ).--.`-' . ---/---.  .-. .-.  .-.    .     (  (_).-._..  .-.    .-.    .
|    _    /   | /    /   / \  /     )/   )   )(  |   / \     `-. (   )  )/   )  (   )  / \\
`.    )_.'    |/  _.(__./ ._)/     '/   /   (  `-'-'/ ._)  _    ) `-'  '/   (    `-/-'/ ._)
  `--'                 /                     `-'   /      (_.--'             `--._/  /

--------------------------------------------------------------------------------------------
2016 v1.0
by
NoDisassemble.me
--------------------------------------------------------------------------------------------
''')

while True:
    # Catch for invalid response
    def invalid_opt():
        print("")
        print("Invalid choice")
        input("Press [Enter] to try again:")
        print("")
    # Options of Songs to choose from
    options = {"A":["Jingle Bells",jingleBells], "B":["Rudolph The Red Nosed Reindeer",rudolphReindeer]}
    for option in options:
        print(option+") "+options.get(option)[0])
    # User Input for Choice
    choice = input("What song would you like to play? [A or B]: ")
    val = options.get(choice)
    if val is not None:
        action = val[1]
    else:
        action = invalid_opt
    action()