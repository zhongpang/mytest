from bluetooth import *

server_sock = BluetoothSocket(RFCOMM)
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service(server_sock, "TestServer", service_id=uuid,service_classes=[uuid,SERIAL_PORT_CLASS],profiles=[SERIAL_PORT_PROFILE],)

client_sock, client_info=server_sock.accept()

print client_info

try:
    while True:
        data=client_sock.recv(1024)
        print("received [%s]" % data)
except IOError:
    pass

print("disconnected")

client_sock.close()
server_sock.close()
print("all done")
