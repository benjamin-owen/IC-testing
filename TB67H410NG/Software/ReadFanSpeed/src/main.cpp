#include <Arduino.h>

void pulse();

long lastTime;
int counter = 0;

void setup() {
  Serial.begin(9600);

  // pinMode(3, INPUT);

  // lastTime = micros();

  pinMode(3, OUTPUT);
  analogWrite(3, 255);

  // attachInterrupt(digitalPinToInterrupt(2), pulse, RISING);
}

void loop() {
  // Serial.println(digitalRead(3));
  // put your main code here, to run repeatedly:
}

void pulse() {

  long currTime = micros();
  long diff = currTime - lastTime;

  Serial.print("Time between: ");
  if (counter >= 10) {
    Serial.println(diff);
    counter = 0;
  } else {
    counter++;
  }
  Serial.print("Conuter: ");
  Serial.println(counter);

  lastTime = currTime;
}