import socket

BYTES_TO_READ = 4096 
HOST = "127.0.0.1" # points to your own machine
PORT = 8080 

'''Question 2'''
def handle_connection(conn, addr): 
    with conn: 
        print(f"Connected by {addr}") # print who is connected to us
        while True: 
            data = conn.recv(BYTES_TO_READ) # recieve information from the socket
            if not data: # if the socket has a problem, disconnect 
                break 
            print(data)
            conn.sendall(data) # sent is back to the same connection (a echo server)
            

def start_server(): 
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # with-block automatically closes some resources after the block executes (no need for s.close)
         s.bind((HOST, PORT)) # bind to a host and a port 
         
         # Set up socket options setsockopt(level, option, value)
         s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # SO_REUSEADDR allows the socket rebind to the same address (when socket is closed, there's a period of time that the socket will remain open, and if you rerun the code within that time it will give an error, and this option remove the error)
         s.listen() 
         
         conn, addr = s.accept() # accept connections and handle it when a connection is recieved
         handle_connection(conn, addr) # conn is a socket created from the server socket that is connected with the client (a hybrid)

start_server() 