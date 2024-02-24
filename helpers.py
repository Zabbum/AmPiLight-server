import socket

def terminateProgram(clientSocket: socket.socket, serverSocket: socket.socket, pixelAmount: int, pixels: list):
    # Close connection if exists
    try:
        clientSocket.close()
        serverSocket.close()
    except:
        pass
    
    # Turn off every LED
    for pixel in range(pixelAmount):
        pixels[pixel] = [0, 0, 0]