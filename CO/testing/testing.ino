#define SENSITIVITY_CODE  4.46
#define TIA_GAIN  100000
#define FIXED_GAIN   pow(10,-6)
//#define SENSOR_CALIBRATION_FACTOR SENSITIVITY_CODE*TIA_GAIN*FIXED_GAIN
//#define GAS_CONCENTRATION (1/SENSOR_CALIBRATION_FACTOR)*(Vgas-Vref)

float Vreg;
float Vref;
float Vgas;
float V5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Vreg = analogRead(A0);
  Vref = analogRead(A1);
  Vreg = Vreg / 1024 * 5;
  Vref = Vref / 1024 * 5;
  
  V5 = analogRead(A3);
  Serial.print("Vreg: ");
  Serial.println(Vreg);
  //Serial.println(Vreg/675.84*3.3);
  Serial.print("Vref: ");
  Serial.println(Vref);
  Serial.print("V5: ");
  Serial.println(V5);
}
float concentration(){
  Vgas = analogRead(A2);
  //Serial.println(Vgas);
  Vgas = Vgas / 1024 * 5;
  //Serial.println(Vgas);

  //float Vgas0 = ( Vreg * float(2000 + 1000000) ) / ( float(2000 + 2000000) * 1000.0 )
  //Serial.print("Vgas-Vref: ");
  //Serial.println(Vgas-Vref);
  float SENSOR_CALIBRATION_FACTOR = SENSITIVITY_CODE * TIA_GAIN * FIXED_GAIN;
  Serial.println(SENSOR_CALIBRATION_FACTOR);
  float GAS_CONCENTRATION = (1/SENSOR_CALIBRATION_FACTOR)*(Vgas-Vref);
  Serial.println(GAS_CONCENTRATION);
  return (float)GAS_CONCENTRATION*1000;

}
//void loop(){}
void loop() {
  // put your main code here, to run repeatedly:
  static int count = 0;
  float ppm = concentration();

  // Serial.println("Vreg: " + String(Vreg));
  // Serial.println("Vref: " + String(Vref));
  // Serial.println("Vgas: " + String(Vgas));
  Serial.print(count++);
  Serial.print(": ");
  Serial.print((int)ppm);
  Serial.println(" ppb.");

  delay(2000);

}
