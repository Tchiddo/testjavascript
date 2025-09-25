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

def cookie():
  while True:
    pg.moveTo(2786, 306)
    pg.click()
    pg.moveTo(2787, 480)
    pg.click()
    pg.sleep(0.4)
    pg.moveTo(2802, 174)
    pg.click()
    pg.sleep(0.2)
cookie()






    # EMAIL_URL = "https://www.gmail.com"
    # EMAIL_TO = "michael.sekol@mahoningctc.com"
    # SUBJECT = "Hello Nerds"
    # BODY = "Welcome to Software Engineering"