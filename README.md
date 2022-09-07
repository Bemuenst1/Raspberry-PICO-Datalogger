#PICO-Datalogger

This script loggs the temperature measured by the DHT22 sensor at pin 14 (Raspberry Pico).
  The sensor is connectet to the PICO as followed:

Image...

At startup (when power is connected) the status-led of the PICO should blink twice!

The configuration can be changed in the "settings.txt":
  - sensor-reading-interval (3600 = every hour, 1800 = every 1/2hour, etc.)
  - record-starting-point (the timeprint appearing in the cvs file).
  
At the end of the day the highest and lowest temperatures are saved into the "log.csv" file with their corrosponding timeprint.

Feel free to ask about this project and have fun!
Benjamin M.
