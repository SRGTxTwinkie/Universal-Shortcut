import subprocess, pyautogui, os
from tkinter import *

class values:
    x = ''
    top = Tk()
    realWebsite = True

def ping():
    ip = os.system('ping www.' + values.x + '.com -n 1 >>text.txt') ### Uses bach to ping website to make sure it exists
    if ip == 0:
        return
    else:
        values.realWebsite = False
        

def windowOpen():
    try:
        for y in range(5): ### Retries 5 times because sometimes it errors out for permissions 
            try:
                subprocess.call(['C:\Program Files\Mozilla Firefox\\firefox.exe'])### Bottom***
                browserOpen = True
                return
            except:
                try:
                    subprocess.call(['C:\Program Files (x86)\Google\Chrome'])### Calls Chrome second because Chrome is bad
                    browserOpen = True
                    return
                except: 
                    if z >= 5:
                        print('Failed')
                    else:
                        print('Retrying')
                        time.sleep(.5)
                        z += 1
    except:
        print('an error has occured')### Ideally this should never appear, because of the other error checking. But that remains to be seen

def reddit():
    values.x = 'old.reddit'
    ping()
    if values.realWebsite == True:
        print('Website Unavailible')
        return
    else:
        windowOpen()
        pyautogui.typewrite('https://' + 'old.reddit' + '.com')
        pyautogui.press('enter')
        print('...Done')

def youtube():
    values.x = 'youtube'
    ping()
    windowOpen()
    pyautogui.typewrite('https://' + 'youtube' + '.com')
    pyautogui.press('enter')
    print('...Done')    

reddit = Button(text = 'Reddit', command = reddit)
youtube = Button(text = 'Youtube', command = youtube)
reddit.pack()
youtube.pack()
values.top.mainloop()

