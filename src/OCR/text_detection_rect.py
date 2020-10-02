import numpy as np
import cv2
import pytesseract
cap = cv2.VideoCapture(0)

index = 0
text = ""
while(True):
    index = index + 1
    # Capture frame-by-frame
    ret, frame = cap.read()

    cv2.imwrite("1.jpg" ,frame )
    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    # print(frame.shape)
    startX , startY , endX ,endY = int(frame.shape[1] * 0.10), int(frame.shape[0] * 0.30) ,int(frame.shape[1] * 0.90) , int(frame.shape[0] * 0.70)
    cv2.rectangle(frame, (startX, startY),(endX,endY),(0, 0, 255), 2)
    width, height = abs(startX - endX), abs(startY - endY)
    edag = 0
    pts1 = np.float32([[startX - edag, startY - edag], [endX - edag, startY + edag],
                       [startX + edag, endY - edag], [endX + edag, endY + edag]])

    pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    if index == 15:
        index = 0
        M = cv2.getPerspectiveTransform(pts1, pts2)
        dst = cv2.warpPerspective(frame, M, (width, height))
        #dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
        config = ("-l eng --oem 1 --psm 7")
        text = pytesseract.image_to_string(dst, config=config)
    cv2.putText(frame, text, (startX, startY - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    cv2.imshow('frame',frame)

    # text_detection(image="1.jpg", east="frozen_east_text_detection.pb", min_confidence=0.5, width=320,height=320, )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
