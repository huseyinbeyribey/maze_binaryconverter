import cv2
import numpy as np
resim = cv2.imread("AS.png",1)
resizeResim = cv2.resize(resim,(120,120))
dizin = np.zeros( (120,120) , dtype = int )
sayac = 0
yesilBulundu = False
kirmiziBulundu = False

for a in range (0,120):
    for b in range (0,120):

        piksel = resizeResim[a,b]



        if piksel [0] <= 80 and piksel[1] >= 160 and piksel [2] <= 90 and yesilBulundu == False:


            yesilBulundu = True
            dizin[a,b] = 2


        elif piksel [0] <=50 and piksel[1] <= 50 and piksel [2] >= 150 and yesilBulundu == True:

            resizeResim[a,b] = [255,255,255]



        if piksel [0] <= 50 and piksel[1] <= 50 and piksel [2] >= 150 and kirmiziBulundu == False:

            kirmiziBulundu = True
            dizin[a,b] = 3


        elif piksel [0] <=50 and piksel[1] <= 50 and piksel [2] >= 150 and kirmiziBulundu == True:

            resizeResim[a,b] = [255,255,255]


        if piksel [0] <= 50 and piksel[1] <= 50 and piksel [2] <= 50:

            dizin[a,b] = 1

for x in range (0,120):
    for y in range (0,120):
            with open("a.txt","a") as file :
                sayac +=1
                file.write(str(dizin[x,y]))
                if sayac % 120 == 0:
                    file.write("\n")
