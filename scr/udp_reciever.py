import socket
import cv2
import numpy as np

MAX_DGRAM = 2**15  # Reduce the size to 32,768 bytes

class UDPReceiver:
    def __init__(self, receiver_ip, port=12345):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.client_socket.bind((receiver_ip, port))

    def receive_frame(self):
        buffer = b''
        while True:
            packet, _ = self.client_socket.recvfrom(MAX_DGRAM)
            buffer += packet
            if len(packet) < MAX_DGRAM:
                break
        frame = np.frombuffer(buffer, dtype=np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
        return frame

if __name__=="__main__":
    receiver_ip = '192.168.1.2'  # Replace with your receiver IP address
    port = 12345  # Replace with your desired port number

    udp_receiver = UDPReceiver(receiver_ip, port)
    cv2.namedWindow('Video', cv2.WINDOW_NORMAL)  # Make the window resizable
    cv2.resizeWindow('Video', 640, 480)  # Set the initial size
    while True:
        frame = udp_receiver.receive_frame()
        if frame is not None:
            cv2.imshow('Received Frame', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    pass