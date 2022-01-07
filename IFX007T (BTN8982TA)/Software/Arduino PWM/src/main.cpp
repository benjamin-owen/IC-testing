#include <Arduino.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  int pot = analogRead(A0);
  int mapped_value = map(pot, 0, 1023, 0, 255);

  delay(1);

  analogWrite(9, mapped_value);
}