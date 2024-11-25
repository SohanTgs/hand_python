import cv2
import mediapipe as mp

# Initialize Mediapipe Hand Detection
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Access the webcam
cap = cv2.VideoCapture(0)

# Function to format and print hand landmarks to console
def display_landmarks(landmarks):
    print("\nHand Landmarks:")
    print(f" 0. WRIST:             ({landmarks[0].x:.2f}, {landmarks[0].y:.2f}, {landmarks[0].z:.2f})")
    print(f" 1. THUMB_CMC:         ({landmarks[1].x:.2f}, {landmarks[1].y:.2f}, {landmarks[1].z:.2f})")
    print(f" 2. THUMB_MCP:         ({landmarks[2].x:.2f}, {landmarks[2].y:.2f}, {landmarks[2].z:.2f})")
    print(f" 3. THUMB_IP:          ({landmarks[3].x:.2f}, {landmarks[3].y:.2f}, {landmarks[3].z:.2f})")
    print(f" 4. THUMB_TIP:         ({landmarks[4].x:.2f}, {landmarks[4].y:.2f}, {landmarks[4].z:.2f})")
    print(f" 5. INDEX_FINGER_MCP:  ({landmarks[5].x:.2f}, {landmarks[5].y:.2f}, {landmarks[5].z:.2f})")
    print(f" 6. INDEX_FINGER_PIP:  ({landmarks[6].x:.2f}, {landmarks[6].y:.2f}, {landmarks[6].z:.2f})")
    print(f" 7. INDEX_FINGER_DIP:  ({landmarks[7].x:.2f}, {landmarks[7].y:.2f}, {landmarks[7].z:.2f})")
    print(f" 8. INDEX_FINGER_TIP:  ({landmarks[8].x:.2f}, {landmarks[8].y:.2f}, {landmarks[8].z:.2f})")
    print(f" 9. MIDDLE_FINGER_MCP: ({landmarks[9].x:.2f}, {landmarks[9].y:.2f}, {landmarks[9].z:.2f})")
    print(f"10. MIDDLE_FINGER_PIP: ({landmarks[10].x:.2f}, {landmarks[10].y:.2f}, {landmarks[10].z:.2f})")
    print(f"11. MIDDLE_FINGER_DIP: ({landmarks[11].x:.2f}, {landmarks[11].y:.2f}, {landmarks[11].z:.2f})")
    print(f"12. MIDDLE_FINGER_TIP: ({landmarks[12].x:.2f}, {landmarks[12].y:.2f}, {landmarks[12].z:.2f})")
    print(f"13. RING_FINGER_MCP:   ({landmarks[13].x:.2f}, {landmarks[13].y:.2f}, {landmarks[13].z:.2f})")
    print(f"14. RING_FINGER_PIP:   ({landmarks[14].x:.2f}, {landmarks[14].y:.2f}, {landmarks[14].z:.2f})")
    print(f"15. RING_FINGER_DIP:   ({landmarks[15].x:.2f}, {landmarks[15].y:.2f}, {landmarks[15].z:.2f})")
    print(f"16. RING_FINGER_TIP:   ({landmarks[16].x:.2f}, {landmarks[16].y:.2f}, {landmarks[16].z:.2f})")
    print(f"17. PINKY_MCP:         ({landmarks[17].x:.2f}, {landmarks[17].y:.2f}, {landmarks[17].z:.2f})")
    print(f"18. PINKY_PIP:         ({landmarks[18].x:.2f}, {landmarks[18].y:.2f}, {landmarks[18].z:.2f})")
    print(f"19. PINKY_DIP:         ({landmarks[19].x:.2f}, {landmarks[19].y:.2f}, {landmarks[19].z:.2f})")
    print(f"20. PINKY_TIP:         ({landmarks[20].x:.2f}, {landmarks[20].y:.2f}, {landmarks[20].z:.2f})")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)  # Flip for a mirror effect
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks and connections
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Overlay landmark indices and coordinates
            for idx, landmark in enumerate(hand_landmarks.landmark):
                h, w, c = frame.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)
                label = f"{idx}: ({landmark.x:.2f}, {landmark.y:.2f}, {landmark.z:.2f})"
                cv2.putText(frame, label, (cx, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

            # Print landmarks to the console
            display_landmarks(hand_landmarks.landmark)

    # Display the video feed
    cv2.imshow("Hand Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
