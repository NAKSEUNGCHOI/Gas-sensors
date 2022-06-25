import time
import board
import adafruit_scd4x

count = 0
i2c = board.I2C()
scd4x = adafruit_scd4x.SCD4X(i2c)
print("Serial number:", [hex(i) for i in scd4x.serial_number])

scd4x.start_periodic_measurement()
print("Waiting for first measurement....")

while True:
    if scd4x.data_ready:
        count = count + 1
        print("%d." % count)
        print("SCD41 CO2: %d ppm" % scd4x.CO2)
        print("SCD41 Temperature: %0.1f *C" % scd4x.temperature)
        print("SCD41 Humidity: %0.1f %%" % scd4x.relative_humidity)
        print()
    time.sleep(1)