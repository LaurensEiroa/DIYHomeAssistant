# config.py
class Config:
    IPs = {"pi5":"192.168.129.11",
           "piZero1":"192.168.129.14",
           "piZero2":"192.168.129.15",
           "piZero3":"192.168.129.22",
           "piZero4":"192.168.129.21"
           }
    APP_PORT = 8000
    UDP_PORT = 0000
    HTTP_PORT = 1111
    WEBSOCKET_PORT = 2222

    UDP_MAX_DGRAM = 2**15
