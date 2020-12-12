# Hackoffv3 - Team Dotpy
Every code related to our project for HackOff3.0 is present here.

## Motivation:
Due to the COVID-19 pandemic, social distancing and contact-less systems have become norms and becoming the new normal. Considering this, our project will upgrade any normal lift to a contact-less lift. This will help in avoiding the physical pressing of the lift buttons for its operation

## Command Center Script:
A python script to be implemented as the final code on a Raspberry Pi. This code contains the mechanism to take in user input and send the suitable floor number to the button_control script. 
A user can feed in his choice of floor by several means:
1) Speaking out the floor number
2) Showing a QR Code corresponding to a specific floor generated on our app

The app is user friendly app to generate a specific QR code for any floor the user wants to go to. 
By this, all he/she has to do is provide a floor number in the app and show the QR code to the camera on the button panel. The system would automatically recognise the QR code and press the required button.
In anycase if the user doesnot have the app, he/she can choose the voice command facility.

## Button Control Script:
Arduino script to control the motion of the cursor on the button panel of a lift. The code is built on C++ Arduino IDE.

## Android Mobile App:
The developed android app is built for the purpose of generating a specific QR code for each floor, that is givem as an input by the user. 

## Advantages:
1. Scalable: Can be easily installed on *any existing or new* lift button panel. 
2. Easily installable: The entire lift need not be halted for hours for this system to be installed
3. Easy maintanence: Does not require heavy machinery to be installed or fixed
4. User friendly: The lift can be easily operated by the user, without internet connectivity   
5. COVID19: The project's main aim is to eliminate the possibility of physical contact with any surface in the lift. Thus reducing the spread of the Coronavirus

## Future developments:
Hand Gesture control mechanism
Advancements in the App
More generalized button pressing mechanism
