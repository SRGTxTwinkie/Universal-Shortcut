import pyautogui, os, subprocess, time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = False ### No longer needed because program is stable, with **no** loops that I have found
browserOpen = False ### Checks to see if the browser is actually open, just another error checker
x = ''

pyautogui.size()

def opener(): ### Opens browser and pings website to make sure it 
    global x, browserOpen
    z = 0
    
    ip = os.system('ping www.' + x + '.com -n 1 >>text.txt') ### Uses bash to ping website to make sure it exists
    if ip == 0:
        try:
            for y in range(5): ### Retries 5 times because sometimes it errors out for permissions 
                try:
                    subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])### Bottom***
                    browserOpen = True
                    end()
                except:
                    try:
                        subprocess.call(['C:\Program Files (x86)\Google\Chrome'])### Calls Chrome second because Chrome is bad
                        browserOpen = True
                        end()
                    except: 
                        if z >= 5:
                            print('Failed')
                        else:
                            print('Retrying')
                            time.sleep(.5)
                            z += 1
        except:
            print('an error has occured')### Ideally this should never appear, because of the other error checking. But that remains to be seen
    else:
        print('That website doesn\'t exist')
def position():
    while True:
        print(pyautogui.position())

def meat():### The shortcut handler, and goes into opener to actually interpret the user website 
    global x

    x = input('Website Name: ')

    if x.upper() in ('R','REDDIT'):
        x = 'old.reddit'
        opener()
    elif x.upper() == 'CURSOR': ### Prints out location of the cursor, not needed anymore
        position()
    elif x.upper() == 'Y':
        x = 'youtube'
        opener()
    else:
        opener()


def end(): ### The function that types the actual user string, it goes as fast as the browser supports, which is why Edge and IE do not work
    if browserOpen == True:
        time.sleep(1)
        pyautogui.typewrite('https://' + x + '.com')
        pyautogui.press('enter')
        print('...Done')
        meat()
    else:
        print('BROWSER OPEN ERROR')
        meat()

meat()

### ***Looks for FireFox and chrome, Edge doesn't support fast key inputs and I'm too lazy to add just Edge and Internet Exploer support 
