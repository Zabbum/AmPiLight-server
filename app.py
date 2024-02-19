# Import modules
import board, neopixel
import json
import socket, pickle

# Global variables
dinPin = 0      # GPIO pin that is connected to NeoPixel Din
pxAmount = 0    # Amount of LEDs connected (vertically and horizontally)
order = 0       # Order of pixel colors (RGB or GRB)
port = 0        # Network port
pixels = 0      # Neopixel output data

# TODO: Verify that config.json exists and if not,
# prompt user for settings and write them to fil

# Read configuration from config.json
with open('config.json') as configFile:
    jsonData = json.load(configFile)
    dinPin = getattr(board, jsonData['dinPin'])
    pxAmount = jsonData['LEDAmount']
    pxAmount["sum"] = 2*pxAmount["vertical"] + pxAmount["horizontal"]
    order = jsonData['RGBOrder']
    port = jsonData['port']
    skipFirstPixel = jsonData["skipFirstPixel"]
    if skipFirstPixel:
        pxAmount["sum"] +=1

# Neopixel setup
pixels = neopixel.NeoPixel(dinPin, pxAmount["sum"])

# Network setup
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('0.0.0.0', port))

try:
    # Listen for connection
    print("Listening for connection...")
    serverSocket.listen(1)
    clientSocket, clientAddress = serverSocket.accept()

    # Program loop
    while True:
        try:
            # Listen for data
            data = clientSocket.recv(1024)
            if not data:
                clientSocket.close()
                continue

            LEDdata = pickle.loads(data)
            print(f'Received data: {LEDdata}\n')

            # Analyze data and send it to LED strip
            for pixel in range(pxAmount["sum"]):
                listIndex = pixel # Define which index in list is data to send to pixel (useful if skipping first pixel)
                if skipFirstPixel: # Check whether skip first pixel
                    if pixel == 0: # Skip first pixel
                        continue
                    listIndex -= 1

                pixels[pixel] = LEDdata[listIndex] # Send data to LED strip

        # Continue if bad data is sent
        except (pickle.UnpicklingError, UnicodeDecodeError) as error:
            print(f"Error {error} while unpickling or decoding data. Continuing.")
            continue

# If user closes program, close program
except OSError as error:
    if error.errno == 9:
        print("Connection closed from client side.")
        exit()
    error

# If program was not run as administrator
except RuntimeError:
    print("You must run program as administrator!")
    clientSocket.close()
    serverSocket.close()
    exit(1)

# If received terminate signal, end program casually.
except KeyboardInterrupt:
    print("Received stop sygnal.")
    try:
        clientSocket.close()
        serverSocket.close()
    except NameError:
        pass
    exit()