import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)
 
mat = [[0, 0, 0, 5, 200, 50],[8, 100, 50, 15, 255, 80],[150,150,100 ,180 ,255, 255],[5, 150, 100, 25, 255, 255], [20, 150, 100, 50, 255, 153],[60, 70, 10, 100, 150, 200],[100, 100, 50, 119, 255, 150],[120, 50, 50, 170, 255 ,255] ,  [120, 10, 10, 160, 200, 130],[50, 0, 100, 120, 80 ,255]] 
print(np.shape(mat))


value = [0,0,0,0,0,0,0,0,0,0]






while(1):
 # Take each frame
 _, frame = cap.read()
 frame1 = frame.copy()

 img = cv2.line(frame,(220,256),(310,256),(0,0,0),2)

 crop = frame1[226:286,190:340]

 crop2 = cv2.medianBlur(crop,5)

 crop1 = cv2.GaussianBlur(crop2,(5,5),3)

 crop_gray = cv2.Canny(crop,30,60,apertureSize=3)

 #print( len(crop[0]))
 #frame_blur = cv2.medianBlur(crop,5)

 x_cord = [[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],[0,-1],[0,-1]]
 
 for i in range(10) :
     #print(i)
     hsv = cv2.cvtColor(crop, cv2.COLOR_BGR2HSV)
     lower_lt = np.array([mat[i][0],mat[i][1],mat[i][2]])
     upper_lt = np.array([mat[i][3],mat[i][4],mat[i][5]])
     mask = cv2.inRange(hsv, lower_lt, upper_lt)
     res = cv2.bitwise_and(crop,crop, mask= mask)
     
     for j in range(10) :
      value[i] = 0



     color = 'No'

     if i == 0 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'black'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break
     if i == 1 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'brown'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break 
     if i == 2 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'red'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))  
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break 
     if i == 3 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'orange'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break
     if i == 4 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'yellow'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break
     if i == 5 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'green'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break
     if i == 6 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'blue'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break
     if i == 7 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'violet'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break
     '''
     if i == 8 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'grey'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500 :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break
     '''
     '''
     if i == 9 and mask.sum() > 25000 :
      value[i]  = 1
      color = 'white'
      for t in range(150) :
        #print(np.sum(mask[0:59 , t:t+5]))
        if np.sum(mask[0:59 , t:t+5]) >= 7500  :
              x_cord[i][0] = 1
              x_cord[i][1] = t
              break
     '''

     print (i,mask.sum(),color)
     #print(i,mat[i][0],mat[i][1],mat[i][2],mat[i][3],mat[i][4],mat[i][5])
     
     #cv2.imshow('mask',mask)
     #cv2.imshow('res',res) 
     #time.sleep(0.2)
 
 color_band = [0,0,0,0]
 for t in range(4) : 

     temp = x_cord[0][1]
     for i in range(10) :
       if x_cord[i][1] >= temp :
          temp = x_cord[i][1]
          band = i
     
     if x_cord[band][1] != -1 :
         x_cord[band][1] = -1  
         color_band[t] =  band  
     else :
       color_band[t] = 0


 
 print(color_band)





 resistance = ( 10*color_band[0] + color_band[1] )  *  10**color_band[2]
 print(resistance)


 font = cv2.FONT_HERSHEY_SIMPLEX
 cv2.putText(frame,str(resistance)+' ohm',(200,200), font, 1,(0,0,0),2,cv2.LINE_AA)






 #time.sleep(1)

 cv2.imshow('cropped',crop) 
 cv2.imshow('frame',frame)
 #cv2.imshow('canny',crop)
 
 k = cv2.waitKey(5) & 0xFF
 if k == 27:
   break

cv2.destroyAllWindows()    