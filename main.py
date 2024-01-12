#  import all the necessary libraries

import cv2
import mediapipe as mp
import pyautogui

#  open webcam
my_webcam = cv2.VideoCapture(0)  # '0' is for default laptop camera
if not my_webcam.isOpened():
    print("Cannot Open Webcamera.")
    exit()

#  create an object for hand tracking from 'solutions' module.
my_hands = mp.solutions.hands.Hands()

#  create an object for drawing utils or points in image using 'solutions' module.
utils = mp.solutions.drawing_utils

#  create a loop to continuously read the frames
while True:
    #  capture frame by frame.
    success, image = my_webcam.read()
    #  if not true print error statement.
    if not success:
        print("Cannot read frame.")
        break
    #  convert the image from BGR to RGB format.
    image_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #  determining the height, width, channel(success) from shape of image.
    frame_height, frame_width , success = image.shape
    #  we will now store the hand markings in the variable called 'output'.
    #  'output' only accepts rgb image format.
    output = my_hands.process(image_RGB)
    #  storing hand landmark for every hand in the webcam to variable 'hands'.
    hands = output.multi_hand_landmarks
    # creating a statement for hands detection.
    if hands:
        for hand in hands:
            utils.draw_landmarks(image, hand)  # draw utils on every hand detected in hands.
            landmarks = hand.landmark  # store the landmark of each hand in variable landmarks.
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                if id == 8:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(0, 255, 255), thickness=3)
                    x2 = x
                    y2 = y
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 // 4
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 5)

        #  adjust volume based on distance.
        if distance > 50 :
            pyautogui.press("volumeup")
        else:
            pyautogui.press("volumedown")

    cv2.imshow("Hand Brightness Control", image)
    key = cv2.waitKey(10)
    if key == 27:
        break

my_webcam.release()
cv2.destroyAllWindows()




