# NETWORKING

## IP ADDRESS

A unique strings of number seprated by full stops that identifies each computer using the **Internet Protocol** to communicate over a network.
e.g. 192.168.0.104

### PUBLIC IP vs PRIVATE IP

* A Public IP address is globally unique and is assigned to a device by the Internet Assigned Numbers Authority (IANA) or a regional Internet registry (RIR).

* Googling "Whats my Ip" will provide you your public IP.

* A private IP address is used within a private network and is not globally unique.

* You can find your private IP in your computer settings or `ifconfig` for linux `ipconfig` for windows can show your private ip.

### Static vs Dynamic

*  Static IP address is manually configured for a device and remains constant unless changed by a network administrator. e.g. servers, website etc.

* A dynamic IP address is automatically assigned to a device by a Dynamic Host Configuration Protocol (DHCP) server. e.g. computers, mobile devices etc.

* Static ip never changes but dynamic ip always keep changing.

### Ports

* A port is a communication endpoint that identifies a specific process or service on a networked device.
(think about port as exact room number)

* Some common port numbers are:

    1. 80: HTTP
    2. 443: HTTPS
    3. 20/21: FTP
    4. 22: SSH

* Check open ports 
    * `sudo lsof -i -P -n | grep LISTEN` for mac.
    * `netstat -tuln` for linux.
    * `netstat -an | find "LISTENING"` for windows.

### Sockets

* A socket is a one endpoint of two way communication link between two programs running on the network.

* A socket is bound to a **port** number so that the tcp layer can identify the application the data is destined to be sent to.

* An endpoint is a combination of an IP address and port number.

