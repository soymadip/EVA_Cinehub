#!/bin/bash

echo "Installing Requirements..."
pip3 install -U -r requirements.txt

echo "Starting Bot, Please Wait..."
python3 bot.py

