from machine import Pin
import random, ujson, utime
import dht
import gc

gc.collect() 


sensor = dht.DHT22(Pin(16))

while True:
    temperature_dht = 35
    humidity_dht = 50
    fahrenheit = 100
    temperature_esp32 = (fahrenheit - 32.0)/1.8
    print("Temperature (DHT): {}C, Humidity (DHT): {}%, Temperature (ESP32): {:.2f}C".format(
        temperature_dht, humidity_dht, temperature_esp32))
    
    payload = ujson.dumps({
        'temperature': temperature_dht,
        'humidity': humidity_dht,
        'esp32Temperature': temperature_esp32
    })
    
    gc.collect()
    utime.sleep(3)
