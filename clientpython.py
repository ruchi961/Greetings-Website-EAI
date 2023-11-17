import socket
import ast

def getOffersCoupons():
    SERVER_IP = "localhost"
    #SERVER_IP = '0.0.0.0'

    PORT_NUMBER = 9988
    SIZE = 1024
    print(f"Server address: {SERVER_IP}:{PORT_NUMBER}")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, PORT_NUMBER))

    flag = True
    #while flag:

        # send
    message = "sendData"
    print(f"Send message: {message}")
    client_socket.send(bytes(message, "utf-8"))

    # receive
    byte_message = client_socket.recv(SIZE)
    message = byte_message.decode("utf-8")

    print(f"Receive message: {message}")
        
    print("\n\n",message,type(message))
    message = message.replace("}{","},{")
    message = "["+message+"]"
    print(message)
    data = ast.literal_eval(message)
    print(data,type(data))   
        #flag = False
    return data
#getOffersCoupons()      
