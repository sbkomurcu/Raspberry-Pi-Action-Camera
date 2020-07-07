# Raspberry Pi Action Camera
Python program for Raspberry Pi to take pictures, images and stream to hdmi output by using GPIO pins and Raspberry Pi camera module. 


# Features
● Take picture by just pressing on the picture/video button.

● Record video by holding the picture/video button.

● Stream camera preview to hdmi output by pressing hdmi button.

● Automatically converts recorded videos from .h264 to .mp4.

● Creates thumbnail pictures of the recorded media (video & picture). 

● Pictures, videos and thumbnails are recorded into the following directory "./Raspberry-Pi-Action-Camera/media/"

● Pictures and videos are recorded with a name based on the date format and amount of pictures/videos in target folder. 

● LED's are used to indicate the current process of the program, see below.;

    ○ Green Led (cont.) -> Program is ready to take commands.

    ○ Blue Led (cont.) -> HDMI mode is active, see hdmi output.

    ○ Red Led (cont.) -> Taking picture.

    ○ Red Led (blink) -> Recording video.



# Installation

● Enable camera support with the following commands:

    ○ sudo raspi-config 
    ○ Select Option 5 "Interfacing Options", then "P1 Camera", then Yes.
    ○ Exit and reboot your Pi.

● Update your RPi with the following commands:

    ○ sudo apt-get update

    ○ sudo apt-get dist-upgrade

    ○ sudo apt-get install git

● Clone the code from github with the following commands: 

    ○ git clone https://github.com/sbkomurcu/Raspberry-Pi-Action-Camera.git

    ○ cd Raspberry-Pi-Action-Camera

● Connect buttons and leds onto GPIO pins on the RPi based on the following pins;

    ○ Green Led -> GPIO 13

    ○ Blue Led -> GPIO 19

    ○ Red Led -> GPIO 26

    ○ Picture/Video Button -> GPIO 5

    ○ Hdmi Button -> GPIO 6

● Run python program with the following command;

    ○ sudo python3 main.py

     













