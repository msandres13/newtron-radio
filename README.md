newtron-radio
==============

This project used https://github.com/5Volt-Junkie/RPi-Tron-Radio as a base and the changes done by https://github.com/lavolp3/newtron-radio and https://ottelo.jimdofree.com/rpi-radio/.
The goal of this Project is to supply an up to date version which can be installed on a Raspberrypi with an LCD and touch as well on the PC.

Main screen

![Player](https://raw.githubusercontent.com/msandres13/newtron-radio/master/screenshoots/main-screen.png)

Small web radio with support for Raspberry Pi B+ and newer and 2.8" 320x240 TFT Touchscreen. The interface of the web radio was written in python/pygame.


See the [Installation guide](https://raw.githubusercontent.com/msandres13/newtron-radio/master/docu/Installation.md)

## Features
* uses mpd and mpc.
* 8 skin colors
* Displays station data
* Displays current playing song
* Displays volume in %
* Displays time and date
* Displays IP address
* Displays CPU temp
* Screensaver (screen burn prevention)
* Can write the title of the current song to the text file.

* Buttons:
Menu 1
  * Play
  * Pause
  * Volume Up
  * Volume Down
  * Mute
  * Next
  * Previous
  * -> Menu 2

  * Fav
  * Switch skin color
  * Run stream in background
  * Close/stop radio
  * Poweroff
  * Reboot
  * Reserved for on/off RGB-LED
  * -> Menu 1