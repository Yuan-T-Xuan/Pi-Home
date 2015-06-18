import RPi.GPIO as GPIO
import os
import time
"""
LED representing Aircon will use GPIO2.
LED representing Dryer will use GPIO3.
"""

def list2int(alist):
    result = 0
    for bit in alist:
        if bit == '1':
            result = result * 2 + 1
        else:
            result = result * 2
    return result

def interpret(alist):
    threshold = 8
    result = [ ]
    i = 0
    prev_i = 0
    while i < len(alist):
        if alist[i] == 1:
            break
        i = i + 1
    while i < len(alist):
        if alist[i] == 0:
            break
        i = i + 1
    for j in range(0, 40):
        while i < len(alist):
            if alist[i] == 1:
                break
            i = i + 1
        prev_i = i
        while i < len(alist):
            if alist[i] == 0:
                break
            i = i + 1
        if i - prev_i <= threshold:
            result.append('0')
        else:
            result.append('1')
    result2 = list2int(result[0:8])
    result1 = list2int(result[16:24])
    return (result1, result2)

def get_Temp_Mois():
    #data is on GPIO22
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, 0)
    time.sleep(0.02)
    GPIO.setup(22, GPIO.IN)
    result = []
    for i in range(0, 10000):
        result.append(GPIO.input(22))
    return interpret(result)

def get_Dist():
    #data is on GPIO24
    #trig is on GPIO23
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.IN)
    GPIO.output(23, 1)
    time.sleep(0.00001)
    GPIO.output(23, 0)
    result = []
    for i in range(0, 1000):
        result.append(GPIO.input(24))
        time.sleep(0.000002)
    return result

def main_Task():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    #first, initiate the states
    curr_aircon_on = False
    curr_dryer_on = False
    counter_temp_sensor = 0
    #infinite loop
    while True:
        thefile = open("state.txt")
        stored_data = thefile.readlines()
        thefile.close()
        thefile = open("state2.txt")
        stored_data2 = thefile.readlines()
        thefile.close()
        for i in range(0, len(stored_data)):
            stored_data[i] = stored_data[i][:-1]
        for i in range(0, len(stored_data2)):
            stored_data2[i] = stored_data2[i][:-1]
        #Aircon
        if stored_data2[0] == "auto":
            if int(stored_data2[2]) <= int(stored_data[0]):
                if curr_aircon_on == False:
                    curr_aircon_on = True
                    GPIO.output(2, 1)
            if int(stored_data2[2]) - 2 > int(stored_data[0]):
                if curr_aircon_on == True:
                    curr_aircon_on = False
                    GPIO.output(2, 0)
        elif stored_data2[0] == "manual":
            if stored_data2[1] == 'T':
                if curr_aircon_on == False:
                    curr_aircon_on = True
                    GPIO.output(2, 1)
            if stored_data2[1] == 'F':
                if curr_aircon_on == True:
                    curr_aircon_on = False
                    GPIO.output(2, 0)
        else: #timming mode
            curr_hour = int(time.strftime("%H"))
            curr_min = int(time.strftime("%M"))
            start_hour = int(stored_data2[3][:2])
            start_min = int(stored_data2[3][-2:])
            stop_hour = int(stored_data2[4][:2])
            stop_min = int(stored_data2[4][-2:])
            if curr_hour < start_hour or (curr_hour == start_hour and curr_min < start_min):
                if curr_aircon_on == True:
                    curr_aircon_on = False
                    GPIO.output(2, 0)
            else:
                if curr_hour < stop_hour or (curr_hour == stop_hour and curr_min < stop_min):
                    if curr_aircon_on == False:
                        curr_aircon_on = True
                        GPIO.output(2, 1)
                else:
                    if curr_aircon_on == True:
                        curr_aircon_on = False
                        GPIO.output(2, 0)
        #Dryer
        if stored_data2[5] == "auto":
            if int(stored_data2[7]) <= int(stored_data[1]):
                if curr_dryer_on == False:
                    curr_dryer_on = True
                    GPIO.output(3, 1)
            if int(stored_data2[7]) - 2 > int(stored_data[1]):
                if curr_dryer_on == True:
                    curr_dryer_on = False
                    GPIO.output(3, 0)
        elif stored_data2[5] == "manual":
            if stored_data2[6] == 'T':
                if curr_dryer_on == False:
                    curr_dryer_on = True
                    GPIO.output(3, 1)
            if stored_data2[6] == 'F':
                if curr_dryer_on == True:
                    curr_dryer_on = False
                    GPIO.output(3, 0)
        else: #timming mode
            curr_hour = int(time.strftime("%H"))
            curr_min = int(time.strftime("%M"))
            start_hour = int(stored_data2[8][:2])
            start_min = int(stored_data2[8][-2:])
            stop_hour = int(stored_data2[9][:2])
            stop_min = int(stored_data2[9][-2:])
            if curr_hour < start_hour or (curr_hour == start_hour and curr_min < start_min):
                if curr_dryer_on == True:
                    curr_dryer_on = False
                    GPIO.output(3, 0)
            else:
                if curr_hour < stop_hour or (curr_hour == stop_hour and curr_min < stop_min):
                    if curr_dryer_on == False:
                        curr_dryer_on = True
                        GPIO.output(3, 1)
                else:
                    if curr_dryer_on == True:
                        curr_dryer_on = False
                        GPIO.output(3, 0)
        #
        if counter_temp_sensor < 20:
            counter_temp_sensor += 1
        else:
            counter_temp_sensor = 0
            curr_temp_mois = get_Temp_Mois()
            stored_data[0] = str(curr_temp_mois[0])
            stored_data[1] = str(curr_temp_mois[1])
        #
        distance = get_Dist().count(1)
        stored_data[2] = str(distance)
        to_be_written = ""
        for datum in stored_data[:3]:
            to_be_written += datum + "\n"
        thefile = open("state.txt", "w")
        thefile.write(to_be_written)
        thefile.close()
        time.sleep(0.05)
    #it will never reach here ...