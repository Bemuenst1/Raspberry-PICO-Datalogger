#
# Datalogger for RPICO and DHT22 Sensor (Pin 14)
# by Benjamin M.
#

from machine import Pin;
import utime, csv, dht, os;

#Init Static
led_Status = Pin(25, Pin.OUT);
dht22 = dht.DHT22(Pin(14));

settings = [];
readings = [];

day = 0;
time = 0;
#

def main():
    init();
    
    global day, time;
    
    intR = int(settings[1]);
    repR = int((86400 / intR) - 1);
    
    while True:
        if time < repR:
            readSensor(time);
            time +=1;
            utime.sleep(intR);
        if time == repR:
            readSensor(time);
            saveDataset(getDataset());
            reset();
            utime.sleep(intR);
            
def init():
    global time;
    loadSettings();
    time = int(settings[3]);
    ledBlink(0.5);
    
def loadSettings():
    global settings;
    
    with open("settings.txt") as file:
        for line in file:
            settings.append(line);
        file.close();

def ledBlink(duration):
    led_Status.on();
    utime.sleep(duration);
    led_Status.off();

def readSensor(time):
    global readings;
    
    dht22.measure();
    reading = (time, dht22.temperature());
    readings.append(reading);
    
    ledBlink(0.1);
    print(reading);

def getDataset():
    #values are just placeholders!
    TMax = -100;
    TMin = 100;
    tMax = 10000;
    tMin = 10000;
    
    for dSet in readings:
        if dSet[1] > TMax:
            TMax = dSet[1];
            tMax = dSet[0];
        elif dSet[1] < TMin:
            TMin = dSet[1];
            tMin = dSet[0];
            
    dataset = createDataset(day, tMax, tMin, TMax, tMin);
    
    return dataset;

def createDataset(day, tMax, tMin, TMax, TMin):
    dataset = str(day) + ";" + str(tMax) + ";" + str(TMax) + ";" + str(tMin) + ";" + str(TMin) + "\n";
    return dataset;

def saveDataset(data):
    with open("log.csv") as file:
        for line in file:
            pass;
        
        file.write(data);
        file.close();
        
def reset():
    global day, time;
    day = 0;
    time = 0;
    readings.clear();

if __name__ == "__main__":
    main();
