#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""SETTINGS Dataformats
"""
DATE_FORMAT_HM = '%H:%M'
DATE_FORMAT_HMS = '%H:%M:%S'
DATE_FORMAT_H = '%H'
DATEFORMAT_YMD = '%Y-%m-%d'
DATEFORMAT_YM = '%Y-%m'
DATEFORMAT_Y = '%Y'
DATEFORMAT_UTC = '%Y-%m-%dT%H:%M:%SZ'
DATEFORMAT_TIMESTAMP = '%Y-%m-%d %H:%M:%S.%f'
LAST_SCANTIMESTAMP = '1900-01-01 00:00:00'


"""SETTINGS LOGGER
"""
# switch logging on/off
LOG_LEVEL = 10  # LOG_LEVEL DEBUG: 10
# LOG_LEVEL = 20  # LOG_LEVEL INFO: 20
# LOG_LEVEL = 30   ## LOG_LEVEL WARNING: 30
# LOG_LEVEL = 40   ## LOG_LEVEL ERROR: 40
# LOG_LEVEL = 50   ## LOG_LEVEL CRITICAL: 50
# LOG_LEVEL = 100  ## LOG_LEVEL DISABLED: 100
LOG_DIR = './logs/'


"""SETTINGS MQTT Client
"""
MQTT_HOST = 'localhost'  # Add your MQTT HOST
MQTT_PORT = 1883
MQTT_TIMEOUT = 60
MQTT_USERNAME = 'miscale.service'
MQTT_PASSWORD = '8DmLcN7YPGmg8q9jy63C'
MQTT_DISCOVERY = True
MQTT_DISCOVERY_PREFIX = 'homeassistant'
MQTT_AVAILABILITY_TOPIC = 'tele/miscale2/LWT'
MQTT_TOPIC = 'tele/miscale2/data'
MQTT_PREFIX = 'tele/miscale2'
MQTT_CLEINTID = 'misacle.service'
MQTT_KEEPALIVE = 60
MQTT_ENABLE_LOGGING = False

"""SETTINGS INFLUX DATABASR SERVICE
"""
# all for the influx database
# disable INFLUXDB Service: set INFLUXDB = None
INFLUXDB_NAME = 'historydata'
INFLUXDB_HOST = 'localhost'  # Add your INFLUXDB HOST
INFLUXDB_PORT = 8086
INFLUXDB_USER = 'admin'
INFLUXDB_PASSWORD = '3parpXA7AhN3B3i5si4E'
INFLUXDB_LOG_DIR = None  # './data/influxdb'

"""SETTINGS MISCALE V2
"""
MI2_MAC = "5c:ca:d3:4c:ee:74"
MI2_SCALE2ID = '1b18'
MI2_DATAFLAG = 1
MI2_NOSERVICE = 2
MI2_MANUFACTORID = 255

HCI_DEV = 'hci0'  # sudo hciconfig
TIME_INTERVAL = 30
ATTRIBUTION = 'Data provided by Peter Siebler'

"""SETTINGS for all users
"""
USER1_GT = 60
USER1_SEX = "male"
USER1_NAME = "Peter"
USER1_HEIGHT = 175
USER1_IDEALWEIGHT = 68.00
USER1_IDEALFAT = 11.50
USER1_ATHLETIC = True
USER1_DOB = "2000-12-16"
USER1_ADJUSTMENTS = {
    "78.0": {"fat": 0.766, "visceral": 0.628, "water": 1.186, "bone": 1.271, "muscle": 0.750},
    "77.0": {"fat": 0.756, "visceral": 0.620, "water": 1.187, "bone": 1.276, "muscle": 0.758},
    "77.5": {"fat": 0.759, "visceral": 0.622, "water": 1.188, "bone": 1.276, "muscle": 0.756},
    "76.5": {"fat": 0.745, "visceral": 0.611, "water": 1.188, "bone": 1.285, "muscle": 0.767},
    "76.0": {"fat": 0.742, "visceral": 0.608, "water": 1.189, "bone": 1.289, "muscle": 0.770},
    "75.5": {"fat": 0.739, "visceral": 0.606, "water": 1.189, "bone": 1.289, "muscle": 0.774},
    "75.0": {"fat": 0.734, "visceral": 0.602, "water": 1.190, "bone": 1.294, "muscle": 0.780},
    "74.5": {"fat": 0.725, "visceral": 0.594, "water": 1.190, "bone": 1.263, "muscle": 0.786},
    "74.0": {"fat": 0.638, "visceral": 0.523, "water": 1.045, "bone": 1.312, "muscle": 0.825},
    "73.5": {"fat": 0.634, "visceral": 0.520, "water": 1.044, "bone": 1.317, "muscle": 0.823},
    "73.0": {"fat": 0.626, "visceral": 0.514, "water": 1.044, "bone": 1.317, "muscle": 0.833},
    "72.5": {"fat": 0.593, "visceral": 0.487, "water": 1.052, "bone": 1.321, "muscle": 0.839},
    "72.0": {"fat": 0.591, "visceral": 0.485, "water": 1.050, "bone": 1.326, "muscle": 0.843},
    "71.5": {"fat": 0.585, "visceral": 0.480, "water": 1.051, "bone": 1.326, "muscle": 0.848},
    "71.0": {"fat": 0.604, "visceral": 0.495, "water": 1.044, "bone": 1.331, "muscle": 0.845},
    "70.5": {"fat": 0.592, "visceral": 0.486, "water": 1.044, "bone": 1.300, "muscle": 0.854},
    "70.0": {"fat": 0.586, "visceral": 0.481, "water": 1.044, "bone": 1.304, "muscle": 0.858},
    "69.5": {"fat": 0.585, "visceral": 0.480, "water": 1.044, "bone": 1.304, "muscle": 0.861},
    "69.0": {"fat": 0.576, "visceral": 0.473, "water": 1.043, "bone": 1.309, "muscle": 0.867},
    "68.5": {"fat": 0.563, "visceral": 0.462, "water": 1.217, "bone": 1.300, "muscle": 0.886},
    "68.0": {"fat": 0.558, "visceral": 0.458, "water": 1.215, "bone": 1.304, "muscle": 0.892},
    "67.5": {"fat": 0.553, "visceral": 0.453, "water": 1.041, "bone": 1.324, "muscle": 0.895},
    "67.0": {"fat": 0.544, "visceral": 0.446, "water": 1.040, "bone": 1.324, "muscle": 0.898},
    "66.5": {"fat": 0.533, "visceral": 0.437, "water": 1.038, "bone": 1.292, "muscle": 0.913},
    "66.0": {"fat": 0.532, "visceral": 0.436, "water": 1.038, "bone": 1.296, "muscle": 0.913},
    "65.0": {"fat": 0.520, "visceral": 0.426, "water": 1.036, "bone": 1.301, "muscle": 0.926},
    "65.5": {"fat": 0.488, "visceral": 0.400, "water": 1.044, "bone": 1.296, "muscle": 0.930},
    "64.5": {"fat": 0.508, "visceral": 0.417, "water": 1.035, "bone": 1.306, "muscle": 0.936},
    "64.0": {"fat": 0.499, "visceral": 0.409, "water": 1.035, "bone": 1.306, "muscle": 0.941},
    "63.5": {"fat": 0.486, "visceral": 0.398, "water": 1.033, "bone": 1.316, "muscle": 0.952},
    "63.0": {"fat": 0.483, "visceral": 0.396, "water": 1.033, "bone": 1.316, "muscle": 0.954},
    "62.5": {"fat": 0.560, "visceral": 0.459, "water": 1.014, "bone": 1.326, "muscle": 0.948},
    "61.5": {"fat": 0.462, "visceral": 0.378, "water": 1.030, "bone": 1.288, "muscle": 0.970},
    "61.00": {"fat": 0.462, "visceral": 0.378, "water": 1.030, "bone": 1.288, "muscle": 0.970}
}

USER2_LT = 60
USER2_SEX = "female"
USER2_NAME = "Reni"
USER2_HEIGHT = 168
USER2_IDEALWEIGHT = 54.00
USER2_IDEALFAT = 18.50
USER2_ATHLETIC = True
USER2_DOB = "2004-01-02"
USER2_ADJUSTMENTS = {
    "77": {"fat": 0.756, "visceral": 0.545, "water": 1.187, "bone": 1.276, "muscle": 0.758},
    "78": {"fat": 0.766, "visceral": 0.552, "water": 1.186, "bone": 1.271, "muscle": 0.750},
    "76": {"fat": 0.745, "visceral": 0.536, "water": 1.188, "bone": 1.285, "muscle": 0.767},
    "75": {"fat": 0.736, "visceral": 0.530, "water": 1.190, "bone": 1.294, "muscle": 0.777},
    "74": {"fat": 0.638, "visceral": 0.460, "water": 1.045, "bone": 1.312, "muscle": 0.823},
    "73": {"fat": 0.634, "visceral": 0.457, "water": 1.044, "bone": 1.317, "muscle": 0.823},
    "72": {"fat": 0.593, "visceral": 0.427, "water": 1.052, "bone": 1.321, "muscle": 0.839},
    "71": {"fat": 0.604, "visceral": 0.435, "water": 1.044, "bone": 1.331, "muscle": 0.845},
    "70": {"fat": 0.587, "visceral": 0.423, "water": 1.044, "bone": 1.304, "muscle": 0.857},
    "69": {"fat": 0.586, "visceral": 0.422, "water": 1.044, "bone": 1.304, "muscle": 0.858},
    "68": {"fat": 0.566, "visceral": 0.408, "water": 1.217, "bone": 1.300, "muscle": 0.883},
    "67": {"fat": 0.552, "visceral": 0.398, "water": 1.215, "bone": 1.304, "muscle": 0.895},
    "66": {"fat": 0.542, "visceral": 0.390, "water": 1.040, "bone": 1.328, "muscle": 0.906},
    "65": {"fat": 0.528, "visceral": 0.380, "water": 1.039, "bone": 1.296, "muscle": 0.919},
    "64": {"fat": 0.508, "visceral": 0.366, "water": 1.035, "bone": 1.306, "muscle": 0.936},
    "63": {"fat": 0.491, "visceral": 0.354, "water": 1.035, "bone": 1.311, "muscle": 0.945},
    "62": {"fat": 0.560, "visceral": 0.403, "water": 1.014, "bone": 1.326, "muscle": 0.948}
}

USER3_SEX = "female"
USER3_NAME = "Tina"
USER3_HEIGHT = 165
USER3_IDEALWEIGHT = 68.00
USER3_ATHLETIC = False
USER3_DOB = "1980-10-18"


"""SETTINGS data logger
"""
DATA_DIR = '../data/'
