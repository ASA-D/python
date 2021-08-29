import socket
import threading

scan_range = [1, 10000];

host = "10.0.0.2";

threads = [];
ports = [];
isopen = [];

def Run(port, i):
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return_code = con.connect_ex((host, port))
    con.close()

    if return_code == 0:
        isopen[i] = 1;


count = 0;
for port in range(scan_range[0], scan_range[1]):
    ports.append(port);
    isopen.append(0);
    thread = threading.Thread(target=Run, args=(port, count));
    thread.start();
    threads.append(thread);
    count = count + 1;

for i in range(len(threads)):
    threads[i].join();
    if isopen[i] == 1:
        print("%d open" % ports[i]);
