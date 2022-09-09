# Project Gas(Air quality) sensors

* University of Washington Summer 2022 
* Prof. Vikram Iyer.
* Nakseung Choi | graduate research assistant @ SSOL UW 

## Description

* Prof. Vikram Iyer and I are currently building low power low cost gas sensors (CO2, CO, and black carbon) to help two groups of scientists collect data for their research studies. One group wants to get data in the greater Seattle area to study on where these gasses are coming from. Ultimately, they would like to expand the number of the gas sensors in different locations such that they can compare with other locations for further studies.
The other group would like to place these gas sensors in the middle of moutains in the eastern Washington to study how these gases(CO2 and CO) affect wild animals when there is an unexpected wildfire going. 

* We are currently testing several CO2 sensors to compare their functionality with a commercial device. In the mean time, we just got done with our own PCB design for SPEC CO sensor as well as hardware/software integration. Depending on how precise data the scientists need, we are going to make it acordingly. nRF52480 Arm Cortex-m4 is probably going to be used for the MCU. Using Lora radio communication, a long distance communication interface will also be implemented to update data to the web server such that the scientists can check the data in real time.  

## Authors

- Nakseung Choi
- Please check out my Linkedin: https://www.linkedin.com/in/nakseung-choi-090a1b69/

## Release Notes

* <pre> Wrote a python code that creates a plot for a sensor - avg of two aranets                9-08-2022</pre>
* <pre> wrote a python program using mathplot to graph the CO2 data  (Still testing MA350)       9-07-2022</pre>
* <pre> Testing the MA350                                                                        8-29-2022</pre>
* <pre> arduino / python serial communication script complete. Sending data to adafruitIO        8-26-2022</pre>
* <pre> presentation done. more CO testing / preparing to set up MA350.                          8-24-2022</pre>                                                     
* <pre> got the CO sensor working with noise. more testing...........                            8-23-2022</pre>
* <pre> created a new PCB board and testing..                                                    8-22-2022</pre>
* <pre> presentation preparation2                                                                8-20-2022</pre>
* <pre> presentation preparation                                                                 8-20-2022</pre>
* <pre> Software done. software/hardware integration started                                     8-18-2022</pre>
* <pre> Testing CO sensor 2                                                                      8-17-2022</pre>
* <pre> Testing CO sensor                                                                        8-16-2022</pre>
* <pre> setting up Black Carbon sensor & CO sensor                                               8-15-2022</pre>
* <pre> testing two SCD41s, two aranets, two PASCO2s all together.                               8-15-2022</pre>
* <pre>Debugging Complete. Ready to go for a testing.                                            8-14-2022</pre>
* <pre>Debugging...                                                                              8-12-2022</pre>
* <pre>PASCO2s are going to be tested with scd41 and aranet4 together for the functionality      8-11-2022</pre>
* <pre>Xensiv PAS CO2 coding in python complete.                                                 8-11-2022</pre>
* <pre>Xensiv PAS CO2 working. Testing started.                                                  8-10-2022</pre>
* <pre>Debugging Xensiv PAS CO2                                                                  8-09-2022</pre>
* <pre>Testing Xensiv PAS CO2 manufactured by Infineon.                                          8-08-2022</pre>
* <pre>All parts are done soldering onto the board. Going to test the PCB.                       8-07-2022</pre>
* <pre>CO sensor PCB design complete. About to sorder the CO sensor circuit.                     8-03-2022</pre> 
* <pre>Designing a new circuit for CO sensor due to the chip shortage (LMP9100 out of stock)     8-02-2022</pre>
* <pre>Installed CO2 sensor's in an office with two people.                                      7-28-2022</pre>
* <pre>CO Sensor PCB Design V2 complete.                                                         7-28-2022</pre>
* <pre>CO Sensor PCB Design complete.                                                            7-27-2022</pre>
* <pre>Testing 24 hours success.                                                                 7-26-2022</pre>
* <pre>Testing two SCD41s and two aranets4s on Raspberry pi 3.                                   7-25-2022</pre>
* <pre>Working on PCB design for CO sensor                                                       7-24-2022</pre>
* <pre>Implemented two SCD41s and two aranet4s on Raspberry pi 3 for a testing.                  7-21-2022</pre>
* <pre>Implemented SCD41 on nRF52480 express with Lora Radio (RFM9x)                             7-07-2022</pre>
* <pre>Implemented SCD41 (via I2C) and Aranet4 (via Bluetooth) on Raspberry pi 3 (B type)        7-01-2022</pre>
* <pre>Started                                                                                   6/24/2022</pre>

## License

Copyright @ Nakseung Choi.
