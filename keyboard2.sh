#!/bin/bash

# Enable HID gadget
modprobe libcomposite

# Create HID gadget
cd /sys/kernel/config/usb_gadget/
mkdir -p raspberrypi
cd raspberrypi

echo 0x05ac > idVendor # Apple Inc.
echo 0x0255 > idProduct # Assigned by Apple Inc.
echo 0x0100 > bcdDevice # v1.0.0
echo 0x0200 > bcdUSB    # USB2

# Create English locale
mkdir -p strings/0x409
echo "123456789abcdef0" > strings/0x409/serialnumber
echo "Apple Inc." > strings/0x409/manufacturer
echo "Apple Keyboard" > strings/0x409/product

# Create HID function for keyboard
mkdir -p functions/hid.usb0
echo 1 > functions/hid.usb0/protocol # HID protocol
echo 1 > functions/hid.usb0/subclass # Boot interface subclass
echo 8 > functions/hid.usb0/report_length # Report descriptor size
echo -ne \\x05\\x01\\x09\\x06\\xA1\\x01\\x05\\x07\\x19\\xE0\\x29\\xE7\\x15\\x00\\x25\\x01\\x75\\x01\\x95\\x08\\x81\\x02\\x95\\x01\\x75\\x08\\x81\\x01\\x95\\x05\\x75\\x01\\x05\\x08\\x19\\x01\\x29\\x05\\x91\\x02\\x95\\x01\\x75\\x03\\x91\\x01\\x95\\x06\\x75\\x08\\x15\\x00\\x25\\x65\\x05\\x07\\x19\\x00\\x29\\x65\\x81\\x00\\xC0\\x05\\x01\\x09\\x02\\xA1\\x01\\x09\\x01\\xA1\\x00\\x05\\x09\\x19\\x01\\x29\\x03\\x15\\x00\\x25\\x01\\x95\\x03\\x75\\x01\\x81\\x02\\x95\\x01\\x75\\x05\\x81\\x01\\x05\\x01\\x09\\x30\\x09\\x31\\x09\\x38\\x15\\x81\\x25\\x7F\\x75\\x08\\x95\\x03\\x81\\x06\\xC0\\x05\\x0C\\x09\\x01\\xA1\\x01\\x15\\x81\\x25\\x7F\\x75\\x08\\x95\\x01\\x81\\x02\\x05\\x01\\x09\\x30\\x09\\x31\\x09\\x38\\x15\\x81\\x25\\x7F\\x75\\x08\\x95\\x03\\x81\\x06\\xC0\\xC0 > functions/hid.usb0/report_desc # Keyboard report descriptor

# Create HID configuration
mkdir -p configs/c.1
mkdir -p configs/c.1/strings/0x409
echo "Config 1: Keyboard" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

# Link HID function to HID configuration
ln -s functions/hid.usb0 configs/c.1/

# Enable the gadget
ls /sys/class/udc > UDC

