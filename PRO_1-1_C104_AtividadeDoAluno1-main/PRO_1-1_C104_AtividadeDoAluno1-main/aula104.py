import cv2

img=cv2.imread("solar-system.jpg")
print(img)
#cinza=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#cv2.imshow("fogueteCinza",cinza)

cv2.putText(img,"sol",(100,80),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255))
cv2.putText(img,"mercurio",(100,180),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"venus",(190,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"terra",(280,160),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"marte",(370,270),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"jupiter",(560,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"saturno",(740,120),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"urano",(970,140),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.putText(img,"saturno",(1110,145),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,0,0))
cv2.imshow("foguete",img)
cv2.waitKey(0)