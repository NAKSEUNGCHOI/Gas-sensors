import serial
import time
from Adafruit_IO import RequestError, Client, Feed

class Arduino:
    
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
    
    def get_port(self):
        return self.port
        
    def get_baudrate(self):
        return self.baudrate
        
    def get_timeout(self):
        return self.timeout
    
    def set_port(self):
        temp = input("/dev/tty: ")
        print("/dev/tty" + temp + " added.")
        port = "/dev/tty" + temp
        self.port = port
    
    def set_baudrate(self):
        baudrate = input("baudrate: ")
        self.baudrate = baudrate
        print(baudrate + " has been applied.")
        
    def set_timeout(self):
        timeout = input("timeout: ")
        self.timeout = timeout
        print(timeout + " has been applied.")
    
    def set_serial(self):
        ser = serial.Serial(self.port, self.baudrate, timeout = self.timeout)
        ser.flush()
        print("Loading...")
        return ser
    

def read_data(name, serial):
    if serial.in_waiting > 0:
        line = serial.readline().decode('utf-8').rstrip()
        print(line)
        split = line.split(",")
        if(name == "digital"):
            split = split[1]
        if(name == "analog" or name == "mine"):
            split = split[3]
    return split

def adafruitIO_init():
    ADAFRUIT_IO_USERNAME = "SSOLCHOI2"
    ADAFRUIT_IO_KEY = "aio_Ksex19Yas0alZuiL7f03Mx4YEWKb"
    aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
    print("Adafruit IO connected")
    return aio

if __name__ == '__main__':
    
    #Arduino initialization
    digital1 = Arduino('/dev/ttyUSB0', 9600, 5)
    arduino1 = Arduino('/dev/ttyACM0', 9600, 5)
    arduino2 = Arduino('/dev/ttyACM1', 9600, 5)
    
    #adafruitIO initialization
    aio = adafruitIO_init()
    
    #set serials
    serial1 = digital1.set_serial()
    serial2 = arduino1.set_serial()
    serial3 = arduino2.set_serial()
    time.sleep(2)
    
    # write anything to analog and mine to respond to zeroing out.
    hey = 'h'.strip()
    serial2.write(hey.encode())
    time.sleep(0.5)
    serial3.write(hey.encode())
    time.sleep(5)
    
    # count: to send data every 5 seconds
    count = 3
    
    #infinite loop
    while True:
        try:
            if count != 0:
                
                # get data from digital module and convert ppb into ppm in 2 decimal.
                digital_data = read_data("digital", serial1)
                digital_data = float(digital_data)/1000.0
                digital_data = "{:.2f}".format(digital_data)
                
                analog_data = read_data("analog", serial2)
                mine_data = read_data("mine", serial3)
                
                count = count - 1
                print(count)
            if count == 0:
                count = 3
                print("here!")
                aio.send('digital', digital_data)
                
                # to block non-values from being sent to adafruitIO.
                if float(analog_data) > -9999999 or float(analog_data) < 9999999:
                   aio.send("analog", analog_data)
                if float(mine_data) > -9999999 or float(mine_data) < 9999999:
                   aio.send('mine', mine_data)
        except:
            pass

