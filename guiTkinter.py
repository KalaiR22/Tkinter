from tkinter import *
count = 0
foods = ['pizza','hamburger', 'donuts' ]
def clickme():
    global count 
    count+=1
    print(count)


def display():
    name = entry.get()
    print('hello {}'.format(name))



def checkbuttonHandle():
    if agree.get() == 1:
        print("You agree to the statement :)")
    else:
        print("You don't agree to the statement :(")


def foodHandle():
    if  y.get() == 0:
        print('you choosed pizza')
    elif  y.get() == 1:
        print('you choosed hamburger')
    elif  y.get() == 2:
        print('you choosed donuts')
    else:
        print("you doesn't choose anything")


window = Tk()
window.geometry("500x500")
window.title('GUI program')
icon = PhotoImage(file='python.png')
window.iconphoto(True,icon)
window.config(background='black')

#label
labelImage = PhotoImage(file='python.png')
label = Label(window, text='This is a stuff From TKinter', 
              font=('Arial', 20, 'bold'),
              relief=SUNKEN,
              image=labelImage,
              compound='bottom'
              )
label.pack()

#button
button = Button(window, text='click me!', command=clickme)
button.pack()

#entry
entry = Entry(window)
entry.pack()
button_submit = Button(window, text='submit', command=display)
button_submit.pack()

#checkbutton
agree = IntVar()
checkbutton = Checkbutton(window, text='I agree to the above statement.',
                          variable=agree,
                          onvalue=1,
                          offvalue=0,
                          command=checkbuttonHandle)
checkbutton.pack()

#radiobuttons
y = IntVar()
for food in range(len(foods)):
    radio_button = Radiobutton(window, text=foods[food],
                               padx=10,
                               value=food,
                               variable=y,
                                command=foodHandle )
    radio_button.pack(anchor=W)
window.mainloop()