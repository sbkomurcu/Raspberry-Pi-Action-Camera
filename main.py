#!/usr/bin/python3

# Python program for Raspberry Pi to take pictures,
#                                 images and stream to hdmi output by using GPIO pins and Raspberry Pi Camera Module.
# Author: Samet Buyukkomurcu
# Copyright: Copyright 2020, Raspberry-Pi-Action-Camera
# License: MIT License
# Version: 1.0
# Contact: linkedin.com/in/sbkomurcu

from gpiozero import Button, LED
from signal import pause
from PIL import Image
import subprocess
import datetime
import glob
import os

Button.was_held = False

Button.is_active_hdmi = None
Button.is_capture = None
Button.is_record = None

green = LED(13)  # Green Led - Pin Number: GPIO 13
blue = LED(19)  # Blue Led - Pin Number: GPIO 19
red = LED(26)  # Red Led - Pin Number: GPIO 26

btn = Button(5, hold_time=1)  # HDMI Button - GPIO 5
cptr = Button(6, hold_time=1)  # Picture/Video Button - GPIO 6


def hdmi(btn):
    if not btn.is_active_hdmi:
        btn.is_active_hdmi = True
        blue.on()
        green.off()
        print("Started HDMI")
        from picamera import PiCamera
        global camera
        camera = PiCamera()
        # camera.hflip = True     # Uncomment to horizontal flip.
        # camera.vflip = True     # Uncomment to vertical flip.
        # camera.rotation = 90    # Uncomment to rotate 90 degrees.
        # camera.rotation = 180   # Uncomment to rotate 180 degrees.
        # camera.rotation = 270   # Uncomment to rotate 270 degrees.
        camera.sensor_mode = 5
        camera.framerate = 30
        camera.start_preview()
        return

    if btn.is_active_hdmi:
        print("Stopped HDMI")
        green.on()
        blue.off()
        camera.close()
        btn.is_active_hdmi = False
        return
    return


def capture():
    if not cptr.was_held:
        if not cptr.is_record:
            from picamera import PiCamera
            camera = PiCamera()
            red.on()
            green.off()
            datetime_object = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            print("Captured")
            picture_counter = ((counter(1) + 2) / 2)
            img_name = ("im_%04d_%04s.jpg" % (picture_counter, datetime_object))
            img_name_thumb = ("im_%04d_%04s.jpg.i%04d.th.jpg" % (picture_counter, datetime_object, picture_counter))
            camera.capture("/home/pi/media/%s" % img_name)
            thumbnail_picture(img_name, img_name_thumb)
            camera.close()
            red.off()
            cptr.was_held = False
            main()
        if cptr.is_record:
            video()
            return
        return
    cptr.was_held = False
    return


def video():
    cptr.was_held = True
    if not cptr.is_record:
        print("Started recording")
        from picamera import PiCamera
        global camera
        cptr.is_record = True
        camera = PiCamera()
        green.off()
        video_counter = counter(2)
        red.blink()
        camera.start_recording("/home/pi/media/temp/temp.h264")
        return video_counter
    else:
        print("Stopped recording")
        camera.stop_recording()
        red.off()
        green.on()
        blue.on()
        camera.close()
        cptr.is_record = False
        convert()
        return


def counter(what_is_needed):  # Counts amount of video/picture in the ./media folder.
    mp4Counter = len(glob.glob1("/home/pi/media/", "*.mp4"))
    jpgCounter = len(glob.glob1("/home/pi/media/", "*.jpg"))

    finalized_mp4 = int(abs(mp4Counter))
    finalized_jpg = int(abs(jpgCounter))

    if what_is_needed == 1:
        return int(finalized_jpg)
    if what_is_needed == 2:
        return int(finalized_mp4)
    return


def thumbnail_picture(img_name, img_name_thumb):  # Created thumbnail for the taken picture.
    image = Image.open(r"/home/pi/media/%s" % img_name)
    MAX_SIZE = (100, 100)
    image.thumbnail(MAX_SIZE)
    image.save("/home/pi/media/%s" % img_name_thumb)
    os.system("sudo chown www-data:www-data /home/pi/media/*")
    return


def thumbnail_video(video_name, datetime_object, video_counter):  # Created thumbnail for the recorded video.
    video_input_path = '/home/pi/media/%s' % video_name
    img_output_path = '/home/pi/media/vi_%04d_%s.mp4.v%04d.th.jpg' % (video_counter, datetime_object, video_counter)
    subprocess.call(['ffmpeg', '-i', video_input_path, '-ss', '00:00:00.000', '-vframes', '1', img_output_path])
    os.system("sudo chown www-data:www-data /home/pi/media/*")
    main()
    return


def convert():  # Converts .h264 video format to .mp4.
    datetime_object = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    video_counter = (counter(2) + 1)
    video_name = ("vi_%04d_%04s.mp4" % (video_counter, datetime_object))
    print("Video Recorded \r\n")
    command = "MP4Box -add " + "/home/pi/media/temp/temp.h264" + " " + "/home/pi/media/%s" % video_name
    subprocess.call([command], shell=True)
    print("\r\nVideo Converted \r\n")
    thumbnail_video(video_name, datetime_object, video_counter)
    return


def main():
    print("Ready-to-use")
    blue.off()
    red.off()
    green.on()

    btn.when_pressed = hdmi

    cptr.when_held = video
    cptr.when_released = capture


main()
pause()
