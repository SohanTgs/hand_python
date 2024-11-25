#include <Servo.h>

// Create servo objects for wrist and fingers
Servo wristServo;
Servo thumbServo;
Servo indexServo;
Servo middleServo;
Servo ringServo;
Servo pinkyServo;

void setup() {
  Serial.begin(9600);  // Start serial communication
  wristServo.attach(3);  // Connect wrist servo to pin 3
  thumbServo.attach(5);  // Connect thumb servo to pin 5
  indexServo.attach(6);  // Connect index servo to pin 6
  middleServo.attach(9);  // Connect middle servo to pin 9
  ringServo.attach(10);  // Connect ring servo to pin 10
  pinkyServo.attach(11);  // Connect pinky servo to pin 11
}

void loop() {
  if (Serial.available()) {
    String data = Serial.readStringUntil('\n');  // Read data until newline
    int wrist_angle = data.substring(data.indexOf('W') + 1, data.indexOf('T')).toInt();
    int thumb_angle = data.substring(data.indexOf('T') + 1, data.indexOf('I')).toInt();
    int index_angle = data.substring(data.indexOf('I') + 1, data.indexOf('M')).toInt();
    int middle_angle = data.substring(data.indexOf('M') + 1, data.indexOf('R')).toInt();
    int ring_angle = data.substring(data.indexOf('R') + 1, data.indexOf('P')).toInt();
    int pinky_angle = data.substring(data.indexOf('P') + 1).toInt();

    // Move servos to the specified angles
    wristServo.write(wrist_angle);
    thumbServo.write(thumb_angle);
    indexServo.write(index_angle);
    middleServo.write(middle_angle);
    ringServo.write(ring_angle);
    pinkyServo.write(pinky_angle);

    // Debug output
    Serial.print("Wrist: "); Serial.print(wrist_angle);
    Serial.print(", Thumb: "); Serial.print(thumb_angle);
    Serial.print(", Index: "); Serial.print(index_angle);
    Serial.print(", Middle: "); Serial.print(middle_angle);
    Serial.print(", Ring: "); Serial.print(ring_angle);
    Serial.print(", Pinky: "); Serial.println(pinky_angle);
  }
}
