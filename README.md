# micropython-covid-counter
esp32 with oled screen shows total amount of covid cases in Poland 


Libraries used in this project:
- ssd1306 https://github.com/micropython/micropython/blob/master/drivers/display/ssd1306.py 
- urequests  https://micronote.tech/2020/06/Introduction-to-API-Calls-with-a-NodeMCU-and-MicroPython/


Before upload rename file 'covid-counter' to 'main.py'

wiring is on the photo


LCD     $~$ ESP32<br/>
LCD_scl ----> pin 22<br/>
LCD_sda ----> pin 21<br/>
VCC     ----> 3V3<br/>
GND     ----> GND<br/>

![](photo_esp32.PNG)
