# sockets - communication between programs on networks
# socket can be used as a server or a client
import socket 

BYTES_TO_READ = 4096 

'''Question 1'''
def get(host, port): 
    # Form the HTTP request
    request_data = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b"\n\n" # Send raw bytes using b""
    
    # Create a new internet socket, use as a stream 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port)) # pass (host, port) as a tuple 
    s.send(request_data)
    s.shutdown(socket.SHUT_WR) # not entirely shuted down! just end client -> server
    result = s.recv(BYTES_TO_READ)
    
    while len(result) > 0: 
        print(result)
        result = s.recv(BYTES_TO_READ)
        
    s.close() # close up the socket 

get("www.google.com", 80)