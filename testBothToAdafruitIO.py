import time
import board
import adafruit_scd4x
import aranet4
from Adafruit_IO import RequestError, Client, Feed

# @brief Adafruit IO set up
# @param ADAFRUIT_IO_USERNAME NAME OF USER
# @param ADAFRUIT_IO_KEY KEY provided by Adafruit IO
# @param aio connecting as a client.
ADAFRUIT_IO_USERNAME = "SSOLCHOI"
ADAFRUIT_IO_KEY = "aio_feVe71MMaK7z3azpmAgTbmj3CjL1"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
#####################################################

# @brief scd41 measurement set-up.
# @param count counting a number of sensor measurement taken place.
# @param i2c enable i2c using import board
# @param scd4x enable scd41
# @param scd4x.start_periodic_measurement() start periodic measurement
count = 0
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
print("Serial number:", [hex(i) for i in scd4x.serial_number])

scd4x.start_periodic_measurement()
###################################################################

# @brief aranet4 air-quality measuring device setup
# @param device_rasp server ip
# 
device_rasp = "EB:9A:51:3D:33:93"

print("Waiting for first measurement....")

while True:
    if scd4x.data_ready:
        count = count + 1
        print("%d." % count)
        print("SCD41 CO2: %d ppm" % scd4x.CO2)
        aio.send("testscd41", scd4x.CO2)
#         print("SCD41 Temperature: %0.1f *C" % scd4x.temperature)
#         print("SCD41 Humidity: %0.1f %%" % scd4x.relative_humidity)
        current = aranet4.client.get_current_readings(device_rasp)
        print("Aranet4 CO2: %d ppm" % current.co2)
        aio.send("testaranet4", current.co2)
        print()
    time.sleep(20)
    ## Test1. 11:42 started
    ## Aranet bluetooth connection takes place every 10 second.
    ## Test2. 12:25 started
    ## Test2. 13:10 ended
    ## To disable power sleep mode, rebooted.
    ## Bluetooth issue generated.
    ## Having a hard time connecting to bluetooth.
    ## reboot all the devices & seems working fine.
    ## Test3. 13:34 started
    ## I physically went close to th SCD41 sensor &
    ## CO2 level jumped up high.
    ## aranet sensor did not respond to this change as much?
    ## b/c the value didn't jump up as high. (85.)
    ## 2:26 still working without any issue.
    ## Test4. 2:27 test ended
