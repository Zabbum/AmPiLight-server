# AmPiLight server
### This program was made as final project for CS50x
[Video demo](https://youtu.be/XjO_DUD1B1E)

### Description
AmPiLight is a program that aims to do effect like Philips Ambilight, but using RaspberryPi as NeoPixel LED controller.

## Installation, configuration and running
**Note that you will also need a [client side](https://github.com/Zabbum/AmPiLight-client) to make program work.**

### Installation
1. Clone the repository and navigate to it.
```
git clone https://github.com/Zabbum/AmPiLight-server.git
cd AmPiLight-server
```
2. Install required dependencies.
```
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```
### Configuration
`config.json` contains all the configuration.
- `"dinPin"` is GPIO pin to which NeoPixel *Din* is connected. [ex. `"D18"`] ([How to connect](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring))
- `"LEDAmount"`
    - `"vertical"` is how many diodes are vertically behind monitor. [ex. `10`]
    - `"horizontal"` is how many diodes are horizontally behind monitor. [ex. `16`]
- `"skipFirstPixel"` is whether do skip first pixel or not (sometimes if you do not have proper wiring first LED behaves weird). [ex. `true`]
- `"RGBOrder"` is order of pixel colors. [ex. `"GRB"`]
- `"port"` is network port which program will be using. [ex. `7602`]
### Running
You must run program as administrator.
```
sudo python3 app.py
```
