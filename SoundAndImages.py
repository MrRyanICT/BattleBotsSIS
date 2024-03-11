#pip install playsound==1.2.2
from playsound import playsound
#playsound('Resources/sounds/explosion.wav')

import sys  # to access the system
#import from Python Packages
import cv2
img1 = cv2.imread("Resources/images/explosion.png", cv2.IMREAD_ANYCOLOR)
while True:
	cv2.imshow("Explosion", img1)
	cv2.waitKey(0)
	sys.exit()  # to exit from all the processes
cv2.destroyAllWindows()  # destroy all windows
#from CheckIfHitShip import check_hit
#from Isallsunk import is_all_sunk
def PlaySound(soundname):
    if soundname == "Win":
       playsound('Resources/sounds/Win.wav')
    if soundname == "Lose":
        playsound('Resources/Sounds/Lose.wav')
    if soundname == "Hit":
        playsound('Resources/Sounds/hit.wav')
    if soundname == "miss":
        playsound('Resources/Sounds/miss.wav')

#def Background(Image)

