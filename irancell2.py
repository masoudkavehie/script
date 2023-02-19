import datetime
import paramiko
from time import sleep
from rich.console import Console
class Pass_credit:
    def __init__(self,tsknumb):
        self.tsknumb=tsknumb
        self.currentdateandtime=datetime.datetime.now()
        self.currenttime=self.currentdateandtime.strftime("%H:%M")
        self.commands=open("MSISDN.txt","r")
        self.connection=paramiko.SSHClient()

        
        self.modes={
            "Air2":f"cp -r tsk-{self.tsknumb} ra_credit/RA_ADJUST_00{self.tsknumb}_0{self.currenttime}.DAT",
            "Air1":f"cp -r tsk-{self.tsknumb} export/home/ra_credit/DED_ADJUST_00{self.tsknumb}_0{self.currenttime}.DAT",
            "warrior":f"cd warrior/UCIP \n ./SetDaOffer.py /home/masoud.kav/tsk-{tsknumb} 0"
        }
        self.log={
            "Air2":f"cat ra_credit/tsk-{self.tsknumb}.RPT",
            "Air1":f"cat export/home/ra_credit/tsk-{self.tsknumb}.RPT",
            "warrior":f"cat tsk-{self.tsknumb}.RPT"     
        }
    def loading(self,message,duration):
        console = Console()
        tasks = True
        with console.status(f"[bold green] {message}") as status:
            while tasks:
                sleep(int(duration))
                console.log(f"complete")
                break

    def Air2(self,username,password,serveraddress,keyword):
        lines=str(self.commands.readlines())
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.connection.connect(hostname=serveraddress,port=22,username=username,password=password,look_for_keys=False, allow_agent=False)
            print("you are connected successfuly! \n")
            commands=f"touch tsk-{self.tsknumb}"
            self.loading("your task are creating please wait!!",3)
            self.connection.exec_command(commands)
            self.connection.exec_command(f"echo {str(lines)} > tsk-{self.tsknumb} \n {self.modes[keyword]}")
            self.loading("Please wait to generate report!",10)
            stdin,stdout,stderr=self.connection.exec_command(self.log[keyword])
            return(str(stdout.readlines()))
        except:
            raise ConnectionError("you cant connect to server.please double check your information!")


    def Air1(self,username,password,serveraddress,keyword):
        lines=str(self.commands.readlines())
        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.connection.connect(hostname=serveraddress,port=22,username=username,password=password,look_for_keys=False, allow_agent=False)
            print("you are connected successfuly! \n")
            commands=f"touch tsk-{self.tsknumb}"
            self.loading("your task are creating please wait!!",3)
            self.connection.exec_command(commands)
            self.connection.exec_command(f"echo {str(lines)} > tsk-{self.tsknumb} \n {self.modes[keyword]}")
            self.loading("Please wait to generate report!",10)
            stdin,stdout,stderr=self.connection.exec_command(self.log[keyword])
            return(str(stdout.readlines()))
        except:
            raise ConnectionError("you cant connect to server.please double check your information!")
 

    