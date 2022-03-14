import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

video = cv2.VideoCapture(0)
video.set(3,640)
video.set(4,480)
video.set(cv2.CAP_PROP_FPS,60)
segmentor = SelfiSegmentation()
fps = cvzone.FPS()

backgrounds = os.listdir('images')
backgroundList = []
backgroundIndex = 0
for backgroundPath in backgrounds:
    background = cv2.imread(f'images/{backgroundPath}')
    backgroundList.append(background)

while True:
    try:
        success,vid = video.read()
        vidOut = segmentor.removeBG(vid,backgroundList[backgroundIndex],threshold=0.4)
        fps.update(vid)

        vidStck = cvzone.stackImages([vid,vidOut],2,1)
        cv2.imshow("Video",vidStck)
    except:
        print("Bu index te tutulan bir background yok!")
        backgroundIndex -= 1
    key = cv2.waitKey(1)
    if key == ord('a'):
        backgroundIndex -= 1
    elif key == ord('d'):
        backgroundIndex += 1
    elif key == ord('q'):
        break
