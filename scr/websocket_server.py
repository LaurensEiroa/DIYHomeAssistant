import asyncio
import websockets
import time

async def pi_zero_request(rpi_name,instruction):
    # instructions = ["turn_on_relay","turn_off_relay","toggle_relay","read_sht31d"]
    rpi_IPs = {"zero1":"192.168.129.14",
           "zero2":"192.168.129.15",
           "zero3":"192.168.129.22",
           #"zero4":"192.168.129.14",
           }

    uri = f"ws://{rpi_IPs[rpi_name]}:8080"  

    async with websockets.connect(uri) as websocket:
        print("Connection from pi 5 to Zero established")
        print(f"sending instruction to {room}({rpi_IPs[rpi_name]}): {instruction}") 

        await websocket.send(instruction) 
        message = await websocket.recv() 

        # Receive one message per instruction 
        print(f"Received message on rpi5: {message}\nSleeping") 
        if instruction=="read_sht31d":
            T = message.split("-")[0].split("Temperature:")[-1]
            H = message.split("-")[1].split("Humidity:")[-1]
            return round(float(T),2), round(float(H),2)
        return message

if __name__=="__main__":
    room = "zero1"
    instruction = "read_sht31d"
    asyncio.get_event_loop().run_until_complete(pi_zero_request(room,instruction))