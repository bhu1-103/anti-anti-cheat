#!/bin/bash

# Send keystrokes to the laptop
echo -ne '\0\0\x04\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\40\0\0\0\0\0' > /dev/hidg0
echo -ne '\0\0\0\0\0\0\0\0' > /dev/hidg0

