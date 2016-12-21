import sys
import time
import winsound

# print('''
#
#
#       .----.                     .         .-.                .    .    .-.
#         / .-.                   /         (_) )-.            /    /    (_) )-.                 /
#        /  `-'.  .-.    .-.     /   .-.       / __)    .-.   /    /        /   \  .-._..-.     /-.
# ..-.   /  /    )/   )  (   )   /  ./.-'_     /    `. ./.-'_ /    /        /     )(   )(       /   )
# `.   /_.(__. '/   (    `-/-'_/_.-(__.'     /'      )(__.'_/_.-_/_.-   .-/  `--'  `-'  `---'_/    \
#   `-'              `--._/               (_/  `----'                  (_/     `-._)
#
#
# -------------------------------------------------------------------------
# Dec 2016 v1.0
# by
# NoDisassemble.me
# -------------------------------------------------------------------------
# ''')

# Begin Jingle Bell Rock
def jingleBellRock():
    loading = "Generating Song and Lyrics for Jingle Bell Rock: [-------------------]"
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
    for i in range(1, 32):
        print(x, end="")
    print("")
    print("[+] Plying Jingle Bell Rock [+]")
    x = "-"
    for i in range(1, 32):
        print(x, end="")
    print("")
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(588, 300)  #D
    winsound.Beep(588, 300)  #D
    print("Bell")
    winsound.Beep(588, 700)  #D
    print("Jingle")
    winsound.Beep(554, 300)  #C#
    winsound.Beep(554, 300)  #C#
    print("Bell")
    winsound.Beep(554, 700)  #C#
    print("Jingle")
    winsound.Beep(494, 300)  #B
    winsound.Beep(554, 300)  #C#
    print("Bell")
    winsound.Beep(494, 700)  #B
    print("Rock")
    winsound.Beep(370, 500)  #F#
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(494, 300)  #B
    winsound.Beep(554, 300)  #C#
    print("Bells")
    winsound.Beep(494, 700)  #B
    print("Swing")
    winsound.Beep(370, 500)  #F#
    print("And")
    winsound.Beep(440, 300)  #A
    print("Jingle")
    winsound.Beep(494, 300)  #B
    winsound.Beep(554, 300)  #C#
    print("Bells")
    winsound.Beep(494, 700)  #B
    print("Ring")
    winsound.Beep(392, 500)  #G
    time.sleep(0.7)
    print("Snowing")
    winsound.Beep(330, 500)  #E
    winsound.Beep(370, 500)  #F#
    print("And")
    winsound.Beep(370, 300)  #F#
    print("Blowing")
    winsound.Beep(440, 500)  #A
    winsound.Beep(494, 500)  #B
    print("Up")
    winsound.Beep(440, 300)  #A
    print("Bushels")
    winsound.Beep(330, 500)  #E
    winsound.Beep(370, 500)  #F#
    print("Of")
    winsound.Beep(392, 300)  #G
    print("Fun")
    winsound.Beep(440, 700)  #A
    time.sleep(0.7)
    print("Now")
    winsound.Beep(494, 500)  #B
    print("The")
    winsound.Beep(440, 300)  #A
    print("Jingle")
    winsound.Beep(494, 500)  #B
    winsound.Beep(440, 500)  #A
    print("Hop")
    winsound.Beep(494, 300)  #B
    print("Has")
    winsound.Beep(494, 500)  #B
    print("Begun")
    winsound.Beep(330, 500)  #E
    winsound.Beep(330, 500)  #E
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(588, 300)  # D
    winsound.Beep(588, 300)  # D
    print("Bell")
    winsound.Beep(588, 700)  # D
    print("Jingle")
    winsound.Beep(554, 300)  # C#
    winsound.Beep(554, 300)  # C#
    print("Bell")
    winsound.Beep(554, 700)  # C#
    print("Jingle")
    winsound.Beep(494, 300)  # B
    winsound.Beep(554, 300)  # C#
    print("Bell")
    winsound.Beep(494, 700)  # B
    print("Rock")
    winsound.Beep(370, 500)  # F#
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(494, 300)  # B
    winsound.Beep(554, 300)  # C#
    print("Bells")
    winsound.Beep(494, 700)  # B
    print("Chime")
    winsound.Beep(370, 500)  # F#
    print("In")
    winsound.Beep(440, 300)  # A
    print("Jingle")
    winsound.Beep(494, 300)  # B
    winsound.Beep(554, 300)  # C#
    print("Bells")
    winsound.Beep(494, 700)  # B
    print("Time")
    winsound.Beep(392, 500)  # G
    time.sleep(0.7)
    print("Dancing")
    winsound.Beep(330, 500)  # E
    winsound.Beep(370, 500)  # F#
    print("And")
    winsound.Beep(370, 300)  # F#
    print("Prancing")
    winsound.Beep(440, 500)  # A
    winsound.Beep(494, 500)  # B
    print("In")
    winsound.Beep(440, 300)  # A
    print("Jingle")
    winsound.Beep(330, 500)  # E
    winsound.Beep(370, 500)  # F#
    print("Bell")
    winsound.Beep(392, 300)  # G
    print("Square")
    winsound.Beep(440, 700)  # A
    time.sleep(0.5)
    print("In")
    winsound.Beep(494, 500)  # B
    print("The")
    winsound.Beep(494, 300)  # B
    print("Frosty")
    winsound.Beep(554, 500)  # C#
    winsound.Beep(440, 500)  # A
    print("Air")
    winsound.Beep(588, 1000)  # D
    time.sleep(0.7)
    print("What")
    winsound.Beep(588, 500)  # D
    print("A")
    winsound.Beep(588, 300)  # D
    print("Bright")
    winsound.Beep(660, 700)  # E
    print("Time")
    winsound.Beep(588, 700)  # D
    print("Its")
    winsound.Beep(494, 500)  # B
    print("The")
    winsound.Beep(588, 300)  # D
    print("Right")
    winsound.Beep(660, 700)  # E
    print("Time")
    winsound.Beep(588, 700)  # D
    time.sleep(0.5)
    print("To")
    winsound.Beep(588, 300)  # D
    print("Rock")
    winsound.Beep(588, 500)  # D
    print("The")
    winsound.Beep(554, 500)  # C#
    print("Night")
    winsound.Beep(494, 500)  # B
    print("Away")
    winsound.Beep(440, 300)  # A
    winsound.Beep(370, 1000)  # F#
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(588, 300)  # D
    winsound.Beep(588, 500)  # D
    print("Bell")
    winsound.Beep(660, 700)  # E
    print("Time")
    winsound.Beep(588, 700)  # D
    print("Is")
    winsound.Beep(494, 500)  # B
    print("A")
    winsound.Beep(588, 300)  # D
    print("Swell")
    winsound.Beep(660, 700)  # E
    print("Time")
    winsound.Beep(588, 700)  # D
    time.sleep(0.7)
    print("To")
    winsound.Beep(440, 300)  # A
    print("Go")
    winsound.Beep(440, 500)  # A
    print("Gliding")
    winsound.Beep(494, 300)  # B
    winsound.Beep(494, 300)  # B
    print("In")
    winsound.Beep(494, 500)  # B
    print("A")
    winsound.Beep(494, 500)  # B
    print("One")
    winsound.Beep(554, 300)  # B
    print("Horse")
    winsound.Beep(494, 500)  # B
    print("Sleigh")
    winsound.Beep(440, 700)  # A
    time.sleep(0.7)
    print("Giddy")
    winsound.Beep(588, 300)  # D
    winsound.Beep(588, 300)  # D
    print("Up")
    winsound.Beep(588, 700)  # D
    print("Jingle")
    winsound.Beep(554, 300)  # C#
    winsound.Beep(554, 300)  # C#
    print("Horse")
    winsound.Beep(554, 700)  # C#
    print("Pick")
    winsound.Beep(494, 500)  # B
    print("Up")
    winsound.Beep(554, 300)  # C#
    print("Your")
    winsound.Beep(494, 700)  # B
    print("Feet")
    winsound.Beep(370, 500)  # F#
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(494, 300)  # B
    winsound.Beep(554, 500)  # C#
    print("Around")
    winsound.Beep(494, 300)  # B
    winsound.Beep(370, 700)  # F#
    print("The")
    winsound.Beep(440, 500)  # A
    print("Clock")
    winsound.Beep(494, 1000)  # B
    time.sleep(0.7)
    print("Mix")
    winsound.Beep(494, 500)  # B
    print("And")
    winsound.Beep(588, 300)  # D
    print("A")
    winsound.Beep(588, 300)  # D
    print("Mingle")
    winsound.Beep(660, 300)  # E
    winsound.Beep(660, 500)  # E
    print("In")
    winsound.Beep(588, 300)  # D
    print("The")
    winsound.Beep(588, 300)  # D
    print("Jingling")
    winsound.Beep(440, 300)  # A
    winsound.Beep(440, 300)  # A
    winsound.Beep(588, 500)  # D
    print("Feet")
    winsound.Beep(660, 700)  # E
    time.sleep(0.5)
    print("That's")
    winsound.Beep(588, 300)  # D
    print("The")
    winsound.Beep(494, 500)  # B
    print("Jingle")
    winsound.Beep(554, 300)  # C#
    winsound.Beep(588, 300)  # D
    print("Bell")
    winsound.Beep(660, 700)  # E
    print("Rock")
    winsound.Beep(588, 1000)  # D
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(588, 300)  # D
    winsound.Beep(588, 300)  # D
    print("Bell")
    winsound.Beep(588, 700)  # D
    print("Jingle")
    winsound.Beep(554, 300)  # C#
    winsound.Beep(554, 300)  # C#
    print("Bell")
    winsound.Beep(554, 700)  # C#
    print("Jingle")
    winsound.Beep(494, 300)  # B
    winsound.Beep(554, 300)  # C#
    print("Bell")
    winsound.Beep(494, 700)  # B
    print("Rock")
    winsound.Beep(370, 500)  # F#
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(494, 300)  # B
    winsound.Beep(554, 300)  # C#
    print("Bells")
    winsound.Beep(494, 700)  # B
    print("Chime")
    winsound.Beep(370, 500)  # F#
    print("In")
    winsound.Beep(440, 300)  # A
    print("Jingle")
    winsound.Beep(494, 300)  # B
    winsound.Beep(554, 300)  # C#
    print("Bells")
    winsound.Beep(494, 700)  # B
    print("Time")
    winsound.Beep(392, 500)  # G
    time.sleep(0.7)
    print("Dancing")
    winsound.Beep(330, 500)  # E
    winsound.Beep(370, 500)  # F#
    print("And")
    winsound.Beep(370, 300)  # F#
    print("Prancing")
    winsound.Beep(440, 500)  # A
    winsound.Beep(494, 500)  # B
    print("In")
    winsound.Beep(440, 300)  # A
    print("Jingle")
    winsound.Beep(330, 500)  # E
    winsound.Beep(370, 500)  # F#
    print("Bell")
    winsound.Beep(392, 300)  # G
    print("Square")
    winsound.Beep(440, 700)  # A
    time.sleep(0.5)
    print("In")
    winsound.Beep(494, 500)  # B
    print("The")
    winsound.Beep(494, 300)  # B
    print("Frosty")
    winsound.Beep(554, 500)  # C#
    winsound.Beep(440, 500)  # A
    print("Air")
    winsound.Beep(588, 1000)  # D
    time.sleep(0.7)
    print("What")
    winsound.Beep(588, 500)  # D
    print("A")
    winsound.Beep(588, 300)  # D
    print("Bright")
    winsound.Beep(660, 700)  # E
    print("Time")
    winsound.Beep(588, 700)  # D
    print("Its")
    winsound.Beep(494, 500)  # B
    print("The")
    winsound.Beep(588, 300)  # D
    print("Right")
    winsound.Beep(660, 700)  # E
    print("Time")
    winsound.Beep(588, 700)  # D
    time.sleep(0.5)
    print("To")
    winsound.Beep(588, 300)  # D
    print("Rock")
    winsound.Beep(588, 500)  # D
    print("The")
    winsound.Beep(554, 500)  # C#
    print("Night")
    winsound.Beep(494, 500)  # B
    print("Away")
    winsound.Beep(440, 300)  # A
    winsound.Beep(370, 1000)  # F#
    time.sleep(0.7)
    print("Jingle")
    winsound.Beep(588, 300)  # D
    winsound.Beep(588, 500)  # D
    print("Bell")
    winsound.Beep(660, 700)  # E
    print("Time")
    winsound.Beep(588, 700)  # D
    print("Is")
    winsound.Beep(494, 500)  # B
    print("A")
    winsound.Beep(588, 300)  # D
    print("Swell")
    winsound.Beep(660, 700)  # E
    print("Time")
    winsound.Beep(588, 700)  # D
    time.sleep(0.7)
    print("To")
    winsound.Beep(440, 300)  # A
    print("Go")
    winsound.Beep(440, 500)  # A
    print("Gliding")
    winsound.Beep(494, 300)  # B
    winsound.Beep(494, 300)  # B
    print("In")
    winsound.Beep(494, 500)  # B
    print("A")
    winsound.Beep(494, 500)  # B
    print("One")
    winsound.Beep(554, 300)  # B
    print("Horse")
    winsound.Beep(494, 500)  # B
    print("Sleigh")
    winsound.Beep(440, 700)  # A
    time.sleep(0.7)
    print("Giddy")
    winsound.Beep(588, 300)  # D
    winsound.Beep(588, 300)  # D
    print("Up")
    winsound.Beep(588, 700)  # D
    print("Jingle")
    winsound.Beep(554, 300)  # C#
    winsound.Beep(554, 300)  # C#
    print("Horse")
    winsound.Beep(554, 700)  # C#
    print("Pick")
    winsound.Beep(494, 500)  # B
    print("Up")
    winsound.Beep(554, 300)  # C#
    print("Your")
    winsound.Beep(494, 700)  # B
    print("Feet")
    winsound.Beep(370, 500)  # F#
    time.sleep(0.5)
    print("Jingle")
    winsound.Beep(494, 300)  # B
    winsound.Beep(554, 500)  # C#
    print("Around")
    winsound.Beep(494, 300)  # B
    winsound.Beep(370, 700)  # F#
    print("The")
    winsound.Beep(440, 500)  # A
    print("Clock")
    winsound.Beep(494, 1000)  # B
    time.sleep(0.7)
    print("Mix")
    winsound.Beep(494, 500)  # B
    print("And")
    winsound.Beep(588, 300)  # D
    print("A")
    winsound.Beep(588, 300)  # D
    print("Mingle")
    winsound.Beep(660, 300)  # E
    winsound.Beep(660, 500)  # E
    print("In")
    winsound.Beep(588, 300)  # D
    print("The")
    winsound.Beep(588, 300)  # D
    print("Jingling")
    winsound.Beep(440, 300)  # A
    winsound.Beep(440, 300)  # A
    winsound.Beep(588, 500)  # D
    print("Feet")
    winsound.Beep(660, 700)  # E
    time.sleep(0.5)
    print("That's")
    winsound.Beep(588, 500)  # D
    print("The")
    winsound.Beep(494, 300)  # B
    print("Jingle")
    winsound.Beep(554, 300)  # C#
    winsound.Beep(588, 300)  # D
    print("Bell")
    winsound.Beep(440, 700)  # A
    time.sleep(0.7)
    print("That's")
    winsound.Beep(588, 500)  # D
    print("The")
    winsound.Beep(494, 300)  # B
    print("Jingle")
    winsound.Beep(554, 300)  # C#
    winsound.Beep(588, 300)  # D
    print("Bell")
    winsound.Beep(440, 700)  # A
    time.sleep(0.7)
    print("That's")
    winsound.Beep(588, 500)  # D
    print("The")
    winsound.Beep(494, 300)  # B
    print("Jingle")
    winsound.Beep(554, 300)  # C#
    winsound.Beep(588, 300)  # D
    print("Bell")
    winsound.Beep(660, 700)  # E
    print("Rock")
    winsound.Beep(588, 2000) # D
# End Song
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