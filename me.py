import cv2
import os
import time
import uuid

IMAGES_PATH = 'Tensorflow\workspace\images\collectedImages'

labels = ['hello', 'thanks', 'yes', 'no', 'iloveyou']
number_imgs = 15

for label in labels:
    !mkdir = {'Tensorflow\workspace\images\collectedImages\\' + label}
    cap = cv2.VideoCapture(0)   # check the number (8:42 in vid)
    print("Collecting images for {}".format(label))
    time.sleep(5)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMAGES_PATH, label. label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        
        if cv2.waitkey(1) & 0xFF == ord('q'):
            break
            
        cap.release()