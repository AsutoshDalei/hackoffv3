# Hackoffv3 - Team Dotpy
Every code related to our project for HackOff3.0 is present here.

## Button_Control:
Arduino script to control the motion of 

## Command_center:
A python script to be implemented as the final code on a Raspberry Pi. This code contains the mechanism to take in user input and send the suitable floor number to the button_control script. 
A user can feed in his choice of floor by several means:
1) Speaking out the floor number
2) Hand gesture
3) Showing a QR Code corresponding to a specific floor

We have developed an user friendly app to generate a specific QR code for any floor the user wants to go to. 
By this, all he has to do it provide a floor number in the app and show the QR code to the camera on the button panel. The system would automatically recognise the QR code and press the required button.
