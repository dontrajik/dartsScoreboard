from tkinter import *
import serial
from time import sleep

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)  # open serial port
    
def show_values():
    if entry1.get() == "":
        entry1.insert(0," P1")
    if entry2.get() == "":
        entry2.insert(0," P2")
    result = [str(entry1.get()), str(entry2.get()), str(legs.get()), str(sets.get())]
    for i in range(len(result)):
        result[i] = result[i][:3].upper()
    print (result)
    s = ""
    for i in result:
        s += str(i)
        s += ";"
    ser.write(bytes("START".encode()))
    line = ser.readline()
    while (line.decode("UTF-8").strip() != "OK"):
        print(line)
        line = ser.readline()
    print(s)

    ser.write(bytes(s.encode()))
    root.destroy()

while True:
    throws = []
    root = Tk()
    root.title("Darts Scoreboard")
    root.geometry("350x200")
    root.resizable(0,0)

    Label(root, text="Name should be 3 character long(ENG, TOM, EDD...)", padx=10).grid(row=0,columnspan=2, sticky="N")
    root.grid_columnconfigure(1, weight=1)
    
    Label(root, text="Player1:").grid(row=1, column=0)
    entry1 = Entry(root, width=100)
    entry1.grid(row=1, column=1)
    Label(root, text="Player2:").grid(row=2, column=0)
    entry2 = Entry(root, width=100)
    entry2.grid(row=2, column=1)

    Label(root, text="Zero == Infinite").grid(row=3,columnspan=2, sticky="NS")
    Label(root, text="Sets:").grid(row=4,column=0)
    legs = Scale(root, orient=HORIZONTAL, from_=0, to=50, length=1000)
    legs.grid(row=4,column=1)
    legs.set(1)
    Label(root, text="Legs:").grid(row=5,column=0)
    sets = Scale(root, orient=HORIZONTAL, from_=0, to=50, length=1000)
    sets.grid(row=5,column=1)
    sets.set(1)
    
    button1 = Button(root, text = "QUIT", command=root.destroy).grid(row=6,column=0, sticky="WE")
    button2 = Button(root, text = "START", command=show_values).grid(row=6,column=1, columnspan=2, sticky="WE")

    entry1.focus()
    mainloop()

    line = ""
    while line[:3] != "END":
        line = ser.readline()
        line = line.decode("UTF-8", "ignore").strip()
        print(line)
        if (line == "BACK") and (len(throws) > 0):
            print(throws)
            ser.write(bytes(str(throws[-1]).encode()))
            throws.pop(-1)
        elif line == "LEG":
            throws = []
        if (line == "EXIT"):
            break
        elif line.isdigit():
            throws.append(int(line))
    new_match = str(input("want a new match? y/n  "))
    if new_match == 'n':
        break