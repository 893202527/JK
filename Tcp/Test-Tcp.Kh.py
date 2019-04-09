import  socket

sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


sk.connect(('127.0.0.1',8000))


sk.send('xxdddxx'.encode('utf-8'))
data=sk.recv(1024)

print('收到服务器的消息',data)