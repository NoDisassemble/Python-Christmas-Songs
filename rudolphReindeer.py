import sys
import time
import winsound

# =====================================================================================================
#    .-.                  .       .               .-.                               .
#   (_) )-.              /       /         /     (_) )-.           .-.             /
#      /   \  )  (  .-../ .-._. /  .-.    /-.       /   \   .-.    `-'.  .-.  .-../   .-.   .-.  ).--.
#     /     )(    )(   / (   ) /   /  )  /   |     /     )./.-'_  /    )/   )(   /  ./.-'_./.-'_/
#  .-/  `--'  `--': `-'-..`-'_/_.-/`-'_.'    |  .-/  `--' (__.'_.(__. '/   (  `-'-..(__.' (__.'/
# (_/     `-._)                  /             (_/     `-._)                `-
#
# -----------------------------------------------------------------------------------------------------
# Description: Rudolph The Red Nosed Reindeer.  Must be run from christmasSongs.py
# Keywords: [Python 3, Rudolph The Red Nosed Reindeer, Python Christmas Songs]
# Dec 2016 v1.0
# by
# NoDisassemble.me
# -----------------------------------------------------------------------------------------------------

# Begin Rudolph
def rudolphReindeer():
    loading = "Generating Song and Lyrics for Rudolph The Red Nosed Reindeer: [-------------------]"
    print("")
    for i in range(101):
        time.sleep(0.05)
        sys.stdout.write("\r" + loading + " %d%%" % i)
        if i == 5 or i == 10 or i == 15 or i == 20 or i == 25 or i == 30 or i == 35 or i == 40 or i == 45 or i == 50 or i == 55 or i == 60 or i == 65 or i == 70 or i == 75 or i == 80 or i == 85 or i == 90 or i == 95 or i == 100:
            loading = loading.replace("-", "=", 1)
        sys.stdout.flush()
    print("")
    print("")
    x = "-"
    for i in range(1, 46):
        print(x, end="")
    print("")
    print("[+] Plying Rudolph The Red Nosed Reindeer [+]")
    x = "-"
    for i in range(1, 46):
        print(x, end="")
    print("")
    time.sleep(1)
    print("Rudolph")
    winsound.Beep(588, 500)  #D
    winsound.Beep(660, 500)  #E
    print("The")
    winsound.Beep(588, 300)  #D
    print("Red")
    winsound.Beep(494, 500)  #B
    print("Nosed")
    winsound.Beep(784, 700)  #G
    print("Reindeer")
    winsound.Beep(660, 500)  #E
    winsound.Beep(588, 1000) #D
    time.sleep(0.5)
    print("Had")
    winsound.Beep(588, 300)  #D
    print("A")
    winsound.Beep(660, 300)  #E
    print("Very")
    winsound.Beep(588, 300)  #D
    winsound.Beep(660, 300)  #E
    print("Shiny")
    winsound.Beep(588, 700)  #D
    winsound.Beep(784, 700)  #G
    print("Nose")
    winsound.Beep(740, 1200) #F#
    time.sleep(1)
    print("And")
    winsound.Beep(522, 500)  #C
    print("If")
    winsound.Beep(588, 500)  #D
    print("You")
    winsound.Beep(522, 300)  #C
    print("Ever")
    winsound.Beep(440, 500)  #A
    winsound.Beep(784, 700)  #F#
    print("Saw")
    winsound.Beep(660, 500)  #E
    print("It")
    winsound.Beep(588, 1000) #D
    time.sleep(0.5)
    print("You")
    winsound.Beep(588, 300)  #D
    print("Would")
    winsound.Beep(660, 300)  #E
    print("Even")
    winsound.Beep(588, 300)  #D
    winsound.Beep(660, 300)  #E
    print("Say")
    winsound.Beep(588, 700)  #D
    print("It")
    winsound.Beep(660, 700)  #E
    print("Glows")
    winsound.Beep(494, 1200) #B
    time.sleep(1)
    print("All")
    winsound.Beep(588, 500)  #D
    print("Of")
    winsound.Beep(660, 500)  #E
    print("The")
    winsound.Beep(588, 300)  #D
    print("Other")
    winsound.Beep(494, 500)  #B
    winsound.Beep(784, 700)  #G
    print("Reindeer")
    winsound.Beep(660, 500)  #E
    winsound.Beep(588, 1000) #D
    time.sleep(0.5)
    print("Used")
    winsound.Beep(588, 300)  #D
    print("To")
    winsound.Beep(660, 300)  #E
    print("Laugh")
    winsound.Beep(588, 300)  #D
    print("And")
    winsound.Beep(660, 300)  #E
    print("Call")
    winsound.Beep(588, 700)  #D
    print("Him")
    winsound.Beep(784, 700)  #G
    print("Names")
    winsound.Beep(740, 1200) #F#
    time.sleep(1)
    print("They")
    winsound.Beep(522, 500)  #C
    print("Never")
    winsound.Beep(588, 500)  #D
    winsound.Beep(522, 300)  #C
    print("Let")
    winsound.Beep(440, 500)  #A
    print("Poor")
    winsound.Beep(784, 700)  #F#
    print("Rudolph")
    winsound.Beep(660, 500)  #E
    winsound.Beep(588, 1000) #D
    time.sleep(0.5)
    print("Join")
    winsound.Beep(588, 300)  #D
    print("In")
    winsound.Beep(660, 300)  #E
    print("Any")
    winsound.Beep(588, 300)  #D
    winsound.Beep(660, 300)  #E
    print("Reindeer")
    winsound.Beep(588, 700)  #D
    winsound.Beep(440, 700)  #A
    print("Games")
    winsound.Beep(392, 1200) #G
    time.sleep(1)
    print("Then")
    winsound.Beep(660, 500)  #E
    print("One")
    winsound.Beep(660, 500)  #E
    print("Foggy")
    winsound.Beep(784, 500)  #G
    winsound.Beep(660, 500)  #E
    print("Christmas")
    winsound.Beep(588, 700)  #D
    winsound.Beep(494, 500)  #B
    print("Eve")
    winsound.Beep(588, 1000) #D
    time.sleep(0.5)
    print("Santa")
    winsound.Beep(522, 500)  #C
    winsound.Beep(660, 500)  #E
    print("Came")
    winsound.Beep(588, 500)  #D
    print("To")
    winsound.Beep(522, 500)  #C
    print("Say")
    winsound.Beep(494, 1200) #B
    time.sleep(1)
    print("Rudolph")
    winsound.Beep(440, 500)  #A
    winsound.Beep(494, 500)  #B
    print("With")
    winsound.Beep(588, 500)  #D
    print("Your")
    winsound.Beep(660, 500)  #
    print("Nose")
    winsound.Beep(740, 500)  #F#
    print("So")
    winsound.Beep(740, 500)  #F#
    print("Bright")
    winsound.Beep(740, 1000) #F#
    time.sleep(0.5)
    print("Wont")
    winsound.Beep(784, 500)  #G
    print("You")
    winsound.Beep(784, 500)  #G
    print("Guide")
    winsound.Beep(740, 500)  #F#
    print("My")
    winsound.Beep(660, 500)  #E
    print("Sleigh")
    winsound.Beep(588, 500)  #D
    print("Tonight")
    winsound.Beep(522, 500)  #C
    winsound.Beep(440, 1000) #A
    time.sleep(0.5)
    print("Then")
    winsound.Beep(588, 500)  #D
    print("How")
    winsound.Beep(660, 500)  #E
    print("The")
    winsound.Beep(588, 300)  #D
    print("Reindeer")
    winsound.Beep(494, 500)  #B
    winsound.Beep(784, 700)  #G
    print("Loved")
    winsound.Beep(660, 500)  #E
    print("Him")
    winsound.Beep(588, 1000) #D
    time.sleep(0.5)
    print("As")
    winsound.Beep(588, 300)  #D
    print("They")
    winsound.Beep(660, 300)  #E
    print("Shouted")
    winsound.Beep(588, 300)  #D
    winsound.Beep(660, 300)  #E
    print("Out")
    winsound.Beep(588, 700)  #D
    print("With")
    winsound.Beep(784, 700)  #G
    print("Glee")
    winsound.Beep(740, 1200) #F#
    time.sleep(1)
    print("Rudolph")
    winsound.Beep(522, 500)  #C
    winsound.Beep(588, 500)  #D
    print("The")
    winsound.Beep(522, 300)  #C
    print("Red")
    winsound.Beep(440, 500)  #A
    print("Nosed")
    winsound.Beep(784, 700)  #F#
    print("Reindeer")
    winsound.Beep(660, 500)  #E
    winsound.Beep(588, 1000) #D
    time.sleep(0.5)
    print("You'll")
    winsound.Beep(588, 300)  #D
    print("Go")
    winsound.Beep(660, 300)  #E
    print("Down")
    winsound.Beep(588, 300)  #D
    print("In")
    winsound.Beep(660, 300)  #E
    print("History!")
    winsound.Beep(588, 1000) #D
    winsound.Beep(880, 1000) #A
    winsound.Beep(784, 3000) #G
    time.sleep(1)
    x = "-"
    for i in range(1, 28):
        print(x, end="")
    print("")
    print("[+] Song Completed [+]")
    x = "-"
    for i in range(1, 28):
        print(x, end="")
    print("")
    print("")
    input("Press Enter to play another song: ")
    print("")
