from tkinter import *
import serial
from time import sleep
import smtplib
import getpass

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
address = input("Email: ")
password = getpass.getpass()
server.login(address,password)
password = ""

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600)  # open serial port
 
def show_values():
    if entry1.get() == "":
        entry1.insert(0," P1")
    if entry2.get() == "":
        entry2.insert(0," P2")
    player1 = str(entry1.get())
    player2 = str(entry2.get())
    result = [player1, player2, str(sets.get()),str(legs.get())]
    for i in range(len(result)):
        result[i] = result[i][:3].upper()
    s = ""
    for i in result:
        s += str(i)
        s += ";"
    ser.write(bytes("START".encode()))
    line = ser.readline()
    while (line.decode("UTF-8").strip() != "OK"):
        print(line)
        line = ser.readline()

    ser.write(bytes(s.encode()))
    root.destroy()

while True:
    throws = []
    p1throws = []
    p2throws = []
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

  
    Label(root, text="Sets:").grid(row=3,column=0)
    legs = Scale(root, orient=HORIZONTAL, from_=0, to=50, length=1000)
    legs.grid(row=3,column=1)
    legs.set(1)
    Label(root, text="Legs:").grid(row=4,column=0)
    sets = Scale(root, orient=HORIZONTAL, from_=0, to=50, length=1000)
    sets.grid(row=4,column=1)
    sets.set(1)
    
    button1 = Button(root, text = "QUIT", command=root.destroy).grid(row=7,column=0, sticky="WE")
    button2 = Button(root, text = "START", command=show_values).grid(row=7,column=1, columnspan=2, sticky="WE")

    entry1.focus()
    mainloop()
    
    matchdata = ser.readline()
    matchdata = matchdata.decode("UTF-8", "ignore")
    matchdata = matchdata.strip().split(";")
    print(matchdata)
    line = ser.readline()
    line = line.decode("UTF-8", "ignore")
    line = line.strip().split(";")
    inputted = line[0]
    while inputted != "END":
        print(line)
        if inputted != "EXIT":
            player = line[1]
        if (inputted == "BACK") and (len(throws) > 0):
            print(throws)
            ser.write(bytes(str(throws[-1]).encode()))
            throws.pop(-1)
            if player == "p1":
                p1throws.pop(-1)
            elif player == "p2":
                p2throws.pop(-1)
        elif inputted == "LEG":
            throws = []
        elif inputted == "EXIT":
            print("EXITTED LINE:", line)
            break
        elif inputted.isdigit():
            throws.append(int(inputted))
            if player == "p1":
                p1throws.append(int(inputted))
            elif player == "p2":
                p2throws.append(int(inputted))
        line = ser.readline()
        line = line.decode("UTF-8", "ignore")
        line = line.strip().split(";")
        inputted = line[0]
    result = line
    print(result)    
    new_match = str(input("want a new match? y/n  "))
    if new_match.strip() == 'n':
        import statistics
        msg = "" + line[2] + " " + str(line[3]) + " - " + str(line[5]) + " " + line[6] 
        print(type(msg))
        msg += "\n" + matchdata[0] + " avarage: " + str(statistics.mean(p1throws))
        msg += "\n" + matchdata[1] + " avarage: " + str(statistics.mean(p2throws))
        print(msg)
        sendto = input("Who to send?: ")
        server.sendmail(address,sendto,msg)
        server.close()
        print("Email sent")
        break