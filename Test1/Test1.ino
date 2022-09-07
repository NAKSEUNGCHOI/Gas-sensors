#include <Arduino.h>
#include <Adafruit_TinyUSB.h>

#define PIN12 24

int count = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(19200);
  while (!Serial) { delay(1); } // wait until serial console is open, remove if not tethered to computer
  pinMode(LED_BUILTIN, OUTPUT);
}
// antenna must be connected..  
void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(count);
  Serial.print(". Hey! ");
  Serial.println("");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(200);
  digitalWrite(LED_BUILTIN, LOW);
  delay(200);
  count = count + 1;
  if(count > 10){
    exit(0);
  }
  
}
