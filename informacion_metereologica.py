#necesitaremos la instalación de la librería pyown (sudo pip install pyown) y una clave para la Open Weather API, que provee un acceso gratuito para leer información metereológica tras obtener una clave de acceso a la API registrándose en su página web.

import pyowm
import time
import sys
import scrollphat

scrollphat.set_brightness(3)

owm = pyowm.OWM("0123456789asdfghjklñ") #Aquí debes incluir tu Open Weather Map API Key.


while True:
    try:
        observation = owm.weather_at_place('Salamanca,es') # Cámbialo por la ciudad que quieras
        w = observation.get_weather()
        wind = w.get_wind()
        hum = w.get_humidity()
        temp = w.get_temperature('celsius')
        print(wind)
        print (hum)
        print(temp)
        results = ("Meteo Milano Temp min: "+str(temp['temp_min'])+" Temp max: "+str(temp['temp_max'])+" Humy: "+str(hum)+"%  Wind: "+str(wind['speed']))
        time.sleep(3)
        for i in range(600):
            scrollphat.write_string(results, 11)
            scrollphat.scroll()
            time.sleep(0.1)
    except KeyboardInterrupt:
        scrollphat.clear()
        sys.exit(-1)
