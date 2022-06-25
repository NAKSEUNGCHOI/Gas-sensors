import aranet4
import time

device_rasp = ""

while True:
    current = aranet4.client.get_current_readings(device_rasp)
    print("co2 reading:", current.co2)
    print("Temperature:", current.temperature)
    print("Humidity:", current.humidity)
    print("Pressure:", current.pressure)
    time.sleep(5)
    
