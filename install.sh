#!/bin/bash

# install python3
sudo apt install python3

# install pip for python3
sudo apt install python3-pip

# install pyautogui
pip3 install pyautogui

# install xlib (for some reason it is not a pyautogui dependency, even though it does not run without it)
pip3 install xlib