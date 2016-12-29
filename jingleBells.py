import sys
import time
import winsound

# ==========================================================================
#       .----.                     .         .-.                .    .
#         / .-.                   /         (_) )-.            /    /
#        /  `-'.  .-.    .-.     /   .-.       / __)    .-.   /    /   .
# ..-.   /  /    )/   )  (   )   /  ./.-'_     /    `. ./.-'_ /    /   / \\
# `.   /_.(__. '/   (    `-/-'_/_.-(__.'     /'      )(__.'_/_.-_/_.-/ ._)
#   `-'              `--._/               (_/  `----'               /
#
# --------------------------------------------------------------------------
# Description: Jingle Bells.  Must be run from christmasSongs.py
# Keywords: [Python 3, Jingle Bells, Python Christmas Songs]
# Dec 2016 v1.0
# by
# NoDisassemble.me
# --------------------------------------------------------------------------


# Begin Jingle Bells

def jingleBells():
    loading = "Generating Song and Lyrics for Jingle Bells: [-------------------]"
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
    for i in range(1, 28):
        print(x, end="")
    print("")
    print("[+] Plying Jingle Bells [+]")
    x = "-"
    for i in range(1, 28):
        print(x, end="")
    print("")
    time.sleep(1)
    print("Jingle")
    winsound.Beep(660, 500)  # E
    winsound.Beep(660, 500)  # E
    print("Bells")
    winsound.Beep(660, 1000)  # E
    print("Jingle")
    winsound.Beep(660, 500)  # E
    winsound.Beep(660, 500)  # E
    print("Bells")
    winsound.Beep(660, 1000)  # E
    print("Jingle")
    winsound.Beep(660, 500)  # E
    winsound.Beep(784, 500)  # G
    print("All")
    winsound.Beep(523, 700)  # C
    print("The")
    winsound.Beep(587, 300)  # D
    print("Waaaaaaay")
    winsound.Beep(660, 1200)  # E
    time.sleep(1)
    print("Oh")
    winsound.Beep(700, 500)  # F
    print("What")
    winsound.Beep(700, 500)  # F
    print("Fun")
    winsound.Beep(700, 1000)  # F
    print("It")
    winsound.Beep(700, 300)  # F
    print("Is")
    winsound.Beep(700, 500)  # F
    print("To")
    winsound.Beep(660, 500)  # E
    print("Ride")
    winsound.Beep(660, 700)  # E
    print("On")
    winsound.Beep(660, 300)  # E
    print("A")
    winsound.Beep(660, 300)  # E
    print("One")
    winsound.Beep(660, 300)  # E
    print("Horse")
    winsound.Beep(587, 500)  # D
    print("Open")
    winsound.Beep(587, 500)  # D
    winsound.Beep(660, 500)  # E
    print("Sleigh")
    winsound.Beep(587, 1000)  # D
    print("HEEEEEY!")
    winsound.Beep(784, 1000)  # G
    print("")
    time.sleep(0.2)
    print("Jingle")
    winsound.Beep(660, 500)  # E
    winsound.Beep(660, 500)  # E
    print("Bells")
    winsound.Beep(660, 1000)  # E
    print("Jingle")
    winsound.Beep(660, 500)  # E
    winsound.Beep(660, 500)  # E
    print("Bells")
    winsound.Beep(660, 1000)  # E
    print("Jingle")
    winsound.Beep(660, 500)  # E
    winsound.Beep(784, 500)  # G
    print("All")
    winsound.Beep(523, 700)  # C
    print("The")
    winsound.Beep(587, 300)  # D
    print("Waaaaaaay")
    winsound.Beep(660, 1200)  # E
    time.sleep(1)
    print("Oh")
    winsound.Beep(700, 500)  # F
    print("What")
    winsound.Beep(700, 500)  # F
    print("Fun")
    winsound.Beep(700, 1000)  # F
    print("It")
    winsound.Beep(700, 300)  # F
    print("Is")
    winsound.Beep(700, 500)  # F
    print("To")
    winsound.Beep(660, 500)  # E
    print("Ride")
    winsound.Beep(660, 700)  # E
    print("On")
    winsound.Beep(660, 300)  # E
    print("A")
    winsound.Beep(660, 300)  # E
    print("OOOOOOOONE")
    winsound.Beep(784, 1000)  # G
    print("HOOOOOORSE")
    winsound.Beep(784, 1000)  # G
    print("OOOOOOOPEN")
    winsound.Beep(880, 1000)  # A
    winsound.Beep(988, 1000)  # B
    print("SLLLLLLEIGH!!!")
    winsound.Beep(1046, 2500)  # C
    time.sleep(0.5)
    winsound.Beep(523, 500)  # C
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
