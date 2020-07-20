import cv2
import sys
import numpy 
from numpy import array
import serial
import time

# Gets the name of the image file (filename) from sys.argv
cap= cv2.VideoCapture(0)
if cap.isOpened():

    ret,frame=cap.read()

else:

    ret= False

img1 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
a1 = frame
imagePath = "C:\Python27\images1\img1.jpg"
cv2.imwrite(imagePath,img1)


cascPath = "haarcascade_frontalface_alt2.xml"

# This creates the cascade classifcation from file 


faceCascade = cv2.CascadeClassifier(cascPath)#or cv2.CascadeClassifier(cascPath1)

# The image is read and converted to grayscale

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# The face or faces in an image are detected
# This section requires the most adjustments to get accuracy on face being detected.


faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(1,1),flags = cv2.CASCADE_SCALE_IMAGE)
print("Detected {0} faces!".format(len(faces)))
a =(len(faces))
# This draws a green rectangle around the faces detected
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Faces Detected", image)
cv2.imwrite("output.jpg", image)
cv2.waitKey( )
cv2.destroyAllWindows()


a1 = cv2.imread('output.jpg')
height,width = image.shape[:2]
print (image.shape)


start_row,start_col = int(0),int(0)
end_row, end_col = int(height),int(width*0.5)
c = numpy.index_exp[start_row:end_row , start_col:end_col]
cropped_top = a1[c]
print (start_row,end_row)
print (start_col,end_col)
cv2.imshow("Cropped_top", cropped_top)
cv2.imwrite("cropped_top.jpg", cropped_top)
faceCascade = cv2.CascadeClassifier(cascPath)#or cv2.CascadeClassifier(cascPath1)

# The image is read and converted to grayscale

image1 = cv2.imread('cropped_top.jpg')
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

# The face or faces in an image are detected
# This section requires the most adjustments to get accuracy on face being detected.


faces1 = faceCascade.detectMultiScale(gray,scaleFactor=1.035
                                      ,minNeighbors=5,minSize=(1,1),flags = cv2.CASCADE_SCALE_IMAGE)
print("Detected {0} faces!".format(len(faces1)))
r = len(faces1)
print ("the value of r is",r)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
start_row,start_col = int(0),int(width*0.5)
end_row, end_col = int(height),int(width)
d = numpy.index_exp[start_row:end_row , start_col:end_col]
cropped_bot = a1[d]
print start_row,end_row
print start_col,end_col
cv2.imshow("Cropped_bottom", cropped_bot)
cv2.imwrite("cropped_bot.jpg", cropped_top)
faceCascade = cv2.CascadeClassifier(cascPath)#or cv2.CascadeClassifier(cascPath1)

# The image is read and converted to grayscale

image2 = cv2.imread('cropped_bot.jpg')
gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

# The face or faces in an image are detecte
# This section requires the most adjustments to get accuracy on face being detected.


faces2 = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(1,1),flags = cv2.CASCADE_SCALE_IMAGE)
print("Detected {0} faces!".format(len(faces2)))
s = len(faces2)
print ("value of s is",s)
cv2.waitKey(0)'
cv2.destroyAllWindows()'''
start_row,start_col = int(0),int(width*0.5)
end_row, end_col = int(height),int(width)
d = numpy.index_exp[start_row:end_row , start_col:end_col]
cropped_bot = a1[d]
print (start_row,end_row)
print (start_col,end_col)
cv2.imshow("Cropped_bottom", cropped_bot)
cv2.imwrite("cropped_bot.jpg", cropped_top)

s = a-r
print("Detected " +format(s)+ " faces!")
print("value of s is",s)
cv2.waitKey(0)
cv2.destroyAllWindows()




ser = serial.Serial('COM7', 9600)

def led_on_off():
   
    
    if ((r >= 1) & (s>=1)):
        print("LED 1&2&3&4 is on...")
        time.sleep(0.1) 
        ser.write('H') 
        
    if ((r == 0) & (s >= 1)):
        print("LEDs 3&4 is on...")
        time.sleep(0.1)
        ser.write('L')
        
    if ((r >= 1) & (s == 0)):
        print("LED 1&2 is on...")
        time.sleep(0.1) 
        ser.write('K') 
       
    if ((s == 0) & (r == 0)):
        print("LEDs are off...")
        time.sleep(0.1)
        ser.write('M')

        


time.sleep(2) # wait for the serial connection to initialize



led_on_off()
