import mediapipe as mp
import cv2 as cv

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

img = cv.imread('Photos/nah1')

font = cv.FONT_HERSHEY_SIMPLEX
text = 'Hello, World!'
org = (10, 100)
font_scale = 2
color = (0, 255, 0)
thickness = 2
cv.putText(img, text, org, font, font_scale, color, thickness)

cap = cv.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

# To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv.cvtColor(image, cv.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        
    # Get the positions of the landmarks for the index and middle fingers
        index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        index_finger_knuckle = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_MCP]
        middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        middle_finger_knuckle = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP]
        
    # For "Nah Çekme operations"
        thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP] #4
        index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP] #8
        middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP] #12
        index_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP] #7
        middle_finger_dip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP] #11
        index_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]
        middle_finger_pip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP]

        # Check if the user is pointing their index finger
        #First we need to find whether hand is pointing up or down
        if( thumb_tip.y > index_finger_tip.y):
            if(thumb_tip.x > index_finger_tip.x):
                if( 
              #Controlling y axis
              ((index_finger_tip.y > thumb_tip.y and middle_finger_tip.y > thumb_tip.y) or 
                (index_finger_dip.y > thumb_tip.y and middle_finger_dip.y > thumb_tip.y)
                ) 
                or                
                #Controlling x axis     
                (thumb_tip.x > middle_finger_pip.x and thumb_tip.x < index_finger_pip.x)
                ):
                   print("Nah Cekme!")



    # Flip the image horizontally for a selfie-view display.
    cv.imshow('MediaPipe Hands', cv.flip(image, 1))
    if cv.waitKey(5) & 0xFF == 27:
      break
cap.release()