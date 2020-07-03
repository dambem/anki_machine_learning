# anki_machine_learning
Machine learning project using Anki Overdrive

## Requirements - 
Python 3.4+ 
(bluepy)[https://github.com/IanHarvey/bluepy]
Root Permission

As this code is expected to run on a Raspberry PI, bluepy is required for communication. The default raspberry PI bluetooth installation WILL NOT WORK

## Finding the overdrive:
In order to find the overdrive, you need to first work out the MAC address of the device. This can be done through the following:

hcitool scan  
bluetoothctl
agent on
scan on 
(At this point, switch on your anki_overdrive device, and it's MAC address should show up, note this address for later)
scan off

Replace MAC address in EXAMPLE.PY (car = Overdrive("F6:ED:77:8C:70:CA"))

## Overdrive Methods: 
The necessary methods can be found in the following (github)[https://github.com/xerodotc/overdrive-python/blob/master/overdrive.py] 

## Running the code:
Ensure that your Anki Overdrive is  turned on. run example.py, and the device should connect. The locationChangeCallBack will send a message twice for each curved piece (Once for entering, once for leaving), and three times for each straight piece (One for entering, one for entering the middle, one for leaving).  


Credit to - https://github.com/xerodotc/overdrive-python/blob/master/overdrive.py
