#import library
from tkinter import *

#initialize window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title(" Website Blocker")
color = "lightblue"
root.configure(background = color)

#heading
Label(root, text = 'WEBSITE BLOCKER' , font = 'arial 20 bold',background = color).pack()
Label(root,text = 'group2' , font = 'arial 20 bold',background = color).pack(side = BOTTOM)

#path of our host file ang ip address 
host_path = 'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

#ENTER WEBSITE

Label(root, text= 'please enter Website to block :', font = 'arial 13 bold ',background = color).place(x=10,y=30)
Websites = Text(root, font = 'arial 10', height ='2', width = '40', wrap = WORD,padx = 5, pady=5)
Websites.place(x = 140, y =60)

#block function
def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                Label(root, text = 'is Blocked already' , font = 'arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address + " " + website + '\n')
                Label(root, text = "Blocked", font = 'arial 12 bold').place(x=230,y =200)

block_btn = Button(root, text = 'BLOCK' , font = 'arial 12 bold', command = Blocker, width = 6 , bg = 'red', activebackground = 'sky blue')
block_btn.place(x = 230, y =150)


root.mainloop
    
