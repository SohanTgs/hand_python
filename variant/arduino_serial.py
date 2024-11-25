import cv2
import mediapipe as mp
import serial
import time

# Initialize Mediapipe Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize Serial Communication (adjust COM port and baud rate)
arduino = serial.Serial(port='COM3', baudrate=9600, timeout=1)
time.sleep(2)  # Wait for Arduino to initialize

# Access the webcam
cap = cv2.VideoCapture(0)

# Function to map values from one range to another
def map_value(value, in_min, in_max, out_min, out_max):
    return int((value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for a mirror effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Example: Extract landmark positions for wrist and fingertips
            wrist = hand_landmarks.landmark[0]
            thumb_tip = hand_landmarks.landmark[4]
            index_tip = hand_landmarks.landmark[8]
            middle_tip = hand_landmarks.landmark[12]
            ring_tip = hand_landmarks.landmark[16]
            pinky_tip = hand_landmarks.landmark[20]

            # Map normalized coordinates (0 to 1) to servo angles (0 to 180 degrees)
            wrist_angle = map_value(wrist.y, 0, 1, 0, 180)
            thumb_angle = map_value(thumb_tip.y, 0, 1, 0, 180)
            index_angle = map_value(index_tip.y, 0, 1, 0, 180)
            middle_angle = map_value(middle_tip.y, 0, 1, 0, 180)
            ring_angle = map_value(ring_tip.y, 0, 1, 0, 180)
            pinky_angle = map_value(pinky_tip.y, 0, 1, 0, 180)

            # Send servo angles to Arduino
            data = f"W{wrist_angle}T{thumb_angle}I{index_angle}M{middle_angle}R{ring_angle}P{pinky_angle}\n"
            arduino.write(data.encode('utf-8'))
            print(f"Sent: {data}")

    # Display the video feed
    cv2.imshow("Hand Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
arduino.close()
cv2.destroyAllWindows()
