# Mr_Port_Warden
A basic python port scanner project...

📝 Python Port Scanner
This document describes a basic port scanner written in Python. The script uses the socket library to check for open TCP ports on a specified target IP address.

How It Works
The scanner operates by attempting to establish a connection to a specific port on the target IP. It leverages the socket.connect_ex() method, which is a key component of the script. This method is non-intrusive and ideal for scanning because it returns a status code rather than raising an error if a connection fails.

Socket Creation: The script first creates a TCP socket (socket.AF_INET for IPv4 and socket.SOCK_STREAM for TCP).

Timeout: A timeout is set to prevent the script from hanging indefinitely on filtered or closed ports.

Connection Check: connect_ex() returns 0 if the connection is successful, indicating the port is open. Otherwise, the port is considered "not available."

Logging: If a port is found to be open, its status is logged to a file named ports.txt for easy review.

The script iterates through a user-defined range of ports, applying this check to each one to build a basic report of open ports.

💡 Testing Method
You can test this port scanner using a simple Python HTTP server. This is a common method for penetration testers and developers to quickly create a listening service on a specific port.

Start a server: In your terminal, use the following command to start a simple HTTP server on a chosen port (e.g., 8000):

Bash

python -m http.server <port number>
Run the scanner: Execute your port scanner script and target the IP address of the machine running the server. The scanner should successfully identify that the specified port is open.

Stop the server: Once the scan is complete, press Ctrl + C in the terminal to stop the HTTP server. The next time you run the scanner, that port will appear as closed.

This method provides a reliable and simple way to confirm your scanner is working correctly.

## This is note 1 for this projects , next  versions will be coming....