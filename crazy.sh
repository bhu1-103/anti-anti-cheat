#!/bin/bash

# Send keystrokes to the laptop
echo "hello world" | sudo tee /dev/hidg0 > /dev/null
