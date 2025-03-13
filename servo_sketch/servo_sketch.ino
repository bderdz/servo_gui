#include <Servo.h>

#define SERV_PIN 9

Servo serv;
int angle;

void setup() {
  Serial.begin(9600);

  serv.attach(SERV_PIN);
  serv.write(0);
}

void loop() {
  if(Serial.available() > 0) {
    int current_angle = Serial.read();
    Serial.println(current_angle);

    if(angle != current_angle && (current_angle >= 0 && current_angle <= 180)) {
      angle = current_angle;
      serv.write(angle);
    }
  }
}
