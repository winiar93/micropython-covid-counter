from machine import Pin, I2C
import ssd1306
from time import sleep
import esp32
import connect
import urequests
from parse import urlencode
connect.polacznie()

i2c =I2C(-1,scl=Pin(22), sda=Pin(21))

oled = ssd1306.SSD1306_I2C(128, 32, i2c, 0x3c)
led = Pin(2, Pin.OUT)
for i in range(5):
    led.value(not led.value())
    sleep(0.5)



def get(url):
    return urequests.get(url)

# response = get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=PKEATZ48HU1QVAVE').text
# print(response[:7])
# data = response.json()
for i in range(3):
    led.value(not led.value())
    sleep(3)

while True:
    response = get('https://api.thingspeak.com/apps/thinghttp/send_request?api_key=PKEATZ48HU1QVAVE').text
    temp_f = esp32.raw_temperature()
    temp_c = round(((temp_f - 32)* 5/9),1)

    oled.fill(0)
    oled.show()
    sleep(1)
    oled.text('chorzy na ',1,1)
    oled.text('covid',5,9)
    oled.text(response[:7],15,20)
    oled.show()
    sleep(4)