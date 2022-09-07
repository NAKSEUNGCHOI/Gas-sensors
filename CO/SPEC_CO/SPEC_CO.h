const float Vcc = 4.96;
const float Vsup = 3.284;
const float R2 = 2000.0;
const float Vref = Vsup * float(R2 + 1000000) / float(R2 + 2000000) * 1000.0;
const float Toffset = 18.0;
const float Tspan = 87.0;

// CO trans-impedance amplifier gain
const long CO_TIA_GAIN = 100000;

// temperature span correction coefficient
const float CO_TEMP_C = 0.25;

// temperature baseline correction coefficients
const float O3_A_HI = 0.04;
const float O3_A_LO = 0.02;

// sensitivity code (nA/ppm)
const float SENS_CODE = 4.24;

// analog pins connected to sensor module
int vgasPin = A2;
//int vtempPin = A3;

// sensor calibration values
float voffset = 0;
float tzero = 20;

