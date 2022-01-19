import random
import cv2

video_path = "" #Enter video path including file extension 
data_path = "" #Enter path to folder ending with "/"

vid = cv2.VideoCapture(video_path)
length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))

for i in [random.randrange(0, length-1) for i in range(1000)]:
    vid.set(1, i)
    ret, still = vid.read()
    print(f'{data_path}{i}.jpg')
    cv2.imwrite(f'{data_path}{i}.jpg', still)
