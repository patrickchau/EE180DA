import socket
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(('192.168.43.215', 8585))
serv.listen(5)
while True:
	conn, addr = serv.accept()
	from_client = ""
	while True:
		data = conn.recv(4096).decode('utf-8')
		if not data: break
		from_client += data
		print(from_client)
		conn.send("I am SERVER\n".encode('utf-8'))
	conn.close()
	print("client disconnected")
