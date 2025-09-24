import pyautogui as pg
import time, sys


pg.FAILSAFE = True # Fling mouse to top left to abort.
print ("Move the mouse to top left, or press Ctrl+C to abort")


#-------------------------------------------------------------------------
# IF YOU NEED TO FIND MOUSE POSITION, UNCOMMENT BELOW AND COMMENT def send_email():
# try:
#     while True:
#         x, y = pg.position()
#         sys.stdout.write(f"\r(x, y) = ({x:4d}, {y:4d})")
#         sys.stdout.flush()
#         time.sleep(0.05) # ~ 20 updates per sec
        
# except KeyboardInterrupt:
#     print ("\nDone")
#-------------------------------------------------------------------------

def send_email():

    pg.moveTo(2269, 60)
    pg.click()
    pg.write("https://www.gmail.com")
    pg.press("enter")
    pg.moveTo(2071, 219)
    pg.sleep(2)
    pg.click()
    pg.sleep(1)
    pg.write("michael.sekol@mahoningctc.com")
    pg.press("enter")
    pg.moveTo(3261, 540)
    pg.click()
    pg.write("Hello Nerds")
    pg.moveTo(3334, 736)
    pg.click()
    pg.write("Welcome to Software Engineering")
    pg.moveTo(3217, 994)
    pg.click()

send_email()



    # EMAIL_URL = "https://www.gmail.com"
    # EMAIL_TO = "michael.sekol@mahoningctc.com"
    # SUBJECT = "Hello Nerds"
    # BODY = "Welcome to Software Engineering"