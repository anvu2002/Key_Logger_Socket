import socket

hostname = 'localhost'

port = 3000

#define socket object s (IPv4, TCP stream)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the IP address and port in a tpuple --> create a LISTENING SVR SOCKET
s.bind((hostname, port))

#listen for connection on the socket <IP>:3128

s.listen()
print(f"[+]Listenning on {port}")




#conn: connection object
#address: the client address
conn, address = s.accept()
print(f"[+]Client {address} connected! Let's chat")

#Handle the current session
while True:
	try:
		#this socket would try to receive data, rate: 2048 bytes/time
		recv = conn.recv(2048)
		quit = b'SECRET-QUIT-COMMAND'
		if recv != quit:
			print(f'Client: {recv}')		
		if not recv or recv.strip() == b'SECRET-QUIT-COMMAND': #quit in bytes type
			print("[+]Connection Terminated")
			break
		to_reply = "Received" 
		conn.send(to_reply.encode('utf-8'))
	except KeyboardInterrupt:
		break




		