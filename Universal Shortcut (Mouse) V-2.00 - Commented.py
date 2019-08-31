import subprocess, pyautogui, os, time
import tkinter as tk


class values:
    x = '' ### User URL
    top = tk.Tk() ### IDK why I named it top, but it's shorter than tk.TK()
    var = tk.StringVar() ### Converts the Custom Text Box to A string that Python can Interpret
    realWebsite = True ### This is the variable that controls whether the browser opens, Boolean cuz I hate myself
    E1 = '' ### This is What the user Enters in the custom text box
    custom = False ### Controls whether the custom() function is active
    ip = 0 ### Can either be 1 or 0, depending on what the ping() function returns
    suffix = '' ### Controls the ending of the URL ie: .com,.org, shit like that
def ping(): ### Pings Website that the user types in to make sure it a real website, my god this looks like a mess
    values.ip = os.system('ping www.' + values.x + '.com -n 1 >>text.txt') ### Uses bach to ping website to make sure it exists
    if values.ip == 1: 
        values.ip = os.system('ping www.' + values.x + '.org -n 1 >>text.txt') 
        if values.ip == 1:
            values.realWebsite = False
            return
        else: ### Controls Suffix, may add more in the future, but I doubt it
            values.suffix = '.org'
            values.realWebsite = True
            return
    else:
        values.realWebsite = True
        return

    
def windowOpen(): ### Opens the internet browswer of choice, FireFox is better
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


def reddit(): ###This and Youtube are the same, customString() is the only one that is different 
    values.x = 'old.reddit'
    ping()
    if values.realWebsite == False:
        print('Website Unavailible')
        return
    else:
        windowOpen()
        time.sleep(.5) ### You gotta wait like .5 seconds because for some reason it stopped working before I put it in, just randomly
        pyautogui.typewrite('https://' + 'old.reddit' + '.com')
        pyautogui.press('enter')
        print('...Done')



def youtube(): ### Same as Reddit, exactly
    values.x = 'youtube'
    ping()
    if values.realWebsite == False:
        print('Website Unavailible')
        return
    else:
        windowOpen()
        time.sleep(.5)
        pyautogui.typewrite('https://' + 'youtube' + '.com')
        pyautogui.press('enter')
        print('...Done')


def custom(): ### Oh doggy, does this control the custom URL
    L1 = tk.Label(values.top, text="Gimme dat link: ") ### This is the Label for the Text Box, Kinda unessicary
    L1.pack() ### Still don't know what tk Pack(), reallly wish I did.
    values.E1 = tk.Entry(values.top, textvariable = values.var) ### This is where the textbox that you type in is.
    values.E1.pack() ### Really wish I knew what pack() did.
    go = tk.Button(text = 'Go!', command = customString) ### sudo Enter key cuz I can't be fucked to find a good listener library
    go.pack()

def customString(): ### Jesus this was a giant pain in the ass. This is like the other 2, but this has a little more meat ---
                    ### including a whole ass nother' fucntion that controls whether this one even works.
    values.x = values.E1.get() ### This is where the tk.Stringvar() comes in, because E1 is a stringvar, python can get a real string from E1
    ping()
    if values.realWebsite == True:
        if values.suffix == '': ### If .org and .com don't work no suffix is assigned and it errors out. 
            print('Website Unavailible')
            return
        windowOpen()
        time.sleep(.5)
        pyautogui.typewrite('https://' + values.x + values.suffix) ### Only place suffix is used lol
        pyautogui.press('enter')
        print('...Done')
        values.custom = False
    else: ### Standard ass Error checking
        print('Website Unavailible')
        return

    
reddit = tk.Button(text = 'Reddit', command = reddit) ###}
youtube = tk.Button(text = 'Youtube', command = youtube)###}} These are the buttons, and they just link to the functions, they call em' you could say
custom = tk.Button(text = 'Custom', command = custom)###}
reddit.pack()
youtube.pack()
custom.pack()
values.top.mainloop() ### Wish I knew what mainloop() did, all I know is that it makes the tk library work

