#!/bin/sh

DATE=$(date +"%Y-%m-%d_%H%M%S")
raspistill -hf -vf -o /home/pi/Desktop/CCTV/$DATE.jpg
