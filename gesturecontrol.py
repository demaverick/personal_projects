import cv2
import time
import handTracingModule as  htm
import pyautogui

def diff(finger):
    sum =0 
    for i in finger:
        for j in finger:
            sum+= abs(i[1]- j[1]) + abs(i[2] - j[2])
    return sum
vid = cv2.VideoCapture(0)
hCam, wCam = 720,1080
vid.set(3, wCam)
vid.set(4, hCam)
pTime = 0
detector = htm.handDetector()
while(True):
    ret, frame = vid.read()
    cTime = time.time()
    fps = 1/ (cTime - pTime)
    frame = detector.findHands(frame)
    lmlist = detector.findPosition(frame, draw = False)
    if len(lmlist) >0:
        if len(lmlist[0]) > 0:
            try:
                pyautogui.moveTo(int(((lmlist[0][17][1]-199)*1920/400)), int(((lmlist[0][17][2]-149)*1080/200)))
                if abs(lmlist[0][8][2]- lmlist[0][4][2]) < 20:
                    pyautogui.click() 
            except Exception as e:
                continue


    

    frame = cv2.putText(frame, 'FPS :'+ str(int(fps)), (80,80), cv2.FONT_HERSHEY_PLAIN, 5, (0,0, 255), 3 )
    cv2.imshow('frame', frame)
    
    pTime = cTime
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()

cv2.destroyAllWindows()
    
