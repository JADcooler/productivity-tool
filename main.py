#sudo pip3 install keyboard
import keyboard
import pyautogui as pya
import pyperclip  # handy cross-platform clipboard text handler
import time

def copy_clipboard():
    #pya.hotkey('ctrl', 'c')
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.1)  # ctrl-c is usually very fast but your program maybe faster
    return pyperclip.paste()

def writeIt(out):
    keyboard.write(out)

## TO USE, highlight text and press the combination ##
def uppercaseit():
    print("ADS")
    var = copy_clipboard()
    print("input is ",var)
    out = var.upper()
    writeIt(out)
    print(out)
    
keyboard.add_hotkey("shift+a", uppercaseit,  suppress=True)   

keyboard.wait()

#while True:
    # Wait for the next event.
        
#       print('space was pressed')



# double clicks on a position of the cursor
# pya.doubleClick(pya.position())

