import aranet4
import time

device_rasp = "EB:9A:51:3D:33:93"

while True:
    current = aranet4.client.get_current_readings(device_rasp)
    print("co2 reading:", current.co2)
    print("Temperature:", current.temperature)
    print("Humidity:", current.humidity)
    print("Pressure:", current.pressure)
    time.sleep(5)