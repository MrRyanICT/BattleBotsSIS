#pip install playsound==1.2.2
from playsound import playsound
#playsound('Resources/sounds/explosion.wav')

# import sys  # to access the system
# #import from Python Packages
# import cv2
# img1 = cv2.imread("Resources/images/explosion.png", cv2.IMREAD_ANYCOLOR)
# while True:
# 	cv2.imshow("Explosion", img1)
# 	cv2.waitKey(0)
# 	sys.exit()  # to exit from all the processes
# cv2.destroyAllWindows()  # destroy all windows
playsound('Resources/sounds/Lose.wav')

def PlayMedia(name):
    if name == "enemy down":
        playsound('Resources/sounds/Enemy Down.wav')
        print('ENEMY SHIP HIT!')
    elif name == "explosion":
        playsound('Resources/sounds/explosion.wav')
        print('BOOM!')
    elif name == "lose":
        playsound('Resources/sounds/Lose.wav')
        print('YOU LOST!')
    elif name == "miss":
        playsound('Resources/sounds/miss.wav')
        print('YOU MISSED!')
    elif name == "ship down":
        playsound('Resources/sounds/Ship down.wav')
        print('YOUR SHIP HAS SUNK!')



