# Key_Logger_Socket
## Motivation
Build a portfolio for basic python and networking background \
Developed a simple keylogger script with added remote connection feature using python socket module

## Features
### Keyboard module
```
 keyboard.on_release(callback=callback)
```
<br>For every KeyUp event caught by on_release() method from keyboard class, call the callback funcntion. Callback function would categorize the KeyUp event and populate the log variable. Using callback allow the next line of code to run without having to wait for the return values of on_release()</br>




### Initialize s socket to create a connection back to attacking server
```
 s = socket.socket(AF_INET,SOCK_STREAM)
```


