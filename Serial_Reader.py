#
# Thank you to https://raspberrypi.stackexchange.com/questions/74742/python-serial-serial-module-not-found-error
#    http://archive.fabacademy.org/archives/2017/fablabverket/students/100/web/assignments/week16/pyserial_tutorial.html
#    https://uclalemur.com/blog/python-script-to-read-serial-monitor

# https://www.geeksforgeeks.org/find-path-to-the-given-file-using-python/#:~:text=In%20order%20to%20obtain%20the,to%20the%20current%20working%20directory.
#
import serial
import argparse

import os

import binascii

# base directory of the program TODO dependent on folder location
BASE_DIR = r"C:\Users\keith\Desktop\CSCE A470\Team_Rocket_Visualization\static" #os.getcwd()

#RECORD_FLIGHT_PATH = os.listdir(f'{BASE_DIR}/recorded_flights')

RECORD_FLIGHT_PATH = os.listdir(r"C:\Users\keith\Desktop\CSCE A470\Team_Rocket_Visualization\static\recorded_flights")
print(RECORD_FLIGHT_PATH)

# checks if record flight folder exists, if not then create the folder
# if (not 'recorded_flights' in os.listdir(BASE_DIR)):
#     os.mkdir(f'{BASE_DIR}/recorded_flights/')


def send_to_file(flight_file, data):
    f = open(f'{BASE_DIR}/recorded_flights/{flight_file}','ab')
    f.write(data)
    f.close()


# check for
def current_file():
    i=0
    while(True):
        # print(f'flight{i}.txt' in f'{RECORD_FLIGHT_PATH}')
        if(f'flight{i}.txt' in f'{RECORD_FLIGHT_PATH}'):
            i+=1
        else:
            f = open(f'{BASE_DIR}/recorded_flights/flight{i}.txt','ab')
            f.write(b'200') #create file
            f.close()
            break

    print(f'flight{i}.txt') #confirmation of file creation/recorded
    return f'flight{i}.txt'


def print_serial(name, flight_file):
    try:
        serial_port = serial.Serial(name, 115200)
        print(f"The Port name is {serial_port.name}")
        while True:
            lines = serial_port.readline()
            print(str(lines), type(str(lines)))  # show incoming data

            send_to_file(flight_file,lines)
    except Exception as e:
        print("ERROR", e)
        print("check port")
        exit()


ap = argparse.ArgumentParser()
ap.add_argument("-p", "--port", required=True, help="Enter Port Name")
args = vars(ap.parse_args())

PORT = args['port']
print("hi this is port", PORT)
flight_file = current_file()

print_serial(PORT,flight_file)
