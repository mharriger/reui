reui
====

Rotary Encoder User Interface library

This is a python library to facilitate creation of applications using a rotary encoder and a small monochrome screen as a user interface. Currently it targets the adafruit ssd-1306 based OLED displays and the adafruit rotary encoder on the Raspberry Pi platform.

This library depends on PyDispatcher for event handling, and on gaugette for communication with the display and encoder.

Initial plan is for interface layout to be based around non-overlapping boxes, and to provide methods for placing text and bitmapped icons within those boxes.
