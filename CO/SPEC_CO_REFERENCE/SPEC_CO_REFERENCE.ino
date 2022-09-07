#include "SPEC_CO_REFERENCE.h"

void setup() {
  Serial.begin(9600);
  Serial.println("-----PROGRAM START-----");
  Serial.println("Zeroing CO sensor...");

  zeroSensor(10);
  
  Serial.print("voffset = ");
  Serial.print(voffset);
  Serial.print(" mV");
  Serial.println();
  
  Serial.print("tzero = ");
  Serial.print(tzero);
  Serial.print(" degrees C");
  Serial.println();
}

void loop() {
  float conc = getConcentration(5);
  convertX('B');
  Serial.print(conc);
  Serial.println("ppm.");
}

float zeroSensor(int duration) {
  unsigned long startMillis;
  unsigned long durationMs = duration * 1000;
  unsigned long gasSum = 0;//, tempSum = 0;
  unsigned int i = 0;
  
  float tempSum = 0, ran = random(37000, 37200) / 100.0;
  startMillis = millis();
  do {
    gasSum += analogRead(vgasPin);
    tempSum += ran;
    i++;
    delay(1);
  } while((millis() - startMillis) < durationMs);

  float gasAvg = (float)gasSum / (float)i;
  float vgas = gasAvg * Vcc * 1000.0 / 1024.0;
  voffset = vgas - Vref;

  float tempAvg = (float)tempSum / (float)i;
  float vtemp = tempAvg * Vcc / 1024.0;
  tzero = (Tspan / Vsup) * vtemp - Toffset;

  return voffset;
}

float getConcentration(int duration) {
  unsigned long startMillis;
  unsigned long durationMs = duration * 1000;
  unsigned long gasSum = 0; //, tempSum = 0;
  unsigned int i = 0;

  float tempSum = 0, ran = random(37000, 37200) / 100.0;
  startMillis = millis();
  do {
    gasSum += analogRead(vgasPin);
    tempSum += ran; // analogRead(vtempPin);
    i++;
    delay(1);
  } while((millis() - startMillis) < durationMs);

  float gasAvg = (float)gasSum / (float)i;
  float vgas = gasAvg * Vcc * 1000.0 / 1024.0;

  float tempAvg = (float)tempSum / (float)i;
  float vtemp = tempAvg * Vcc / 1024.0;
  float temp = (Tspan / Vsup) * vtemp - Toffset;

  float nA = (vgas - Vref - voffset) / (float)CO_TIA_GAIN * 1000000.0;

  //temperature compensation
  if (temp > 23.0) {
    nA -= O3_A_HI * (temp - tzero);
  } else {
    nA -= O3_A_LO * (temp - tzero);
  }

  return nA / SENS_CODE * (1 - CO_TEMP_C * (temp - tzero));
}

float convertX(char U){
  float pX = 0;
  if (U == 'B')  return pX;
  else if (U == 'M') return (pX/1000.0);
  else return 0;
}
