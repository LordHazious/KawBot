import time
import random
from random import randint
from threading import Thread
import pyautogui
import keyboard

print("""\
                _                     _                                             
   ___ ___   __| |_   _  ___ ___   __| | ___  ___   ___ ___  _ __ ___    __ _ _   _ 
  / __/ _ \ / _` | | | |/ __/ _ \ / _` |/ _ \/ __| / __/ _ \| '_ ` _ \  / _` | | | |
 | (_| (_) | (_| | |_| | (_| (_) | (_| |  __/\__ \| (_| (_) | | | | | || (_| | |_| |
  \___\___/ \__,_|\__, |\___\___/ \__,_|\___||___(_)___\___/|_| |_| |_(_)__,_|\__,_|
                  |___/                                                             
Kaw Bot v0.1
""")


# move click function
def moveClick(ld, ln):
    ok = pyautogui.locateOnScreen('C:/KawBot/img/ok.png')
    if ok is not None:
        moveClick('C:/KawBot/img/ok.png', 'Ok')

    count = 1
    while count <= 3:
        locate = pyautogui.locateOnScreen(ld)
        if locate is not None:
            print("Located: ", ln)
            break
        else:
            print("Locating: ", ln, " attempt: ", count)
            count += 1

    if locate is not None:
        center = pyautogui.center(locate)
        if center is not None:
            xy = list(center)
            x = xy[0]
            y = xy[1]

            # Random move
            cX = random.choice([True, False])
            cY = random.choice([True, False])

            # if fight move to Do action
            if ln == "Fight":
                x = x + 195
                y = y + 70
            elif ln == "Assassinate":
                x = x + 195
                y = y + 310

            # True = Higher False = Lower
            if cX == True:
                x = x + randint(2, 6)
            else:
                x = x - randint(2, 6)

            if cY == True:
                y = y + randint(2, 6)
            else:
                y = y - randint(2, 6)

            pyautogui.moveTo(x, y, duration=0.2)

            print("Moved to: ", ln)

            if ln == "Repeat":
                count = 0
                while count <= 30:
                    ok = pyautogui.locateOnScreen('C:/KawBot/img/ok.png')
                    if ok is None:
                        pyautogui.click(x, y)
                        time.sleep(0.2)
                        count += 1
                    elif ok is not None:
                        moveClick('C:/KawBot/img/ok.png', 'Ok')
                        break
                    else:
                        print("Error")
        else:
            pyautogui.click(x, y)

            print("Clicked: ", ln)
            time.sleep(0.2)
    else:
        print("error: ", ln)
        return


def fa():
    moveClick('C:/KawBot/img/continue.png', 'Continue')
    moveClick('C:/KawBot/img/repeat.png', 'Repeat')
    moveClick('C:/KawBot/img/close.png', 'Close')
    return


class Bot(Thread):

    while True:
    
        # move and click on Kingdom
        #moveClick('C:/KawBot/img/kingdom.png', 'Kingdom')
    
        # move and click on clan
        #moveClick('C:/KawBot/img/clan.png', 'clan')

        # move and click on Kingdom
        #moveClick('C:/KawBot/img/view_epic_battle.png', 'View Epic Battle')

        # move and click on Attack
        #moveClick('C:/KawBot/img/attack.png', 'Attack')

        # move and click on Fight, continue and repeat attack
        #moveClick('C:/KawBot/img/select.png', 'Fight')
        #fa()
    
        # move and click on Attack
        moveClick('C:/KawBot/img/attack.png', 'Attack')

        # move and click on Fight, continue and repeat attack
        moveClick('C:/KawBot/img/select.png', 'Assassinate')
        #fa()


class KeyboardListener(Thread):
    toggle = 0

    while True:
        try:
            if keyboard.is_pressed('ctrl+space'):
                if toggle == 1:
                    time.sleep(0.3)
                    toggle = 0
                    bot.stop()
                    print("Bot Stopped!")
                elif toggle == 0:
                    time.sleep(0.3)
                    toggle = 1
                    bot.start()
                    print("Bot Started!")
                else:
                    print("error")
        except:
            pass


if __name__ == '__main__':
    kb_listener = KeyboardListener()
    bot = Bot()

    kb_listener.start()
    bot.stop()

