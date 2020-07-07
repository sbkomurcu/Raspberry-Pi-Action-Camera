# Raspberry Pi Action Camera
Python program for Raspberry Pi to take pictures, images and stream to hdmi output by using GPIO pins. 


# Features
● Take picture by just pressing on the picture/video button.

● Record video by holding the picture/video button.

● Stream camera preview to hdmi output by pressing hdmi button.

● Automatically converts recorded videos from .h264 to .mp4.

● Creates thumbnail pictures of the recorded media (video & picture). 

● LED's are used to indicate the current process of the program, see below.;

      ○ Green Led (cont.) -> Program is ready to take commands.

      ○ Blue Led (cont.) -> HDMI mode is active, see hdmi output.

      ○ Red Led (cont.) -> Taking picture.

      ○ Red Led (blink) -> Recording video.



# Installation
Green Led -> GPIO 25

Blue Led -> GPIO 7

Red Led -> GPIO 8

Picture/Video Button -> GPIO 5

Hdmi Button -> GPIO 6

