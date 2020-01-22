# dartsScoreboard

Darts match marker project with remote controll and email notification.
![wiring](https://github.com/dontrajik/dartsScoreboard/blob/master/src/wiring.png)

## Requirements
+ Hardware:
  + Arduino uno
  + Raspberry pi with usb
  + 1x 10Kohm Potentiometer
  + 1x 270ohm Resistor
  + [1x 1602A LCD Board](https://www.openhacks.com/uploadsproductos/eone-1602a1.pdf)
  + [1x vs1838b IR Reciever Module](http://eeshop.unl.edu/pdf/VS1838-Infrared-Receiver-datasheet.pdf)
  + [Remote Contoller](https://www.amazon.co.uk/Samsung-BN59-01303A-Remote-Control/dp/B07JPLDLNS)
  + Breadboard
  + Cables
+ Software:
  + The .ino file uploaded to the arduino with the following libraries:
    + [LiquidCrystal Library](https://www.arduino.cc/en/Reference/LiquidCrystal)
    + [IRremote Library](https://www.arduinolibraries.info/libraries/i-rremote)
  + The .py file onto the Raspberry Pi with the following packages:
    + Tkinter
    + smtplib
    + getpass
    + serial
    + statistics

## How it is made?
I started by mapping the hex codes of the buttons on my remote controller, and made communication between the Arduino and Raspberry. After that made the GUI of the python program and the LCD handling. Then coded the basic darts rules to be able to mark down a darts match. Finally I maded an email notification with the result and the rough avarages of each player.

## How to use
1. Connect all the wiring.
   ![loading](https://github.com/dontrajik/dartsScoreboard/blob/master/src/loading.png)

2. Execute the python file
	
	- ```python <PATH>dartsScoreboadStartWindow.py```
	
3. If you want to use email notification type in your email address and password else leave it blank.

	To use email notification you have to enable "Less secure apps" in your [google account>>Security](https://myaccount.google.com/security)
	
4. Then fill Player1 and Player2. Only the first 3 letter will be shown. If you leave it empty the player names will be "p1" and "p2"

5. Select how much legs and sets you want to play. (FIRST TO)

6. Click START
  ![gui](https://github.com/dontrajik/dartsScoreboard/blob/master/src/gui.png)

  1. Then you can start inputting the score and then press "OK" button.
     ![OKbutton](https://github.com/dontrajik/dartsScoreboard/blob/master/src/OKbutton.png)
     ![inmatch](https://github.com/dontrajik/dartsScoreboard/blob/master/src/inmatch.png)

7. If you misstype you can UNDO the last score by pressing "RETURN" and "OK" twice, but you cant revert the checkouts.
   ![RETURNbutton](https://github.com/dontrajik/dartsScoreboard/blob/master/src/RETURNbutton.png)

8. You can finish any match at any time by pressing "EXIT".
   ![EXITbutton](https://github.com/dontrajik/dartsScoreboard/blob/master/src/EXITbutton.png)

9. If you inserted an email address at the start of the program now you can add an email to send the results and the avararages to. If you leave it blank you don't send email notification.

10. Now you can choose if you want to play a new match or not.
    ```Want a new match?```  ```y/n```
    
