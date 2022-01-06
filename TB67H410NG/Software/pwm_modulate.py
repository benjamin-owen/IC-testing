#!/usr/bin/python
import sys
import time
import pyvisa

# CHANGE THESE VALUES IF NEEDED FOR SPECIFIC FUNCTION GENERATORS
# CAN BE USED FOR GENERATORS THAT GIVE ERRORS AT 0.00% AND 100.00% DUTY CYCLE
# MINIMUM DUTY CYCLE
PWM_MIN = 0
# MAXIMUM DUTY CYCLE
PWM_MAX = 100

# initialize pyvisa
rm = pyvisa.ResourceManager()

# list available devices
print("Available devices:")
print(rm.list_resources())

# check if function generator address was passed
# otherwise, ask user which address is function generator
if (len(sys.argv) > 1): # passed from command line
    inst_addr = sys.argv[1]
else:
    inst_addr = input("\nFunction generator address: ")

# connect to device
print("Connecting to device...")
inst = rm.open_resource(inst_addr)

# print device information
print(inst.query("*IDN?"))

# get values for PWM modulation
if (len(sys.argv) == 6): # passed from command line
    freq = float(sys.argv[2])
    pwm_low = float(sys.argv[3])
    pwm_high = float(sys.argv[4])
    delay = float(sys.argv[5])
else:
    freq = float(input("Frequency (Hz): "))
    pwm_low = float(input("Minimum duty cycle (%): "))
    pwm_high = float(input("Maximum duty cycle (%): "))
    delay = float(input("Time per modulation (Low-High-Low) (s): "))

# avoid errors with function generator with 100% duty cycle
if (pwm_high > PWM_MAX):
    pwm_high = PWM_MAX

# avoid errors with function generator with 0% duty cycle
if (pwm_low < PWM_MIN):
    pwm_low = PWM_MIN

# set up function generator with initial values
# run the following commands:
# 1) set output wave on source 1 to square
# 2) set output frequency on source 1 to 'freq' variable
# 3) set output duty cycle on source 1 to 'pwm_low' variable
print("Setting up function generator...")
inst.write("SOUR1:FUNC SQU")
inst.write("SOUR1:FREQ %f" % freq)
inst.write("SOUR1:FUNC:SQU:DCYC %f" % pwm_low)

# begin PWM modulation
print("\nBeginning PWM modulation...")

# PWM modulation:
# loop from 'pwm_min' to 'pwm_max'
# set duty cycle to current value in loop
# delay as long as user set (based on 'delay')
# repeat in reverse
# this results in a low-high-low-high-etc duty cycle modulation
while True:
    # loop from low-high
    for pwm_curr in range(int(pwm_low), int(pwm_high)):
        start_time = time.time()
        inst.write("SOUR1:FUNC:SQU:DCYC %f" % pwm_curr)
        print("Current duty cycle: %.0f%%   " % pwm_curr, end='\r')
        time_diff = time.time() - start_time
        if (time_diff <= ((delay / 2) / (pwm_high - pwm_low))):
            time.sleep(((delay / 2) / (pwm_high - pwm_low)) - time_diff)

    # loop from high-low
    for pwm_curr in range(int(pwm_high), int(pwm_low), -1):
        start_time = time.time()
        inst.write("SOUR1:FUNC:SQU:DCYC %f" % pwm_curr)
        print("Current duty cycle: %.0f%%   " % pwm_curr, end='\r')
        time_diff = time.time() - start_time
        if (time_diff <= ((delay / 2) / (pwm_high - pwm_low))):
            time.sleep(((delay / 2) / (pwm_high - pwm_low)) - time_diff)
