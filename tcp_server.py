import socket

def main():
    host = '127.0.0.1' # Local host
    port = 5000

    s = socket.socket()
    s.bind((host, port))

    s.listen(1) # Listen for one connection at a time
    c, addr = s.accept() # accept the connect you're trying to connect to

    print "Connection from: " + str(addr)
    while True:
        data = c.recv(1024) # Buffer is 1024 bytes
        if not data: # If False
            break
        print "from connected user: " + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        c.send(data)
    c.close() # Close the socket

if __name__ == '__main__':
    main()
