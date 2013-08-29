def getip():
    sock = socket.create_connection(('ns1.dnspod.net', 6666))
    ip = sock.recv(16)
    sock.close()
    return ip
    
if __name__ == '__main__':
    print getip()
