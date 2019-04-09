import  socket
sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sk.bind(('127.0.0.1',8000))
sk.listen(5)

conn,add=sk.accept()

msg=conn.recv(1024)#收消息

print('客户发的信息: ',msg)

conn.send(msg)

conn.close()
sk.close()