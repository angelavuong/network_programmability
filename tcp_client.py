import socket

def main():
    host = '127.0.0.1'
    port = 5000

    s = socket.socket()
    s.connect((host,port))

    message = raw_input("-> ")
    while message != 'q':
        s.send(message)
        data = s.recv(1024) # Buffer of 1024 bytes
        print "Received from server: " + str(data)
        message = raw_input('-> ')

    s.close()

if __name__ == '__main__':
    main()
