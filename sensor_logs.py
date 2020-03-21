#!/usr/bin/python
import mysql.connector as mariadb
import sys
sys.path.append('/home/pi/PlanterPi/')
import configparser
import hardware as hw
from datetime import datetime

config = configparser.ConfigParser()
config.read("/home/pi/Sprinkler/config.ini")

host = config.get('credentials','host')
user = config.get('credentials','user')
passwd = config.get('credentials','passwd')
db = config.get('credentials','db')

mysql = mariadb.connect(user=user, password=passwd, database=db)
cursor = mysql.cursor()
temperature = hw.read_temperature()
humidity = hw.read_humidity()
light = hw.read_light()
soil_temperature = hw.read_soil_temperature()
soil_moisture = hw.read_soil_moisture()

print(datetime.now())
print('	Temperature: ' + str(temperature))
print('	Humidity: ' + str(humidity))
print('	Light: ' + str(light))
print('	Soil Temp: ' + str(soil_temperature))
print('	Soil Moisture: ' + str(soil_moisture))
cursor.execute('insert into sensor_data (planter_id, temperature, humidity, light, soil_temperature, soil_moisture) values (1, {},{},{},{},{})'.format(temperature, humidity, light, soil_temperature, soil_moisture));
	
mysql.commit()
