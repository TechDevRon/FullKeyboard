import keyboard as k
import pyautogui as pag

def shoot():
    pag.mouseDown(button="left"); pag.mouseUp(button="left")
def right():
    xpre, ypre = pag.position()
    xpre+=int(sen)
    pag.moveTo(xpre,ypre)
def left():
    xpre, ypre = pag.position()
    xpre-=int(sen)
    pag.moveTo(xpre,ypre)
def up():
    xpre, ypre = pag.position()
    ypre-=int(sen)
    pag.moveTo(xpre,ypre)
def down():
    xpre, ypre = pag.position()
    ypre+=int(sen)
    pag.moveTo(xpre,ypre)

sen = input("senitivity: ")
rightB = input("Right Button: ")
leftB = input("Left Button: ")
upB = input("Up Button: ")
downB = input("Down Button: ")
shootB = input("Shoot Button: ")


k.add_hotkey(f"{shootB}",shoot)
k.add_hotkey(f"w+{shootB}",shoot)
k.add_hotkey(f"a+{shootB}",shoot)
k.add_hotkey(f"s+{shootB}",shoot)
k.add_hotkey(f"d+{shootB}",shoot)
k.add_hotkey(f"w+a+{shootB}",shoot)
k.add_hotkey(f"w+s+{shootB}",shoot)
k.add_hotkey(f"w+d+{shootB}",shoot)
k.add_hotkey(f"a+w+{shootB}",shoot)
k.add_hotkey(f"a+s+{shootB}",shoot)
k.add_hotkey(f"a+d+{shootB}",shoot)
k.add_hotkey(f"s+w+{shootB}",shoot)
k.add_hotkey(f"s+a+{shootB}",shoot)
k.add_hotkey(f"s+d+{shootB}",shoot)
k.add_hotkey(f"d+w+{shootB}",shoot)
k.add_hotkey(f"d+a+{shootB}",shoot)
k.add_hotkey(f"d+s+{shootB}",shoot)
k.add_hotkey(f"w+a+s+{shootB}",shoot)
k.add_hotkey(f"w+a+s+d+{shootB}",shoot)


k.add_hotkey(f"{rightB}",right)
k.add_hotkey(f"w+{rightB}",right)
k.add_hotkey(f"a+{rightB}",right)
k.add_hotkey(f"s+{rightB}",right)
k.add_hotkey(f"d+{rightB}",right)
k.add_hotkey(f"w+a+{rightB}",right)
k.add_hotkey(f"w+s+{rightB}",right)
k.add_hotkey(f"w+d+{rightB}",right)
k.add_hotkey(f"a+w+{rightB}",right)
k.add_hotkey(f"a+s+{rightB}",right)
k.add_hotkey(f"a+d+{rightB}",right)
k.add_hotkey(f"s+w+{rightB}",right)
k.add_hotkey(f"s+a+{rightB}",right)
k.add_hotkey(f"s+d+{rightB}",right)
k.add_hotkey(f"d+w+{rightB}",right)
k.add_hotkey(f"d+a+{rightB}",right)
k.add_hotkey(f"d+s+{rightB}",right)
k.add_hotkey(f"w+a+s+{rightB}",right)
k.add_hotkey(f"w+a+s+d+{rightB}",right)

k.add_hotkey(f"{leftB}",left)
k.add_hotkey(f"w+{leftB}",left)
k.add_hotkey(f"a+{leftB}",left)
k.add_hotkey(f"s+{leftB}",left)
k.add_hotkey(f"d+{leftB}",left)
k.add_hotkey(f"w+a+{leftB}",left)
k.add_hotkey(f"w+s+{leftB}",left)
k.add_hotkey(f"w+d+{leftB}",left)
k.add_hotkey(f"a+w+{leftB}",left)
k.add_hotkey(f"a+s+{leftB}",left)
k.add_hotkey(f"a+d+{leftB}",left)
k.add_hotkey(f"s+w+{leftB}",left)
k.add_hotkey(f"s+a+{leftB}",left)
k.add_hotkey(f"s+d+{leftB}",left)
k.add_hotkey(f"d+w+{leftB}",left)
k.add_hotkey(f"d+a+{leftB}",left)
k.add_hotkey(f"d+s+{leftB}",left)
k.add_hotkey(f"w+a+s+{leftB}",left)
k.add_hotkey(f"w+a+s+d+{leftB}",left)

k.add_hotkey(f"{upB}",up)
k.add_hotkey(f"w+{upB}",up)
k.add_hotkey(f"a+{upB}",up)
k.add_hotkey(f"s+{upB}",up)
k.add_hotkey(f"d+{upB}",up)
k.add_hotkey(f"w+a+{upB}",up)
k.add_hotkey(f"w+s+{upB}",up)
k.add_hotkey(f"w+d+{upB}",up)
k.add_hotkey(f"a+w+{upB}",up)
k.add_hotkey(f"a+s+{upB}",up)
k.add_hotkey(f"a+d+{upB}",up)
k.add_hotkey(f"s+w+{upB}",up)
k.add_hotkey(f"s+a+{upB}",up)
k.add_hotkey(f"s+d+{upB}",up)
k.add_hotkey(f"d+w+{upB}",up)
k.add_hotkey(f"d+a+{upB}",up)
k.add_hotkey(f"d+s+{upB}",up)
k.add_hotkey(f"w+a+s+{upB}",up)
k.add_hotkey(f"w+a+s+d+{upB}",up)

k.add_hotkey(f"{downB}",down)
k.add_hotkey(f"w+{downB}",down)
k.add_hotkey(f"a+{downB}",down)
k.add_hotkey(f"s+{downB}",down)
k.add_hotkey(f"d+{downB}",down)
k.add_hotkey(f"w+a+{downB}",down)
k.add_hotkey(f"w+s+{downB}",down)
k.add_hotkey(f"w+d+{downB}",down)
k.add_hotkey(f"a+w+{downB}",down)
k.add_hotkey(f"a+s+{downB}",down)
k.add_hotkey(f"a+d+{downB}",down)
k.add_hotkey(f"s+w+{downB}",down)
k.add_hotkey(f"s+a+{downB}",down)
k.add_hotkey(f"s+d+{downB}",down)
k.add_hotkey(f"d+w+{downB}",down)
k.add_hotkey(f"d+a+{downB}",down)
k.add_hotkey(f"d+s+{downB}",down)
k.add_hotkey(f"w+a+s+{downB}",down)
k.add_hotkey(f"w+a+s+d+{downB}",down)

k.wait()
