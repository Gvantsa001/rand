import cv2
import random


video = cv2.VideoCapture("nature.mp4")


if not video.isOpened():
    print("Error: Could not open the video file!")
rand_s=random.randrange(0,60)
while (video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        cv2.imshow('Frame', frame)
        video.set(cv2.CAP_PROP_POS_MSEC, rand_s*1000)
        cv2.waitKey(0)
        height, width, _ = frame.shape
        rand_x = random.randint(0, width - 1)
        rand_y = random.randint(0, height - 1)
        b, g, r = frame[rand_y, rand_x]
        video.release()
        if ord('q'):
            break
        else:
            break



print(rand_s, (rand_x, rand_y), (r, g, b))



cv2.destroyAllWindows()





