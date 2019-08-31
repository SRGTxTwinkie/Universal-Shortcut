import subprocess, pyautogui, os
import tkinter as tk


class values:
    x = ''
    top = tk.Tk()
    var = tk.StringVar()
    realWebsite = True
    E1 = ''
    custom = False
    var = tk.StringVar()
    ip = 0
    suffix = ''

def ping():
    print(values.x)
    values.ip = os.system('ping www.' + values.x + '.com -n 1 >>text.txt') ### Uses bach to ping website to make sure it exists
    if values.ip == 1:
        values.ip = os.system('ping www.' + values.x + '.org -n 1 >>text.txt')
        if values.ip == 1:
            values.realWebsite = False
            print('22')
            return
        else:
            values.suffix = '.org'
            values.realWebsite = True
            return
    else:
        print('30')
        values.realWebsite = True
        return
        

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
    if values.realWebsite == False:
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
    if values.realWebsite == False:
        print('Website Unavailible')
        return
    else:
        windowOpen()
        pyautogui.typewrite('https://' + 'youtube' + '.com')
        pyautogui.press('enter')
        print('...Done')

def custom():
    L1 = tk.Label(values.top, text="Gimme dat link: ")
    L1.pack()
    values.E1 = tk.Entry(values.top, textvariable = values.var)
    values.E1.pack()
    go = tk.Button(text = 'Go!', command = customString)
    go.pack()
    
    
    

def customString():
    values.x = values.E1.get()
    ping()
    if values.realWebsite == True:
        if values.suffix == '':
            print('Website Unavailible')
            return
        windowOpen()
        pyautogui.typewrite('https://' + values.x + values.suffix)
        pyautogui.press('enter')
        print('...Done')
        values.custom = False
    else:
        print('Website Unavailible')
        return


reddit = tk.Button(text = 'Reddit', command = reddit)
youtube = tk.Button(text = 'Youtube', command = youtube)
custom = tk.Button(text = 'Custom', command = custom)
reddit.pack()
youtube.pack()
custom.pack()
values.top.mainloop()

